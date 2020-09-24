# Fetch surf conditions from surfline's static site
import requests
import re


class ConditionFetcher:
    def __init__(self):
        self.surf_height_selector = 'Surf height</div><span class="quiver-surf-height">(.+?)<sup>FT'
        self.water_temp_selector = 'Tourmaline Water Temp"/>(.+?)<'
        self.surf_quality_selector = 'quiver-colored-condition-bar quiver-colored-condition-bar--.+?\">(.+?)</div>'

    def get_conditions(self):
        page = requests.get('https://www.surfline.com/surf-report/old-man-s-at-tourmaline/5842041f4e65fad6a77088c4')
        text = page.text

        surf_height = re.search(self.surf_height_selector, text).group(1)
        water_temp = re.search(self.water_temp_selector, text).group(1)
        surf_quality = re.search(self.surf_quality_selector, text).group(1)

        return self.parse_surf_height(surf_height), int(water_temp), self.translate_surf_quality(surf_quality)

    # Expected format is %d-%d, eg 1-2
    def parse_surf_height(self, raw_surf_height):
        low, high = raw_surf_height.split('-')
        avg = float(int(high) + int(low)) / 2.0
        return avg

    def translate_surf_quality(self, surf_quality):
        return [
            None,
            'FLAT',
            'VERY POOR',
            'POOR',
            'POOR to FAIR',
            'FAIR',
            'FAIR to GOOD',
            'GOOD',
            'VERY GOOD',
            'GOOD to EPIC',
            'EPIC'
        ].index(surf_quality)

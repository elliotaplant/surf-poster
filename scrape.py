# Fetch surf conditions from surfline's static site
import requests
import re


class ConditionFetcher:
    def __init__(self):
        self.surf_height_selector = 'Surf height</div><span class="quiver-surf-height">(.+?)<sup>FT'
        self.water_temp_selector = 'Tourmaline Water Temp"/>(.+?)<'
        self.wind_speed_selector = (
            '.Wind</div><div class="quiver-conditions-stats__stat-reading"><span class="quiver-reading">(.+?)<sup>'
        )

    def get_conditions(self):
        page = requests.get('https://www.surfline.com/surf-report/old-man-s-at-tourmaline/5842041f4e65fad6a77088c4')
        text = page.text

        surf_height = re.search(self.surf_height_selector, text).group(1)
        water_temp = re.search(self.water_temp_selector, text).group(1)
        wind_speed = re.search(self.wind_speed_selector, text).group(1)

        return self.parse_surf_height(surf_height), int(water_temp), int(wind_speed)

    # Expected format is %d-%d, eg 1-2
    def parse_surf_height(self, raw_surf_height):
        low, high = raw_surf_height.split('-')
        avg = (int(high) + int(low)) / 2
        return avg

# Fetch surf conditions from surfline's static site
import requests
import re


class ConditionFetcher:
    def __init__(self):
        self.surf_height_selector = 'Surf height</div><span class="quiver-surf-height">(.+?)<sup>FT'
        self.water_temp_selector = ' Water Temp"/>(.+?)<'
        self.surf_quality_selector = 'quiver-colored-condition-bar quiver-colored-condition-bar--.+?\">(.+?)</div>'
        self.wind_speed_selector = '<span class=\"quiver-reading\">(\d+?)<sup>KTS</sup></span>'


    def get_conditions(self, surfline_id):
        page = requests.get('https://www.surfline.com/surf-report/' + surfline_id)
        text = page.text

        surf_height = re.search(self.surf_height_selector, text).group(1)
        water_temp = re.search(self.water_temp_selector, text).group(1)
        surf_quality_match = re.search(self.surf_quality_selector, text)
        wind_speed_match = re.search(self.wind_speed_selector, text)

        surf_quality = None
        parsed_surf_height = self.parse_surf_height(surf_height)

        if surf_quality_match:
            surf_quality = self.translate_surf_quality(surf_quality_match.group(1))
        elif wind_speed_match:
            surf_quality = self.correlate_wind_height_to_surf(wind_speed_match.group(1), parsed_surf_height)

        return parsed_surf_height, int(water_temp), surf_quality

    # Expected format is %d-%d, eg 1-2
    def parse_surf_height(self, raw_surf_height):
        low, high = raw_surf_height.split('-')
        avg = float(int(high) + int(low)) / 2.0
        return avg

    def translate_surf_quality(self, surf_quality):
        return [
            'REPORT COMING SOON',
            'FLAT',
            'VERY POOR',
            'POOR',
            'POOR TO FAIR',
            'FAIR',
            'FAIR TO GOOD',
            'GOOD',
            'VERY GOOD',
            'GOOD TO EPIC',
            'EPIC'
        ].index(surf_quality.upper())

    # Super rough calculation
    def correlate_wind_height_to_surf(self, wind_speed_str, surf_height):
        wind_speed = float(wind_speed_str)
        return int(surf_height - wind_speed / 2)

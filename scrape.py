# Fetch surf conditions from surfline's static site
from lxml import html
import requests


class ConditionFetcher:
    def __init__(self):
        self.surf_height_selector = '.quiver-spot-forecast-summary__stat-container--surf-height .quiver-surf-height'
        self.water_temp_selector = '.quiver-wetsuit-recommender .quiver-water-temp div'
        self.wind_speed_selector = '.quiver-spot-forecast-summary__stat-container--wind .quiver-reading'

    def get_conditions(self):
        page = requests.get('https://www.surfline.com/surf-report/old-man-s-at-tourmaline/5842041f4e65fad6a77088c4')
        tree = html.fromstring(page.content)

        surf_height = tree.cssselect(self.surf_height_selector)[0].text_content()
        water_temp = tree.cssselect(self.water_temp_selector)[0].text_content()
        wind_speed = tree.cssselect(self.wind_speed_selector)[0].text_content()

        return self.parse_surf_height(surf_height), self.parse_water_temp(water_temp), self.parse_wind_speed(wind_speed)

    # Expected format is %d-%dFT, eg 1-2FT
    def parse_surf_height(self, raw_surf_height):
        without_suffix = raw_surf_height[:-2]
        low, high = without_suffix.split('-')
        avg = (int(high) + int(low)) / 2
        return avg

    # Expected format is %d%d - %d%d ºF, eg 62 - 65 ºF
    def parse_water_temp(self, raw_water_temp):
        without_suffix = raw_water_temp[:-3]
        low, high = without_suffix.split(' - ')
        avg = (int(high) + int(low)) / 2
        return avg

    # Expected format is %d+KTS
    def parse_wind_speed(self, raw_wind_speed):
        return int(raw_wind_speed[:-3])

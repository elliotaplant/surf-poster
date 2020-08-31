from lxml import html
import requests

page = requests.get('https://www.surfline.com/surf-report/old-man-s-at-tourmaline/5842041f4e65fad6a77088c4')
tree = html.fromstring(page.content)

surf_height = tree.cssselect('.quiver-spot-forecast-summary__stat-container--surf-height .quiver-surf-height')[0].text
water_temp = tree.cssselect('.quiver-wetsuit-recommender .quiver-water-temp div')[0].text_content()
wind_speed = tree.cssselect('.quiver-spot-forecast-summary__stat-container--wind .quiver-reading')[0].text_content()

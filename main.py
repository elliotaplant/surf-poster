import logging
from scrape import ConditionFetcher
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster update')

condition_fetcher = ConditionFetcher()
servo_controller = ServoController()

logging.info('Fetching conditions')
surf_height, water_temp, wind_speed = condition_fetcher.get_conditions()

logging.info(f"Surf height: {surf_height}, Wind speed: {wind_speed}, Water temp {water_temp}")

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, wind_speed)
servo_controller.stop()

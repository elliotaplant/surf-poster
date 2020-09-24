import logging
from scrape import ConditionFetcher
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster update')

condition_fetcher = ConditionFetcher()
# servo_controller = ServoController()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions()

logging.info("Surf height: %(surf_height)s, Surf quality: %(surf_quality)s, Water temp %(water_temp)s")

# servo_controller.setup()
# servo_controller.set_to_angles(surf_height, water_temp, surf_quality)
# servo_controller.stop()

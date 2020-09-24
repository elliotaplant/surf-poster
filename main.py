import logging
from scrape import ConditionFetcher
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster update')

condition_fetcher = ConditionFetcher()
servo_controller = ServoController()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions()

logging.info("Surf height:  %s" % surf_quality)
logging.info("Water temp:   %s" % surf_quality)
logging.info("Surf quality: %s" % surf_quality)

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality)
servo_controller.stop()

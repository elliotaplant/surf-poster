import logging
import sys
from scrape import ConditionFetcher
from actuate import ServoController
from beaches import beaches

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

if len(sys.argv) < 2:
    raise ReferenceError('Beach name is a required agument. See list of beaches in beaches.py')

beach_name = sys.argv[1]
beach = beaches.get(beach_name)

if not beach:
    raise ReferenceError('Unknown beach "%s". See list of beaches in beaches.py', beach_name)

logging.info('Running surf poster update for beach ' + beach_name)
condition_fetcher = ConditionFetcher()
servo_controller = ServoController()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions(beach["surfline_id"])

logging.info('Surf height:  %s' % surf_height)
logging.info('Water temp:   %s' % water_temp)
logging.info('Surf quality: %s' % surf_quality)

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality, beach["dial_range"])
servo_controller.stop()

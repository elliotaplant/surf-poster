import logging
import sys
from scrape import ConditionFetcher
from beaches import beaches

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

if len(sys.argv) < 2:
    raise ReferenceError('Beach name is a required agument. See list of beaches in beaches.py')

beach_name = sys.argv[1]
surfline_id = beaches.get(beach_name)

if not surfline_id:
    raise ReferenceError('Unknown beach. See list of beaches in beaches.py')

logging.info('Getting surf conditions for ' + beach_name)

condition_fetcher = ConditionFetcher()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions(surfline_id)

logging.info('Surf height:  %s' % surf_height)
logging.info('Water temp:   %s' % water_temp)
logging.info('Surf quality: %s' % surf_quality)

import logging
import sys
from scrape import ConditionFetcher

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

beach_name = sys.argv[1]

if not beach_name:
    raise ReferenceError('Beach name is a required agument. See list of beaches in beaches.py')

logging.info('Getting surf conditions for ' + beach_name)

condition_fetcher = ConditionFetcher()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions(beach_name)

logging.info('Surf height:  %s' % surf_height)
logging.info('Water temp:   %s' % water_temp)
logging.info('Surf quality: %s' % surf_quality)

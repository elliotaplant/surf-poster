import logging
from scrape import ConditionFetcher

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster update')

condition_fetcher = ConditionFetcher()

logging.info('Fetching conditions')
surf_height, water_temp, surf_quality = condition_fetcher.get_conditions()

logging.info("Surf height:  %s" % surf_height)
logging.info("Water temp:   %s" % water_temp)
logging.info("Surf quality: %s" % surf_quality)

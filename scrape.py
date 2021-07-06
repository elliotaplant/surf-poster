# Fetch surf conditions from surfline's static site
import requests
import json
import time

SURFLINE_BASE_URL = 'https://services.surfline.com/kbyg/spots/forecasts'
PARAMS = '?sds=true&spotId='



class ConditionFetcher:

    def get_conditions(self, beach):
        waves_response = json.loads(requests.get(SURFLINE_BASE_URL + '/wave' + PARAMS + beach['surfline_id']).text)
        surf_height = 0
        surf_optimal = 0
        for d in waves_response['data']['wave']:
            if d['timestamp'] - time.time() > 0:
                surf_height = (d['surf']['max'] + d['surf']['min']) / 2
                surf_optimal = d['surf']['optimalScore']
                break

        wind_response = json.loads(requests.get(SURFLINE_BASE_URL + '/wind' + PARAMS + beach['surfline_id']).text)
        wind_optimal = 0
        for d in wind_response['data']['wind']:
            if d['timestamp'] - time.time() > 0:
                wind_optimal = d['optimalScore']
                break

        surf_quality = 2 * (surf_optimal + wind_optimal) + (surf_height / beach['dial_range']['surf_height'][1]) * 6

        temp_response = requests.get(SD_WATER_TMP).text
        parsed_temp_response = json.loads(temp_response)
        water_temp = round(float(temp_response['data'][0]['v']))

        return surf_height, water_temp, surf_quality

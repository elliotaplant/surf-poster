import logging
import sys
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster manual update')
servo_controller = ServoController()

logging.info('Reading conditions')
surf_height, water_temp, wind_speed = [int(arg) for arg in sys.argv[1:]]

logging.info(f"Surf height: {surf_height}, Wind speed: {wind_speed}, Water temp {water_temp}")

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, wind_speed)
servo_controller.stop()

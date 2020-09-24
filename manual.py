import logging
import sys
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster manual update')
servo_controller = ServoController()

logging.info('Reading conditions')
surf_height, water_temp, surf_quality = [int(arg) for arg in sys.argv[1:]]

logging.info("Surf height duty cycle: %(surf_height)s")
logging.info("Water temp duty:        %(water_temp)s")
logging.info("Surf quality duty:      %(surf_quality)s")

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality)
servo_controller.stop()

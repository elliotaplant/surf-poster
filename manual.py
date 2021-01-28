import logging
import sys
from actuate import ServoController

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info('Running surf poster manual update')
servo_controller = ServoController()

logging.info('Reading conditions')
surf_height, water_temp, surf_quality = [float(arg) for arg in sys.argv[1:]]

logging.info('Surf height duty cycle: %s' % surf_height)
logging.info('Water temp duty:        %s' % water_temp)
logging.info('Surf quality duty:      %s' % surf_quality)

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality)
servo_controller.stop()

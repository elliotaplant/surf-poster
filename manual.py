import logging
import sys
from actuate import ServoController
from beaches import beaches

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

if len(sys.argv) < 5:
    raise ReferenceError(
        'Arguments <beach_name> <wave_height> <water_temp> <surf_quality> required. See list of beaches in beaches.py'
    )

beach_name = sys.argv[1]
beach = beaches.get(beach_name)

if not beach:
    raise ReferenceError('Unknown beach "%s". See list of beaches in beaches.py', beach_name)

logging.info('Running surf poster manual update')
servo_controller = ServoController()

logging.info('Reading conditions')
surf_height, water_temp, surf_quality = [float(arg) for arg in sys.argv[2:]]

logging.info('Surf height duty cycle: %s' % surf_height)
logging.info('Water temp duty:        %s' % water_temp)
logging.info('Surf quality duty:      %s' % surf_quality)

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality, beach["dial_range"])
servo_controller.stop()

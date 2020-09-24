import sys
from actuate import ServoController

print(sys.argv)

servo_controller = ServoController()

surf_quality = float(sys.argv[1])
surf_height = float(sys.argv[2])
water_temp = float(sys.argv[3])

servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, surf_quality)
servo_controller.stop()

from scrape import ConditionFetcher
from actuate import ServoController


condition_fetcher = ConditionFetcher()
servo_controller = ServoController()

surf_height, water_temp, wind_speed = condition_fetcher.get_conditions()
servo_controller.setup()
servo_controller.set_to_angles(surf_height, water_temp, wind_speed)
servo_controller.stop()

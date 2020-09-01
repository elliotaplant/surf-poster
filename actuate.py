import RPi.GPIO as GPIO


SURF_HEIGHT_PIN_NUMBER = 21
WATER_TEMP_PIN_NUMBER = 20
WIND_SPEED_PIN_NUMBER = 16

SERVO_PWM_FREQUENCY = 50  # Hz
DUTY_CYCLE_RANGE = [1, 2]

SURF_HEIGHT_RANGE = [0, 6]
WATER_TEMP_RANGE = [55, 75]
WIND_SPEED_RANGE = [0, 15]


class ServoController:
    def setup(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(SURF_HEIGHT_PIN_NUMBER, GPIO.OUT)
        GPIO.setup(WATER_TEMP_PIN_NUMBER, GPIO.OUT)
        GPIO.setup(WIND_SPEED_PIN_NUMBER, GPIO.OUT)

        self.surf_height_pin = GPIO.PWM(SURF_HEIGHT_PIN_NUMBER, SERVO_PWM_FREQUENCY)
        self.water_temp_pin = GPIO.PWM(WATER_TEMP_PIN_NUMBER, SERVO_PWM_FREQUENCY)
        self.wind_speed_pin = GPIO.PWM(WIND_SPEED_PIN_NUMBER, SERVO_PWM_FREQUENCY)

    def stop(self):
        self.surf_height_pin.stop()
        self.water_temp_pin.stop()
        self.wind_speed_pin.stop()
        GPIO.cleanup()

    def set_to_angles(self, surf_height, water_temp, wind_speed):
        self.surf_height_pin.ChangeDutyCycle(self._convert_to_duty_cycle(surf_height, SURF_HEIGHT_RANGE))
        self.surf_height_pin.ChangeDutyCycle(0)
        self.water_temp_pin.ChangeDutyCycle(self._convert_to_duty_cycle(water_temp, WATER_TEMP_RANGE))
        self.water_temp_pin.ChangeDutyCycle(0)
        self.wind_speed_pin.ChangeDutyCycle(self._convert_to_duty_cycle(wind_speed, WIND_SPEED_RANGE))
        self.wind_speed_pin.ChangeDutyCycle(0)
        # Need to chagne to 0?
        # Need sleep?

    def _convert_to_duty_cycle(self, metric, metric_range):
        metric_ratio = (metric - metric_range[0]) / (metric_range[1] - metric_range[0])
        return metric_ratio * (DUTY_CYCLE_RANGE[1] - DUTY_CYCLE_RANGE[0]) + DUTY_CYCLE_RANGE[0]

import RPi.GPIO as GPIO
import logging
import time

SURF_HEIGHT_PIN_NUMBER = 20
WATER_TEMP_PIN_NUMBER = 16
WIND_SPEED_PIN_NUMBER = 21

SERVO_PWM_FREQUENCY = 50  # Hz
DUTY_CYCLE_RANGE = [12.5, 2.5]

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
        self.surf_height_pin.start(3)
        self.water_temp_pin = GPIO.PWM(WATER_TEMP_PIN_NUMBER, SERVO_PWM_FREQUENCY)
        self.water_temp_pin.start(3)
        self.wind_speed_pin = GPIO.PWM(WIND_SPEED_PIN_NUMBER, SERVO_PWM_FREQUENCY)
        self.wind_speed_pin.start(3)

    def stop(self):
        logging.info("Cleaning up")
        self.surf_height_pin.stop()
        self.water_temp_pin.stop()
        self.wind_speed_pin.stop()
        GPIO.cleanup()

    def set_to_angles(self, surf_height, water_temp, wind_speed):
        surf_height_duty = self._convert_to_duty_cycle(surf_height, SURF_HEIGHT_RANGE)
        water_temp_duty = self._convert_to_duty_cycle(water_temp, WATER_TEMP_RANGE)
        wind_speed_duty = self._convert_to_duty_cycle(wind_speed, WIND_SPEED_RANGE)
        logging.info(f"Surf height duty cycle: {surf_height_duty}, Water temp duty: {water_temp_duty}, Wind speed duty: {wind_speed_duty}")
        self.surf_height_pin.ChangeDutyCycle(surf_height_duty)
        self.water_temp_pin.ChangeDutyCycle(water_temp_duty)
        self.wind_speed_pin.ChangeDutyCycle(wind_speed_duty)
        time.sleep(1)
        self.surf_height_pin.ChangeDutyCycle(0)
        self.water_temp_pin.ChangeDutyCycle(0)
        self.wind_speed_pin.ChangeDutyCycle(0)
        time.sleep(1)

    def _convert_to_duty_cycle(self, metric, metric_range):
        metric_ratio = (metric - metric_range[0]) / (metric_range[1] - metric_range[0])
        return metric_ratio * (DUTY_CYCLE_RANGE[1] - DUTY_CYCLE_RANGE[0]) + DUTY_CYCLE_RANGE[0]

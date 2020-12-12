import RPi.GPIO as GPIO
import time

SERVO_PWM_FREQUENCY = 50  # Hz

pin_number, duty_cycle = sys.argv[1:]
pin_number = int(pin_number)
duty_cycle = float(duty_cycle)


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.OUT)

pin = GPIO.PWM(pin_number, SERVO_PWM_FREQUENCY)
pin.start(3)

pin.ChangeDutyCycle(duty_cycle)
time.sleep(1)

self.surf_height_pin.ChangeDutyCycle(0)
time.sleep(1)

pin.stop()

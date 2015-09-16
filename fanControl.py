import RPi.GPIO as GPIO
import time
pin=18 #GPIO PWM pin

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
fan = GPIO.PWM(pin,100)
fan.start(10)

def setSpeed(speed):
	fan.ChangeDutyCycle(speed)

def main():
	exit()

if __name__ == "__main__":
        main()

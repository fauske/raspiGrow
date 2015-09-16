import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def set(pin, status):
	GPIO.setup(pin, GPIO.OUT)
	if status == True:
		status=GPIO.LOW
	else:
		status=GPIO.HIGH
	GPIO.output(pin, status)

def main():
	exit()

if __name__ == "__main__":
        main()

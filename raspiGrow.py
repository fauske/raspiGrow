from time import strftime, sleep
import tempRead as temp
import fanControl as fan
import relayControl as relay
import logg

# GPIO pins that controls the relay switch
#rel1=22 # unused
#rel2=23 # unused
#rel3=24 # unused
rel4=25 # Light

#D18B20 temp sensors
sens1='28-000006876fc9'
sens2='28-00000688212c'
sens3='28-0000068944b8'

# Status variables 
#statusRel1=False
#statusRel2=False
#statusRel3=False
statusRel4=False
varSpeed=0

# The thought here is that when the temp reaches maxTemp, then maxSpeed is activated
maxTemp=30
maxSpeed=70

# In the example the script turns on at 6 in the morning and off at 10 in the evening
lightOn=6
lightOff=22

# How often to run the script in seconds
interval=60

def adjustFan(intake, exhaust):
	global varSpeed
	if int(intake*1.5) == varSpeed:
		return
	elif intake >= maxTemp:
		speed=maxSpeed
	else:
		speed=int(intake*1.5)
	fan.setSpeed(speed)
	varSpeed=speed
	logg.inputSYS("Fanspeed is {!s}".format(speed))

def adjustLight(time):
	
	time=int(time)
	global rel4, statusRel4
	
	if time > lightOn and time < lightOff:
		if statusRel4:
			return
		switch=True
	else:
		if not statusRel4:
			return
		switch=False

	relay.set(rel4, switch)
	statusRel4=switch
	logg.inputSYS("Light is {!s}".format(statusRel4))

def main():
	logg.inputSYS("Started the raspiGrow system")
	while True:
		try:
			# The D18B20 sensors need to be read every time the while loop executes
			intake = float(temp.read(sens1))
			water = float(temp.read(sens2))
			exhaust = float(temp.read(sens3))

			adjustFan(int(intake), int(exhaust))
			adjustLight(strftime("%H"))
			logg.inputTMP("{!s}, {!s}, {!s}".format(intake, water, exhaust))
			sleep(interval)
		except KeyboardInterrupt:
			logg.inputSYS("Program terminated by user!")
			exit()

if __name__ == "__main__":
	main()

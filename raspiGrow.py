from time import strftime, sleep
import tempRead as temp
import fanControl as fan
#import humRead as hum
import relayControl as relay
import logg

# GPIO pins that controls the relay switch
rel1=22 # unused
rel2=23 # unused
rel3=24 # unused
rel4=25 # Light

# Status variables 
statusRel1=False
statusRel2=False
statusRel3=False
statusRel4=False
varSpeed=0

# The thought here is that when the temp reaches maxTemp, then maxSpeed is activated
maxDiff=4
maxTemp=30
maxSpeed=70

# In the example the script turns on at 6 in the morning and off at 10 in the evening
lightOn=6
lightOff=22

def adjustFan(intake, exhaust):
	global varSpeed
	intake=int(intake)
	exhaust=int(exhaust)
	diff=exhaust-intake
	diff=int(diff)

	if intake == varSpeed:
		return
	elif intake >= maxTemp or diff >= maxDiff:
		speed=maxSpeed
	else:
		speed=intake
	fan.setSpeed(speed)
	varSpeed=speed
	logg.inputSYS("Fanspeed is {!s}".format(speed))

def adjustLight(time):
	
	time=int(time)
	global rel4, statusRel4
	
	if time > lightOn and time < lightOff:
		if statusRel4:
			return
		check=True
	else:
		check=False
	relay.set(rel4, check)
	statusRel4=check
	logg.inputSYS("Light is {!s}".format(statusRel4))

def main():
	logg.inputSYS("Started the raspiGrow system")
	while True:
		try:
			# The D18B20 sensors need to be read every time the while loop executes
			intake = float(temp.read('28-000006876fc9'))
			water = float(temp.read('28-00000688212c'))
			exhaust = float(temp.read('28-0000068944b8'))

			adjustFan(intake, exhaust)
			adjustLight(strftime("%H"))
			logg.inputTMP("{!s}, {!s}, {!s}".format(intake, water, exhaust))
			sleep(60)
		except KeyboardInterrupt:
			logg.inputSYS("Program terminated by user!")
			exit()

if __name__ == "__main__":
	main()

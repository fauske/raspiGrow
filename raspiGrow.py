#If running this script with python 2.7, try to change configparser to ConfigParser

from time import strftime, sleep
import configparser
import tempRead as temp
import fanControl as fan
import relayControl as relay
import logg

cfg = configparser.ConfigParser()
cfg._interpolation = configparser.ExtendedInterpolation()
confFile='config.ini'
cfg.read(confFile)

def adjustFan(temp1):
	maxTemp = int(cfg.get("Fan", 'maxtemp'))
	if temp1 >= maxTemp:
		speed=temp1*2
	else:
		speed=int(temp1*1.5)
	fan.setSpeed(speed)
	return speed

def lightSwitch(time, lightStatus):
	sunrise = int(cfg.get("Light", 'sunrise'))
	sunset = int(cfg.get("Light", 'sunset'))
	relN = int(cfg.get("Light", 'relay'))

	if time > sunrise and time < sunset:
		check=True
		if not lightStatus:
			adjustLight(relN, check)
	else:
		check=False
		if lightStatus:
			adjustLight(relN, check)
	return check

def adjustLight(relN, switch):	
	relay.set(relN, switch)

def ConfigSectionMap(section):
	dict1 = {}
	options = config.options(section)
	for option in options:
		try:
			dict1[option] = config.get(section, option)
			if dict1[option] == -1:
				DebugPrint("skip: %s" % option)
		except:
			print("exception on %s!" % option)
			dict1[option] = None
	return dict1

def reReadConfig():
	cfg.read(confFile)

def main():
	logg.inputSYS("Started the raspiGrow system")
	sens1 = cfg.get("Sensors", 'sensor1')
	sens2 = cfg.get("Sensors", 'sensor2')
	sens3 = cfg.get("Sensors", 'sensor3')

	lightStatus=False
	fanStatus=0

	while True:
		try:
			# Get settings and values
			reReadConfig()
			intake = float(temp.read(sens1))
			water = float(temp.read(sens2))
			exhaust = float(temp.read(sens3))
			maxtemp = int(cfg.get("Fan", 'maxtemp'))
			relN = int(cfg.get("Light", 'relay'))
			time=int(strftime("%H"))



			check = lightSwitch(time, lightStatus)
			if check != lightStatus:
				logg.inputSYS("Light is "+str(check))
			lightStatus=check

			check=int(intake)
			if check*1.5 != fanStatus or check*2 != fanStatus:
				adjustFan(check)
				flog="Fanspeed is: "+str(fanStatus)+"%"
				logg.inputSYS(flog)
			fanStatus=check

			logg.inputTMP("{!s}, {!s}, {!s}".format(intake, water, exhaust))
			sleep(int(cfg.get("System", 'interval')))
		except KeyboardInterrupt:
			logg.inputSYS("Program terminated by user!")
			exit()

if __name__ == "__main__":
	main()

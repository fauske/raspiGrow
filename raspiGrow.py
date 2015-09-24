#!/usr/bin/env python
#title          :raspiGrow.py
#description    :Automated hydroponic system.
#author         :O.A.Fauske
#date           :21.09.2015
#usage          :python3 raspiGrow.py
#python_version :3.0
#==============================================================================

from time import strftime, sleep
import configparser
import tempRead as temp
import fanControl as fan
import relayControl as relay
import logg

cfg = configparser.ConfigParser()
cfg._interpolation = configparser.ExtendedInterpolation()
confFile='/etc/raspiGrow/config.cfg'
cfg.read(confFile)

def adjustFan(temp, status):
	maxTemp = int(cfg.get("Fan", 'maxtemp'))
	if temp >= maxTemp:
		speed=int(temp*2)
		if speed == status:
			return speed
	else:
		speed=int(temp*1.5)
		if speed == status:
			return speed
	fan.setSpeed(speed)
	logWrite("Fans is: "+str(speed)+"%")
	return speed

def lightSwitch(time, lightStatus):
	sunrise = int(cfg.get("Light", 'sunrise'))
	sunset = int(cfg.get("Light", 'sunset'))
	relN = int(cfg.get("Light", 'relay'))

	if time >= sunrise and time <= sunset:
		check=True
	else:
		check=False

	if check != lightStatus:
		adjustLight(relN, check)
		logWrite("Light is: "+str(check))
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

def logWrite(string):
	logg.inputSYS(string)

def main():
	logWrite("Started the raspiGrow system")
	sens1 = cfg.get("Sensors", 'sensor1')
	sens2 = cfg.get("Sensors", 'sensor2')
	sens3 = cfg.get("Sensors", 'sensor3')

	lightStatus=None
	fanStatus=0

	while True:
		try:
			# Get settings and values
			reReadConfig()
			intake = float(temp.read(sens1))
			water = float(temp.read(sens2))
			exhaust = float(temp.read(sens3))
			time=int(strftime("%H"))

			# Light commands
			lightStatus = lightSwitch(time, lightStatus)

			# Fan commands
			fanStatus = adjustFan(int(intake), fanStatus)

			# Temperature log
			logg.inputTMP("{!s},{!s},{!s}".format(intake, water, exhaust))
			sleep(int(cfg.get("System", 'interval')))

		except KeyboardInterrupt:
			logg.inputSYS("Program terminated by user!")
			exit()

if __name__ == "__main__":
	main()

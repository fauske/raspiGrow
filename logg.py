from time import strftime
import os.path

def write(file, input, check=False):
	if not os.path.isfile(file):
		with open(file, 'a') as f:
			f.write("|--- Log created {!s}\n".format(strftime("%d.%m.%y %H:%M ---|")))
			if check:
				f.write("{!s}\n".format("Time, Intake, Water, Exhaust"))
	with open(file, 'a') as f:
		f.write("{!s} {!s}\n".format(strftime("%H:%M "), input))
	f.close()

def inputSYS(string):
	logfile='/var/log/raspiGrow.log'
	write(logfile, string)

def inputTMP(string):
	logfile='/var/log/temp.log'
	write(logfile, string, check=True)

def main():
	exit()

if __name__ == "__main__":
        main()

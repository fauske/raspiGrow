from time import strftime
import os.path

def inputSYS(input):
	loggfil='/var/log/raspiGrow.log'
	if not os.path.isfile(loggfil):
		with open(loggfil, 'a') as f:
			f.write("|--- Log created {!s}\n".format(strftime("%d.%m.%y %H:%M ---| ")))
	with open(loggfil, 'a') as f:
		f.write("{!s} {!s}\n".format(strftime("%H:%M "), input))
	f.close()

def inputTMP(input):
	loggfil='/var/log/tmp.log'
	if not os.path.isfile(loggfil):
		with open(loggfil, 'a') as f:
			f.write("|--- Log created {!s}\n".format(strftime("%d.%m.%y %H:%M ---| ")))
			f.write("{!s}\n".format("Time, Intake, Water, Exhaust") )

	with open(loggfil, 'a') as f:
		f.write("{!s} {!s}\n".format(strftime("%H:%M "), input))
	f.close()

def main():
	exit()

if __name__ == "__main__":
        main()

def read(tmp):
        try:
                string='/sys/bus/w1/devices/%s/w1_slave' % str(tmp)
                f = open(string, 'r')
                lines = f.readlines()
                f.close()
                pos = lines[1].find('t=')
                if pos != -1:
                        tmp_string = lines[1][pos+2:]
                        tmp = float(tmp_string)/1000
                        return format(tmp, '.2f')
        except:
                return '00.00'

def main():
	exit()

if __name__ == "__main__":
        main()

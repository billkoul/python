import subprocess
import sys, getopt

def main(argv):
	HOST="myhost.com"
	PROCESS = "mysql"

	COMMAND="ps aux | grep %s" % PROCESS

	ssh = subprocess.Popen(["ssh", "-p22", "username@%s" % HOST, COMMAND],
        	shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
    		error = ssh.stderr.readlines()
    		print >>sys.stderr, "ERROR: %s" % error
	else:
    		print result

if __name__ == "__main__":
   main(sys.argv[1:])

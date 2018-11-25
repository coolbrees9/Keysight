
import json
import sys
import os.path
import subprocess
from pathlib import Path

class VendingMachine(object):

	args = ["python3", "history.py"]
	tempinventory = sys.argv[1]
	temptransactions = sys.argv[2]
	inventory = open(sys.argv[1]).read()
	transactions = open(sys.argv[2]).read()
	seconds = 5
	#May need to change based on the filepath
	path = './'
	filename = 'output.json'
	writefilepath = './' + path + '/' + filename

	if os.path.isfile(tempinventory) and os.path.isfile(temptransactions):
		print("Starting Vending Machine\n")
		args.append(str(tempinventory))
		args.append(str(temptransactions))
		result = subprocess.run(args, check = True, shell = True, stdout = subprocess.PIPE, timeout = seconds)
		writefilepath.write_bytes(result.stdout)
		print("Finished Vending Machine. Output stored in ", filename)
	else:
		print("Invalid files entered")
		sys.exit(1)


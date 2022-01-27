import csv
import time

"""Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV)."""

successful_response = 200

with open('Jmeter_logs/Jmeter_log1.jtl', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for row in csv_reader:
		print (row[3])
		if row[3] != 200:
			print (row[2], row[3], row[4], row[8], row[0])

		# elif line[3] == 200:
		# 	print (line[3])
			
		# elif line[3] != 200:
		# 	print (line[2], line[3], line[4], line[8], line[0])
		# if 'responseCode' line[3] in csv_reader != 200
	


# https://gist.github.com/tomdottom/b017244a221f8076c4b0adc6feeeb921




# label
# responseCode
# responseMessage
# failureMessage
# timeStamp
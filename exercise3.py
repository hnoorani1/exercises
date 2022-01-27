import pandas as pd

"""Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV)."""

jmeter_log_files = ('Jmeter_logs/Jmeter_log1.jtl')

jmeter_records_df = pd.read_csv(jmeter_log_files)
not_two_hundred_codes_df = jmeter_records_df[jmeter_records_df['responseCode']!=200]
log_specific_headers = not_two_hundred_codes_df[['label', 'responseCode', 'responseMessage', 'failureMessage', 'timeStamp']]
print (log_specific_headers)

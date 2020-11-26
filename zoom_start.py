import datetime
import data
import os
# import subprocess

def openlink(s):
	os.system("start \"\" {}".format(s))
	# os.chdir("{}\\Zoom\\bin".format(os.getenv('APPDATA')))
	# print(s)
	# subprocess.run(["Zoom.exe", "--url=zoommtg://{}".format(s.replace('https://',''))])

def look_and_run():
	now = datetime.datetime.now()
	week = now.isoweekday()
	data.lectures.reverse()
	for d in data.lectures:
		if d[0] == week:
			t1 = datetime.datetime.combine(now.today(), datetime.datetime.strptime(d[1], '%H:%M').time())
			t2 = datetime.datetime.combine(now.today(), datetime.datetime.strptime(d[2], '%H:%M').time())
			if t1 - datetime.timedelta(minutes=15) < now and t2 > now:
				print(d[3])
				if 'zoom' in d[3]: openlink(d[3])
				if 'gotomeeting' in d[3]: openlink(d[3])
				return True

	return False

look_and_run()

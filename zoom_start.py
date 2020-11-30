import datetime
import data
import os
# import subprocess

def openlink(s):
	print("Openning {}".format(s))
	os.system("start \"\" {}".format(s))
	# os.chdir("{}\\Zoom\\bin".format(os.getenv('APPDATA')))
	# print(s)
	# subprocess.run(["Zoom.exe", "--url=zoommtg://{}".format(s.replace('https://',''))])

def look_and_run():
	now = datetime.datetime.now()
	week = now.isoweekday()
	data.lectures.reverse()
	lect = []
	for d in data.lectures:
		# print(d)
		if d[0] == week:
			t1 = datetime.datetime.combine(now.today(), datetime.datetime.strptime(d[1], '%H:%M').time())
			t2 = datetime.datetime.combine(now.today(), datetime.datetime.strptime(d[2], '%H:%M').time())
			if t1 - datetime.timedelta(minutes=15) < now and t2 > now:
				lect.append(d)

	if len(lect)==1:
		if 'zoom' in lect[0][3]: openlink(lect[0][3])
		if 'gotomeeting' in lect[0][3]: openlink(lect[0][3])
		return True

	elif len(lect):
		lect.reverse()
		print("Choose lecture :")
		for i, d in enumerate(lect):
			print("{} -> {} ({}-{} {})".format(i+1,d[3] if len(d)==4 else d[4],d[1],d[2],['all','Mon','Tue','Wed','Thu','Fri','Sat','Sun'][d[0]]))

		l = int(input("choice (put 0 for nothing) : "))
		if l>0:
			if 'zoom' in lect[l-1][3]: openlink(lect[l-1][3])
			if 'gotomeeting' in lect[l-1][3]: openlink(lect[l-1][3])
			return True

	print("Nothing is now. Choose your lecture from all:")
	data.lectures.reverse()
	for i, d in enumerate(data.lectures):
		print("{} -> {} ({}-{} {})".format(i+1,d[3] if len(d)==4 else d[4],d[1],d[2],['all','Mon','Tue','Wed','Thu','Fri','Sat','Sun'][d[0]]))

	l = int(input("choice (put 0 for nothing) : "))
	if l>0:
		if 'zoom' in data.lectures[l-1][3]: openlink(data.lectures[l-1][3])
		if 'gotomeeting' in data.lectures[l-1][3]: openlink(data.lectures[l-1][3])
		return True

	return False

look_and_run()

import time

def dark_light():

	darks = {
		1: 16,
		2: 17,
		3: 18,
		4: 19,
		5: 19,
		6: 18,
		7: 18,
		8: 19,
		9: 18,
		10: 17,
		11: 18,
		12: 17
	}

	lights = {
		1: 8,
		2: 7,
		3: 6,
		4: 6,
		5: 6,
		6: 7,
		7: 8,
		8: 7,
		9: 7,
		10: 8,
		11: 9,
		12: 8
	}

	now = time.localtime()

	if now.tm_hour >= darks[now.tm_mon] or now.tm_hour < lights[now.tm_mon]:
		print "Don't even step out of your house. It's dark outside."
		return True
	else:
		print "Yes you can linger outside."
		return False
	return

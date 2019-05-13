def infiniteLoop(x):
	while True:
		print("do something with x")
	return x

5 in [5, 10, infiniteLoop(5)]
from datetime import datetime
import time


def isEven(value):
    start_time = datetime.now()
    print(value%2 == 0)
    print(datetime.now() - start_time)

def myEven(value):
	start_time = datetime.now()
	while True:
		
		value = value - 2
		
		if value==0:
			print(True)
			break

		elif value<2:
			print(False)
			break

	print(datetime.now() - start_time)

value = 500
	
#print("стандарт")
isEven(value)

#print("моё")
myEven(value)

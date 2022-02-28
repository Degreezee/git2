
def fibbonachi(end_number:int):
	if end_number <= 1:
		return end_number
	else:
		return fibbonachi(end_number - 1) + fibbonachi(end_number - 2)

def factorial(end_number:int):
	if end_number == 0:
		return 1
	else:
		return end_number * factorial(end_number - 1)
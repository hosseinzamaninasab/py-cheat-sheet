import math
number = input()
number = int(number)
def round(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

round_up = round(number, -1)
if round_up == number:
	print(int(round_up) + 10)
else:
	print(int(round_up))
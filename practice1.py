number = input()
if len(number) == 3 and not number[0] == '0' :
 	print(2*(int(number[-1::-1])))
 	
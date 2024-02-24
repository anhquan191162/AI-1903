from collections import Counter

'''
arr1 = list(int(y) for y in input("Enter values: ").split())
arr2 = list(int(x) for x in input('Enter values: ').split())
counter_arr1 = Counter(arr1)
counter_arr2 = Counter(arr2)

comb_counter = counter_arr1 + Counter(i for i in counter_arr2 if i not in counter_arr1)
comb_list = list(comb_counter.elements())
print(comb_list)
'''



fhand = open('D:\\txt\s.txt')
lines = []
for line in fhand:
    print(line.rstrip())
    lines.append(line)
    
print("=====================")

n = int(input("Enter value: "))
if n >= len(lines):
    print("nununu")

line = (lines[n])
words = line.split()
print(words)


from math import pi
def circle_or_square(rad, area):
	flag = ''
	square_per = int(area**0.5)*4
	cir = float(round(rad*2*pi, 2))
	if cir > square_per:
		flag = True
	else:
		flag = False
	return flag

print(circle_or_square(16, 625))
print(circle_or_square(8, 144))
print(circle_or_square(15, 400))
print(circle_or_square(5, 100))
print(circle_or_square(18, 900))
print(circle_or_square(1, 4))

print(int(round(50.69)))
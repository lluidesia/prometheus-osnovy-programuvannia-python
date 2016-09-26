import sys

num1 = int(sys.argv[1])
num2= int(sys.argv[2])

happy=0

for num in range(num1,num2+1):
	sum1= (int(num/100000))+(int(num/10000)-int(num/100000)*10)+(int(num/1000)-int(num/10000)*10)
	sum2= (int(num/100)-int(num/1000)*10)+(int(num/10)-int(num/100)*10)+(int(num/1)-int(num/10)*10)
	#print(sum1)
	#print(sum2)
	if sum1==sum2:
		happy=happy+1
		
print(happy)








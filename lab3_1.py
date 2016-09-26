
a = 55
b = 54.2
c = 0.8

if a<=0 or b<=0 or c<=0:
	print("not triangle")

elif a+b>c or a+c>b or b+c>a:
	print("triangle")
else:
	print("not triangle")
import sys

text = sys.argv[1]

while text.find("()")!=-1:
	text=text.replace("()", "")


if text=="":
	print("YES")
else:
	print("NO")


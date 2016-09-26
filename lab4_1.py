import sys

text = sys.argv[1].lower()
text=text.replace(" ", "")

text_reverse=text[::-1]

n=len(text)
is_palindrom="YES"

for i in range(n):
	if text[i] != text_reverse[i]:
		is_palindrom="NO"

print(is_palindrom)

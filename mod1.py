import sys

text = sys.argv[1].replace(" ","")
text=text[:len(text)-len(text)%5]
text_ab=""
answer=''
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in text:
	if letter.isupper():
		text_ab=text_ab+"b"
	else:
		text_ab=text_ab+"a"

i=0
for count in range(int(len(text_ab)/5)):
	let_ab=text_ab[i:i+5]
	answer=answer+alphabet[key.find(let_ab)]
	i=i+5

print(answer)
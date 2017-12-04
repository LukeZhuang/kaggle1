import codecs
import re
f=codecs.open('original_cata.txt',encoding='utf-8')

for line in f:
	l=line.strip()
	if 'gym' in re.split('\W',l.lower()):
		print(l)

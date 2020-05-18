import re

def cb(m):
	if m.group(0) == '&amp;':
		return '&'
	elif m.group(0) == '&gt;':
		return '>'
	elif m.group(0) == '&lt;':
		return '<'
	elif m.group(0) == '&nbsp;':
		return ' '

rexp = re.compile('<title>(.+)</title>',re.DOTALL)
rexp2 = re.compile('<!--.+?-->',re.DOTALL)
rexp3 = re.compile(r'<(script|style).*?>.*?</\1>',re.DOTALL)
rexp4 = re.compile('<a.*?href="(.+?)".*?>(.*?)</a>',re.DOTALL)
rexp5 = re.compile('<.+?>',re.DOTALL)
rexp6 = re.compile('&amp;|&gt;|&lt;|&nbsp;')
rexp7 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:
	text = fp.read()
		
	for m in rexp.finditer(text):
		print(m.group(1),'\n')
		
	text = rexp2.sub(' ',text)
	text = rexp3.sub(' ',text)
		
	for m in rexp4.finditer(text):
		print(m.group(1),m.group(2),'\n')
		
	text = rexp5.sub(' ',text)
	text = rexp6.sub(cb,text)
	text = rexp7.sub(' ',text)
	print(text,end='')

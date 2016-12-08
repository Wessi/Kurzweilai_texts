#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
#html_ascii_chars = {"&#33;":"!","&#35;":"#","&#36;":"$","&#37;":"%","&#38;":"&","&amp;":"&"}

html_ascii_chars ={ "&#32;":"","&#33;":"!","&#34;":"\"","&#35;":"#","&#36;":"$","&#37;":"%","&#38;":"&","&#39;":"'","&#40;":"(","&#41;":")","&#42;":"*","&#43;":"+","&#44;":",","&#45;":"-","&#46;":".","&#47;":"/","&#58;":":","&#59;":";","&#60;":"<","&#61;":"=","&#62;":">","&#63;":"?","&#64;":"@","&#91;":"[","&#92;":"\\","&#93;":"]","&#94;":"^","&#95;":"_","&#96;":"`","&#123;":"{","&#124;":"|","&#125;":"}","&#126;":"~","&#8211;":"–","&#8212;":"—","&#8216;":"‘","&#8230;":"..."}



def replace_ascii_chars(content,pattern="&#[1-9]{2,4};"): #the pattern to match the html_ascci characters is &#[1-9]{2,4}; it is set by default
	cleaned = bytearray(content)
	
	iterable_object = re.finditer(pattern,content)
	global html_ascii_chars
	while(True):
		try:
			obj = iterable_object.next().group()
			cleaned = re.sub(obj,html_ascii_chars[obj],cleaned)
		except(StopIteration):
			return cleaned
			break
	
	print(cleaned)

readed = " this is test string &#33; and &#38; &#96; &#038; AND &#126; then &#8211; &amp;"

print(replace_ascii_chars(readed,"&#[1-9]{2,4};"))



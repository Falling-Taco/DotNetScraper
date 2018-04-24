import re
import codecs

f = codecs.open('compiledxml.txt', 'r', encoding='utf-8')
fx = open('imglinks.txt', 'w+', encoding='utf-8')

for line in f:

	all_jpgs = [x for x in line.split('\t') if '.jpg' in x]
	all_ujpgs = [x for x in line.split('\t') if '.JPG' in x]
	all_jpegs = [x for x in line.split('\t') if '.jpeg' in x]
	all_pngs = [x for x in line.split('\t') if '.png' in x]

	for img in all_jpgs:
		a = 0
		if '"' in img:
			img = re.sub('"', '\"', img)
		if '<img alt="" src=' in img:
			img1 = img.split('<img alt="" src=')
			img2 = img1[1].split(' style="')
			a = 1
		if a == 1:
			fx.write(img2[0]+",")
		else:
			fx.write("\"http://www.homeschoolerpost.com/Files/"+img+"\",")

	for img in all_ujpgs:
		b = 0
		if '"' in img:
			img = re.sub('"', '\"', img)
		if '<img alt="" src=' in img:
			img1 = img.split('<img alt="" src=')
			img2 = img1[1].split(' style="')
			b = 1
		if b == 1:
			fx.write(img2[0])
		else:
			fx.write("\"http://www.homeschoolerpost.net/Files/"+img+"\",")

	for img in all_jpegs:
		c = 0
		if '"' in img:
			img = re.sub('"', '\"', img)
		if '<img alt="" src=' in img:
			img1 = img.split('<img alt="" src=')
			img2 = img1[1].split(' style="')
			c = 1
		if c == 1:
			fx.write(img2[0])
		else:
			fx.write("\"http://www.homeschoolerpost.net/Files/"+img+"\",")

	for img in all_pngs:
		d = 0
		if '"' in img:
			img = re.sub('"', '\"', img)
		if '<img alt="" src=' in img:
			img1 = img.split('<img alt="" src=')
			img2 = img1[1].split(' style="')
			d = 1
		if d == 1:
			fx.write(img2[0])
		else:
			fx.write("\"http://www.homeschoolerpost.net/Files/"+img+"\",")

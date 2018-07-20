# -*- coding: UTF-8 -*-
import urllib.request
from urllib.parse import quote

imglinks = []

for link in imglinks:
    try:
        filename = link.split('/')[-1]
        link = urllib.parse.quote(link,safe=':/')
        urllib.request.urlretrieve(link, filename)
    except:
        pass

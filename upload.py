#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re

brut = urllib2.urlopen("http://mafreebox.freebox.fr/pub/fbx_info.txt")
ulrate = re.search(".*ATM.*", brut.read()).group().split()[4]
print ulrate


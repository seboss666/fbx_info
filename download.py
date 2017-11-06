#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re

brut = urllib2.urlopen("http://mafreebox.freebox.fr/pub/fbx_info.txt")
dlrate = re.search(".*ATM.*", brut.read()).group().split()[2]
print dlrate


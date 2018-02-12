#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:08:04 2018

@author: ishanagarwal
"""

from urllib import request,parse

def profanity_check(text):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(text)
    connection = request.urlopen(url)
    output = connection.read()
    connection.close()
    if b'true' in output:
        print ("Profnaity Alert!!!")
    elif b'false'  in output:
        print ("No cuss word ---- Good to go :-)")
    else:
        print ("Can't read the file")
        
def read_file():
    file = open("/Users/ishanagarwal/Downloads/Udacity/Python Programmin/movie_quotes.txt")
    content = file.read()
    file.close()
    profanity_check(content)


read_file()


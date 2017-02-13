#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

def htmlHead():
    print ("Content-type: text/plain\n")


if __name__ == "__main__":
    try:
        htmlHead()
        data = cgi.FieldStorage()
        target = data["target"].value
        fileName = target + '.txt'
        f = open(fileName, 'a')
        f.write("B\n")
        f.close()
        print("DONE")
    except:
        print('oops')
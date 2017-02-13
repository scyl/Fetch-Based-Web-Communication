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
        f = open(fileName, 'r')
        lines = f.readlines()
        f.close()
        if len(lines) > 0:
            lines.reverse()
            print(lines.pop())
            f = open(fileName, 'w')
            while len(lines) > 0:
                f.write(lines.pop())
        else:
            print("N")
    except:
        print('oops')
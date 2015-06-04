#!/usr/bin/env python
from subprocess import call
import sys
from getpass import getpass

if len(sys.argv) == 1:
  print "Error: no arguments"
  quit()

username = raw_input("Enter username under which database should be created:")
password = getpass("Password:")

call("cd " + sys.argv[1], shell=True)
call(["touch", "Script1.py"])
call(["chmod", "755", "Script1.py"])
call(["touch", "Script2.py"])
call(["chmod", "755", "Script2.py"])

fout = open("Script1.py", "w")

script1Content = """#!/usr/bin/env python
import MySQLdb as msd
con = msd.connect("localhost", \"""" + username + "\", \"" +  password + """\")
with con:
  cur = con.cursor()
  cur.execute("DROP DATABASE IF EXISTS nub")
  cur.execute("CREATE DATABASE nub")
  cur.execute("USE nub")
  cur.execute("DROP TABLE IF EXISTS Times")
  cur.execute("CREATE TABLE Times(Time VARCHAR(50))")
"""

fout.write(script1Content)
fout.close()

fout = open("Script2.py", "w")

script2Content = """#!/usr/bin/env python
import MySQLdb as msd
from datetime import datetime
time = str(datetime.now().time())
con = msd.connect("localhost", \"""" + username + "\", \"" + password + """\")
with con:
  cur = con.cursor()
  cur.execute("USE nub")
  cur.execute("INSERT INTO Times VALUES(%s)", (time)) 
"""

fout.write(script2Content)
fout.close()

call("(crontab -l; echo \"*/10 * * * * " + sys.argv[1] + "/Script2.py\") | crontab", shell=True)

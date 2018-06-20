#!/system/bin/python
"""
Author: DedSecTL
Date  : 19-05-2017 (12:30)
Name  : Scriptux

Copyright (c) 2017, DedSecTL All rights reserved.
"""
import os
import sys
import time

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print "+-----------------------------------------+"
print "|--------------Scriptux v1.0--------------|"
print "+-----------------------------------------+"
print "| [+] Author: DedSecTL                    |"
print "| [+] Date  : 19-05-2017 (12:30)          |"
print "| [+] Team  : AndroSec1337 Cyber Team     |"
print "| [+] Deface Simple Script Maker          |"
print "| [+] Its free and easy to use            |"
print "+-----------------------------------------+"
print
print "Select:"
print
print "[1] Start"
print "[2] About"
print "[q] Exit"
print
aa = '"'
menu = raw_input("scriptux> ")

try:
   file = open("script.txt", 'w')
except(IOError):
   print ("ERROR")
   sys.exit()
  
if menu == '1':
  print "Simple Script"
  print
  defstyletitle_simple = raw_input("Title: ")
  defstyleimage_src = raw_input("Image: ")
  defstyleimage_width = raw_input("Width: ")
  defstyleimage_height = raw_input("Height: ")
  defstylehacked_simple = raw_input("Hacked by: ")
  defstylemessage_simple = raw_input("Message: ")
  defstyleteam_simple = raw_input("Team: ")
  time.sleep(1)
  print "[+] Success"
  print "[!] Script is save as script.txt"
  a = '"center"'
  aaa = '"#111111"'
  b = '"100%"'
  bb = '""'
  c = '"0"'
  d = '"align"'
  e = '"#000000"'
  f = '"10"'
  gg = '"1"'
  h = '"#ffffff"'
  hh = '"#b21f25"'
  hhh = '"#333333"'
  
  file.write(" <body bgcolor=black>\n")
  file.write("\n")
  file.write("<br><title>"+defstyletitle_simple+"</title></br>\n")
  file.write("<td><div align="+a+">\n")
  file.write("</div>        <table width="+b+" border="+c+" cellpadding="+c+" cellspacing="+c+">\n")
  file.write("          <tbody><tr>\n")
  file.write("     <center><img src="+aa+""+defstyleimage_src+""+aa+" alt="+bb+" width="+aa+""+defstyleimage_width+""+aa+" height="+aa+""+defstyleimage_height+""+aa+" align="+d+"></a></center>\n")
  file.write("          </tr>\n")
  file.write("        </tbody></table>\n")
  file.write("<table width="+b+" bgcolor="+e+" border="+c+" cellpadding="+f+" cellspacing="+gg+">\n")
  file.write("\n")
  file.write("  <tbody><tr bgcolor="+h+">\n")
  file.write("    <td bgcolor="+h+"><center><b><font color="+hh+">Hacked By "+defstylehacked_simple+"</font></b></center></td>\n")
  file.write("\n")
  file.write("  </tr>\n")
  file.write("\n")
  file.write("  <tr bgcolor="+hhh+">\n")
  file.write("    <td bgcolor="+aaa+"><center><center><font color="+hh+"><b><br>"+defstylemessage_simple+"</center>\n")
  file.write("      <br><center>"+defstyleteam_simple+"</b></center>\n")
  file.write("\n")
  file.write("\n")
  file.write("   </td></tr><tr bgco")
  sys.exit()
  
if menu == '2':
  print "Scriptux v1.0 19-05-2017 (12:30)"
  print "Author: DedSecTL"
  print "Team  : AndroSec1337 Cyber Team"
  print "Disclaimer: This tool is for educational purpose only."
  print "Thanks to:"
  print "[+] ./Xi4u7"
  print "[+] Mr_/bon'007"
  print "[+] Why"
  print "[+] Fajar"
  print "[+] Ananta Tarigan"
  print "[+] TgrCyber_Dotcoid"
  print "[+] m4z.pH4L(oN"
  print "[+] Aan Pranesia"
  print "[+] V-Z3RO"
  print "For the support..."
  
if menu == 'q':
  print "Exiting..."
  sys.exit()
from sys import argv
import re
script, filename ,erlog = argv
#print "enter the file name u want to read"
#t = raw_input()
#print " enter the file name u want to write"
#x = raw_input()

txt = open (filename,"r")  #open file
out = open(erlog,'w')      #write file

count = 0
for line in txt:
#    if "Path" in line and "Exception"  in line and "GET" in line and "POST" in line:
    	m = re.search("(?<=Path: ).*(?=Exception).*(?=GET)",line)
    	if (m):
    		 output = out.write(m.group()+"\n\n")
    		 count += 1
    		#print m
    # if "/api/v2/post-gcm/" in line:
    # 	output = out.write(line)
    # 	count1 += 1



print "count : "
print count




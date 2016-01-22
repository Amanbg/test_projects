from sys import argv
import re
script, filename ,erlog = argv


txt = open(filename,"r")  #open file
out = open(erlog,'w')      #write file

count = 0
#dict[] = 0
for line in txt.readlines():

   # if "Path" in line and "Exception"  in line and "GET" in line and "POST" in line
        #m1 = re.search("(?<=Path:)(?P<path1>.*)(?= GET:)",line)
        m2 = re.search("(\d+\w+)+/(?P<detail>.*)/(\w+[a-z-]+)",line)
        #m3 = re.search("(?<=Path:)(?P<path2>.*)(?=; Data)",line)
    	
    	#if m1 and m1.group():
    		#output = out.write(m1.group('path1')+"\n")
    	if m2 and m2.group():
    		output = out.write(m2.group('detail')+"\n")
        #elif m3 and m3.group():
        #   output = out.write(m3.group('path2')+"\n")
                #print m2.group('detail')
    	#	count += 1
    	# elif m and m.group(3):
    	# 	output = out.write(m.group(3)+"\n")
    	# 	count += 1

    		#print m
    # if "/api/v2/post-gcm/" in line:
    # 	output = out.write(line)
    # 	count1 += 1


#?<=Path:
#?=Exception
print "count : "
#print count




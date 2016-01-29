from sys import argv
import re
import pdb
script ,filename, method, url = argv

count = 0
totalcount = 0
errors = {}

for line in open(filename):
	if method == 'GET' in line and url in line:
		  # print "hww"
	  	totalcount += 1
	  	m1 = re.search("http:(?P<url_path1>.*)",line)
		if m1 and m1.group():
			url_path = m1.group('url_path1')
		    # #url_path = url_path.split('HTTP')[0]
			url_path = url_path.split('?')[0]
			url_path = url_path.split('" "Mozilla')[0]
			
			# print url_path
		 #  	else:
		 #   			url_path = "-"
   #     			 	 totalcount += 1
   #  			 prepare get url for 2nd file
	   
			# pdb.set_trace()
			if url in errors:
				if url_path in errors[url]:
					errors[url][url_path] +=1
				else:
					errors[url][url_path] = 1
			else:
				errors[url] = {url_path: 1}

	elif method == 'POST' in line and url in line:
		  # print "hww"
	  	totalcount += 1
	  	m1 = re.search("http:(?P<url_path1>.*)",line)
		if m1 and m1.group():
			url_path = m1.group('url_path1')
		    # #url_path = url_path.split('HTTP')[0]
			url_path = url_path.split('?')[0]
			url_path = url_path.split('" "Mozilla')[0]
			
			# print url_path
		 #  	else:
		 #   			url_path = "-"
   #     			 	 totalcount += 1
   #  			 prepare get url for 2nd file
	   
			# pdb.set_trace()
			if url in errors:
				if url_path in errors[url]:
					errors[url][url_path] +=1
				else:
					errors[url][url_path] = 1
			else:
				errors[url] = {url_path: 1}

 
	elif method == 'PUT' in line and url in line:
		  # print "hww"
	  	totalcount += 1
	  	m1 = re.search("http:(?P<url_path1>.*)",line)
		if m1 and m1.group():
			url_path = m1.group('url_path1')
		    # #url_path = url_path.split('HTTP')[0]
			url_path = url_path.split('?')[0]
			url_path = url_path.split('" "Mozilla')[0]
			
			# print url_path
		 #  	else:
		 #   			url_path = "-"
   #     			 	 totalcount += 1
   #  			 prepare get url for 2nd file
	   
			# pdb.set_trace()
			if url in errors:
				if url_path in errors[url]:
					errors[url][url_path] +=1
				else:
					errors[url][url_path] = 1
			else:
				errors[url] = {url_path: 1}



print "\nTotal Count : " + str(totalcount)


for key, value in errors.items():
        count = sum(value.values())
        print "Total Hit Url : "+ str(count) +" "+key + '\n'
        for k,v in value.items():
            print "\t" + "Count : "+ str(v) +" "+k + '\n'


if count == 0:
	unreff_url = totalcount
	print "Unreferred Urls : "+ str(unreff_url)
else:
	unreff_url = totalcount - count
	print "Unreferred Urls : " + str(unreff_url)


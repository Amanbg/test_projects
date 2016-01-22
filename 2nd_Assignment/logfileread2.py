from sys import argv
import re
script, filename ,erlog,errcount = argv
#print "enter the file name u want to read"
#t = raw_input()
#print " enter the file name u want to write"
#x = raw_input()

txt = open (filename,"r")  #open file
out = open(erlog,'w')      #write file

count = 0
totalcount = 0
errors = {}

#dict[] = 0
for line in txt.readlines():

   # if "Path" in line and "Exception"  in line and "GET" in line and "POST" in line
    	m1 = re.search("Path: \s*(?P<error_path>.*)Exception:\s*(?P<exception_value>.*)GET:",line)
        if m1 and m1.group():

            # prepare error path
            error_path = m1.group('error_path')
            error_path = error_path.split('?')[0]


            # prepare exception value
            exception_value = m1.group('exception_value')
            # exception_value = exception_value.split('Exception: ')[1]

            for exception_type in ['ValidationError', '[Errno 2] No such file or directory:']:
                if exception_type in exception_value:
                    exception_value = exception_type

            # write to 1st file        
            output = out.write('{} {} \n'.format(error_path, exception_value))
            totalcount += 1

            # prepare errors for 2nd file
            if error_path in errors:
                if exception_value in errors[error_path]:
                    errors[error_path][exception_value] +=1
                else:
                    errors[error_path][exception_value] = 1
            else:
                errors[error_path] = {exception_value: 1}


# import ipdb; ipdb.set_trace()


    
# for count elements in the particular url and write to another file
with open(errcount, 'w') as f:
    for key, value in errors.items():
        count = sum(value.values())
        f.write("count :"+ str(count) +" "+key + '\n')
        for k,v in value.items():
            f.write("\t" + "count :"+ str(v) +" "+k + '\n')

    # f.write(errors.keys(), '')

f.close()
            # print m1
            #output = out.write(m1.group('hello')+"\n")
        #m1 = re.search("(?<=Exception:)(?P<xam>.*)..../\w+/",line) # for resumes error
        #m2 = re.search("(?<=Exception:)(?P<gol>.\w*.)(.\w+)",line) #for validation error
        #m2 = re.search("(?<=Exception:)(?P<gol>.ValidationError)",line)
        #m3 = re.search("(?<=Exception:)(?P<exc>\s.*)",line) #for others
    	#m2 = re.search("(?<=Path:)(?P<path2>.*)(?=; Data:)",line)

        #m4 = re.search("(?<=Exception: )(?P<hello>([/['\w:=;\s>//]+)?)",line)
        # m4 = re.search("(?<=Exception: )(?P<hello>(['\w:=;\s>//]+)?)",line)
        # m5 = re.search("(?<=Exception: )(?P<xam>.*)(?<=Resumes)",line)
        # if m4 and m4.group():
        #          output = out.write(m4.group('hello')+"\n")
        #          count += 1
        # elif m5 and m5.group():
        #         output = out.write(m5.group('xam')+"\n")
        #         count +=1
        #m6 = re.search("(?<=Exception: )(?P<hello>(['\-\w:=;\s>//]+)?([\['\w\s\]]+)?)",line)
        # m6 = re.search("(?<=Exception: )(?P<hello>(['\-\w:=;\s>]+)?([\"\w]+)?([\['\w\s:\]]+)?)",line)
        # if m6 and m6.group():
        #     output = out.write(m6.group('hello')+"\n")
        #     count += 1
    	# if m1 and m1.group():
     #            output = out.write(m1.group('xam')+"\n")
     #            #count += 1
    	# elif m2 and m2.group():
    	#         output = out.write(m2.group('gol')+"\n")
    	       #count += 1
        # if m3 and m3.group():
        #     output = out.write(m3.group('exc')+"\n")
        #     count +=1
            #print m3
    	  	
    	
            # for extract urls from the log files --> http://[a-zA-Z+.-/]+
    		
    # if "/api/v2/post-gcm/" in line:
    # 	output = out.write(line)
    # 	count1 += 1


#?<=Path:
#?=Exception
print "count : "
print totalcount




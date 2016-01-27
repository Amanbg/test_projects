from sys import argv
import re
# script, filename ,erlog,errcount = argv
script, filename ,erlog,errcount = argv

txt = open (filename,"r")  #open file
out = open(erlog,'w')      #write file

count = 0
totalcount = 0
errors = {}                             #m1 = re.search("http:(?P<url_path1>.[/a-z-.-@]+)/?/",line) for url
                                        #m1 = re.search("GET \s*(?P<get_path1>.[/a-z-.-@]+)/?/",line) for get path
#dict[] = 0                             #PUT \s*(?P<put_path1>.[/a-z-.-@]+)\s+HTTP
for line in txt.readlines():

   # if "Path" in line and "Exception"  in line and "GET" in line and "POST" in line
    	# m1 = re.search("Path: \s*(?P<error_path>.*)Exception:\s*(?P<exception_value>.*)GET:",line)
        m1 = re.search("GET \s*(?P<get_path1>.*)http:(?P<url_path1>.*)",line)
        m2 = re.search("POST \s*(?P<post_path1>.*)http:(?P<url_path2>.*)",line)
        m3 = re.search("PUT \s*(?P<put_path1>.*)http:(?P<url_path3>.*)",line)

        if m1 and m1.group():
        # output = out.write(m1.group('get_path1')+'\n')
        # count += 1
        # if m2 and m2.group():
        #     output = out.write(m2.group('post_path1')+'\n')
 
        # if m1 and m1.group():
        #     output = out.write('{} {} \n'.format('get_path1','url_path1'))
            get_path = m1.group('get_path1')
            get_path = get_path.split('?')[0]
            get_path = get_path.split('HTTP')[0]
           # output = out.write(get_path+'\n')            

            url_path = m1.group('url_path1')
            #url_path = url_path.split('HTTP')[0]
            url_path = url_path.split('?')[0]
            url_path = url_path.split('" "Mozilla')[0]
            output = out.write('{} {} \n'.format(get_path, url_path))
            totalcount += 1
            # prepare get url for 2nd file
            if get_path in errors:
                if url_path in errors[get_path]:
                    errors[get_path][url_path] +=1
                else:
                    errors[get_path][url_path] = 1
            else:
                errors[get_path] = {url_path: 1}

        elif m2 and m2.group():
            #count += 1
        
 
            post_path = m2.group('post_path1')
            post_path = post_path.split('?')[0]
            post_path = post_path.split('HTTP')[0]
           # output = out.write(get_path+'\n')            

            url_path = m2.group('url_path2')
            #url_path = url_path.split('HTTP')[0]
            url_path = url_path.split('?')[0]
            url_path = url_path.split('" "Mozilla')[0]
            output = out.write('{} {} \n'.format(post_path, url_path))
            totalcount += 1
        #prepare post url for 2nd file
            if post_path in errors:
                if url_path in errors[post_path]:
                    errors[post_path][url_path] +=1
                else:
                    errors[post_path][url_path] = 1
            else:
                errors[post_path] = {url_path: 1}

        elif  m3 and m3.group():
           # count += 1
        # if m2 and m2.group():
        #     output = out.write(m2.group('post_path1')+'\n')
 
            put_path = m3.group('put_path1')
            put_path = put_path.split('?')[0]
            put_path = put_path.split('HTTP')[0]
           # output = out.write(get_path+'\n')            

            url_path = m3.group('url_path3')
            #url_path = url_path.split('HTTP')[0]
            url_path = url_path.split('?')[0]
            url_path = url_path.split('" "Mozilla')[0]
            output = out.write('{} {} \n'.format(put_path, url_path))
            totalcount += 1

            # prepare put url for 2nd file
            if put_path in errors:
                if url_path in errors[put_path]:
                    errors[put_path][url_path] +=1
                else:
                    errors[put_path][url_path] = 1
            else:
                errors[put_path] = {url_path: 1}


# for count elements in the particular url and write to another file
with open(errcount, 'w') as f:
    for key, value in errors.items():
        count = sum(value.values())
        f.write("count :"+ str(count) +" "+key + '\n')
        for k,v in value.items():
            f.write("\t" + "count :"+ str(v) +" "+k + '\n')

f.close()

print "totalcount : "
print totalcount
        ###########################################################################################
        
#         if m1 and m1.group():

#             # prepare error path
#             error_path = m1.group('error_path')
#             error_path = error_path.split('?')[0]


#             # prepare exception value
#             exception_value = m1.group('exception_value')
#             # exception_value = exception_value.split('Exception: ')[1]

#             for exception_type in ['ValidationError', '[Errno 2] No such file or directory:']:
#                 if exception_type in exception_value:
#                     exception_value = exception_type

#             # write to 1st file        
#             output = out.write('{} {} \n'.format(error_path, exception_value))
#             totalcount += 1

#             # prepare errors for 2nd file
#             if error_path in errors:
#                 if exception_value in errors[error_path]:
#                     errors[error_path][exception_value] +=1
#                 else:
#                     errors[error_path][exception_value] = 1
#             else:
#                 errors[error_path] = {exception_value: 1}


# # import ipdb; ipdb.set_trace()


    
# # for count elements in the particular url and write to another file
# with open(errcount, 'w') as f:
#     for key, value in errors.items()
#         count = sum(value.values())
#         f.write("count :"+ str(count) +" "+key + '\n')
#         for k,v in value.items():
#             f.write("\t" + "count :"+ str(v) +" "+k + '\n')

    # f.write(errors.keys(), '')

#f.close()
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





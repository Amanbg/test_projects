
#execfile("logfileread.py")
from sys import argv
script, filename,errcount = argv

txt = open(filename,"r")
# out = open(errcount,"w")
errors = {}
# count = 0
# found = 0

# string = "/api/v2/search/candidate"
#  count1 = 0
# for line in txt.readlines():
	
# 	if string in line:
# 		found +=1
# 		output = out.write(line)

# import ipdb; ipdb.set_trace()

for path in txt.readlines():
	if path in errors:
		errors[path] += 1
	else:
		errors[path] = 1

with open(errcount, 'w') as f:
	for key, value in errors.items():
		f.write("count :"+ str(value)+ " " + key)
	# f.write(errors.keys(), '')

f.close()
		

#print found
# for line in txt:
# 	string = line
# 	m = search(line)
#  	if (m):
#  		count += 1
#  		#string = line
#  		print string
#  		print count
#  		#string1 = line.count(line)
#  		output = out.write(line+count)
#  	string = line 	
#  	count1 += 1
#     output = out.write(string+"\n")



	
import re

email = "Jan  7 11:43:28 candapp148 apache2[19293]: [:error] [pid 19293:tid 139720851453696] ERROR Path: http://www.shine.com/myshine/block_recruiter/ Exception: 'NoneType' object has no attribute 'encode' GET: <QueryDict: {}> POST: <QueryDict: {}>"

#m = email.strip()
#for line in email:
pattern = "(http:.*)(Exception:.*)[^>}{ :tciDyreuQ<TSOPEG]"
prog = re.compile(pattern)

result = prog.match(email)

#m = re.match(pattern,email)

print result
#ma = email.split("Path:")

#for lin in ma:
 #     print lin

#print ma

#final regular expression is :

(?<=Path: ).*(?=Exception).*(?=GET)


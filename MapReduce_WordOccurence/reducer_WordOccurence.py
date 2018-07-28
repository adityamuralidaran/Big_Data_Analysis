#!/usr/bin/python

# Aditya Subramanian Muralidaran


import sys

curr_key = None
curr_val = 0

for key_val in sys.stdin:
	key,str_val = key_val.split("\t",1)

	try:
		val = int(str_val)
	except:
		continue
	if(curr_key==key):
		curr_val=curr_val+val;
	else:
		if(curr_key is not None):			
			print(curr_key+"\t"+str(curr_val))
		curr_key=key;
		curr_val=val;
print(curr_key+"\t"+str(curr_val))		






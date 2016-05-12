import sys
import random
import string

if len(sys.argv) != 4:
	print "Usage: create_data name_num low_bound up_bound"
	sys.exit()

name_num = int(sys.argv[1])
low_bound = int(sys.argv[2])
up_bound = int(sys.argv[3])
name_len = 5

char_list = []
for i in range(26):
	char_list.append(chr(ord('a') + i))
for i in range(name_num):
	c = ''
	for j in range(name_len):
		c = c + random.sample(char_list, 1)[0]
	print c , int(random.randint(low_bound, up_bound))

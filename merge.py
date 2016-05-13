# Program
#	This programme merge data for each map file and group them
# Usage:
#	merge.py mapper_num
# Output:
#	./map/i.merge (i=1:n)

import sys
import os


if len(sys.argv) != 2:
	print "Usage: merge.py mapper_num"
	sys.exit()

mapper_num = int(sys.argv[1])
if not os.path.exists("./merge/"):
	os.mkdir("./merge/")

for i in range(1, mapper_num + 1):
	fp_map = open("./map/%d.map"%(i), "r")
	fp_merge = open("./merge/%d.merge"%(i), "w")
	mp = []
	last_h = -1
	cnt = -1
	for line in fp_map.readlines():
		record = line[0:-1]
		record_list = record.split(' ')
		h = int(record_list[0])
		name = record_list[1]
#		print h, name
#		mp.setdefault(h, []).append(name)
		if h != last_h:
			mp.append([h,[name]])
			cnt = cnt + 1
			last_h = h
		else:
			mp[cnt][1].append(name)
	for i in range(0, len(mp)):
#		print mp[i][0],
		fp_merge.write("%d "%(mp[i][0]))
		for j in range(0, len(mp[i][1])):
#			print mp[i][1][j],
			fp_merge.write("%s "%(mp[i][1][j]))
#		print
		fp_merge.write("\n")
	fp_map.close()
	fp_merge.close()

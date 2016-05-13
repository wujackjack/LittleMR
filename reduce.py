# Program 
# 	This program reduce data after merge.py
# Usage:
#	python reduce.py mapper_num
# Output:
#	stdout on screen
import os
import commands
import Queue
import sys

if len(sys.argv) != 2:
	print "Usage: reduce.py mapper_num"
	sys.exit()

mapper_num = int(sys.argv[1])

fp_vec = []

for i in range(1, mapper_num + 1):
	fp = open("./merge/%d.merge"%(i), "r")
	fp_vec.append(fp)

pq = Queue.PriorityQueue()

for i in range(mapper_num):
	line = fp_vec[i].readline()
	if line:
		line = line[0:-1]
		re = line.split()
		pq.put((int(re[0]), [i, re[1:]]))
# the item structure in priorityQueue is [height, [map_idx, [name_list...]]]
res = []
last_height = -1
cur_row = -1
while not pq.empty():
	cur = pq.get()
	if not res:
		res.append([cur[0], cur[1][1]])
		last_height = cur[0]
		cur_row = cur_row + 1
	else:
		if cur[0] == last_height:
			for k in range(0, len(cur[1][1])):
				res[cur_row][1].append(cur[1][1][k])
		else:
			res.append([cur[0], cur[1][1]])
			last_height = cur[0]
			cur_row = cur_row + 1
	line = fp_vec[cur[1][0]].readline()
	if line:
		line = line[0:-1]
		re = line.split()
		pq.put((int(re[0]), [cur[1][0], re[1:]]))

for i in range(len(res)):
	for j in range(0, len(res[i][1])):
		print res[i][1][j], res[i][0]
	

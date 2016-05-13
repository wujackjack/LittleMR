# !/bin/bash
# This programme simulate the process of MapReduce. Sort students height.
# Usage: 
#	main.sh input_data
# Format of input_data: name height

if [ "$#" -ne 2 ]; then
	echo "Usage: main.sh input_data map_num"
	exit 0
fi

tmp=0
map_num=$2

if [ "$map_num" -le "$tmp" ]; then
	echo "Map num should be positive"
	exit 0
fi
echo "Map num equals:" $map_num

#mapper
rm -rf "./map"
mkdir "./map"
cat $1 | awk -v map_num="$map_num" ' \
{cur_file = (NR - 1) % map_num + 1; printf("%d %s\n", $2, $1) > "map/"cur_file".map"}'

#shuffle
for ((i=1;i<=$map_num;i++));
do
	sort -k 1 -n "./map/$i.map" -o "./map/$i.map"
done


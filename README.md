# LittleMR
A simple example of Mapreduce by shellscript, awk, python.

Main procedure controlled by shellscript, mapper by awk, merge and reduce by python.

For own study purpose.

Format of input file and output: `name` `height`

Procedure:

	python create_data.py name_number height_low_bound height_upper_bound > inputfile
	sh main.sh inputfile map_num
	python merge.py map_num 
	python reduce.py map_num

Input:

ytjyu 180

kpzbd 170

llohk 170

bhiil 180

blzzz 167

kvyrq 177

qrtce 168

wpnou 174

xmnpm 167

usxem 174

Output:

blzzz 167

xmnpm 167

qrtce 168

kpzbd 170

llohk 170

usxem 174

wpnou 174

kvyrq 177

bhiil 180

ytjyu 180

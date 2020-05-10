#!/bin/bash
#echo "type in timestep value: "
#read i 
./Allclean.sh
timestep=(5000 2000 1000)
for i in "${timestep[@]}" ; do
	./trajectory "${i}"

	gnuplot plotdata.gp

	mkdir -p "results/h${i}/"
	mv trajectory.png "results/h${i}/moon-trajectory.png"
	mv energy.png "results/h${i}/moon-energy.png"

	echo "done with timestep h${i}"
done

echo "DONE!!"

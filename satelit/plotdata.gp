set terminal png
set output "trajectory.png"

set title "trajectory"
set grid
plot "solCollatz.dat" using 1:2 with linespoints pt 0.7 ps 0.1 lt rgb "red", \
     "solRK.dat" using 1:2 with linespoints pt 0.7 ps 0.1 lt rgb "blue"

set terminal png
set output "energy.png"

set title "energy"
set grid
set ylabel "[gJ]"
set xlabel "[t]"
set yrange [:-7.5e19]
plot "solCollatz.dat" using 3:4 with linespoints pt 0.7 ps 0.1 lt rgb "red", \
     "solRK.dat" using 3:4 with linespoints pt 0.7 ps 0.1 lt rgb "blue"

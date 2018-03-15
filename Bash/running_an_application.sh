#Running in the foreground

cmd="myprog -c file.1 -p -f -q"
$cmd < my_input_file

#output is directed to the file res
$cmd < my_input_file > res

#process res file by Sed, Awk, Perl, or Python

#Running in the background

myprog -c file.1 -p -f -q < my_input_file &

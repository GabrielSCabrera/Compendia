rm -v *.txt # stdout and stderr are displayed on the terminal
rm -v *.txt 1> out.txt # Redirect stdout to a file, same as >
rm -v *.txt 2> err.txt # Redirect stderr to a file
rm -v *.txt &> outerr.txt # Redirect stdout and stderr to a file

#Print to stderr with:
echo "Wrong arguments" >&2

#Redirects and pipes can be combined:
./compile 2>&1 | less # View both stdout and stderr in less

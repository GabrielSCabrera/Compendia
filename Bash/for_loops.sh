# For loops for file management
files=`ls *.tmp`

for file in $files
do
  echo removing $file
  rm -f $file
done

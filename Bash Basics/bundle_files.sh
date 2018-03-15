#Pack a series of files into one file
#Executing this single file as a Bash script packs out all the individual files again

#Usage:

bundle file1 file2 file3 > onefile # pack
bash onefile # unpack

#Writing "bundle" is easy:
#/bin/sh
for i in $@; do
  echo "echo unpacking file $i"
  echo "cat > $i <<EOF"
  cat $i
  echo "EOF"
done

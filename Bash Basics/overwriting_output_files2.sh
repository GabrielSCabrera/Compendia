dir=$case
# check if $dir is a directory:
if [ -d $dir ]
  # exit script to avoid overwriting data
  then
    echo "Output directory exists, provide a different name"
    exit
  fi
mkdir $dir  # create a new directory $dir
cd $dir     # move to $dir

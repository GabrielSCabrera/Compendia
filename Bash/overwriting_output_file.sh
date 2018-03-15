jobdir=$PWD/$(date)
mkdir $jobdir
cd $jobdir

./pulse app -cmt $CMT -cname $CASE < $INFILE | tee $OUTFILE
cd ..
if [ -L 'latest' ]; then
  rm latest
fi
ln -s $jobdir latest

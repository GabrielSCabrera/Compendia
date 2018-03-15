CASE='textbox'
CMT='WinslowRice'
if [ $# -gt 0 ]; then
  CMT=$1
fi
INFILE='ellipsoid test.i'
OUTFILE='main_output'

./pulse app -cmt $CMT -cname $CASE < $INFILE | tee $OUTFILE

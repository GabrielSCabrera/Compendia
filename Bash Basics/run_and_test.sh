#run_and_test.sh
$@

if [ "$?" == "0" ]; then
  echo "Hurray, everything went fine."
else
  echo "Oops, there was an error."
fi

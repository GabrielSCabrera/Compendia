#the 'then' statement can also appear on the list line:
if [ -d $dir ];
then
  exit
fi

# another form of if-tests:
if test -d $dir; then
  exit
fi

# and a shortcut:
[ -d $dir ] && exit
test -d $dir && exit

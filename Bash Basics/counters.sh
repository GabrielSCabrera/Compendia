#Declare an integer counter

declare -i counter
counter=0
# arithmetic expressions must appear inside (( ))
((counter++))
echo $counter # yields 1

#For-loop with counter

declare -i n; n=1
for arg in $@; do
  echo "command-line argument no. $n is <$arg>"
  ((n++))
done

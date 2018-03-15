ls -l | grep 3331 # the pipe sends the output of one command as input to the next
#will list all files having 3331 as part of the name
#grep is a filter searching for the given keyword

ls -s | sort -rn #sends files with size to "sort" -rn (reverse numerical sort) to get a list of files
#sorted after their sizes

du -a assignments | sort -rn | less #makes a new application: sort all files in a directory tree "assignments"
#with the largest files appearing first, and equip the output with paging functionality

#Inefficient Code:
ls > files && grep 2017 < files

#Better Code:
ls | grep 2017

#Inefficient Code:
cat INF3331-$username | ./test

#Better Code:
./test < INF3331-$username

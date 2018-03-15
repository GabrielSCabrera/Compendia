#A while loop can always replace a for loop, but not vice-versa

start = 1
finish = 11

while start < finish:       #While loop requires a predetermined set of values.
    print start             #This will repeat itself and print values between
    start += 1              #1 and 10, so remember to set finish to n + 1

start = 1
finish = 11
increment = 2

for i in range(start, finish, increment):   #Increment will determine how many
    print i                                 #numbers to jump by in each
                                            #repetition
loop_list = [1,2,3,4,5,6,7,8,9,10]

for j in loop_list:                     #You can also use a list instead of a
    print loop_list[j-1]                #variable as your loop parameter

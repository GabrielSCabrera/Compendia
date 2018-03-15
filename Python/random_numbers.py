import random, numpy
a = 2
b = 4
N = 5   #number of values to create in array

m = 1   #Gaussian m
s = 5   #Gaussian s

i = 5   #Seed value

mylist = [0,1,2,3,4,5]

#Uniform numbers in range [0,1)

rand = random.random()
nprand = numpy.random.random(N)

#Uniform numbers in range [a,b)

rand = random.uniform(a,b)
nprand = numpy.random.uniform(a,b,N)

#Integers in [a,b]

rand = random.randint(a,b)
nprand = numpy.random.randint(a,b,N)
nprand = numpy.random.random_integers(a,b,N)

#Gaussian numbers
rand = random.gauss(m,s)
nprand = numpy.random.normal(m,s,N)

#Setting a seed

rand = random.seed(i)
nprand = numpy.random.seed(i)

#Shuffling a list

rand = random.shuffle(mylist)
nprand = numpy.random.shuffle(mylist)

#Pick a random list element

rand = random.choice(mylist)

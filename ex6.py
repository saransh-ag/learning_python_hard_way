# Exercise 6
# https://learnpythonthehardway.org/book/ex6.htm

#defining string x,binary and do_not
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#concat string in y
y = "Those who know %s and those who %s" %(binary, do_not)

#printing off x and y
print x
print y

print "I said %r." % x
print "I also said %s." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "A string with a right side."

print w + e

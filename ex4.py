#Exercise 4
#https://learnpythonthehardway.org/book/ex4.html


cars = 100      #number of cars
space_in_a_car = 4.0    #space in each cars
drivers = 30    #total number of drivers
passengers = 90     #total number of passengers
cars_not_driven = cars - drivers    #number of cars idle
cars_driven = drivers   #number of cars being driven
carpool_capacity = cars_driven * space_in_a_car     #people to be carpooled for
average_passengers_per_car = passengers / cars_driven   #average number of passengers in each car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

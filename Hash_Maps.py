# A data structure’s main utility is allowing for data to be represented in a way that resembles the way people will use that data. 
# In some cases, the primary function of that data is that it will be sequenced through like a list and so we use a data structure that allows for easier iteration, like a linked list. 
# In others, the usefulness comes from specifying interrelationships within the data.
# In the case of tabular data there is a relationship between the elements of a row. Each column corresponds to a different feature of the row.
# This kind of table, with only two columns, represents a special relationship that mathematicians would call a “map”. Being a map means relating two pieces of information.

# In the case of a map between two things, we don’t really care about the exact sequence of the data. 
# We only care that a given input, when fed into the map, gives the accurate output.
# Developing a data structure that performs this is tricky because computers care much more about values than relationships. 
# A computer doesn’t really care to memorize the astrological signs of all of our friends, so we need to trick the computer into caring.
# We perform this trick using a structure that our computer is already familiar with, an array. 
# An array uses indices to keep track of values in memory, so we’ll need a way of turning each key in our map to an index in our array.

# Imagine we want our computer to remember that our good friend Joan McNeil is a Libra. We take her name, and we turn that name into a number. 
# Let’s say that the number we correspond with the name “Joan McNeil” is 17. We find the 17th index of the array we’re using to store our map and save the value (Libra) there.
# How did we get 17, though? We use a special function that turns data like the string “Joan McNeil” into a number. This function is called a hashing function, or a hash function. 
# Hashing functions are useful in many domains, but for our data structure the most important aspect is that a hashing function returns an array index as output.

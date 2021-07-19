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

# A hash function takes a string (or some other type of data) as input and returns an array index as output. 
# In order for it to return an array index, our hash map implementation needs to know the size of our array. 
# If the array we are saving values into only has 4 slots, our hash map’s hashing method should not return an index bigger than that.
# In order for our hash map implementation to guarantee that it returns an index that fits into the underlying array, the hash function will first compute a value using some scoring metric: this is the hash value, hash code, or just the hash. 
# Our hash map implementation then takes that hash value mod the size of the array.
# This guarantees that the value returned by the hash function can be used as an index into the array we’re using.

# It is actually a defining feature of all hash functions that they greatly reduce any possible inputs (any string you can imagine) into a much smaller range of potential outputs (an integer smaller than the size of our array). 
# For this reason, hash functions are also known as compression functions.
# Much like an image that has been shrunk to a lower resolution, the output of a hash function contains less data than the input. 
# Because of this, hashing is not a reversible process. With just a hash value it is impossible to know for sure the key that was plugged into the hashing function.

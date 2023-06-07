# Question 1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ", "Argentina", " ", "San Diego", "", "  ", "", "Boston", "New York"]
filtered_places = list(filter(lambda x: x.strip() != "", places))
print(filtered_places)

# Question 2

#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
sorted_author = sorted(author, key=lambda x: x.split()[-1].lower())
print(sorted_author)


#Question 3

# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 
# F = (9/5)*C + 32

places = [('Nashua', 32), ("Boston", 12), ("Los Angeles", 44), ("Miami", 29)]
converted_places = list(map(lambda x: (x[0], (x[1] * 9/5) + 32), places))
print(converted_places)

# Question 4

# Create a generator function that individually returns each movie genre back from the list
genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]
def my_genre(arr):
    for genre in arr:
        yield genre

my_generator_object = my_genre(genres)

try:
    while True:
        print(next(my_generator_object))
except StopIteration:
    print("End of the list")


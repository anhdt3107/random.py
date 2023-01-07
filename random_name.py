import random

# Create an empty list to store the names
names = []

# Use a while loop to allow the user to enter names until they enter an empty string
name = input("Enter a name (or press enter to finish): ")
while name != "":
  # Add the name to the list
  names.append(name)
  # Get the next name
  name = input("Enter a name (or press enter to finish): ")

# Use the shuffle function from the random module to shuffle the list of names
random.shuffle(names)

# Print out the shuffled list of names
print("\nHere is the list of names in a random order:")
for name in names:
  print(name)

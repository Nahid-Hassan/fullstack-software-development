from sys import argv

# read the "WYSS" section for how to ru this
print(argv)
print(type(argv))

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

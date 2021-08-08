""""
    * close(): Closes the file. Like File->Save .. in your editor. 
    * read(): Reads the contents of the file. You can assign the result to a variable.
    * readline(): Reads just on line of text file.
    * readlines(): Reads all line of text file.
    * truncate(): Empties the file. Watch out if you care about the file.
    * write("something"): Writes "something" to the file.
    * seek(0): Moves the read/write location to the beginning of the file.
"""
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

# instead of repeating call write 1 times.
formatter = format('{}\n{}\n{}\n')

target.write(formatter.format(line1, line2, line3))

print("And finally, we close it.")
target.close()

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

data = open(from_file).read()

print(f"The input file is {len(data)} bytes long.")

print(f"Does the output file exits? {exists(to_file)}")
print(f"Ready, hit Enter to continue, CTRL-C to abroad.")
input()

output_file = open(to_file, 'w')
output_file.write(data)

print("Allright, all done.")
output_file.close()


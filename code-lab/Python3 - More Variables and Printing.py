import math

# Format string
my_name = "Md. Nahid Hassan"
my_age = 23 # years
my_height = 63 # inches
my_weight = 50 # kg
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on my coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I had {my_age}, {my_height}, and {my_weight} I get {total}.")

my_height_in_cm = my_height * 2.54
my_weight_in_ibs = my_weight * 2.20462
my_height_in_meter = my_height_in_cm / 100

print(f"My height in cm: {my_height_in_cm}.")
print(f"My BMI = {my_weight / (my_height_in_meter ** 2)}")


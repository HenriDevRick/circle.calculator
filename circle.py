# Ask and Collect radius
radius = float(input("What is the radius of the circle? "))

# Calculate diameter (2 * radius)
diameter = 2 * radius

# Calculate circumference (2 * pi * radius)
pi = 3.14
circumference = 2 * pi * radius

# Calculate area (pi * radius squared)
area = pi * radius ** 2

# Print results
print("What is the radius of the circle?",radius)
print(f"A circle with a radius of {radius} units will have a diameter of {diameter} units, a circumference of {circumference:.2f} units and an area of {area:.2f} square units.")

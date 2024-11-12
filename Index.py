def weight_on_mars(weight_on_earth):
    mars_gravity_ratio = 0.38  # Mars gravity relative to Earth
    weight_on_mars = weight_on_earth * mars_gravity_ratio
    return weight_on_mars

# Example usage
weight_on_earth = float(input("Enter your weight on Earth (in kg): "))
mars_weight = weight_on_mars(weight_on_earth)
print(f"Your weight on Mars would be: {mars_weight:.2f} kg")

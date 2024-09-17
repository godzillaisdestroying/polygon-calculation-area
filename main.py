import math

# Base class for Polygon
class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Derived class for Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Function to calculate the area of different polygons
def calculate_area(polygon):
    return polygon.area()

# Example usage
if __name__ == "__main__":
    # Create instances of different polygons
    rectangle = Rectangle(width=5, height=3)
    triangle = Triangle(base=4, height=6)
    circle = Circle(radius=2.5)

    # Calculate and print areas
    print(f"Area of Rectangle: {calculate_area(rectangle)}")
    print(f"Area of Triangle: {calculate_area(triangle)}")
    print(f"Area of Circle: {calculate_area(circle)}")

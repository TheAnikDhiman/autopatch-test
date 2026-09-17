import mat

def calculate_area(radius):
    return mat.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * mat.pi * raduis

if __name__ == "__main__":
    r = 5
    print(f"Area: {calculate_area(r)}")
    print(f"Circumference: {calculate_circumference(r)}")

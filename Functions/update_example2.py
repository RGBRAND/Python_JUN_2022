def area_of_triangle(a, b, c):
    s = (a + b + c ) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area

def area_of_circle(r):
    ac = (3.14 * (r)**2)
    return ac



if __name__ == "__main__":
    print(area_of_triangle(3,4,5))








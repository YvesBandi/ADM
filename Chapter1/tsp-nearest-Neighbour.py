import sys
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def create_random_points(n: int):
    random_points = []
    for i in range(n):
        random_points.append(Point(np.random.rand(), np.random.rand()))
    
    for point in random_points:
        print(f"{point.x}, {point.y}")

    return random_points

def show_points(points):
    x_vals = [point.x for point in points]
    y_vals = [point.y for point in points]

    plt.scatter(x_vals, y_vals)
    plt.show()

    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()



def main():
    points = create_random_points(10)
    show_points(points)



if __name__ == "__main__":
    main()
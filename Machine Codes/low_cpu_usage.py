# HIGH CPU UTILIZATION RUNNING ON AWS EC2 SERVER

import math

def __main__():
    x = 1
    y = 0
    z = 1
    while True:
        if x is 50000:
            x = 0
            z = 0
        y += math.sqrt(x)
        z += y
        x += 1
        print(math.sqrt(z))

if __name__ == "__main__":
    __main__()


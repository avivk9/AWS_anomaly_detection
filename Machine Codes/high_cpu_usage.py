# HIGH CPU UTILIZATION RUNNING ON AWS EC2 SERVER

def __main__():
    x = 1
    y = 0
    while True:
        if x is 1000:
            x = 0
        y = x ** 2
        y += 3
        x += 1

if __name__ == "__main__":
    __main__()

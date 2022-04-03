import math


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def f(self,x):
        return (self.a*x+self.b)

class CorrelatedFeatures:
    def __init__(self,feature1, feature2,corrlation,lin_reg,threshold):
        self.feature1 = feature1
        self.feature2 = feature2
        self.corrlation = corrlation
        self.lin_reg = lin_reg
        self.threshold = threshold

# calculations
def avg(x): # simple average
    average = 0
    for i in x:
        average += i
    average /= len(x)
    return average

def var(x): # returns the variance of X and Y
    avg1 = avg(x)
    avg1 = avg1 * avg1
    xSqr = []
    for i in x:
        xsqr = i*i
    avg2 = avg(xSqr)
    return avg2 - avg1

def cov(x,y): # returns the covariance of X and Y
    avgX = avg(x)
    avgY = avg(y)
    xy = []
    for i in range(len(x)):
        xy[i] = (x[i]- avgX)*(y[i] - avgY)
    return avg(xy)

def pearson(x,y): # returns the Pearson correlation coefficient of X and Y
    sdX = math.sqrt(var(x))
    sdY = math.sqrt(var(y))
    return (cov(x,y) / (sdY * sdX))

def linear_reg(points): # performs a linear regression and returns the line equation
    x = []
    y = []
    for i in range(len(points)):
        x[i] = points[i].x
        y[i] = points[i].y
    a = cov(x,y) / var(x)
    b = avg(y) - a* avg(x)
    l = Line(a,b)
    return l

def dev(p,l):
    return abs(l.f(p.x) - p.y)

def dev(p,points):
    return dev(p,linear_reg(points))

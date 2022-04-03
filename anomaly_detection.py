import details


class anomalyDetection:
    th = 0.9
    normalModel = []
    def __init__(self):
        self.normalModel = None
    def learnNormal(self,var1,var2):
        for i in range(len(var1)):
            maxAbsPear =0
            maxPlace = -1
            valX = var1
            for j in range(i+1,len(var2)):
                valY = var2[j]
                pear = details.pearson(valX,valY)
                if(abs(pear) > self.th & abs(pear)>maxAbsPear)


    def detect(self, times, utilizations):

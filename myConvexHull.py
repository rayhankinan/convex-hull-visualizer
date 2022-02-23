import numpy as np

class ConvexHull():
    data = []

    def __init__(self, *args, **kwargs):
        if "points" in kwargs.keys():
            ConvexHull.data = kwargs["points"].tolist()

            self.indexData = [i for i in range(len(ConvexHull.data))]
            self.line = []

        elif len(args) > 0:
            ConvexHull.data = args[0].tolist()

            self.indexData = [i for i in range(len(ConvexHull.data))]
            self.line = []

        else:
            self.indexData = []
            self.line = []

    def distance(self, point):
        p1 = np.array(ConvexHull.data[self.line[0][0]])
        p2 = np.array(ConvexHull.data[self.line[0][1]])
        p3 = np.array(ConvexHull.data[point])

        return np.cross(p2 - p1, p3 - p1) / np.linalg.norm(p2 - p1)

    def find_extremum(self):
        minimum = self.indexData[0]
        maximum = self.indexData[0]

        if self.line == []:
            for i in self.indexData:
                if ConvexHull.data[i][0] < ConvexHull.data[minimum][0]:
                    minimum = i
                if ConvexHull.data[i][0] == ConvexHull.data[minimum][0] and ConvexHull.data[i][1] < ConvexHull.data[minimum][1]:
                    minimum = i
                if ConvexHull.data[i][0] > ConvexHull.data[maximum][0]:
                    maximum = i
                if ConvexHull.data[i][0] == ConvexHull.data[maximum][0] and ConvexHull.data[i][1] > ConvexHull.data[maximum][1]:
                    maximum = i
        
        else: # KEMUNGKINAN BUG
            for i in self.indexData:
                if self.distance(i) < self.distance(minimum):
                    minimum = i
                if self.distance(i) > self.distance(maximum):
                    maximum = i

        return (minimum, maximum)
    
    def partition(self):
        left = ConvexHull()
        right = ConvexHull()

        if self.line == []:
            minimum, maximum = self.find_extremum()
            self.line = [[minimum, maximum]]

            for i in self.indexData:
                if self.distance(i) < 0:
                    left.indexData.append(i)
                if self.distance(i) > 0:
                    right.indexData.append(i)

            left.line = [[minimum, maximum]]
            right.line = [[minimum, maximum]]

        else: # BUG
            pMin, pMax = self.find_extremum()

            if self.distance(pMin) > 0: # partisi atas
                left.line = [[self.line[0][0], pMax]]
                right.line = [[pMax, self.line[0][1]]]

                for i in self.indexData:
                    if left.distance(i) > 0:
                        left.indexData.append(i)
                    if right.distance(i) > 0:
                        right.indexData.append(i)

            if self.distance(pMax) < 0: # partisi bawah
                left.line = [[self.line[0][0], pMin]]
                right.line = [[pMin, self.line[0][1]]]

                for i in self.indexData:
                    if left.distance(i) < 0:
                        left.indexData.append(i)
                    if right.distance(i) < 0:
                        right.indexData.append(i)

        return (left, right)

    def merge(self, left, right):
        self.line = left.line + right.line
        self.indexData = list(set(left.indexData) | set(right.indexData))

    def divide_and_conquer(self):
        if self.indexData != []:
            left, right = self.partition()

            left.divide_and_conquer()
            right.divide_and_conquer()

            self.merge(left, right)

    def create_convex(self):
        self.divide_and_conquer()

        return np.array(self.line)

    def is_intersecting(self, other):
        return False
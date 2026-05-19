class my_class(object):
    ThreeDimensions = [[]]
    def __init__(self, TimeLineID, PositionString):
        PositionArr = PositionArr.split('-')
        for i in range(4):
            for j in range(4):
                self.ThreeDimensions[i][j].append(PositionArr[i*4 + j])
    def __init__(self,TimeLinePosition):
        self.ThreeDimensions = TimeLinePosition

    def DrawBoard(self):
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    pass
class RoadGenerator:
    def __init__(self):
        self.numOfRoads = 0
    
    def getRoadId(self):
        self.numOfRoads += 1
        return self.numOfRoads
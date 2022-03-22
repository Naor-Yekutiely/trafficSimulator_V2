from .point import Point
from .vehicle import Vehicle
from .road_generator import RoadGenerator


class Road:
    def __init__(startPoint, endPoint):
        self.startPoint = startPoint
        self.endpoint = endPoint
        self.vehicles = []
        self.road_id

class DistanceCalculator:
    def __init__(self):
        self.focal_length = 500  # Adjust based on your camera
        self.known_width = 0.5  # Known width of an average object in meters
        self.threshold = 2  # Distance threshold in meters

    def calculate(self, pixel_width, pixel_height):
        # Using the larger dimension for distance calculation
        pixels = max(pixel_width, pixel_height)
        distance = (self.known_width * self.focal_length) / pixels
        return distance
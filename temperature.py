import random
import time

class TemperatureSensor:
    def __init__(self):
        self.history = []

    def read_temperature(self):
        """Simulate temperature reading between -10°C and 40°C"""
        temp = round(random.uniform(-10.0, 40.0), 2)
        self.history.append((time.time(), temp))
        return temp

    def get_last_n_readings(self, n):
        return self.history[-n:] if n <= len(self.history) else self.history[:]

import unittest
from temperature import TemperatureSensor
import time

class TestTemperatureSensor(unittest.TestCase):

    def test_temperature_range(self):
        sensor = TemperatureSensor()
        for _ in range(100):
            temp = sensor.read_temperature()
            self.assertGreaterEqual(temp, -10.0)
            self.assertLessEqual(temp, 40.0)

    def test_history_length(self):
        sensor = TemperatureSensor()
        for _ in range(10):
            sensor.read_temperature()
        self.assertEqual(len(sensor.history), 10)

    def test_get_last_n_readings(self):
        sensor = TemperatureSensor()
        for _ in range(5):
            sensor.read_temperature()
            time.sleep(0.01)
        last = sensor.get_last_n_readings(3)
        self.assertEqual(len(last), 3)
        self.assertTrue(all(isinstance(x, tuple) for x in last))
        self.assertTrue(all(isinstance(x[1], float) for x in last))

    def test_get_more_than_available(self):
        sensor = TemperatureSensor()
        for _ in range(2):
            sensor.read_temperature()
        result = sensor.get_last_n_readings(5)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()

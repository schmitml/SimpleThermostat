import board
import busio
import adafruit_si7021

i2c = busio.I2C(board.scl, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

print('Temperature: {} degrees C'.format(sensor.temperature))
print('Humidity: {}%'.format(sensor.relative_humidity))
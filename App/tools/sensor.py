import picamera
import RPi.GPIO as GPIO
import board
import adafruit_dht
import time

class Sensors(object):
    def __init__(self):
        self.pir = 17
        self.dht = adafruit_dht.DHT22(board.D4, use_pulseio=False)
        GPIO.setwarnings(False)
        GPIO.setup(self.pir,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        
                
        self.temperature_value = None
        self.humidity_value = None
                
        while self.temperature_value is None:
            try:
                self.temperature_value = self.dht.temperature
                time.sleep(0.1)
            except RuntimeError as error:
                continue
        while self.humidity_value is None:
            try:
                self.humidity_value = self.dht.humidity
                time.sleep(0.1)
            except RuntimeError as error:
                continue
        print('sensor init')

    def __del__(self):
        GPIO.cleanup()
        self.dht.exit()

    def temperature(self):
        try:
            self.temperature_value = self.dht.temperature
        except RuntimeError as error:
            pass
        return self.temperature_value
    
    def humidity(self):
        try:
            self.humidity_value = self.dht.humidity
        except RuntimeError as error:
            pass
        return self.humidity_value
    
    def is_detected(self):
        value=GPIO.input(self.pir)
        if value != 0:
            return True
        else:
            return False
   
'''
sensors = Sensors()

while True:
    msg = 'Temperature: {:.1f} Humidity: {:.1f} Motion: {}'
    msg = msg.format(sensors.temperature(), sensors.humidity(), sensors.is_detected())
    print(msg)
    time.sleep(0.5)
'''

"""
def main():
  while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
        value=GPIO.input(motion_pin)  
        if value!=0:                             #to read the value of a GPIO pin             #turn on led
            print("motion detected")                         #print information
        else:              #turn off led
            print("motion undetected")                        #print information
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)

init()
main()
GPIO.cleanup()
"""


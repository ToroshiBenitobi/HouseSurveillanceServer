class Sensor(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def temperature(self):
        return 27.5
    
    def humidity(self):
        return 27.5
    
    def is_detected(self):
        return False

sensorutl = Sensor()
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


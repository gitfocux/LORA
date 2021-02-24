from machine import UART
from machine import Pin
import time

decoded_data = ""
led = Pin(25, Pin.OUT)
uart = UART(0, 115200)  # use RPI PICO GP0 and GP1

## RAK811 - ABP, Class, Region, keys##
uart.write('at+set_config=lora:join_mode:1\r\n')
time.sleep(2)  
print("OTAA done!\r\n")

decoded_data = ""
uart.write('at+set_config=lora:class:0\r\n')
print("set to Class A")
time.sleep(2) 
print("Class A done!\r\n")

decoded_data = ""
uart.write('at+set_config=lora:region:AS923\r\n')
print("set to AS923 reguion")
print("AS923 done!\r\n")

decoded_data = ""
uart.write('at+set_config=lora:dev_addr:260132F3\r\n')
print("set to Device Address")
time.sleep(2) 
print("Device Address done!\r\n")

decoded_data = ""
uart.write('at+set_config=lora:nwks_key:CE884AC1E36BFD117A382EAEEC0C4861\r\n')
print("set to Network Session Key")
time.sleep(2) 
print("Network Session Key done!\r\n")

decoded_data = ""
uart.write('at+set_config=lora:apps_key:6DC74B56B1F4A4B5CEA7181E4B3D380B\r\n')
print("set to App Session Key")
time.sleep(2) 
print("App Session Key done!\r\n")

decoded_data = ""
uart.write('at+join\r\n')
print("joining!")
time.sleep(2) 
print("join success!")

while(1):
    led.value(1)
    uart.write('at+send=lora:1:1234554321\r\n')
    print("LED ON")
    time.sleep(5)
    led.value(0)
    print("LED OFF")
    time.sleep(5)
    
    


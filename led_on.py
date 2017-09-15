import RPi.GPIO as GPIO
import time

print "Initialize"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
chan_list = [6, 5, 25, 24, 22, 23, 27, 18, 17, 4]
GPIO.setup(chan_list,GPIO.OUT,initial=GPIO.HIGH)

print "LED on"
count = 20 
while count > -1:
  print "%i" % count
  time.sleep(1)
  count = count - 1
  
print "LED off" 
GPIO.cleanup()

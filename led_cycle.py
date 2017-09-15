import RPi.GPIO as GPIO
import time

print "Initialize"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
chan_list = [6, 5, 25, 24, 22, 23, 27, 18, 17, 4]
GPIO.setup(chan_list,GPIO.OUT,initial=GPIO.LOW)
colors = ["black", "white", "gray", "purple", "blue", "green", "yellow", "orange", "red", "brown"]

print "LED cycle"
cycle = 0
#while cycle < 5:
while 1:
  print "cycle %s" % cycle
  for i, channel in enumerate(chan_list):
    print "gpio channel %i, color %s" % (channel, colors[i])
    GPIO.output(channel,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(channel,GPIO.LOW)
  cycle = cycle + 1

print "Complete"
GPIO.cleanup()

# LEDTest

A couple of python scripts to test the LED brightness with different resistors on a Raspberry Pi.

* Setup a Raspberry PI
* Set the pi to boot to command line
* Clone this repo to the ~/programs/LEDTest directory
* Edit /etc/rc.local as below:

```
#> sudo nano /etc/rc.local

# Run the LED cycle tester
printf "Starting Pi LED Tester..."
python /home/pi/programs/LEDTest/led_cycle.py &

exit 0
```


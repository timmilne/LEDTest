# LEDTest

A couple of python scripts to test the LED brightness with different resistors on a Raspberry Pi.

* Setup a Raspberry PI
* Add this to the ~/programs/ledtest directory
* Edit /etc/rc.local as below
* Set the pi to boot to command line

```
#> sudo nano /etc/rc.local

# Run the LED cycle tester
printf "Starting Pi LED Tester..."
python /home/pi/programs/ledtest/led_cycle.py &

exit 0
```


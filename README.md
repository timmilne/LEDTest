# LEDTest

A couple of python scripts to test the LED brightness with different resistors on a Raspberry Pi.

* Setup a Raspberry PI
* Add this to the ~/programs/ledtest directory
* Edit /etc/rc.local as below
* Set the pi to boot to command line

```
#> sudo nano /etc/rc.local

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP adress is %s\n" "$_IP"
fi

# Run the LED cycle tester
printf "Starting Pi LED Tester..."
python /home/pi/programs/ledtest/led_cycle.py &

exit 0
```


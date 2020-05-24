# poweroff
A Python script to run as a service on a Raspberry Pi, powering off the machine on a GPIO button push.

## Background
I run a "headless" Pi (no keyboard or monitor, and not necessarily any network access, either, so maybe no ssh)
as an adaptor of sorts, interfacing an electronic drum kit to a drum sound module. (See my older [miditrans project](https://github.com/RobCranfill/miditrans)).
There is software that does the interfacing (along with hardware of course) that starts automatically when the Pi
is powered up, but how do I shut it down? It's not a good idea to just "pull the plug" on a running Linux system.
So I added a pushbutton switch onto the Pi, and now, with this software, all I have to do is hold the button down
for 1 second, and the Pi automatically and safely shuts down.


## Hardware
This should run on any Raspberry Pi - even a Pi Zero, I think (but I don't have one of those). 

I'm using an old RPi B 2 with the smaller 40-pin GPIO header, 
and using pin 26 ("GPIO7") to short to ground (pin 25) with a momentary-contact switch, 
because those two pins are next to each other and I can use a little 2-contact header.

![RPi with power button](http://robcranfill.net/images/RPiPowerButton.jpg)

You can of course change the code to use whatever GPIO pin you want (as long as it's an input!).


## Software
This was originally written on Raspian version 8 ("Jessie"), but is now running on version 10, "Buster". I don't think it matters. It was developed under Python 3.7.3, but any Python 3.x should work. 

It also uses the [GPIOZero](https://gpiozero.readthedocs.io/en/stable/index.html#) package, 
which makes GPIO programming much easier.

This code can be run stand-alone, in test mode, or installed as a Linux service, which is beyond the scope of this document, as they say.


## Notes
The program was pretty straightforward, although of course I made it a little more complicated than necessary. :-)
I added a "test" mode so that I could test the software without actually shutting the system down every time.
I added logging so I could see what it was doing.

One complication: the code uses [`signal.pause()`](https://docs.python.org/3.5/library/signal.html#signal.pause) 
to allow the code to wait for the button push.
(I could perhaps have used a loop around `sleep()`, but this is what `signal.pause` is for!)
In the real use-case of this service, eveything works as desired because the system shutdown kills the Python process.
But in test mode, the code never exits - even when I put a `sys.exit()` call in there!

But, as noted elsewhere on the web ([here for instance](https://stackoverflow.com/questions/35203141/how-to-exit-python-program-on-raspberry)) the `signal.pause()` won't exit until you do .... something. 
The docs say "Cause the process to sleep until a signal is received" which was a little mysterious to me.
But after handling the button push (in test mode) we can send ourselves a SIGUSER1 signal, and that causes `signal.pause()` to finish.
And as shown in the code, you can either catch this signal, or not - either way serves to let the code exit.
If you don't handle the signal, you will see "User defined signal 1" printed on the console at the end of the run. Fine.



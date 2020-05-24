# poweroff
A Python script to run as a service on a Raspberry Pi, powering off the machine on a GPIO button push.

## Background
I run a "headless" Pi (no keyboard or monitor, and not necessarily any network access, either, so maybe no ssh)
as an adaptor of sorts, interfacing an electronic drum kit to a drum sound module. (See my older project XXXX).
There is software that does the interfacing (along with hardware of course) that starts automatically when the Pi
is powered up, but how do I shut it down? It's not a good idea to just "pull the plug" on a running Linux system.
So I added a pushbutton switch onto the Pi, and now, with this software, all I have to do is hold the button down
for 1 second, and the Pi automatically and safely shuts down.


## Hardware
This should run on any Raspberry Pi - even a Pi Zero, I think (but I don't have one of those). 

I'm using an old RPi B 2 with the smaller 40-pin GPIO header, 
and using pin X to short to ground with a momentary-contact switch, 
because those two pins are next to each other and I can use a little 2-contact header.

[Picture of added switch here?]

You can of course change the code to use whatever GPIO pin you want (as long as it's an input!).


## Software
This was originally written on Raspian version 8 ("Jessie"), but is now running on version 10, "Buster". I don't think it matters.

It also uses the (GPIOZero)[https://gpiozero.readthedocs.io/en/stable/index.html#] package, 
which makes GPIO pgramming very much easier.


## Notes
The program was pretty straightforward, although of course I made it a little more complicated than necessary. :-)

I added a "test" mode so that I could test the software without actually shutting the system down every time.

I added logging so I could see what it was doing.



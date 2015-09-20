# raspiGrow
Software to automate a Hydroponic grow closet, controlled by a Raspberry Pi 2.

## Description
This project is as you may have guessed based on an Raspberry Pi. Now this should actually work fine on most of the raspberries but not tested with all. Furthermore this project contains 3 D18B20 sensors, a 4-channel relay, and pwm controlled fans. So the sensors is monitoring the temperature at the intake fan, the exhaust fan and the water temperature. This may be quite overkill, but I like some statistics. The relay is controlling light, how many hours of light the vegetables is getting. And the fans is controlling airflow, this is to adjust the temperature when the light bulbs is making heat. I should mention that all the fans is controlled together, meaning that all fans have the same speed.

**To summarize hardware:**
* Raspberry Pi 2
* 3 D18B20 temperature sensors
* 4-channel relay
* 3 PWM-controlled fans

## Software
As i already have mentioned, this software should work on every raspberry that is released. The only requirement is that you have the mentioned hardware and have python installed. I think this should work on python 2.7 and python 3, but this remains to be fully tested.


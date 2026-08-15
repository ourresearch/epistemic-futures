---
title: "#IoTH: The Internet of Things and Humans"
person: tim-oreilly
section: by
type: blog-post
year: 2014
date: 2014-08-16
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/ioth-the-internet-of-things-and-humans/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# #IoTH: The Internet of Things and Humans

## Full text

[Rod Smith](<http://solidcon.com/solid2014/public/schedule/speaker/10028>) of IBM and I had a call the other day to prepare for our onstage conversation at O’Reilly’s upcoming [Solid Conference](<http://solidcon.com>), and I was surprised to find how much we were in agreement about one idea: so many of the most interesting applications of the Internet of Things involve new ways of thinking about how humans and things cooperate differently when the things get smarter. It really ought to be called the Internet of Things and Humans — #IoTH, not just #IoT!

Let’s start by understanding the Internet of Things as the combination of sensors, a network, and actuators. The “wow” factor — the magic that makes us call it an Internet of Things application — can come from creatively amping up the power of any of the three elements.

For example, a traditional “dumb” thermostat consists of only a sensor and an actuator — when the temperature goes out of the desired range, the heat or air conditioning goes on. The addition of a network, the ability to control your thermostat from your smartphone, say, turns it into a simple #IoT device. But that’s the bare-base case. Consider the Nest thermostat: where it stands out from the crowd of connected thermostats is that it uses a complex of sensors (temperature, moisture, light, and motion) as well as both onboard and cloud software to provide a rich and beautiful UI with a great deal more intelligence.

  * While you can schedule your heating manually, you can also let the Nest “learn” when you get up in the morning and turn on the heat, and when you go to bed and turn it off. After a week or so, it will “understand” and repeat the pattern.
  * When you are away, the Nest will notice the absence of movement and automatically turn off the heat.
  * When the moisture level is high, the thermostat will adjust the temperature to a lower level than you told it you wanted in order to achieve the right perceived temperature. (When humidity is high, it seems warmer than the thermostat alone would notice.)
  * If you have a forced hot-air system, the Nest will remind you when to change the filters based on the number of hours the system has been running.
  * The Nest uses external weather data to help explain when your energy usage is abnormally low or high and compares your usage with that of other customers.

So, let’s generalize the #IoT paradigm as sensors + network + actuators + local _and_ cloud intelligence + creative UI for gathering both explicit and implicit instructions from humans.

Note that any part of this pattern can vary. For example, some #IoT applications have strong, constant connectivity, while others will increasingly have intermittent connectivity and a lot of autonomy. As the resin.io blog put it, they will be “[Strong Devices, Weakly Connected.](<http://resin.io/blog/the-internet-of-autonomous-things-strong-devices-weakly-connected/>)” A fully autonomous robot is our model for this kind of #IoT device.

But let me play devil’s advocate with the question: is Uber an #IoT application? Most people would say it is not; it’s just a pair of smartphone apps connecting a passenger and driver. But imagine for a moment the consumer end of the Uber app as it is today, and on the other end, a self-driving car. You would immediately see  _that_ as #IoT. Using this thought experiment, one way to think of the present Uber is as an example of what Eric Ries calls “[concierge minimum viable product](<http://scottlthompson.com/lean-lesson-flashback-the-concierge-mvp/>)” — that is, a product where you emulate some of the functions with humans before you build them in software.

This is a powerful way to think about the Internet of Things because it focuses the mind on the human experience of it, not just the things themselves. I’m very fond of [the Aaron Levie Tweet about Uber](<https://twitter.com/levie/status/370776444013510656>): “Uber is a $3.5 billion lesson in building for how the world *should* work instead of optimizing for how the world *does* work.” That is precisely the lesson that Internet of Things designers need to learn: how does a smart thing make it possible to change the entire experience and workflow of a job we do in the real world?

How do quantified self sensors allow us to change how we think about our health care system? How will self-driving cars change transportation and logistics? How might as familiar a sensor as a camera change how we store our stuff? How might power tools like saws, drills, and routers work if they were “smart”?

Long before we get to fully autonomous devices, there are many “halfway house” applications that are really Internet of Things applications in waiting, which use humans for one or more parts of the entire system. When you understand that the general pattern of #IoTH applications is not just sensor + network + actuator but various combinations of human + network + actuator or sensor + network, you will broaden the possibilities for interfaces and business models.

For example, while we can envision a future of fully automated sensor-driven insulin pumps and other autonomous therapeutic devices, we are not there today, as Scott Hanselman [explains](<http://www.hanselman.com/blog/ItsWAYTooEarlyToCallThisInsulinPumpAnArtificialPancreas.aspx>). But that doesn’t mean #IoT-related technology isn’t a powerful tool for rethinking many of the ways we deliver health care. For example, sensors make it possible to do patient “observation” on an outpatient basis, while the health care team monitors those sensors with a tablet or smartphone. Or it might not be the patient who is instrumented, but his or her home, [allowing seniors to age in place](<http://www-03.ibm.com/able/news/homehealthcare.html>). IBM calls this the Patient Centered Medical Home ([pdf](<http://www-01.ibm.com/common/ssi/cgi-bin/ssialias?subtype=XB&infotype=PM&appname=GBSE_GB_TI_USEN&htmlfid=GBE03219USEN&attachment=GBE03219USEN.PDF>)).

Or consider [Cargosense](<http://www.cargosense.com/>), a system for keeping track of environmental conditions for shipment of sensitive medical cargoes. A sensor package tracks the conditions during shipment, but there is, as yet, no opportunity for real-time adjustment. For now, the data is simply consumed via a tablet app that provides regulatory approval of the necessary conditions. This is still incredibly valuable.

How about [Makespace](<https://www.makespace.com/>)? This startup is hardly #IoT at all, but it has that wonderful quality of understanding how a simple sensor, creatively applied, can make possible a complete rethinking of the interaction paradigm. Typical storage units are packed with jumbled boxes of forgotten stuff. What’s in there? I can’t remember. Makespace has the customer photograph what’s in the boxes (we’ve forgotten that the camera is one of the most powerful sensors we carry about with us!), and then Uber-like, takes them away, to be retrieved on demand. The notion that it’s possible to track what’s in the box means that people themselves never need to visit their storage center, meaning that it can be located far away, with the contents returned at will.

It is worth noting that the smartphone is the perfect halfway house #IoTH platform. It has a rich package of sensors (actually, far more sensors than the Nest), network connectivity, local data and intelligence, and easy access to cloud backends. And it has access on the other end to devices with all the same characteristics. The actuator — the “robot” that can act on the sensor data — can simply be a human on the other end, but it can be a human who is also augmented with that same sensor package. (For example, Uber depends on real-time sensing of the location of both passenger and driver via their smartphones.)

There is another axis to consider: sometimes the human provides input to the system explicitly (as I do when I turn down my Nest thermostat) and sometimes implicitly (as I do when I leave my house and the Nest notices I’m away.) The sensor package in the phone allows for a wide range of both implicit and explicit interactions: it notifies the Uber driver of my location without me having to do anything, but it lets me call or send a message for explicit communication.

Armed with this design pattern, let’s look at a number of intriguing #IoTH applications and devices, each of which inserts the human into different parts of the process using the smartphone or tablet as a key link between human and the rest of the system.

  * On the [Moto X](<http://www.motorola.com/us/FLEXR1-1/Moto-X/FLEXR1.html>), Google uses sensor data from the phone (“you seem to be driving”) to offer to read me my text messages, but then asks me explicitly whether I want it to do so. I can also wake up the phone without touching it, simply by talking to it and giving it simple commands. My “smartphone” has become a “smart thing,” with its sensors used to help choose the best modality for the human to provide input.
  * Applications like Waze, which collect real-time traffic data and predict your best route by considering the speed and location of the smartphones of its active users, [will be directly connected to the car](<http://www.pcmag.com/article2/0,2817,2406382,00.asp>). Even short of self-driving cars, you can expect the car’s mapping system to suggest a different route based on information sent automatically from other vehicles.

This pattern of human as part of the #IoTH system, of course, is not limited to applications that include a phone. For example:

  * [Taktia](<http://www.sabertoothinvention.com/fabunit/>)‘s smart hand tools let a human provide the gross motor function, but the robot [provides the fine motor control](<http://www.nytimes.com/2012/09/23/technology/computer-precision-for-power-tools-novelties.html?_r=1&>) to follow exact patterns, which are input via machine vision. (This, incidentally, is how [robotic surgery](<http://en.wikipedia.org/wiki/Robotic_surgery>) also works.)
  * Google’s self-driving car [depends in part on the uploaded memory of humans who have previously driven those same roads in Google Street View cars](<http://www.holovaty.com/writing/streetview/>) — essentially, human drivers as cyborgs augmented with detailed location sensing and cameras.

My point is that when you think about the Internet of Things, you should be thinking about the complex system of interaction between humans and things, and asking yourself how sensors, cloud intelligence, and actuators (which may be other humans for now) make it possible to do things differently. It is that creativity in finding the difference that will lead to the breakthrough applications for the Internet of Things and Humans.

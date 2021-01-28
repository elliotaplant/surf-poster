# Assembly

## Raspberry Pi
Set up your Raspberry Pi on your home WiFi network with SSH setup according to
[these instructions](https://medium.com/@jay_proulx/headless-raspberry-pi-zero-w-setup-with-ssh-and-wi-fi-8ddd8c4d2742)

By the end of this, you should be able to ssh onto your Raspberry Pi.

## Testing the Servos
Once you've gotten your Raspberry Pi setup, take out one servo, attach the the appropriate pins:

|          |Servo | RPi pin |
|----------|------|--------:|
|Ground    |BROWN |6        |
|Power (5v)|RED   |2        |
|GPIO      |ORANGE|16       |

![servo pinout](https://components101.com/sites/default/files/component_pin/Servo-Motor-Wires.png)

![rpi pinout](https://i2.wp.com/peppe8o.com/wp-content/uploads/2020/09/Raspberry-PI-Zero-Pinout-schema.jpg?resize=910%2C657&ssl=1)

Run this command:

`python test_servo.py 16 2.5`

You should see the servo move to its furthest clockwise position. Next, run this command:

`python test_servo.py 16 12.5`

and you should see the servo move to its furthest counter-clockwise position.

Next, connect all the wires and run `python manual.py 0 55 0` to test out all of the connections.

## Testing the code
- Modify the code for your beach
- Run `main.py`, and watch the servos turn

## Constructing the box
- Remove the foam backing from the shadowbox
- Using the black and white printout of your poster picture, mark where the holes will sit on the foamless backing
- Drill out those holes with a 3/8" bit (or whichever bit matches the end of your servos)
-

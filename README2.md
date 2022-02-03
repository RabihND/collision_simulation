# Collision 
### Simulating object collisions 
> Circles which can bounce off one another if they collide
# What are we making?
Our training will be based on **simple circles**.
We can modify the characteristics of the circles to reflect the qualities they represent: We can use circles to make it simpler to use arithmetic to compute collisions, and we can change the properties of the circles to reflect the qualities they represent: More bulk, for example, or a larger radius.

# What do we need to know to simulate a collision?
Before we can simulate a collision, we need to know a few things.
First, we must determine which, if any, two objects are colliding.
We need to find out how fast the two items are colliding, the angle of incidence (which we'll look at in a minute), and the mass of each of the objects once we know which two things are colliding. 

▪️**So, how can we figure out which objects are colliding?**

When you utilize circles, it's quite basic. Every point around the circumference is the same distance from the center as every other point; the radius is the measurement from the edge to the center. We can tell if two items' outlines meet by calculating the distance between their centers. We can deduce that two circles are colliding if the distance between their centers is smaller than the radius of each circle combined together.




## >> Let’s take a quick walk through our code now.

The top of **collisions.py** (between lines 1-24) imports the modules we’ll need for our code and declares the variables that we’ll be using throughout the tutorial. 
```python
import pygame, sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
windowWidth = 1024
windowHeight = 768
pygame.init()
surface = pygame.display.set_mode((
windowWidth, windowHeight))
pygame.display.set_caption(‘Collisions’)
previousMousePosition = [0,0]
mousePosition = None
mouseDown = False
collidables = []
currentObject = None
expanding = True
drawAttractions = False
gravity = 1.0
```
The logic for our keyboard ⌨️ and mouse 🖱️ interactions, as well as our main loop, is found on lines 137-202. Clicking in our window will produce a new particle that will only effect the movement of other particles once the mouse is released. The particle will inherit the velocity of the mouse pointer if the mouse was moving when it was released.

## calculateMovement()
All of our objects will have a mass and will attract every other object gravitationally using the **calculateMovement()** method,which handles the 
gravity of all of our objects.

The last section of **calculateMovement()**  doesn’t have anything to do with moving the circles: it simply draws a line between our droped circle and every other circle that it’s having an effect on. It’s the line of attraction we looked at earlier, and it illustrates the directions that gravity is pulling our circles in.
> You can toggle this on and off with the ‘A’ key.
```pyhton
def calculateMovement():

	for anObject in collidables:

		for theOtherObject in collidables:

			if anObject is not theOtherObject:
				
				direction = (theOtherObject["position"][0] - anObject["position"][0], theOtherObject["position"][1] - anObject["position"][1]) 
				magnitude = math.hypot(theOtherObject["position"][0] - anObject["position"][0], theOtherObject["position"][1] - anObject["position"][1]) 
				nDirection = (direction[0] / magnitude, direction[1] / magnitude)

				if magnitude < 5:
					magnitude = 5
				elif magnitude > 15:
					magnitude = 15

				strength = ((gravity * anObject["mass"] * theOtherObject["mass"]) / (magnitude * magnitude)) / theOtherObject["mass"]

				appliedForce = (nDirection[0] * strength, nDirection[1] * strength)

				theOtherObject["velocity"][0] -= appliedForce[0]
				theOtherObject["velocity"][1] -= appliedForce[1]

				if drawAttractions is True:
					pygame.draw.line(surface, (255,255,255), (anObject["position"][0],anObject["position"][1]), (theOtherObject["position"][0],theOtherObject["position"][1]), 1)

```
## handleCollisions()
This Part will focus on the **handleCollisions()** method, which can be found on lines 86-135. Here, we look for items that are colliding and alter their trajectories accordingly.


import pygame, sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME

windowWidth = 1024
windowHeight = 768

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Collisions')

previousMousePosition = [0,0]
mousePosition = None
mouseDown = False
collidables = []
currentObject = None
expanding = True
drawAttractions = False
gravity = 1.0

def drawCollidables():

	for anObject in collidables:
		anObject["position"][0] += anObject["velocity"][0]
		anObject["position"][1] += anObject["velocity"][1]
		pygame.draw.circle(surface, (255,255,255), (int(anObject["position"][0]), int(anObject["position"][1])), int(anObject["radius"]), 0)

def drawCurrentObject():
	global expanding, currentObject
	currentObject["position"][0] = mousePosition[0]
	currentObject["position"][1] = mousePosition[1]
	if expanding is True and currentObject["radius"] < 30:
		currentObject["radius"] += 0.2
		if currentObject["radius"] >= 30:
			expanding = False
			currentObject["radius"] = 9.9
	elif expanding is False and currentObject["radius"] > 1:
		currentObject["radius"] -= 0.2
		if currentObject["radius"] <= 1:
			expanding = True
			currentObject["radius"] = 1.1
	currentObject["mass"] = currentObject["radius"]
	pygame.draw.circle(surface, (255,0,0), (int(currentObject["position"][0]), int(currentObject["position"][1])), int(currentObject["radius"]), 0)

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

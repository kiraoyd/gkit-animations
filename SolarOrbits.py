from ctypes import *
from Gkit import *
import math

#SETUP
swidth = 500
sheight = 500
G_init_graphics(swidth, sheight)
G_rgb(0, 0, 0)  # dark grey
G_clear()

G_rgb(245/255, 242/255, 66/255)  # yellow
#Draw the sun
sunX = 250
sunY = 250
sunR = 50
G_fill_circle(sunX, sunY, sunR)

#draw the earth
G_rgb(66/255, 114/255, 245/255)  # blue
earthX = 400
earthY = 250
earthR = 10
G_fill_circle(earthX, earthY, earthR)

#Draw the moon
G_rgb(1,1,1)
moonX = 430
moonY = 250
moonR = 5
G_fill_circle(moonX, moonY, moonR)
G_wait_key()

#Get length of line between the sun and earth (radius)
deltaX = earthX - sunX
deltaY = earthY - sunY
sunToEarthR = math.sqrt((deltaX**2)+(deltaY**2))

#Get length of line between the earth and moon (radius)
moonDeltaX = moonX - earthX
moonDeltaY = moonY - earthY
earthToMoonR = math.sqrt((moonDeltaX**2)+ (moonDeltaY**2))

earthAngle = 0
moonAngle = 0

earthChange = 1
#compute angle change for moon, if moon needs to go around the earth 12 times for every single time the earth goes 360 around the sun. 
moonChange = earthChange*12



while(earthAngle < 360):
	#reinitialize background
	G_rgb(0, 0, 0)  # dark grey
	G_clear()
	G_rgb(1, 1, 1)  # white
	#Redraw the sun since it stays in place
	G_rgb(245/255, 242/255, 66/255)  # yellow
	sunX = 250
	sunY = 250
	sunR = 50
	G_fill_circle(sunX, sunY, sunR)

	#recompute new Earth location
	earthAngle = earthAngle + earthChange
	#recompute new outer point coordinates as the angle changes
	earthX = (math.cos(math.radians(earthAngle)))*sunToEarthR
	#acount for distance between center point of Sun and (0,0)
	earthX = earthX + sunX
	earthY = (math.sin(math.radians(earthAngle)))*sunToEarthR
	earthY = earthY + sunY
	
	#Draw Earth in new place
	G_rgb(66/255, 114/255, 245/255)  # blue
	G_fill_circle(earthX, earthY, earthR)
	

	#recompute new Moon location using new earth centerpoin
	moonAngle = moonAngle + moonChange 
	moonX = (math.cos(math.radians(moonAngle)))*earthToMoonR
	moonX = moonX + earthX
	moonY = (math.sin(math.radians(moonAngle)))*earthToMoonR
	moonY = moonY + earthY
	
	#Draw Moon in new place
	G_rgb(1,1,1)
	G_fill_circle(moonX, moonY, moonR)
	G_wait_key()

G_wait_key()

print("Graphics window closing")
G_close()
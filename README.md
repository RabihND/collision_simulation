<div id="top"></div>

<p align="center">
    <a href="https://github.com/RabihND/collision_simulation/graphs/contributors" alt="Contributers">
        <img src="https://img.shields.io/github/contributors/RabihND/collision_simulation?color=6fd671&logo=WhiteSource&style=for-the-badge" /></a>
    <a href="https://github.com/RabihND/collision_simulation/network/members" alt="Forks">
        <img src="https://img.shields.io/github/forks/RabihND/collision_simulation?color=cccccc&logo=Node-RED&style=for-the-badge" /></a>
    <a href="https://github.com/RabihND/collision_simulation/stargazers">
        <img src="https://img.shields.io/github/stars/RabihND/collision_simulation?color=8e6be8&logo=Ethereum&logoColor=8e6be8&style=for-the-badge" alt="Stars" /></a>
    <a alt="Visitors">
        <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FRabihND%2FSecretMsg&label=Visitors&countColor=%23263759&style=flat-square labelStyle=upper"/></a>
    
</p>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> Collision🔮</h3>
  <p align="center"><img src="./stuff/collision.png" width="110"></p>
  <p align="center">
   A Simulating of object collisions designed with Pygame (Python)
    <br />
    <a href="https://github.com/RabihND/collision_simulation"><strong>Explore the documents »</strong></a>
    <br />
    <br />
  </p>
</div>


---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary> 
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#parts">Parts</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#refenences">Refenences</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center"> <img  src="./stuff/Elastic_collision.png" width="300"> </p>  
<b> Circles which can bounce off one another if they collide.</b>

> Our training will be based on **simple circles**.

<b># What are we making? </b>
<p align="justify">We can modify the characteristics of the circles to reflect the qualities they represent: We can use circles to make it simpler to use arithmetic to compute collisions, and we can change the properties of the circles to reflect the qualities they represent: More bulk, for example, or a larger radius.</p>


<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

Major frameworks/libraries used in this project:

* [Python 3.x](https://www.python.org/)
* [Pygame](https://www.pygame.org/news)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- PARTS -->
## Parts
**1. What do we need to know to simulate a collision?**

<i>"Before we can simulate a collision, we need to know a few things."</i> 

<p align="justify">First, we must determine which, if any, two objects are colliding.We need to find out how fast the two items are colliding, the angle of incidence , and the mass of each of the objects once we know which two things are colliding. </p>
 
**2. So, how can we figure out which objects are colliding?** 

<p align="justify">When you utilize circles, it's quite basic. Every point around the circumference is the same distance from the center as every other point; the radius is the measurement from the edge to the center. We can tell if two items' outlines meet by calculating the distance between their centers. We can deduce that two circles are colliding if the distance between their centers is smaller than the radius of each circle combined together.</p>


<div class="row"  style="display: table; text-align:center;">
  <div class="column" style="  float: left;
  width: 33.33%;
  padding: 5px;">
    <img src="./stuff/not_coll.png" alt="Snow" style="width:50%">
  </div>
  <div class="column"  style="  float: left;
  width: 33.33%;
  padding: 5px;">
    <img src="./stuff/yes_coll.png" alt="Forest" style="width:50%">
  </div>
</div> 


**3. main.py [Introduction]**

<p align="justify">The logic for our keyboard ⌨️ and mouse 🖱️ interactions, as well as our main loop, is found on lines 137-202. Clicking in our window will produce a new particle that will only effect the movement of other particles once the mouse is released. The particle will inherit the velocity of the mouse pointer if the mouse was moving when it was released.</p>

**4. calculateMovement() Function** 
<p align="justify">All of our objects will have a mass and will attract every other object gravitationally using the <b>calculateMovement()</b> method,which handles the 
gravity of all of our objects.</p>

<p align="justify">The last section of <b>calculateMovement()</b>  doesn’t have anything to do with moving the circles: it simply draws a line between our droped circle and every other circle that it’s having an effect on. It’s the line of attraction we looked at earlier, and it illustrates the directions that gravity is pulling our circles in. </p>

> You can toggle this on and off with the ‘**A**’ key.

**5. handleCollisions() Function** 
<p align="justify">The <b>handleCollisions()</b> method, which can be found on lines 86-135. Here, we check for colliding objects and adjust their trajectories accordingly</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- RESULTS -->
## Results

> **Left button** :Use the
mouse to create
a new moving object.
<p align="center"> <img  src="./stuff/Run.png" width="150"> </p>  
<details>
<summary>ScreenCapture Preview 🖼️</summary>
  <body>
    <p align="center"> <img src="./stuff/collision.gif" width="300"> </p>
  </body>
</details>



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- REFERENCES -->
## Refenences

- [Raspberry Pi MagPy magazine](https://magpi.raspberrypi.com/)
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contacts

**Project Link:** [https://github.com/RabihND/collision_simulation](https://github.com/RabihND/collision_simulation)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

<p align="right">(<a href="#top">back to top</a>)</p>


---





<div id="top"></div>

<h1 align="center"> AP course project  </h1>

<p align="center">
    <a alt="Version">
        <img src="https://img.shields.io/github/v/release/RabihND/collision_simulation?color=14adfa&logo=Semantic%20Web&logoColor=14adfa&style=for-the-badge" /></a>
    <a  alt="Downloads">
        <img src="https://img.shields.io/github/downloads/RabihND/collision_simulation/total?logo=App%20Store&logoColor=white&style=for-the-badge" /></a>
    <a href="https://github.com/RabihND/collision_simulation/graphs/contributors" alt="Contributers">
        <img src="https://img.shields.io/github/contributors/RabihND/collision_simulation?color=6fd671&logo=WhiteSource&style=for-the-badge" /></a>
    <a href="https://github.com/RabihND/collision_simulation//network/members" alt="Forks">
        <img src="https://img.shields.io/github/forks/RabihND/collision_simulation?color=cccccc&logo=Node-RED&style=for-the-badge" /></a>
    <a href=" https://github.com/RabihND/collision_simulation/stargazers">
        <img src="https://img.shields.io/github/stars/RabihND/collision_simulation?color=8e6be8&logo=Ethereum&logoColor=8e6be8&style=for-the-badge" alt="Stars" /></a>
    <a alt="Visitors">
        <img src="https://visitor-badge-reloaded.herokuapp.com/badge?page_id=RabihND/collision_simulation?color=14adfa&logo=Android&style=for-the-badge" /></a>
    <a href="https://github.com/RabihND/collision_simulation/master/LICENSE.txt">
        <img src="https://img.shields.io/github/license/RabihND/collision_simulation?color=%2363afdb&logo=letsencrypt&style=for-the-badge" alt="License"></a>
    
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
<p align="center"> <img  src="./stuff/mastermind.jpg" width="1000"> </p>  
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
    <img src="./stuff/not_coll.png" alt="Snow" style="width:20%">
  </div>
  <div class="column"  style="  float: left;
  width: 33.33%;
  padding: 5px;">
    <img src="./stuff/yes_coll.png" alt="Forest" style="width:20%">
  </div>
</div> 



**3. GameOverWindow Class** (GUI_Window)

The resulting window, which shows the player's loss(+) or victory(-).
- **display_text()**: Return a text with include the result of the game.(Win/Loss)

**4. Splash Screen Class** (GUI_Windows)
>{⌛} 



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- RESULTS -->
## Results

**GUI OUTPUT:**
<details>
<summary>ScreenShoot Preview 🖼️</summary>
  <body>
    <p align="center"> <img src="./stuff/GUI_output.jpg" width="200"> </p>
  </body>
</details>

---

**TERMINAL OUTPUT:**
<details>
<summary>ScreenShoot Preview 🖼️</summary>
  <body>
    <p align="center"> <img src="./stuff/terminal_output.jpg" width="300"> </p>
  </body>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- REFERENCES -->
## Refenences

🔎

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contacts


Rabih ND - [@RabihND](https://github.com/RabihND) 

Hasan Sanei - [@hasansanei](https://github.com/hasansanei)

**Project Link:** [https://github.com/RabihND/AP2021-2022-Final](https://github.com/RabihND/AP2021-2022-Final)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Write the main code-map.
- [x] Design the GUI window. 
- [x] Write the MasterMain Core Functions.
- [x] Design the GameOver window.
- [x] <a href="https://github.com/RabihND/AP2021-2022-Final/releases/latest"><strong>Build the .EXE Release</strong></a>
- [ ] Splash screen
- [ ] Build APK release.

<p align="right">(<a href="#top">back to top</a>)</p>


---
<div align="center">
<p>
<img src="./stuff/logo.png" width="110">
<p align="center"><b>
Amirkabir University  of Technology</b>

(Tehran Polytechnic)
</p>
</p>
</div>




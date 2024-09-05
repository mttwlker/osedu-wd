# p5.js Animated Starfield
Create an animated starfield that gives the illusion of a space environment using p5.js. Control the speed and density of the stars, observing their movement against a cosmic backdrop. This project introduces basic animation concepts and allows experimentation with parameters to create your own mesmerizing starry scenes.
## Sketch Code
```
let stars = [];

function setup() {
  createCanvas(800, 600);
  for (let i = 0; i < 200; i++) {
    stars.push(new Star());
  }
}

function draw() {
  background(0);

  for (let star of stars) {
    star.update();
    star.display();
  }
}

class Star {
  constructor() {
    this.x = random(width);
    this.y = random(height);
    this.z = random(width); // Depth for the 3D effect
    this.speed = random(1, 10);
  }

  update() {
    this.z = this.z - this.speed;
    if (this.z < 1) {
      this.z = width;
      this.x = random(width);
      this.y = random(height);
    }
  }

  display() {
    fill(255);
    noStroke();

    // Map the 3D coordinates to 2D space
    let sx = map(this.x / this.z, 0, 1, 0, width);
    let sy = map(this.y / this.z, 0, 1, 0, height);
    let r = map(this.z, 0, width, 8, 0);

    ellipse(sx, sy, r, r);
  }
}

```
## Learning notes
Star Class: The Star class represents individual stars with properties like position (x, y, z), and speed. The update method updates the star's position and handles resetting it when it moves off the screen.

Animated Background: The draw function continuously updates and displays the stars, creating the illusion of a moving starfield against a cosmic background.

Depth Perception: The z property adds a 3D effect, making stars appear closer or farther away based on their depth. Users can experiment with different depth values for varying effects.

Map Function: The map function is used to project 3D coordinates onto a 2D space, creating the illusion of movement and depth.

User Control: Users can experiment with the number of stars (stars.push(new Star());), speed, and other parameters to customize the animated starfield.

Experimentation and Creativity: Encourage users to modify the code, such as changing the color scheme, introducing other celestial elements, or adding user-controlled interactions. Documenting changes and observations enhances the learning process.
### Acknowledgement
Provided by: ChatGPT
Github: 

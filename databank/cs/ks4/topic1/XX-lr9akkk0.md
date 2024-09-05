# p5.js - Animated Scene
Write a sketch which creates a basic animation.
## Sketch Code
```
let xPos = 50; // Initial x-position of the object

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(240);

  // Draw a moving object
  fill(0, 150, 200);
  ellipse(xPos, height / 2, 30, 30);

  // Update the x-position for animation
  xPos += 2;

  // Reset x-position when the object goes off-screen
  if (xPos > width + 15) {
    xPos = -15;
  }
}

```
## Learning notes
Setup:
The canvas is created with a size of 400x400 pixels in the setup() function.

Draw Function:
The draw() function contains the main animation loop.

Background:
The background(240) function sets the background to a light gray color in each frame, creating the illusion of animation.

Moving Object:
An ellipse is drawn at the current xPos along the y-axis, creating a simple moving object.

Update for Animation:
The xPos variable is incremented by 2 in each frame, causing the object to move horizontally.

Resetting Position:
When the object goes off-screen (to the right), its position is reset to the left side of the canvas, creating a continuous looping animation.
### Acknowledgement
Provided by: 
Github: 
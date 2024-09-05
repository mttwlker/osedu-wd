# p5.js - Drawing Shapes
Create a simple sketch where the user can draw shapes on a canvas with a mouse press.
## Sketch Code
```
function setup() {
  createCanvas(400, 400);
  background(240);
}

function draw() {
  // Empty draw function for now
}

function mousePressed() {
  // Draw a black ellipse when the mouse is pressed
  fill(0);
  ellipse(mouseX, mouseY, 20, 20);
}

function keyPressed() {
  // Erase the canvas when any key is pressed
  background(240);
}

```
## Learning notes
Setup:
The canvas is created with a size of 400x400 pixels, and the background is set to a light gray color in the setup() function.

Draw Function:
The draw() function is currently empty. In this case, it doesn't need to do anything because the drawing is handled by the mousePressed() and keyPressed() functions.

Mouse Interaction:
When the mouse is pressed (mousePressed() function), a black ellipse is drawn at the current mouse position (represented by mouseX and mouseY). This allows users to create a pattern of black ellipses on the canvas.

Keyboard Interaction:
When any key is pressed (keyPressed() function), the canvas is cleared by setting the background to light gray. This provides a way to erase the drawing and start fresh.
### Acknowledgement
Provided by: Matt Walker
Github: mttwlker
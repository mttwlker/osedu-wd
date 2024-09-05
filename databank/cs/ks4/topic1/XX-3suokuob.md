# Interactive Canvas
Create a sketch which interacts with mouse movements and mouse presses.
## Sketch Code
```
let shapeColor;

function setup() {
  createCanvas(400, 400);
  shapeColor = color(255, 0, 0);
}

function draw() {
  // Gradually change the background color over time
  background(frameCount % 255, frameCount % 255, 200);

  // Update shape color based on mouse press
  if (mouseIsPressed) {
    shapeColor = color(random(255), random(255), random(255));
  }

  // Draw a shape that follows the mouse position
  noStroke();
  fill(shapeColor);
  ellipse(mouseX, mouseY, 50, 50);
}
```
## Learning notes
Dynamic Background:
The background color gradually changes over time by using frameCount % 255 to create a looping effect. 

Shape Color Interaction:
The variable shapeColor is used to store the color of the shape. Initially set to red (color(255, 0, 0)), it changes to a random color each time the mouse is pressed.

Mouse Interaction:
The mouseIsPressed function checks if the mouse button is currently pressed. When pressed, the shape's color changes.

Drawing a Shape:
The ellipse(mouseX, mouseY, 50, 50) draws a circle at the current mouse position with a fixed size of 50x50 pixels.

No Stroke:
The noStroke() function removes the outline of the shape, creating a smooth and clean appearance.

Random Color:
color(random(255), random(255), random(255)) generates a random RGB color, providing an element of surprise and creativity.
### Acknowledgement
Provided by: Matt
Github: mttwlker

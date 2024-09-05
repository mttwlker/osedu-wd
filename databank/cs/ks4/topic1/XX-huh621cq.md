# p5.js - Visual Pattern
Create a visual pattern using loops and basic shapes.
## Sketch Code
```
function setup() {
  createCanvas(400, 400);
  background(240);
}

function draw() {
  // Draw a grid of circles
  for (let x = 20; x <= width - 20; x += 40) {
    for (let y = 20; y <= height - 20; y += 40) {
      fill(random(255), random(255), random(255));
      ellipse(x, y, 30, 30);
    }
  }
}

```
## Learning notes
Setup:
The canvas is created with a size of 400x400 pixels, and the background is set to a light gray color in the setup() function.

Draw Function:
The draw() function contains a nested loop that creates a grid of circles.

Nested Loops:
The for loops iterate over the x and y coordinates, creating a grid of circles at regular intervals.

Random Fill Colors:
The fill(random(255), random(255), random(255)) statement generates random RGB colors for each circle, creating a vibrant and colorful pattern.

Grid of Circles:
Circles are drawn at the specified x and y coordinates with a radius of 30 pixels.

Pattern Generation:
This sketch introduces the concept of using loops to create repetitive patterns and the use of randomness for color variation.
### Acknowledgement
Provided by: 
Github: 
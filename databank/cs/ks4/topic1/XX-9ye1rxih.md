# p5.js Dynamic Generative Art Gallery
Create an interactive web-based art gallery that dynamically generates unique pieces of art using creative coding techniques. Users can navigate through the gallery, witnessing the endless variety of visual compositions generated in real-time. 
## Sketch Code
```
let canvasSize = 500;

function setup() {
  createCanvas(canvasSize, canvasSize);
  noLoop();
}

function draw() {
  background(255);
  generateArt();
}

function generateArt() {
  // Your creative code goes here
  // Experiment with shapes, colors, and patterns
  // Example: Draw a random pattern of circles
  for (let i = 0; i < 100; i++) {
    let x = random(width);
    let y = random(height);
    let diameter = random(10, 50);
    let fillColor = color(random(255), random(255), random(255), 150);
    fill(fillColor);
    ellipse(x, y, diameter, diameter);
  }
}

function mouseClicked() {
  redraw(); // Click to generate new art
}
```
## Learning notes
1. Understanding the Canvas: The createCanvas function sets up the drawing canvas, and background(255) fills it with a white background.

2. Generating Art: The generateArt function is where the creative coding magic happens. Users can experiment with different shapes, colors, and patterns to create their own unique generative art.

3. Interactivity: The mouseClicked function allows users to interact with the project by clicking on the canvas, triggering the regeneration of a new art composition.

4. Exploration: Encourage users to modify the code and observe the impact on the generated art. Changing parameters, adding new shapes, or combining different techniques can lead to diverse and interesting results.

5. Documentation: Comment your code to explain each section and encourage users to document their own modifications. Understanding the code is crucial for learners to build on the provided foundation.
### Acknowledgement
Provided by: Matt Walker
Github: mttwlker

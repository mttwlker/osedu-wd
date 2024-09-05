# p5.js - Bouncing Ball
Create a sketch which has a bounding ball that responds to keyboard input, changing colour when a key is pressed.
## Sketch Code
```
let ball;
let bgColor;

function setup() {
  createCanvas(400, 400);
  ball = {
    x: width / 2,
    y: height / 2,
    radius: 30,
    xSpeed: 5,
    ySpeed: 3,
    color: color(255, 0, 0),
  };
  bgColor = color(200, 200, 255);
}

function draw() {
  // Gradually change the background color over time
  bgColor = lerpColor(bgColor, color(200, 200, 255), 0.01);
  background(bgColor);

  // Update ball position based on speed
  ball.x += ball.xSpeed;
  ball.y += ball.ySpeed;

  // Bounce off walls
  if (ball.x < ball.radius || ball.x > width - ball.radius) {
    ball.xSpeed *= -1;
  }
  if (ball.y < ball.radius || ball.y > height - ball.radius) {
    ball.ySpeed *= -1;
  }

  // Draw the bouncing ball
  noStroke();
  fill(ball.color);
  ellipse(ball.x, ball.y, ball.radius * 2, ball.radius * 2);
}

function keyPressed() {
  // Change the ball's color when a key is pressed
  ball.color = color(random(255), random(255), random(255));
}
```
## Learning notes
Dynamic Background:
Similar to the previous example, the background color gradually changes over time using lerpColor, creating a smooth transition effect.

Bouncing Ball:
The ball's position is updated based on its speed, creating a bouncing effect. The if statements check for collisions with the canvas edges, causing the ball to bounce.

User Input:
The keyPressed() function is triggered whenever a key is pressed. In this case, it changes the color of the ball to a random color.

Object Representation:
The ball is represented as an object (ball) with properties such as x, y, radius, xSpeed, ySpeed, and color. This object-oriented approach makes it easier to manage and update the ball's state.

Color Transition:
The background color transition and the random color change on key press add an element of surprise and playfulness to the sketch.

Interactive Movement:
Users can control the direction and speed of the ball indirectly through the keyboard, making the sketch interactive and engaging.
### Acknowledgement
Provided by: Matt Walker
Github: mttwlker

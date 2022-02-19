let balls = [];

// time in seconds since simulation started
let t = 0;

// time elapsed per frame
let framerate = 30;
let timestep = 1/framerate;

function setup() {
  createCanvas(1000, 500);

  //            radius, mass, vx, vy, x, y, color
  balls.push(new Ball(20, 10, 50, 0, 250, 250, 'blue'));
  balls.push(new Ball(20, 10, 50, 0, 250, 250, 'green'));
  balls.push(new Ball(20, 10, 50, 0, 250, 250, 'purple'));

  frameRate(framerate);
}

function draw() {
  background(220);
  line(0,250,500,250);

  for (let i = 0; i < balls.length; i++) {
    balls[i].draw();
  }

  update();
}

function update() {
  // every frame, increase the time by this timestep
  t += timestep;
  balls[0].standard(timestep);
  balls[1].euler(timestep, 0.1);
  balls[2].runge_kutta_4(timestep);
}

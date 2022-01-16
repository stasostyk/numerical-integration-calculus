let balls = [];


function setup() {
  createCanvas(500, 500);
  balls.push(new Ball(20, 10, 2, 0, 250, 250, 'green'));
  balls.push(new Ball(20, 10, 2, 0, 250, 250, 'blue'));
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
  balls[0].euler(1000);
  balls[1].standard();
}

class Ball {
  constructor(radius, mass, vx, vy, x, y, color) {
    this.r = radius;
    this.m = mass;
    this.vx = vx;
    this.vy = vy;
    this.color = color;

    this.x = x;
    this.y = y;

    this.g = 0.1;
  }

  draw() {
    fill(color(this.color))
    circle(this.x, this.y, this.r);
  }

  bounce() {
    if (this.x+this.r/2 >= width || this.x-this.r/2 <= 0)
        this.vx *= -1;

    if (this.y+this.r/2 >= height || this.y-this.r/2 <= 0)
      this.vy *= -1;
  }

  standard() {
    this.x += this.vx;
    this.vy += this.g;
    this.y += this.vy;

    this.bounce();
  }

  euler(dt) {
    for (let i = 0; i < dt; i++) {
      this.x += this.vx/dt;
      this.vy += this.g/dt;
      this.y += this.vy/dt;

    this.bounce();
    }
  }

  new_vel(x, t) {
    return x + this.g*t;
  }

  runge_kutta_4(dt) {
    let k1, k2, k3, k4;

    k1 = dt*new_vel(this.x, 1)
  }

}

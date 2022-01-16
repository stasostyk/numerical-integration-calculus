class Ball {
  constructor(radius, mass, vx, vy, x, y, color) {
    this.r = radius;
    this.m = mass;
    this.vx = vx;
    this.vy = vy;
    this.color = color;

    this.x = x;
    this.y = y;

    this.g = 981;

    this.w = 500;
    this.h = 500;
  }

  draw() {
    fill(color(this.color))
    circle(this.x, this.y, this.r);
  }

  bounce() {
    if (this.x+this.r/2 >= this.w || this.x-this.r/2 <= 0)
        this.vx *= -1;

    if (this.y+this.r/2 >= this.h || this.y-this.r/2 <= 0)
      this.vy *= -1;
  }

  standard(timestep) {
    this.x += this.vx*timestep;
    this.vy += this.g*timestep;
    this.y += this.vy*timestep;

    this.bounce();
  }

  euler(timestep, h) {
    for (let i = 0; i < 1/h; i++) {
      this.x += this.vx*timestep*h;
      this.vy += this.g*timestep*h;
      this.y += this.vy*timestep*h;

    this.bounce();
    }
  }

  dydt(t) {
    return this.vy + t*this.g;
  }

  runge_kutta_4(timestep) {
    // constant rates of change
    this.x += this.vx*timestep;

    // position
    let k1, k2, k3, k4;
    k1 = this.dydt(timestep * 0);
    k2 = this.dydt(timestep * 0.5);
    k3 = this.dydt(timestep * 0.5);
    k4 = this.dydt(timestep * 1);

    this.y += timestep * (k1 + 2*k2 + 2*k3 + k4)/6;
    this.vy += this.g*timestep;

    this.bounce();
  }

}

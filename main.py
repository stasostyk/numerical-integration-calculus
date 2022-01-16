TIMESTEP = 1
GRAV = 9.81

def standard(ball):
    ball.vy += GRAV*TIMESTEP
    ball.y += ball.vy*TIMESTEP

def euler(ball, h):
    for i in range(h):
        ball.vy += GRAV*TIMESTEP/h
        ball.y += ball.vy*TIMESTEP/h

def dydt(vy, t):
    return vy + t*GRAV


def runge_kutta_4(ball):
    k1 = dydt(ball.vy, TIMESTEP * 0)
    k2 = dydt(ball.vy, TIMESTEP * 0.5)
    k3 = dydt(ball.vy, TIMESTEP * 0.5)
    k4 = dydt(ball.vy, TIMESTEP * 1)

    ball.y += TIMESTEP * (k1 + 2*k2 + 2*k3 + k4)/6
    ball.vy += GRAV*TIMESTEP


class Ball(object):
    def __init__(self, name):
        self.y = 0
        self.vy = 0
        self.name = name

    def __str__(self):
        return self.name + "   y: {0}, vy: {1}".format(self.y, self.vy)


def main():
    time = 0

    ball1 = Ball("Standard")
    ball2 = Ball("Euler   ")
    ball3 = Ball("RK4     ")

    print(ball1)
    print(ball2)
    print(ball3)

    for i in range(1000000):
        time += 1
        standard(ball1)
        euler(ball2, 10)
        runge_kutta_4(ball3)

        print("==== t = {0}s ====".format(time))
        print(ball1)
        print(ball2)
        print(ball3)
        print("Ideal:     y: {0}, vy {1}".format(0.5*GRAV*time*time, GRAV*time))


if __name__ == "__main__":
    main()

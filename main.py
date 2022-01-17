import numpy as np
import matplotlib.pyplot as plt

TIMESTEP = 1/30
GRAV = 981
HEIGHT = 100

def standard(ball):
    # if not ball.bounce():
    ball.vy += GRAV*TIMESTEP
    ball.y += ball.vy*TIMESTEP
    ball.bounce()

def euler(ball, h):
    for i in range(h):
        ball.vy += GRAV*TIMESTEP/h
        ball.y += ball.vy*TIMESTEP/h
    ball.bounce()

def dydt(vy, t):
    return vy + t*GRAV


def runge_kutta_4(ball):

    k1 = dydt(ball.vy, TIMESTEP * 0)
    k2 = dydt(ball.vy, TIMESTEP * 0.5)
    k3 = dydt(ball.vy, TIMESTEP * 0.5)
    k4 = dydt(ball.vy, TIMESTEP * 1)

    ball.y += TIMESTEP * (k1 + 2*k2 + 2*k3 + k4)/6
    ball.vy += GRAV*TIMESTEP
    ball.bounce()


class Ball(object):
    def __init__(self, name):
        self.y = 0
        self.vy = 0
        self.name = name

        self.data_y = [0]
        self.data_vy = [0]

    def bounce(self):
        if self.y >= HEIGHT and self.vy > 0:
            self.vy *= -1
            return True
        return False

    def log(self):
        self.data_y.append(self.y)
        self.data_vy.append(self.vy)

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

    seconds = float(input("Seconds: "))

    for i in range(round(seconds/TIMESTEP)):
        time += 1

        standard(ball1)
        ball1.log()

        euler(ball2, 5)
        ball2.log()

        runge_kutta_4(ball3)
        ball3.log()

    print("==== t = {0}s ====".format(time))
    print(ball1)
    print(ball2)
    print(ball3)
    print("Ideal:     y: {0}, vy {1}".format(0.5*GRAV*time*time, GRAV*time))

    # show graphs
    time_axis = np.array(list(range(0, time+1)))*TIMESTEP

    diff = np.subtract(ball3.data_y, ball1.data_y)
    ideal = [0.5*GRAV*t*t for t in range(time+1)]

    # plt.plot(time_axis, diff, label="RK4-Standard Difference")
    plt.plot(time_axis, ball3.data_y, label="RK4")
    plt.plot(time_axis, ball2.data_y, label="Euler")
    plt.plot(time_axis, ball1.data_y, label="Standard")
    # plt.plot(time_axis, ideal, label="Ideal")
    plt.xlabel('time')
    plt.ylabel('meters')
    plt.title('RK4-Euler Difference Graph')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

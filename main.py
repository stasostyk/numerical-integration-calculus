import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# ============ GLOBAL VARIABLES ============ #
# timestep for the simulation -- 1/(computations per second)
TIMESTEP = 1/30
# gravitational constant 'g', in meters per seconds squared
GRAV = -9.81
# should the ball bounce or not
BOUNCE = True
# height, in meters, at which the ball should bounce
HEIGHT = 0
# show trendline for error graph
MAXIMA = True


# ============ IMPLICIT INTEGRATION METHODS ============ #
# Conventional Integration Approximation
def euler(ball):
    ball.vy += GRAV*TIMESTEP
    ball.y += ball.vy*TIMESTEP
    ball.bounce()

# Euler Method Integration Approximation
def double_euler(ball, h):
    for i in range(round(h):
        ball.vy += GRAV*TIMESTEP*h
        ball.y += ball.vy*TIMESTEP*h
    ball.bounce()

# Ordinary Differential Equation being solved
def dydt(vy, t):
    return vy + t*GRAV

# Runge-Kutte 4th Order Integration Approximation
def runge_kutta_4(ball):
    k1 = dydt(ball.vy, TIMESTEP * 0)
    k2 = dydt(ball.vy, TIMESTEP * 0.5)
    k3 = dydt(ball.vy, TIMESTEP * 0.5)
    k4 = dydt(ball.vy, TIMESTEP * 1)

    ball.y += TIMESTEP * (k1 + 2*k2 + 2*k3 + k4)/6
    ball.vy += GRAV*TIMESTEP
    ball.bounce()

# class object of mass, generalized to a ball
class Ball(object):
    def __init__(self, name, vy):
        self.y = 0
        self.vy = vy
        self.name = name

        self.data_y = [0]
        self.data_vy = [0]

# check for collision with floor
    def bounce(self):
        if BOUNCE and self.y <= HEIGHT and self.vy < 0:
            self.vy *= -1
            return True
        return False

# log current position and velocity
    def log(self):
        self.data_y.append(self.y)
        self.data_vy.append(self.vy)

# print status of current ball object
    def __str__(self):
        return self.name + "   y: {0}, vy: {1}".format(self.y, self.vy)


# main function
def main():
    # time elapsed since simulation began
    time = 0

    # prompt user for seconds to run the simulation for
    # important timesteps: {300 seconds, shows long-term damping
    #                       0.1 seconds, shows miniscule changes}
    seconds = float(input("Seconds: "))

    # initialize instances of all test objects
    ball1 = Ball("Standard", 20)
    ball2 = Ball("Euler   ", 20)
    ball3 = Ball("RK4     ", 20)


    # ============ MAINLOOP ============ #
    for i in range(round(seconds/TIMESTEP)):
        # time goes up by one -- note, this time is not in seconds, rather frames
        time += 1

        # approximate rate of change of each ball and apply it
        euler(ball1)
        ball1.log()

        double_euler(ball2, 0.2)
        ball2.log()

        runge_kutta_4(ball3)
        ball3.log()

    # end mainloop

    # print final status of simulation
    print("==== t = {0}s ====".format(time*TIMESTEP))
    print(ball1)
    print(ball2)
    print(ball3)
    print("Ideal:     y: {0}, vy {1}".format(0.5*GRAV*time*time, GRAV*time))


    # ============ GRAPHICS DISPLAY ============ #
    # time axis, computed using timestep for real-world seconds
    time_axis = np.array(list(range(0, time+1)))*TIMESTEP

    # implicitly solved ODE -- note, this only works when BOUNCE = 'False'
    ideal = [0.5*GRAV*t*t*TIMESTEP*TIMESTEP for t in range(int(time+1))]

    # position-time graph
    plt.figure(1)
    # load all plotlines to be shown on graph
    plt.plot(time_axis, ball3.data_y, label="RK4")
    plt.plot(time_axis, ball2.data_y, label="Double Euler")
    plt.plot(time_axis, ball1.data_y, label="Euler")
    # plt.plot(time_axis, ideal, label="Ideal")

    # setup graph parameters
    plt.xlabel('time (seconds)')
    plt.ylabel('position (meters)')
    plt.title('Position-Time Graph')
    plt.legend()

    # error graph

    # difference between the positions of RK4 and other integration methods across time
    RK4vsSTDRD = np.subtract(ball3.data_y, ball1.data_y)
    RK4vsEULER = np.subtract(ball3.data_y, ball2.data_y)

    plt.figure(2)
    plt.plot(time_axis, RK4vsSTDRD, label="RK4-Standard Difference")
    plt.plot(time_axis, RK4vsEULER, label="RK4-Euler Difference")

    # find all maxima
    if MAXIMA:
        maxima_x = np.array(argrelextrema(RK4vsEULER, np.greater))[0]
        maxima_y = [RK4vsEULER[maxima_x[i]] for i in range(len(maxima_x))]
        maxima_x = [i*TIMESTEP for i in maxima_x]
        maxima_x.insert(0,0)
        maxima_y.insert(0,0)
        print(maxima_x)
        plt.plot(maxima_x, maxima_y, label="Error Maxima")

    plt.xlabel('time (seconds)')
    plt.ylabel('difference (meters)')
    plt.title('Error-Time Graph')
    plt.legend()

    plt.show()


# run script
if __name__ == "__main__":
    main()

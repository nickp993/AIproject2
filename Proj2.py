# Filename: Proj2.py
# Nick Pascarella np5@umbc.edu
# 3/1/16
#
#
#For this project I will code several of the local searches we discussed in class and apply them.


import sys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import math
import random


def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):



    x = random.randrange(xmin, xmax)
    y = random.randrange(ymin, ymax)

    xList = []
    yList = []
    zList = []

    #xTup = (x)
    #yTup = (y)

    counter = 0

    while counter < 100:

        print "x: ", x
        print "y: ", y


        xnew = x + random.random() -step_size
        ynew = y + random.random() -step_size

        print "xnew: ", xnew
        print "ynew: ", ynew

        currValue = function_to_optimize(x,y)
        newValue = function_to_optimize(xnew, ynew)

        print "currValue = ", currValue
        print "newValue = ", newValue

        if newValue < currValue:

            #concatenating tuples
            #tempX = (x)
            #tempY = (y)
            #xTup = xTup + tempX
            #yTup = yTup + tempY

            xList.append(x)
            yList.append(y)
            zList.append(currValue)

            print "        LISTS APPENDED"

            counter = 0
            x = xnew
            y = ynew

        else:
            counter = counter + 1

    return xList, yList, zList

    #pass

def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):

    x = random.randrange(xmin, xmax)
    y = random.randrange(ymin, ymax)

    xList = []
    yList = []
    zList = []

    counter = 0
    currRestarts = 0

    while currRestarts < num_restarts:

        while counter < 100:

            print "x: ", x
            print "y: ", y

            xnew = x + random.random() -step_size
            ynew = y + random.random() -step_size

            print "xnew: ", xnew
            print "ynew: ", ynew


            currValue = function_to_optimize(x,y)
            newValue = function_to_optimize(xnew, ynew)

            print "currValue = ", currValue
            print "newValue = ", newValue

            #initializes lowestValue
            if currRestarts == 0:
                lowestValue = currValue


            if newValue < currValue:

                counter = 0

                xList.append(x)
                yList.append(y)
                zList.append(currValue)

                x = xnew
                y = ynew

            else:
                counter = counter + 1
                print "           Counter = ", counter


        counter = 0

        print("---------Restarted----------")
        currRestarts = currRestarts + 1
        print("Restarts: ", currRestarts)

        #the above while loop can only break when the counter is incremented so
        #currValue never needs to be set to newValue
        if currValue < lowestValue:
            lowestValue = currValue

            print("")
            print("New Low")
            print(lowestValue)
            print("")

            lowX = x
            lowY = y

            print(lowX)
            print(lowY)

        x = random.randrange(xmin, xmax)
        y = random.randrange(ymin, ymax)

    print "Lowest Value is ", lowestValue
    print(lowX)
    print(lowY)

    return xList, yList, zList

def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):

    x = random.randrange(xmin, xmax)
    y = random.randrange(ymin, ymax)

    xList = []
    yList = []
    zList = []

    counter = 0
    temp = max_temp

    while True:

        if temp == 0:

            print "          LOWEST = ", lowestValue
            print lowX
            print lowY
            return xList, yList, zList

        print(x)
        print(y)

        xnew = x + random.random() -step_size
        ynew = y + random.random() -step_size

        currValue = function_to_optimize(x,y)
        newValue = function_to_optimize(xnew, ynew)

        if temp == max_temp:
            lowestValue = currValue

        print "currValue = ", currValue
        print "newValue = ", newValue

        changeInVal = newValue - currValue

        print "Change in Val:"
        print changeInVal
        print "        Temp = ", temp

        if changeInVal < 0:

            xList.append(x)
            yList.append(y)
            zList.append(currValue)

            x = xnew
            y = ynew
        else:

            acceptanceOdds = math.exp(changeInVal/temp)



            print acceptanceOdds

            if acceptanceOdds > 1:

                xList.append(x)
                yList.append(y)
                zList.append(currValue)

                x = xnew
                y = ynew

        if currValue < lowestValue:
            lowestValue = currValue

            lowX = x
            lowY = y

        temp = temp - 1


    #return xList, yList, zList


def testFunction(x, y):
    return x**2 + y**2 -10

#def function_to_optimize(x, y):
#    r = math.sqrt(math.pow(x,2) + math.pow(y,2))

#    z = (math.sin(math.pow(x,2) + 3*math.pow(y,2)))/(0.1 + math.pow(r,2)) + (math.pow(x,2) + 5*math.pow(y,2))*((math.exp(1-math.pow(r, 2)))/2)

#    return z

def function_to_optimize(x, y):

    r = math.sqrt(x**2 + y**2)

    return (math.sin(x**2 + 3*y**2)/(0.1 + r**2)) + (x**2 + 5*y**2)* (math.exp(1-r**2)/2)


def main():


    xList, yList, zList = hill_climb(function_to_optimize, 0.5, -3, 3, -3, 3)

    #xList, yList, zList = hill_climb_random_restart(function_to_optimize, 0.5, 100, -3, 3, -3, 3)

    #xList, yList, zList = simulated_annealing(function_to_optimize, 0.5, 100, -3, 3, -3, 3)
    #plt.ylabel('Example')

    fig = plt.figure()
    ax = Axes3D(fig)
    #use this for 2d plots
    #plt.plot(xList,yList,'ro')
    #or this for 3d

    ax.plot(xList,yList,zList,'ro')
    # coordinates look like [x,y,z]
    # but this is what is being plotted ([x1, x2...], [y1, y2...], [z1, z2...])

    plt.show()



main()
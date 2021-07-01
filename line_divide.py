
import math
import matplotlib.pyplot as plt
import numpy as np


def divide(hub, coords):
    line_weights = {}

    #axes = plt.gca()
    #axes.set_xlim([0,70])
    #axes.set_ylim([-10,60])

    for i in range(0, 180, 5):
        slope = math.tan(i*math.pi/180)
        leftweight = 0
        rightweight = 0

        for village in coords:
            if (village[1]-hub[1])-slope*(village[0]-hub[0]) >= 0:
                leftweight = leftweight + 1

            elif (village[1]-hub[1])-slope*(village[0]-hub[0]) < 0:
                rightweight = rightweight + 1

        line_weight = abs(leftweight-rightweight)

        line_weights[i] = line_weight

    best = {k: v for k, v in sorted(
        line_weights.items(), key=lambda item: item[1])}
    best = next(iter(best))
    slope = best
    weight = line_weights[best]
    #print("ideal", slope, weight)

    x = np.array(range(100))
    slope = math.tan(slope*math.pi/180)
    y = slope*(x-hub[0])+hub[1]
    
    # Create the plot
    #plt.plot(x,y)

    x_coords = []
    y_coords = []

    for village in coords: 
        x_coords.append(village[0])
        y_coords.append(village[1])
    
    #plt.scatter(x_coords,y_coords)
    #plt.scatter(hub[0],hub[1])
    #plt.show()
    space1 = []
    space2 = []

    for village in coords:
        if (village[1]-hub[1])-slope*(village[0]-hub[0]) >= 0:
            space1.append(village)

        elif (village[1]-hub[1])-slope*(village[0]-hub[0]) < 0:
            space2.append(village)
    #print(space1, space2)

    return (space1, space2)

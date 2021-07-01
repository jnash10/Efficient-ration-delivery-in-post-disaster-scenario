import numpy as np

def dist(a, b):
        return int(((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2))

def matrix(cities):
    dist_matrix = []

    for city in cities:
        city_dist = []
        for i in range(0,len(cities)):
            city_dist.append(dist(city,cities[i]))
        #print(type(city_dist), city_dist)
        dist_matrix.append(city_dist)

    dist_matrix = np.array(dist_matrix)
    #print(dist_matrix)
    dist_matrix[:, 0]=0

    return dist_matrix


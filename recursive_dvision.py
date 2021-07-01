from line_divide import divide
from case_generator import case_gen
from python_tsp.exact import solve_tsp_dynamic_programming
from dist_matrix import matrix
import matplotlib.pyplot as plt


coords, distance_matrix = case_gen()

hub = coords[0]
#hub = (20,20)
coords = coords[1:]
print("croods: ",coords)
max_dist=65

def divider(hub, coords, route = []):

    subspace1= divide(hub, coords)[0]
    subspace2 = divide(hub, coords)[1]
    #print(subspace1, subspace2)
    subspace1.insert(0,hub)
    subspace2.insert(0,hub)
    #print(subspace1, subspace2)
    
    dist1 = matrix(subspace1)
    #print(dist1)
    dist2 = matrix(subspace2)
    #print(dist2)
    
    route1 = []
    route2 = []

    perm1, distance1 = solve_tsp_dynamic_programming(dist1)
    perm2, distance2 = solve_tsp_dynamic_programming(dist2)
    #print(perm1,perm2)

    


    for point in perm1:
        #print(point, subspace1, route1)
        #print(point, subspace1)
        route1.append(subspace1[point])

    for point in perm2:
        #print(point, subspace2, route1)
        #print(point, subspace2)
        route2.append(subspace2[point])
    
    subspace1.pop(0)
    subspace2.pop(0)

    if distance1 <= max_dist and len(subspace1)<=17:
        route.append(route1)
    
    else:
        divider(hub, subspace1, route)

    if distance2 <= max_dist and len(subspace2)<=17:
        route.append(route2)
    
    else:
        divider(hub, subspace2, route)

    return route

final_route = divider(hub, coords)

for route in final_route:
        x_coords = []
        y_coords = [] 
        for village in route:
            x_coords.append(village[0])
            y_coords.append(village[1])
        plt.scatter(x_coords,y_coords)
        plt.plot(x_coords, y_coords)
plt.scatter(hub[0],hub[1])  
plt.show()

print(final_route)


    
    





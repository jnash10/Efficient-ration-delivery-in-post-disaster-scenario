from line_divide import divide
from case_generator import case_gen
from python_tsp.exact import solve_tsp_dynamic_programming
from dist_matrix import matrix
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1500)

coords, distance_matrix = case_gen()

hub = coords[0]
#hub = (20,20)
coords = coords[1:]
print("croods: ",coords)
max_dist=65

def divider(hub, coords, route = []):

    subspace1= divide(hub, coords)[0]
    subspace2 = divide(hub, coords)[1]
    

    subspace1.insert(0,hub)
    subspace2.insert(0,hub)
    

    for space in [subspace1, subspace2]:
        if len(space)<17:
            dist1 = matrix(space)
            #print(dist1)
            route1 = []
            perm1, distance1 = solve_tsp_dynamic_programming(dist1)
            if distance1 < max_dist:
                for point in perm1:
                    route1.append(space[point])
                route.append(route1)
            else:
                space.pop(0)
                divider(hub, space, route)
        
        else:
            space.pop(0)
            divider(hub, space, route)

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

for route in final_route:
    print(route)


    
    





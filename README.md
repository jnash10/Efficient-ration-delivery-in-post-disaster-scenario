# Efficient-ration-delivery-in-post-disaster-scenario
Algorithm that combines concepts from TSP to generate an efficient solution to a cost constrained multiple travelling salesman problem. 

Read above PDF for comprehesive guide.(or check it out here: https://drive.google.com/file/d/1Y9pvj-UZODDZr3Sdo1hs6HYyp6qrmbbI/view?usp=sharing)

python library requirements:

```
  pip install python-tsp
  pip install numpy
  pip install matplotlib
```

to run the code:
```
python recrusive_division.py
```
Since the TSP algorithm being used currently is an exact one(using dynamic programming), 25 cities/villages should be the upper limit for the program to run comfortably on most systems. 
(currently it generates random villages and a hub and solves for that)

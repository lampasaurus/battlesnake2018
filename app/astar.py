# Author: Christian Careaga (christian.careaga7@gmail.com)
# A* Pathfinding in Python (2.7)
# Please give credit if used

# Edited for use in Battlesnake by Keiran Reilly (keiranreilly7@gmail.com)
#Use: nextmove(map, start point, end point) will take a grid of 1's and non 1's, 1 being walls and anything other than a 1 being treated as empty space, and return the next step on the path from start point to end point
#example use
import numpy
from heapq import *

WALL = 1
FOOD = 2
HEAD = 3
SELFHEAD = 4

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

#PUT THIS IN THE MAIN SNAKE FILE
#Creates a map of the game board from data
#Call on each move
def createMap(data):
	map =[[0 for x in range(board_width)] for y in range(board_height)] 
	for snake in data['snakes']:
		for data in snake['data']['body']['data']:
			map[data.x, data.y] = WALL
			
	for food in data['food']['data']:
		map[food.x, food.y] = FOOD
		
	print map;
	return map
	
def nextMove(array, start, goal):
	if array[start[0],start[1]] == WALL:
		print "error start point is wall"
	if array[goal[0],goal[1]] == WALL:
		print "error end point is wall"
		return "up"
		
	trail = astar(array, start, goal)
	next = trail[len(trail)-1]
	if next[0]-start[0]==1:
		return "up"
	if next[0]-start[0]==-1:
		return "down"
	if next[1]-start[1]==1:
		return "right"
	if next[1]-start[1]==-1:
		return "left"
		
	return "up"
	
def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == WALL:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

'''Here is an example of using my algo with a numpy array,
   astar(array, start, destination)
   astar function returns a list of points (shortest path)
'''
nmap = numpy.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
print WALL
print nextMove(nmap, (0,0), (0,1))
#print astar(nmap, (0,0), (10,0))
# Credit: https://en.wikipedia.org/wiki/A*_search_algorithm

# Überarbeitung - Anpassen für das Projekt
# Gescheitert

import math

from config import possibleMoves

def reconstructPath(cameFrom: dict, current):
    totalPath = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.insert(0, current)
    return totalPath


def aStar(start, goal, grid):
    openSet = [start]

    cameFrom = dict()

    gScore = dict()
    gScore[start] = 0

    fScore = {}
    fScore[start] = h(start, goal)

    while len(openSet) > 0:
        current = min(openSet, key=lambda x: fScore[x])
        if current == goal:
            return reconstructPath(cameFrom, current)

        openSet.remove(current)
        for neighbor in map(lambda x: (current[0] + x[0], current[1] + x[1]), possibleMoves):
            #if not raum.getFelder()[neighbor[1]][neighbor[0]].canRobotMoveHere():
            #    continue

            tenitive_gScore = gScore[current] + d(current, neighbor)

            if tenitive_gScore < gScore.get(neighbor, math.inf):
                cameFrom[neighbor] = current
                gScore[neighbor] = tenitive_gScore
                fScore[neighbor] = tenitive_gScore + h(neighbor, goal)
                if not neighbor in openSet:
                    openSet.append(neighbor)

    print("Path finding did not work")

def d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

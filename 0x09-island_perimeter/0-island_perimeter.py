#!/usr/bin/python3
"""island perimeter
"""

from typing import List


def island_perimeter(grid: List[list]) -> int:
    # initialize the perimeter
    perimeter: int = 0
    # loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # check if its a land
            if grid[i][j] == 1:
                # calculate the perimeter which is sum of all 4 sides
                # i.e 1+1+1+1 = 4
                perimeter += 4
                # check if the horizontal neighbour share sides
                if i > 0 and grid[i-1][j] == 1:
                    # they share sides, hence subtract 2 from the perimeter
                    perimeter -= 2
                # if the vertical neighbour share sides
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter

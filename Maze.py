"""
Maze.py
Class for the maze to traverse
Adapted from UCSD CSE 12
"""

##from .Tile import Tile

class MazeSolver():
    def __init__(self, maze_spec):
        # Initialize MazeSolver with a Maze instance and an empty Stack
        self.maze = Maze(maze_spec)
        self.ss = Stack()

    def tileIsVisitable(self, row, col):
        """
        Check whether or not the tile at the given coordinates is visitable.
        """
        # Ensure that the given coordinates are within the maze boundaries
        if 0 <= row < self.maze.num_rows and 0 <= col < self.maze.num_cols:
            # Retrieve the tile at the specified coordinates
            tile = self.maze.contents[row][col]
            # Check if the tile is not a wall and has not been visited
            return not tile.isWall() and not tile.visited()
        return False

    def solve(self):
        """
        Solve the maze using the search algorithm.
        """
        # Add the starting tile to the stack
        self.ss.add(self.maze.start)

        # Continue until the stack is empty
        while not self.ss.isEmpty():
            # Remove the next tile from the stack and mark it as visited
            current = self.ss.remove()
            current.visit()

            # Check if the current tile is the goal
            if current == self.maze.goal:
                return current
            else:
                # Define the neighboring tiles in the order North, South, East, West
                neighbors = [
                    (current.getRow() - 1, current.getCol()),  # North
                    (current.getRow() + 1, current.getCol()),  # South
                    (current.getRow(), current.getCol() + 1),  # East
                    (current.getRow(), current.getCol() - 1)   # West
                ]

                # Iterate through neighbors
                for neighbor_row, neighbor_col in neighbors:
                    # Check if the neighbor is visitable
                    if self.tileIsVisitable(neighbor_row, neighbor_col):
                        neighbor = self.maze.contents[neighbor_row][neighbor_col]
                        # Set the previous tile for the neighbor to the current tile
                        neighbor.setPrevious(current)
                        # Add the neighbor to the stack
                        self.ss.add(neighbor)

        # If the loop completes without finding a solution, return None
        return None

    def getPath(self):
        """
        Get the path of the solution to the maze.
        """
        path = []
        current = self.maze.goal

        # Backtrack from the goal to the start to retrieve the path
        while current is not None:
            path.insert(0, current)
            current = current.getPrevious()

        return path
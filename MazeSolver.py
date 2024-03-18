"""
Maze.py
Luis Orellana
"""

##from .Tile import Tile

class MazeSolver:
    def __init__(self, maze_spec):
        # Initialize MazeSolver with a Maze instance and an empty Stack
        self.maze = Maze(maze_spec)  # Assuming this initializes the maze with start and goal tiles
        self.ss = Stack()  # Replace with Queue() if breadth-first search is required

    def tileIsVisitable(self, row, col):
        # Check whether or not the tile at the given coordinates is visitable.
        if 0 <= row < self.maze.num_rows and 0 <= col < self.maze.num_cols:
            tile = self.maze.contents[row][col]
            return not tile.isWall() and not tile.visited()
        return False

    def solve(self):
        # Solve the maze using the search algorithm.
        self.ss.add(self.maze.start)
        while not self.ss.isEmpty():
            current = self.ss.remove()
            current.visit()
            if current == self.maze.goal:
                return current
            else:
                neighbors = [
                    (current.getRow() - 1, current.getCol()),  # North
                    (current.getRow() + 1, current.getCol()),  # South
                    (current.getRow(), current.getCol() + 1),  # East
                    (current.getRow(), current.getCol() - 1)   # West
                ]
                for neighbor_row, neighbor_col in neighbors:
                    if self.tileIsVisitable(neighbor_row, neighbor_col):
                        neighbor = self.maze.contents[neighbor_row][neighbor_col]
                        neighbor.setPrevious(current)
                        self.ss.add(neighbor)
        return None

    def getPath(self):
        # Get the path of the solution to the maze.
        path = []
        current = self.maze.goal
        while current is not None:
            path.insert(0, current)
            current = current.getPrevious()
        return path

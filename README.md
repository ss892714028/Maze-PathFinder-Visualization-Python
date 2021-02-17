## Maze PathFinder Visualizer implemented in Python
### How to use
* The first two left clicks on the board initialize start and end node
* Click or click and drag to create obstacles
* Press space bar and see the algorithm takes off!
### Symbols
#### "@": Start and end node
#### "#": Obstacles
#### "*": Visited node
#### "+": Path

### Algorithm Implemented
* BFS (unweighted Dijastra)
* DFS
* ASTAR (A*)

### Breadth First Search (unweighted Dijkstra)
Breadth First Search is unweighted and guarantee a optimal path.
![BFS](https://github.com/ss892714028/Maze-PathFinder-Visualization-Python/blob/master/gifs/bfs.gif)

### Depth First Search
Depth First Search is unweighted and does not guarantee a optimal path.
![DFS](https://github.com/ss892714028/Maze-PathFinder-Visualization-Python/blob/master/gifs/dfs-nonoptimal.gif)

### Astar (A*)
A* is weighted and guarantee a optimal path.                                                         
![A* easy](https://github.com/ss892714028/Maze-PathFinder-Visualization-Python/blob/master/gifs/a-star_ez.gif)
![A*](https://github.com/ss892714028/Maze-PathFinder-Visualization-Python/blob/master/gifs/a-star.gif)

# Dijkstra's Algorithm 

This program visualizes a pathfinding example using Python's built-in `turtle`
graphics. It draws a grid containing randomly placed blocked cells, builds a
graph from the cells that can be traversed, and searches for a route from the
upper-left corner to the lower-right corner which is fixed.

## Requirements

- Python 3
- A desktop environment that supports Tkinter, which Python's Turtle graphics
  uses to open its window

The program uses only Python standard-library modules; no third-party packages
are needed.

## Run

From the directory containing `dijkstra_algorithm.py`, run:

```bash
python dijkstra_algorithm.py
```

A Turtle window opens with a 6-by-6 grid. Each run generates a new random
obstacle layout, so the route (or whether a route exists) can change.

## What the program does

The code is organized into these functions:

- `initialize_screen()` creates and configures an 800-by-800 Turtle window,
  sets the drawing coordinates, and writes the title.
- `draw_square(x_start_coord, y_start_coord, side_length)` draws one square
  cell, starting at its lower-left coordinate.
- `draw_grid()` draws the 6-by-6 grid and returns the coordinates of traversable
  cells. The start cell `(-300, 200)` is red, the goal cell `(200, -300)` is
  lime, and other cells are randomly colored white or wheat. Wheat cells are
  treated as obstacles; white cells are traversable.
- `build_graph(grid_array)` makes a graph represented by a dictionary. Each
  traversable coordinate is a node, and its value is a list of traversable
  neighbors directly above, below, left, or right. Diagonal movement is not
  allowed.
- `dijkstra(...)` searches the graph for a route. It tracks tentative distances
  in `visited_dist`, uses `999` as the initial "infinity" value, and updates
  neighboring nodes with a cost of one per move. It returns a list of
  coordinates for a route, or `None` when it cannot find one.
- `draw_path(paths)` moves the Turtle through the returned coordinates, drawing
  the route in blue.

## Grid and coordinates

Each cell is 100 units wide. The grid's lower-left coordinates range from
`-300` through `200` on both axes:

```text
Start (-300, 200)                 (200, 200)
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
       |     |     |     |     |     |     |
       +-----+-----+-----+-----+-----+-----+
(-300, -300)                 Goal (200, -300)
```

Coordinates identify the lower-left corner of a cell. The Turtle is moved to
the center of each cell when drawing the route.



####################### IMPORT MODULES #######################
import turtle
import random
##############################################################

def initialize_screen():
    global screen
    screen = turtle.Screen()
    turtle.shape('turtle')
    screen.setup(800, 800)
    screen.title('Dijkstra Algorithm')
    screen.setworldcoordinates(-400, -400, 400, 400)
    turtle.speed(0)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-275, 350)
    turtle.pencolor('red')
    turtle.write('Dijkstra Algorithm using turtle' , font=('Arial', 20, 'bold'))
    turtle.pencolor('black')


def draw_square(x_start_coord, y_start_coord, side_length):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x_start_coord, y_start_coord)
    turtle.pendown()
    for square_side in range(1, 5):
        turtle.forward(side_length)
        turtle.setheading(square_side * 90)


def draw_grid():
    obstacles_coord_list = []
    grid_array = []
    for row in range(200, -400, -100):
        for col in range(-300, 300, 100):
            if row == 200 and col == -300:
                color = ['red']
            elif row == -300 and col == 200:
                color = ['lime']
            else:
                color = random.choices(['wheat', 'white'], weights=(40, 120), k=2)
            if color[0] != 'wheat':
                grid_array.append((col, row))
            turtle.fillcolor(color[0])
            turtle.begin_fill()
            draw_square(col, row, 100)
            turtle.end_fill()
    return grid_array


##############################################################

def build_graph(grid_array):
    """
    Purpose:
    ---
    This function builds the graph required by Dijkstra's Algorithm.

    Input Arguments:
    ---
    `grid_array`	:  [ list of tuples ]
        This list contains cells (excluding random obstacles) in the form (col, row) where the range of values of
        col and row are fixed from -300 to 200. You can refer below for better understanding-

        (Start Node)
        (-300, 200) - - - - (200,200)
        |			  				|
        |	_	_	(0,0)	_	_	|
        |							|
        |							|
        (-300,-300) - - - - (200,-300)
                            (End Node)

    Returns:
    ---
    `graph` 	:  [ dictionary ]
        A dictionary consisting of Key, Value pairs as listed below-
        {(-300, 200): [(-200, 200)], (-200, 200): [(-300, 200), (-200, 100)] ...... }
            Node		Neighbor		Node		Neighbor 1	 Neighbor 2

    """

    graph=({})
    neighbours=[]

    for arr1 in grid_array:
        for arr2 in grid_array:
            y1=arr1[1]
            x1=arr1[0]
            x2=arr2[0]
            y2=arr2[1]
            coordx=x1-x2
            coordy=y1-y2
            if (coordy==0 and coordx==-100) or (coordy==0 and coordx==100):
                if arr1!=arr2:
                    neighbours.append(arr2)
            if (coordx==0 and coordy==-100) or (coordx==0 and coordy==100):
                    if arr1!=arr2:
                        neighbours.append(arr2)
        graph[(arr1)]=(neighbours)
        neighbours=[]
    return graph

##################################################
   


def dijkstra(graph, start_coord, end_coord,visited_dist,unvisited_nodes,path):  
    """
    Purpose:
    ---
    This function returns the shortest path using Dijkstra's Algorithm.

    Input Arguments:
    ---
    `To be decided by teams`

    Returns:
    ---
    `shortest_path` 	:  [ list of tuples]
        List of tuples present in the shortest path. For example:
        [(-300, 200), (-300, 100), (-300, 0), ..... ]

    """

    key1=start_coord
    neighlen=len(graph[key1])
    if key1==(-300,200) and neighlen==0: #START BLOCKED
        path=None
        return path
    if len(graph[end_coord])==0:
        path=None
        return path
    prev=start_coord
    neighlen=len(graph[key1])
    for m in range(neighlen):
        key2=graph[key1][m]
        if key2==end_coord:
            visited_dist.update({key2:visited_dist.get(key1)+1})          
            keys = list(visited_dist)
            for k in keys:
                if visited_dist[k] == 999:
                    del visited_dist[k]
            #path generation
            newgraph=({})
            newneighbours=[]
            paths=[(200,-300)]
            i=visited_dist.get(end_coord)
            i=i-1
            sorted_dist=sorted(visited_dist.items(),key=lambda item:item[1])
            sorted_dist1=(dict(sorted_dist))
            keys=list(sorted_dist1)
            parent=(200,-300)
            rs=[]
            r1=[]
            parents={}
            for r in keys:
                for q in keys:
                    y1=r[1]
                    x1=r[0]
                    x2=q[0]
                    y2=q[1]
                    coordx=x1-x2
                    coordy=y1-y2
                    if (coordy==0 and coordx==-100) or (coordy==0 and coordx==100):
                        if r!=q:
                            newneighbours.append(q)
                    if (coordx==0 and coordy==-100) or (coordx==0 and coordy==100):
                            if r!=q:
                                newneighbours.append(q)
                newgraph[(r)]=(newneighbours)
                newneighbours=[]
            keys2=list(newgraph)
            fp=[]
            newlist={}
            nlist1=[]
            rs=[]
            c=[]
            for keyz in keys2:
                d=len(newgraph[keyz])
                if d==1 and not (start_coord):
                    del newgraph[keyz]
                    fp.append(keyz)
                    for p in fp:
                        for k in newgraph:
                            length2=len(newgraph[k])
                            for m in range (length2):
                                keytemp=newgraph[k][m]
                                if keytemp!=p:
                                    nlist1.append(keytemp)
                            newlist[k]=(nlist1)
                            nlist1=[] #update neighbour list to remove keys with one neighbours
                    newgraph=newlist.copy()
                    c=[]
            for p in newgraph:
                flagb=0
                flaga=0
                tempo=len(newgraph[p])
                ni=sorted_dist1.get(p)
                if p==(200,-300):
                    break
                for g in range(tempo):
                    k2=newgraph[p][g]
                    distcheck=sorted_dist1.get(k2)
                    if distcheck== ni+1:
                        flaga=1
                    if distcheck== ni-1:
                        flagb=1
                if flaga!=1 or flagb!=1:
                    c.append(p)
            for nb in c:
                if nb!=(-300,200) or nb!=(200, -300):
                    del sorted_dist1[nb]          
            for h in reversed(newgraph): #making path
               if sorted_dist1.get(h)==i:
                    rs.append(h)
                    flag=0
                    for qr in rs:
                        y1=qr[1]
                        x1=qr[0]
                        x2=parent[0]
                        y2=parent[1]
                        coordx1=x1-x2
                        coordy1=y1-y2
                        if (coordy1==0 and coordx1==-100) or (coordy1==0 and coordx1==100):
                            i-=1
                            rtemp=r
                            rs=[]
                            paths.append(qr)
                            parent=qr
                            flag=1
                            break
                        if (coordx1==0 and coordy1==-100) or (coordx1==0 and coordy1==100):
                            i-=1
                            rtemp=r
                            rs=[]
                            paths.append(qr)
                            parent=qr
                            flag=1
                            break
            st=(-300,200)
            paths.append(st)
            return paths
            break
        if  (unvisited_nodes.get(key2)==0) and (visited_dist.get(key2) > (visited_dist.get(key1)+1)):
                    visited_dist.update({key2:visited_dist.get(key1)+1})
    del unvisited_nodes[key1]       
    f={}
    s={}
    for n in (unvisited_nodes):
        if unvisited_nodes.get(n)==0 and visited_dist.get(n)<999 and len(graph[n])>1:
            f.update({n:visited_dist.get(n)})
    if f=={}:
        paths=None
        return paths
    b=min(f.values())
    for key, value in f.items():
            if b == value and key in unvisited_nodes:
                prev=start_coord
                start_coord = key
        
    key1=start_coord
    return dijkstra(graph, start_coord, end_coord,visited_dist,unvisited_nodes,path)
             
##################################################
    
def draw_path(paths):
    """
    Purpose:
    ---
    This function should draw the shortest path as shown in documentation.

    Input Arguments:
    ---
    `path`	:	[list of tuples]

    Returns:
    ---
    None
"""
    turtle.shape('turtle')
    turtle.showturtle()
    screen.update()
    turtle.penup()
    for coordinate in reversed(paths):
        x=coordinate[0]+50
        y=coordinate[1]+50
        turtle.speed(10)
        turtle.showturtle()
        turtle.goto(x,y)
        turtle.pendown()

##################################################

if __name__ == "__main__":

    initialize_screen()  # Calling the predefined functions to setup the turtle screen.

    grid_array=draw_grid()  # Calling the predefined functions to generate a grid with randomized obstacles.

    graph=build_graph(grid_array)
    start_coord = (-300, 200)
    end_coord = (200, -300)
    visited_dist={}
    path=[]
    unvisited=list(graph.keys())
    unvisited_nodes={}
    # We'll use 999 to initialize the "infinity" value of the unvisited nodes   
    max_value = 999
    for node in unvisited:
        unvisited_nodes[node]=0
        visited_dist[node] = max_value
    # However, we initialize the starting node's value with 0   
    visited_dist[start_coord] = 0
    unvisited_nodes[end_coord]=0
    unvisited_nodes[start_coord]=0
    for n1 in (graph):
        z=len(graph[n1])
        if n1!=(-300,200) and z==1 : #it is a dead end
             del unvisited_nodes[n1]
    turtle.shape("square")
    turtle.showturtle()
    path1=dijkstra(graph, start_coord, end_coord,visited_dist,unvisited_nodes,path)
    #draw_path(paths)
    if (path1 == None):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(-400,-400)
        turtle.write("No path exists between the start and end points.",font=("Courier", 20, "bold"))
    else:
        turtle.pencolor("royal blue")
        turtle.pensize(5)
        turtle.pendown()
        draw_path(path1)

    turtle.mainloop()

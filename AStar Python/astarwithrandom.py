from random import randint

#Create Maze Filled With 0 Zeros
def createMaze(numrows,numcols):
    return [[0]*numcols for i in range(numrows)]

# Create The Borders In The Maze Randomly
def bordersinmaze(maze,numborders,numrows,numcols):
    numrows=numrows-1
    numcols=numcols-1
    bordersinc=0
    borderarr=[]
    while bordersinc< numborders:
        colindex=randint(0,numcols)
        rowindex=randint(0,numrows)
        if (maze[rowindex][colindex]==0 and ([rowindex,colindex] not in borderarr)):
             borderarr.append([rowindex,colindex])
             bordersinc=bordersinc+1
    return borderarr

# Create Node(s)
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# Astar Algorithm And Function
def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    rowz=int(input("Please enter number of rows: "))
    colz=int(input("Please enter number of columns: "))
    borders=int(input("Please enter number of borders: "))

#   Creating the Maze And Making the Borders
    maze=createMaze(rowz,colz)
    borderarrinmaze=bordersinmaze(maze,borders,rowz,colz)

#   For Assigning the Borders And Printing the Borders
    for borders in borderarrinmaze:
        # print(borders)
        # print(maze[borders[0]][borders[1]])
        maze[borders[0]][borders[1]]=1

#   Print Each Row In The Maze On A New Line
    for rowmaze in maze:
        print(rowmaze)

#   Input the start and end point
    startingpoint=input("Give The row and column with space indetation: ")
    endingpoint=input("Give The row and column with space indentation: ")

#   Split to get the first and second index
    startindex=startingpoint.split()
    endindex=endingpoint.split()

#   Assign Tuple by the indexes above
    start=(int(startindex[0]),int(startindex[1]))
    end=(int(endindex[0]),int(endindex[1]))

#   Solution
    path = astar(maze, start, end)
    print("Path Solution is {} \n".format(path))

    print("Maze Path, Follow 'A' \n")
    for item in path:
        maze[item[0]][item[1]]="A"
    for row in maze:
        print(row)


    # print("{} {} {}".format(type( rowz), type( colz),type (borders)))
    
    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # start = (0, 0)
    # end = (7, 6)

    # path = astar(maze, start, end)
    # print("Path Solution is {} \n".format(path))

    # print("Maze Path, Follow 'A' \n")
    # for item in path:
    #     maze[item[0]][item[1]]="A"
    # for row in maze:
    #     print(row)

  
    #print(bordersinmaze(createMaze(11,10),5,11,10))

if __name__ == '__main__':
    main()

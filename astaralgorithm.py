


class Node():

    def  __init__(self,parent=None,position=None):
        self.parent=parent
        self.position=position

        self.g=0
        self.h=0
        self.f=0




def astarAlgorithm(maze,start,end):

    start_node=Node(None,start)
    goal_node=Node(None,end)

    queuelistchangable=[]
    queuelistfixed=[]
    queuelistchangable.append(start_node)
    queuelistfixed.append(start_node)

    if len(queuelistchangable)==0:
        return False

    while len(queuelistchangable)>0:

        current_node=queuelistchangable.pop(0)

        if current_node.position==goal_node.position:
            path=[]
            path.append(current_node.position)
            while current_node.parent!=None:
                current_node=current_node.parent
                path.append(current_node.position)
            return path[::-1]

        currentnode_children=[]

        for nodeposition in [(1,0),(1,1),(1,-1),(-1,0),(-1,-1),(1,1),(0,1),(0,-1)]:

            nextnode=Node(current_node,(current_node.position[0]+nodeposition[0],current_node.position[1]+nodeposition[1]))

            if nextnode.position[0] > (len(maze) - 1) or nextnode.position[0] < 0 or nextnode.position[1] > (len(maze[len(maze) - 1]) - 1) or nextnode.position[1] < 0:
                continue

            if maze[nextnode.position[0]][nextnode.position[1]]!=0:
                continue

            nextnode.g=current_node.g+1
            nextnode.h=((goal_node.position[0]-nextnode.position[0])**2 + (goal_node.position[1]-nextnode.position[1])**2)
            nextnode.f=nextnode.g+nextnode.h
            currentnode_children.append(nextnode)

            #sort children nodes inline
            currentnode_children.sort(key=lambda childnode:childnode.f,reverse=False)

        current_node=currentnode_children.pop(0)
        queuelistfixed.append(current_node)
        queuelistchangable.append(current_node)


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
start=(0,0)
end=(7,6)
complete_path=astarAlgorithm(maze,start,end)
print(complete_path)
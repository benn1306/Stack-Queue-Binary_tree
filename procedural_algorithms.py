
class queue:
    def __init__(self,Q_len):
        self.Queue = [""for i in range(Q_len)]
        self.back = 0
        self.max_len = Q_len
    def enqueue(self,item):
        if self.back < self.max_len:
            self.Queue[self.back] = item
            self.back += 1
    def dequeue(self):
        self.Queue.pop(0)
        self.Queue.append("")

class stack:
    def __init__(self,max_height):
        self.Stack = [""for i in range(max_height)] ; self.top = 0 ; self.max_height = max_height
    def add_to_stack(self,item):
        if self.top < self.max_height: self.Stack[self.top] = item ; self.top += 1
    def remove_from_stack(self):
        self.Stack[self.top-1] = "" ; self.top -= 1

class binary_tree:
    def __init__(self,depth=int):self.Binary_tree = [[-1,"",-1]for i in range(depth)];self.free_space = 0
    def add_to_tree(self,item=int,node=0):
        if self.free_space == 0:self.Binary_tree[node][1] = item;self.free_space += 1
        if item < self.Binary_tree[node][1] and self.Binary_tree[node][0] == -1:self.Binary_tree[self.free_space][1] = item;self.Binary_tree[node][0] = self.free_space;self.free_space += 1
        elif item < self.Binary_tree[node][1]:node = self.Binary_tree[node][0];self.add_to_tree(item,node)
        elif item > self.Binary_tree[node][1] and self.Binary_tree[node][2] == -1:self.Binary_tree[self.free_space][1] = item;self.Binary_tree[node][2] = self.free_space;self.free_space += 1
        elif item > self.Binary_tree[node][1]:node = self.Binary_tree[node][2];self.add_to_tree(item,node)

    def breadth_first(self,node=0):
        unvisited_q = [self.Binary_tree[node]]
        while len(unvisited_q) != 0:
            node = unvisited_q[0]
            if node[0] != -1:
                unvisited_q.append(self.Binary_tree[node[0]])
            if node[2] != -1:
                unvisited_q.append(self.Binary_tree[node[2]])
                
            print(str(node[1]))
            unvisited_q.pop(0)

    def depth_first(self,node=0,visited = []):
        if (self.Binary_tree[node][0] == -1 and self.Binary_tree[node][2] == -1) or (self.Binary_tree[node][0] == -1 and self.Binary_tree[node][2] in visited) or (self.Binary_tree[node][2] == -1 and self.Binary_tree[node][0] in visited) or (self.Binary_tree[node][2] in visited and self.Binary_tree[node][0] in visited):
            print(self.Binary_tree[node][1])
            visited.append(node)
            return
        if self.Binary_tree[node][0] != -1:
            node = self.Binary_tree[node][0]
            self.depth_first(node,visited)
        if self.Binary_tree[node][2] != -1:
            node = self.Binary_tree[node][2]
            self.depth_first(node,visited)

b = binary_tree(8)
b.add_to_tree(7)
b.add_to_tree(1)
b.add_to_tree(3)
b.add_to_tree(10)
b.add_to_tree(6)
b.add_to_tree(8)
b.add_to_tree(11)
b.add_to_tree(2)
b.depth_first()

class Node:
    def __init__(self,name):
        self.right=None
        self.left=None
        self.name=name

class Main:
    def __init__(self):
        self.n=int(input())
        self.nodes=[Node(chr(65+i)) for i in range(self.n)]
        for _ in range(self.n):
            node_name,left_child,right_child=input().split()
            self.nodes[ord(node_name)-65].left = left_child
            self.nodes[ord(node_name)-65].right = right_child
        self.v=[0]*self.n
        self.r=[[],[],[]]

    def main(self):
        self.v=[0]*self.n
        self.preorder_traversal(0)
        self.v=[0]*self.n
        self.inorder_traversal(0)
        self.v=[0]*self.n
        self.postorder_traversal(0)
        [print(''.join(self.r[i]))for i in range(3)]

    def preorder_traversal(self,node_idx):
        if self.v[node_idx] == 0:
            self.v[node_idx]=1
            node=self.nodes[node_idx]
            self.r[0].append(node.name)
            if node.left != '.':
                self.preorder_traversal(ord(node.left)-65)
            if node.right != '.':
                self.preorder_traversal(ord(node.right)-65)

    def inorder_traversal(self,node_idx):
        if self.v[node_idx]==0:
            self.v[node_idx]=1
            node=self.nodes[node_idx]
            if node.left !='.':
                self.inorder_traversal(ord(node.left)-65)
            self.r[1].append(node.name)
            if node.right !='.':
                self.inorder_traversal(ord(node.right)-65)

    def postorder_traversal(self,node_idx):
        if self.v[node_idx]==0:
            self.v[node_idx]=1
            node=self.nodes[node_idx]
            if node.left !='.':
                self.postorder_traversal(ord(node.left)-65)
            if node.right != '.':
                self.postorder_traversal(ord(node.right)-65)
            self.r[2].append(node.name)
        
sol=Main()
sol.main()
class Node:
    def __init__(self, data, left, right):
        self.data = data         
        self.left = left         
        self.right = right       

def pre_trav(node):
    print(node.data, end='')
    if node.left !='.':
        pre_trav(tree[node.left])
    if node.right !='.':
        pre_trav(tree[node.right])

def in_trav(node):
    
    if node.left !='.':
        in_trav(tree[node.left])
    print(node.data, end='')
    if node.right !='.':
        in_trav(tree[node.right])
        
def pos_trav(node):
    
    if node.left !='.':
        pos_trav(tree[node.left])
    if node.right !='.':
        pos_trav(tree[node.right])
    print(node.data, end='')

N=int(input())
tree={}
for _ in range(N):
    data,left,right = input().split()
    tree[data]=Node(data,left,right)

pre_trav(tree['A'])
print('')
in_trav(tree['A'])
print('')
pos_trav(tree['A'])
print('')
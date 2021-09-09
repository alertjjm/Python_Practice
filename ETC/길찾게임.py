class Node:
    def __init__(self, node, idx):
        self.value = node[0]
        self.pos=node
        self.idx=idx
        self.left = None
        self.right = None
class BST:
    def __init__(self, root):
        self.root = root

    def pre_order_traversal(self):
        result=[]
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                result.append(root.idx)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)
        return result

    def post_order_traversal(self):
        result=[]
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                result.append(root.idx)
        _post_order_traversal(self.root)
        return result

    def insert(self, node, idx):
        self.current_node = self.root
        value=node[0]
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(node, idx)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(node, idx)
                    break
def solution(nodeinfo):
    answer = []
    nodes = []
    for n in range(len(nodeinfo)):
        node=nodeinfo[n]
        nodes.append([-node[1]*100000-(100000-node[0]),node[0],node[1], n+1])
    nodes.sort(key=lambda x: x[0])
    root=Node([nodes[0][1],nodes[0][2]], nodes[0][3])
    bst = BST(root)
    for i in range(1,len(nodes)):
        bst.insert([nodes[i][1],nodes[i][2]], nodes[i][3])
    answer.append(bst.pre_order_traversal())
    answer.append(bst.post_order_traversal())
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
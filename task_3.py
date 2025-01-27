class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root, key)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def balance(self, node, key):
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root = root.right
        return root.key
    
    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.key
    
    def sum_values(self, root):
        if root is None:
            return 0
        return root.key + self.sum_values(root.left) + self.sum_values(root.right)

# Тестуємо AVL дерево
avl = AVLTree()
root = None
values = [50, 30, 100, 70, 20, 40, 60, 80]
for v in values:
    root = avl.insert(root, v)

print("Найбільше значення у AVL дереві:", avl.find_max(root))
print("Найменше значення у AVL дереві:", avl.find_min(root))
print("Сума всіх значень у AVL дереві:", avl.sum_values(root))

# BST using Linked List
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
            return
        
        temp = self.root
        while True:
            if new_node.data < temp.data:  # Left subtree
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:  # Right subtree
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def search(self, key):
        temp = self.root
        while temp is not None:
            if key == temp.data:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

    def delete(self, rt, key):
        if rt is None:
            return rt

        # Traverse to find the node to be deleted
        if key < rt.data:
            rt.left = self.delete(rt.left, key)
        elif key > rt.data:
            rt.right = self.delete(rt.right, key)
        else:
            # Case 1 & 2: Node with only one child or no child
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left

            # Case 3: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            succ = self.get_successor(rt)
            rt.data = succ.data
            # Delete the inorder successor
            rt.right = self.delete(rt.right, succ.data)

        return rt

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.cnt += 1
        self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("Tree is empty")
            return

        # Initialized missing variables from original code
        arr = [rt]
        cnt = 0
        level = 0

        while cnt < len(arr):
            node_count = len(arr) - cnt
            print(f"\nLevel No {level}:", end=" ")
            for _ in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end=" ")
                if temp.left is not None:
                    arr.append(temp.left)
                if temp.right is not None:
                    arr.append(temp.right)
            level += 1
        print()  # Newline at the end


# --- Driver Code ---
b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(1))
b1.insert(Node(65))
b1.insert(Node(300))

print("Inorder Traversal:")
b1.cnt = 0  # Reset counter before traversal
b1.inorder(b1.root)
print("\nNo of nodes:", b1.cnt)

print("\nLevel Order Traversal:", end="")
b1.level_order(b1.root)

# Testing Search and Delete
print("\nSearch 65:", b1.search(65))
print("Deleting 100 (root)...")
b1.root = b1.delete(b1.root, 100)

print("Inorder after deletion:")
b1.cnt = 0
b1.inorder(b1.root)
print("\nNo of nodes:", b1.cnt)
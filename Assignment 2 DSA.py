import datetime

class Node:
    def __init__(self, match_id, team1_name, team2_name, match_date, winner, location):
        self.match_id = match_id
        self.team1 = {'name': team1_name, 'cricketers': []}
        self.team2 = {'name': team2_name, 'cricketers': []}
        self.match_date = match_date
        self.winner = winner
        self.location = location
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def add_match(self, match_id, team1_name, team2_name, match_date, winner, location):
        self.root = self._add_match(self.root, match_id, team1_name, team2_name, match_date, winner, location)

    def _add_match(self, node, match_id, team1_name, team2_name, match_date, winner, location):
        if node is None:
            return Node(match_id, team1_name, team2_name, match_date, winner, location)
        elif match_id < node.match_id:
            node.left = self._add_match(node.left, match_id, team1_name, team2_name, match_date, winner, location)
        else:
            node.right = self._add_match(node.right, match_id, team1_name, team2_name, match_date, winner, location)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and match_id < node.left.match_id:
            return self._right_rotate(node)
        if balance < -1 and match_id > node.right.match_id:
            return self._left_rotate(node)
        if balance > 1 and match_id > node.left.match_id:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and match_id < node.right.match_id:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(f"Match ID: {node.match_id}")
            print(f"Team 1: {node.team1['name']}")
            print(f"Team 2: {node.team2['name']}")
            print(f"Match Date: {node.match_date}")
            print(f"Winner: {node.winner}")
            print(f"Location: {node.location}")
            print("------------------------")
            self._inorder_traversal(node.right)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            self._save_to_file(self.root, f)

    def _save_to_file(self, node, f):
        if node:
            self._save_to_file(node.left, f)
            f.write(f"{node.match_id},{node.team1['name']},{node.team2['name']},{node.match_date},{node.winner},{node.location}\n")
            self._save_to_file(node.right, f)

tree = AVLTree()
tree.add_match('M1', 'Team A', 'Team B', '2022-01-01', 'Team A', 'Location 1')
tree.add_match('M2', 'Team C', 'Team D', '2022-01-15', 'Team C', 'Location 2')
tree.inorder_traversal()
tree.save_to_file('matches.txt')

def load_from_file(filename):
    tree = AVLTree()
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                match_id, team1_name, team2_name, match_date, winner, location = line.strip().split(',')
                tree.add_match(match_id, team1_name, team2_name, match_date, winner, location)
        return tree
    except FileNotFoundError:
        print("File not found.")

loaded_tree = load_from_file('matches.txt')
loaded_tree.inorder_traversal()

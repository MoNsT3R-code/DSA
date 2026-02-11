# Task 1

def get_priority(operator):

    if operator == '^':

        return 3

    elif operator in ('*', '/', '%'):

        return 2

    elif operator in ('+', '-'):

        return 1

    else:

        return 0


def convert_to_postfix(expression):

    stack = []
    result = []

    for ch in expression:

        if ch.isdigit():

            result.append(ch)

        elif ch == '(':

            stack.append(ch)

        elif ch == ')':

            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        elif ch in '+-*/%^':

            while stack and get_priority(stack[-1]) >= get_priority(ch):
                result.append(stack.pop())
            stack.append(ch)

    while stack:

        result.append(stack.pop())

    return result

def solve_postfix(postfix):

    numbers = []

    for item in postfix:

        if item.isdigit():
            numbers.append(int(item))

        else:

            b = numbers.pop()
            a = numbers.pop()

            if item == '+':

                numbers.append(a + b)

            elif item == '-':

                numbers.append(a - b)

            elif item == '*':

                numbers.append(a * b)

            elif item == '/':

                numbers.append(a / b)

            elif item == '%':

                numbers.append(a % b)

            elif item == '^':

                numbers.append(a ** b)

    return numbers[0]


def start_calculator():

    while True:

        user_input = input("Enter expression to evaluate or a clr to quit:\n")

        if user_input.strip() == 'clr':

            print("Goodbye!")
            break

        clean_input = user_input.replace(' ', '').replace('=', '')
        postfix = convert_to_postfix(clean_input)
        result = solve_postfix(postfix)

        print("Postfix Expression:", ' '.join(postfix))
        print("Result =", result)

start_calculator()

# Task 2

class Queue:

    def __init__(self, max_size):

        self.items = []
        self.max_size = max_size

    def enqueue(self, char):

        if not self.is_full():

            self.items.append(char)

        else:

            print("Queue is full. Cannot add more items.")


    def dequeue(self):

        if not self.is_empty():

            return self.items.pop(0)

        else:

            print("Queue is empty.")

            return None


    def front(self):

        if not self.is_empty():

            return self.items[0]

        else:

            print("Queue is empty.")
            return None

    def is_empty(self):

        return len(self.items) == 0

    def is_full(self):

        return len(self.items) == self.max_size

    def get_size(self):

        return len(self.items)

    def print_queue(self):

        print("Queue:", self.items)

class Stack:

    def __init__(self):

        self.items = []

    def push(self, item):

        self.items.append(item)

    def pop(self):

        if not self.is_empty():

            return self.items.pop()

        else:

            print("Stack is empty.")
            return None

    def is_empty(self):

        return len(self.items) == 0

def reverse_queue(queue):

    stack = Stack()

    while not queue.is_empty():

        stack.push(queue.dequeue())

    while not stack.is_empty():

        queue.enqueue(stack.pop())

    print("Queue after reversing:")
    queue.print_queue()

def menu():

    max_size = int(input("Enter maximum size of the queue: "))
    queue = Queue(max_size)

    while True:

        print("\n--- Queue Menu ---")
        print("1. Enqueue (Add item)")
        print("2. Dequeue (Remove item)")
        print("3. Show Front item")
        print("4. Check if Queue is Empty")
        print("5. Check if Queue is Full")
        print("6. Get Queue Size")
        print("7. Print Queue")
        print("8. Reverse Queue")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':

            char = input("Enter a character to add: ")
            queue.enqueue(char)

        elif choice == '2':

            removed = queue.dequeue()
            if removed is not None:

                print("Removed:", removed)

        elif choice == '3':

            front = queue.front()
            if front is not None:

                print("Front item:", front)

        elif choice == '4':

            print("Queue is empty?", queue.is_empty())

        elif choice == '5':

            print("Queue is full?", queue.is_full())

        elif choice == '6':

            print("Current size:", queue.get_size())

        elif choice == '7':

            queue.print_queue()

        elif choice == '8':

            reverse_queue(queue)

        elif choice == '9':

            print("Exiting program.")

            break

        else:

            print("Invalid choice. Please try again.")

menu()

# Task 3

class Deque:

    def __init__(self):

        self.items = []


    def enqueue_right(self, item):

        self.items.append(item)


    def enqueue_left(self, item):

        self.items.insert(0, item)


    def dequeue_right(self):

        if not self.is_empty():

            return self.items.pop()

        else:

            print("Deque is empty.")
            return None

    def dequeue_left(self):

        if not self.is_empty():

            return self.items.pop(0)

        else:

            print("Deque is empty.")

            return None

    def is_empty(self):

        return len(self.items) == 0

    def display(self):

        print("Deque:", self.items)

def input_restricted_menu():

    dq = Deque()

    while True:

        print("\n--- Input Restricted Deque ---")
        print("1. Enqueue (Add item at right)")
        print("2. Dequeue Right (Remove from rear)")
        print("3. Dequeue Left (Remove from front)")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            item = input("Enter item to enqueue: ")
            dq.enqueue_right(item)

        elif choice == '2':

            removed = dq.dequeue_right()

            if removed is not None:

                print("Removed from right:", removed)

        elif choice == '3':

            removed = dq.dequeue_left()

            if removed is not None:

                print("Removed from left:", removed)

        elif choice == '4':

            dq.display()

        elif choice == '5':

            print("Exiting Input Restricted Deque.")

            break

        else:

            print("Invalid choice. Try again.")



def output_restricted_menu():

    dq = Deque()

    while True:

        print("\n--- Output Restricted Deque ---")

        print("1. Enqueue Right (Add at end)")

        print("2. Enqueue Left (Add at front)")

        print("3. Dequeue (Remove from front only)")

        print("4. Display")

        print("5. Exit")



        choice = input("Enter your choice: ")



        if choice == '1':

            item = input("Enter item to enqueue at right: ")

            dq.enqueue_right(item)

        elif choice == '2':

            item = input("Enter item to enqueue at left: ")

            dq.enqueue_left(item)

        elif choice == '3':

            removed = dq.dequeue_left()

            if removed is not None:

                print("Removed from left:", removed)

        elif choice == '4':

            dq.display()

        elif choice == '5':

            print("Exiting Output Restricted Deque.")

            break

        else:

            print("Invalid choice. Try again.")



def main_menu():

    while True:

        print("\nChoose Deque Type:")

        print("1. Input Restricted Deque")

        print("2. Output Restricted Deque")

        print("3. Exit")


        choice = input("Enter your choice: ")



        if choice == '1':

            input_restricted_menu()

        elif choice == '2':

            output_restricted_menu()

        elif choice == '3':

            print("Exiting program.")

            break

        else:

            print("Invalid choice. Try again.")



main_menu()


# Task 4


class CricketerNode:

    def __init__(self, name):

        self.name = name
        self.next = self.prev = self

class CricketerList:

    def __init__(self):

        self.head = None

    def add_cricketer(self, name):

        if self.find_cricketer(name):

            print(f"Cricketer {name} already exists.")
            return

        new_node = CricketerNode(name)

        if not self.head:

            self.head = new_node

        else:

            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head

            self.head.prev = new_node

        print(f"Added cricketer {name}")

    def delete_cricketer(self, name):

        node = self.find_cricketer(name)

        if not node:

            print(f"Cricketer {name} not found.")
            return False

        if node.next == node:

            self.head = None

        else:

            node.prev.next = node.next
            node.next.prev = node.prev

            if self.head == node:

                self.head = node.next

        print(f"Deleted cricketer {name}")
        return True

    def find_cricketer(self, name):

        if not self.head:

            return None

        current = self.head

        while True:

            if current.name == name:

                return current

            current = current.next
            if current == self.head:

                break

        return None

    def print_cricketers(self):

        if not self.head:

            print("No cricketers")
            return

        current = self.head
        names = []

        while True:

            names.append(current.name)
            current = current.next

            if current == self.head:

                break

        print(", ".join(names))

class MatchNode:

    def __init__(self, match_id, team1_name, team2_name, date, winner, location):

        self.match_id = match_id
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.date = date
        self.winner = winner
        self.location = location
        self.team1_cricketers = CricketerList()
        self.team2_cricketers = CricketerList()
        self.next = self.prev = self

class MatchList:

    def __init__(self):

        self.head = None

    def _match_id_key(self, match_id):

        prefix = ''.join(filter(str.isalpha, match_id))
        nums = ''.join(filter(lambda x: x.isdigit() or x == '-', match_id))
        parts = nums.split('-')

        return (prefix, int(parts[0]), int(parts[1]))

    def add_match(self, match_id, team1_name, team2_name, date, winner, location):

        if self.find_match(match_id):

            print(f"Match {match_id} already exists.")
            return

        new_node = MatchNode(match_id, team1_name, team2_name, date, winner, location)

        if not self.head:

            self.head = new_node
            print(f"Added match {match_id} as the first match.")
            return

        current = self.head
        new_key = self._match_id_key(match_id)

        while True:

            current_key = self._match_id_key(current.match_id)

            if new_key < current_key:
                prev_node = current.prev

                prev_node.next = new_node
                new_node.prev = prev_node

                new_node.next = current
                current.prev = new_node

                if current == self.head:

                    self.head = new_node

                print(f"Inserted match {match_id} before {current.match_id}")
                return

            current = current.next

            if current == self.head:
                break

        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node
        print(f"Added match {match_id} at the end.")

    def delete_match(self, match_id):

        node = self.find_match(match_id)

        if not node:

            print(f"Match {match_id} not found.")
            return False

        if node.next == node:  

            self.head = None

        else:

            node.prev.next = node.next
            node.next.prev = node.prev

            if self.head == node:

                self.head = node.next

        print(f"Deleted match {match_id}")
        return True

    def find_match(self, match_id):

        if not self.head:

            return None

        current = self.head
        while True:

            if current.match_id == match_id:

                return current

            current = current.next

            if current == self.head:

                break

        return None

    def print_matches(self):

        if not self.head:

            print("No matches available.")
            return
    
        current = self.head
    
        while True:
    
            print(f"Match ID: {current.match_id}")
            print(f" Date: {current.date}")
            print(f" Location: {current.location}")
            print(f" Winner: {current.winner}")
            print(f" Team 1: {current.team1_name} - Players: ", end='')
            current.team1_cricketers.print_cricketers()
            print(f" Team 2: {current.team2_name} - Players: ", end='')
            current.team2_cricketers.print_cricketers()
            print("-" * 30)
            current = current.next
            if current == self.head:
                break

    def add_cricketer_to_match(self, match_id, team_number, cricketer_name):
    
        match = self.find_match(match_id)
    
        if not match:
    
            print(f"Match {match_id} not found.")
            return
    
        if team_number == 1:
    
            match.team1_cricketers.add_cricketer(cricketer_name)
    
        elif team_number == 2:
    
            match.team2_cricketers.add_cricketer(cricketer_name)
    
        else:
    
            print("Invalid team number. Use 1 or 2.")

    def delete_cricketer_from_match(self, match_id, team_number, cricketer_name):
    
        match = self.find_match(match_id)
        if not match:
    
            print(f"Match {match_id} not found.")
            return
    
        if team_number == 1:
    
            match.team1_cricketers.delete_cricketer(cricketer_name)
    
        elif team_number == 2:
    
            match.team2_cricketers.delete_cricketer(cricketer_name)
    
        else:
    
            print("Invalid team number. Use 1 or 2.")

    def find_matches_by_cricketer(self, cricketer_name):
    
        result_list = MatchList()
    
        if not self.head:
    
            return result_list
    
        current = self.head
    
        while True:
    
            team1_found = current.team1_cricketers.find_cricketer(cricketer_name)
            team2_found = current.team2_cricketers.find_cricketer(cricketer_name)
    
            if team1_found or team2_found:
                
                result_list.add_match(
                    current.match_id,
                    current.team1_name,
                    current.team2_name,
                    current.date,
                    current.winner,
                    current.location
                )
           
            current = current.next
           
            if current == self.head:
           
                break
     
        return result_list



db = MatchList()
db.add_match("PSL1-1", "Team1", "Team2", "2/2/2023", "Team2", "Pakistan")
db.add_match("PSL1-4", "TeamA", "TeamB", "3/3/2023", "TeamA", "UAE")
db.add_match("PSL1-2", "TeamX", "TeamY", "4/4/2023", "TeamY", "India")
db.add_cricketer_to_match("PSL1-1", 1, "Cricketer1")
db.add_cricketer_to_match("PSL1-1", 1, "Cricketer2")
db.add_cricketer_to_match("PSL1-1", 1, "Cricketer3")
db.add_cricketer_to_match("PSL1-1", 2, "Rizwan")
db.add_cricketer_to_match("PSL1-1", 2, "Babar")
db.add_cricketer_to_match("PSL1-1", 2, "Fakhar")

print("\nAll matches:")

db.print_matches()

print("\nMatches played by 'Babar':")

matches_with_babar = db.find_matches_by_cricketer("Babar")
matches_with_babar.print_matches()

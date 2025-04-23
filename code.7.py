print("\nTask 7: Stack implementation")
stack = []

def push(val):
    stack.append(val)
    print(val, "pushed to stack.")

def pop():
    if stack:
        print("Popped:", stack.pop())
    else:
        print("Stack is empty.")

def display_stack():
    print("Stack:", stack)

while True:
    print("\n1.Push 2.Pop 3.Display 4.Exit Stack")
    ch = input("Enter choice: ")
    if ch == '1':
        val = input("Enter value to push: ")
        push(val)
    elif ch == '2':
        pop()
    elif ch == '3':
        display_stack()
    elif ch == '4':
        break
    else:
        print("Invalid choice.")

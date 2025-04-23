print("\nTask 8: Queue implementation")
queue = []

def enqueue(val):
    queue.append(val)
    print(val, "added to queue.")

def dequeue():
    if queue:
        print("Removed:", queue.pop(0))
    else:
        print("Queue is empty.")

def display_queue():
    print("Queue:", queue)

while True:
    print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit Queue")
    ch = input("Enter choice: ")
    if ch == '1':
        val = input("Enter value to enqueue: ")
        enqueue(val)
    elif ch == '2':
        dequeue()
    elif ch == '3':
        display_queue()
    elif ch == '4':
        break
    else:
        print("Invalid choice.")

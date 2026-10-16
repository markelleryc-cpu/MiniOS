

total_memory = 1024
used_memory = 0  

def show_memory():
    free_memory = total_memory - used_memory
    print("\nMemory Status")
    print("-" * 24)
    print(f"Total Memory: {total_memory:>4} MB")
    print(f"Used Memory:  {used_memory:>4} MB")
    print(f"Free Memory:  {free_memory:>4} MB\n")

def allocate_memory(amount_str):
    global used_memory
    try:
        amount = int(amount_str)
        free_memory = total_memory - used_memory
        
        if amount <= 0:
            print("\nError: Amount must be greater than 0.\n")
        elif amount > free_memory:
            print(f"\nError: Not enough free memory. Only {free_memory} MB available.\n")
        else:
            used_memory += amount
            print(f"\n{amount} MB allocated.\n")
    except ValueError:
        print("\nError: Please enter a valid number.\n")

def free_allocated_memory(amount_str):
    global used_memory
    try:
        amount = int(amount_str)
        
        if amount <= 0:
            print("\nError: Amount must be greater than 0.\n")
        elif amount > used_memory:
            print(f"\nError: Cannot release more memory than is currently used ({used_memory} MB).\n")
        else:
            used_memory -= amount
            print(f"\n{amount} MB released.\n")
    except ValueError:
        print("\nError: Please enter a valid number.\n")
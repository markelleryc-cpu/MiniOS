


directories = []


files = {}

def list_directory():
    print("\nDirectory Listing:")
    if not directories and not files:
        print("  (Empty)")
    else:
        for d in directories:
            print(f"  [DIR]  {d}")
        for f in files:
            print(f"  [FILE] {f}")
    print()

def make_directory(dirname):
    if dirname in directories:
        print(f"\nError: Directory '{dirname}' already exists.\n")
    else:
        directories.append(dirname)
        print("\nDirectory created.\n")

def create_file(filename):
    if filename in files:
        print(f"\nError: File '{filename}' already exists.\n")
    else:
        
        files[filename] = "Operating Systems Final Project"
        print("\nFile created.\n")

def read_file(filename):
    if filename in files:
        print(f"\n{files[filename]}\n")
    else:
        print("\nError: File does not exist.\n")

def delete_file(filename):
    if filename in files:
        del files[filename]
        print("\nFile deleted.\n")
    else:
        print("\nError: File does not exist.\n")
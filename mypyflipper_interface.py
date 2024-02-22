import time
from pyflipper import PyFlipper

# Initialize connection to Flipper Zero
# Adjust the 'com' parameter as per your connection
flipper = PyFlipper(com="/dev/ttyACM0")  # Change this to match your device's port

def input_script_content():
    """Helper function to input multiline text from the user."""
    print("Enter the content (end with Ctrl+D on Linux/macOS or Ctrl+Z on Windows, then Enter):")
    content_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content_lines.append(line)
    return '\n'.join(content_lines)

def add_file(path, content):
    """Generic function to write any content to a file at a specified path."""
    flipper.storage.write.file(path, content)
    print(f"File added at: {path}")

def remove_file(path):
    """Generic function to remove a file at a specified path."""
    flipper.storage.remove(file=path)
    print(f"File removed from: {path}")

def rename_file(old_path, new_path):
    """Generic function to rename a file."""
    flipper.storage.rename(file=old_path, new_file=new_path)
    print(f"File renamed from {old_path} to {new_path}")

def manage_badusb_scripts():
    """Manage BadUSB scripts: add, remove, edit, rename."""
    print("1. Add a BadUSB script")
    print("2. Remove a BadUSB script")
    print("3. Edit a BadUSB script")
    print("4. Rename a BadUSB script")
    choice = input("Choose an action: ")

    script_name = input("Enter the script name (e.g., 'hello_world.txt'): ")
    script_path = f"/ext/badusb/{script_name}"

    if choice == '1':  # Add
        content = input_script_content()
        add_file(script_path, content)
    elif choice == '2':  # Remove
        remove_file(script_path)
    elif choice == '3':  # Edit
        new_content = input_script_content()
        add_file(script_path, new_content)  # Overwrite existing content
    elif choice == '4':  # Rename
        new_name = input("Enter the new script name: ")
        new_path = f"/ext/badusb/{new_name}"
        rename_file(script_path, new_path)
    else:
        print("Invalid choice.")

def add_generic_text_file():
    """Add a generic text file to the Flipper Zero."""
    file_name = input("Enter the file name (include path, e.g., '/ext/foo.txt'): ")
    content = input_script_content()
    add_file(file_name, content)

def main_menu():
    """Main menu for the script."""
    while True:
        print("\nFlipper Zero Management Script")
        print("1. Manage BadUSB scripts")
        print("2. Add a generic text file")
        print("3. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            manage_badusb_scripts()
        elif choice == '2':
            add_generic_text_file()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()

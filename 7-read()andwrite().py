# Writing to a file
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

# Reading from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"Error reading from {filename}: {e}")
        return None

# Example usage to write to a file
filename = 'ABC.txt'
content_to_write = "Hello, this is some content written to a file using Python!"
write_to_file(filename, content_to_write)

# Example usage to read from a file
content_read = read_from_file(filename)
if content_read:
    print(f"Content of {filename}:")
    print(content_read)

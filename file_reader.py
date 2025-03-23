def read_file(filename):
    """Reads a text file and prints its content."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    print(read_file("sample.txt"))  # Make sure to add a 'sample.txt' file in the repository!

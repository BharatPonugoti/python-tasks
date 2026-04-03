#Word Count Program#
try:
    with open("article.txt", "r") as file:
        content = file.read()
        
        # Count characters
        char_count = len(content)
        
        # Count words
        words = content.split()
        word_count = len(words)
        
        # Count lines
        lines = content.split("\n")
        line_count = len(lines)

        # Display results
        print("File Analysis:\n")
        print("Number of characters:", char_count)
        print("Number of words:", word_count)
        print("Number of lines:", line_count)

except FileNotFoundError:
    print("Error: article.txt file not found.")
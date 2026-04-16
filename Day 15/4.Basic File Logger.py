# Basic File Logger
try:
    with open("log.txt", "a") as f:
        while True:
            entry = input("Enter log (type 'exit' to stop): ")
            
            if entry.lower() == "exit":
                break
            
            f.write(entry + "\n")

    print("Logs saved successfully.")

except IOError:
    print("Error writing to file.")
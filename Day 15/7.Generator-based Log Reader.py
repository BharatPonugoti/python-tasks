# Generator-based Log Reader
# Generator function
def read_logs(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line.strip()

# Count errors
error_count = {}

for line in read_logs("log.txt"):
    if "ERROR" in line:
        error_count[line] = error_count.get(line, 0) + 1

print("Error Counts:")
for err, count in error_count.items():
    print(err, ":", count)
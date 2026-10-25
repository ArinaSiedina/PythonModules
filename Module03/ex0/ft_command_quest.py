import sys

print("=== Command Quest ===")
args = sys.argv
print(f"Program name: {args[0]}")
if len(args) == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(args) - 1}")
    for i in range(len(args)):
        print(f"Argument {i + 1}: {args[i]}")
print(f"Total arguments: {len(args)}")

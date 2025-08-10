import os

test_path = r"G:\My Drive\Zapier Watch\test.txt"
try:
    with open(test_path, "w") as f:
        f.write("test")
    print("Write successful")
except Exception as e:
    print(f"Error writing file: {e}")

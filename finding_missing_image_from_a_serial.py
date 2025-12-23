import os
import re

# 🔹 CHANGE THIS PATH to your image folder path
FOLDER_PATH = r"C:\Users\WIN 10\Downloads\Larynx-20251222T204034Z-1-001\Larynx\Main"

START = 1
END = 7695

found_numbers = set()

pattern = re.compile(r"(\d+)\.jpg$", re.IGNORECASE)

for filename in os.listdir(FOLDER_PATH):
    match = pattern.search(filename)
    if match:
        found_numbers.add(int(match.group(1)))

expected_numbers = set(range(START, END + 1))
missing_numbers = sorted(expected_numbers - found_numbers)

print(f"Total images expected : {END}")
print(f"Total images found    : {len(found_numbers)}")
print(f"Total missing images  : {len(missing_numbers)}\n")

print("Missing image numbers:\n")

prev = None
for num in missing_numbers:
    if prev is not None and num != prev + 1:
        print()   # 🔹 blank line where serial breaks
    print(num)
    prev = num

# save to file with same formatting
output_file = "missing_images.txt"
with open(output_file, "w") as f:
    prev = None
    for num in missing_numbers:
        if prev is not None and num != prev + 1:
            f.write("\n")
        f.write(f"{num}\n")
        prev = num

print(f"\n✅ Missing image list saved to '{output_file}'")

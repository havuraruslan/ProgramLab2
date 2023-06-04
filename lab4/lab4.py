import os

while True:
    file_path = input("Введіть шлях до файлу: ")

    if not os.path.exists(file_path):
        print("Такий файл не існує")
        continue

    with open(file_path, "r") as f:
        lines = f.readlines()

    total_lines = len(lines)
    empty_lines = lines.count("\n")
    lines_with_z = sum("z" in line for line in lines)
    z_count = sum(line.count("z") for line in lines)
    lines_with_and = sum("and" in line for line in lines)

    print(f"File: {file_path}")
    print(f" total lines: {total_lines}")
    print(f" empty lines: {empty_lines}")
    print(f" lines with \"z\": {lines_with_z}")
    print(f" \"z\" count: {z_count}")
    print(f" lines with \"and\": {lines_with_and}")

    choice = input("Проаналізувати ще один файл? (y/n): ")
    if choice.lower() != "y":
        break
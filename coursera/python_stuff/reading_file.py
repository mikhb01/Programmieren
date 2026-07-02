example1 = "coursera/example1.txt"
file1 = open(example1, "r")

# print(file1.mode)

# FileContent = file1.read()
# print(FileContent)
# print(type(FileContent))
# file1.close()

# with open(example1, "r") as file1:
#     FileContent = file1.read()
#     print(FileContent)
# file1.close()

# with open(example1, "r") as file1:
#     print(file1.read(4))
#     print(file1.read(4))
#     print(file1.read(7))
#     print(file1.read(15))

# with open(example1, "r") as file1:
#     print("First line: " + file1.readline())

# with open(example1, "r") as file1:
#     i = 0
#     for line in file1:
#         print("Iteration", str(i), ":", line)
#         i = i+1

with open(example1, "r") as file1:
    FileasList = file1.readlines()

print(FileasList[0])
print(FileasList[1])
print(FileasList[2])
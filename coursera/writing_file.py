example2 = "coursera/example2.txt"

# with open(example2, "w") as writefile:
#     writefile.write("This is line A\n")
#     writefile.write("This is lIne B\n")

# with open(example2, "r") as readfile:
#     print(readfile.read())

# Lines = ["This is line D\n", "This is line E\n", "This is line F\n"]

# with open(example2, "a") as writefile:
#     for line in Lines:
#         print(line)
#         writefile.write(line)

# with open(example2, "r") as readfile:
#     print(readfile.read())

# with open("coursera/example2-1.txt", "a+") as testwritefile:
#     testwritefile.write("This is line E\n")
#     print(testwritefile.read())

# with open("coursera/example2-1.txt", "a+") as testwritefile:
#     print("Initial Location: {}".format(testwritefile.tell()))

#     data = testwritefile.read()
#     if(not data):
#         print("Read nothing")
#     else:
#         print(testwritefile.read())
    
#     testwritefile.seek(0,0)

#     print("\nNew location: {}".format(testwritefile.tell()))
#     data = testwritefile.read()
#     if(not data):
#         print("Read nothing")
#     else:
#         print(data)

#     print("Location after read: {}".format(testwritefile.tell()))

# with open('coursera/Example2.txt', 'r+') as testwritefile:
#     testwritefile.seek(0,0) #write at beginning of file
#     testwritefile.write("Line 1" + "\n")
#     testwritefile.write("Line 2" + "\n")
#     testwritefile.write("Line 3" + "\n")
#     testwritefile.write("Line 4" + "\n")
#     testwritefile.write("finished\n")
#     testwritefile.seek(0,0)
#     print(testwritefile.read())

# with open('coursera/Example2.txt', 'r+') as testwritefile:
#     testwritefile.seek(0,0) #write at beginning of file
#     testwritefile.write("Line 1" + "\n")
#     testwritefile.write("Line 2" + "\n")
#     testwritefile.write("Line 3" + "\n")
#     testwritefile.write("Line 4" + "\n")
#     testwritefile.write("finished\n")
#     #Uncomment the line below
#     testwritefile.truncate()
#     testwritefile.seek(0,0)
#     print(testwritefile.read())

with open("coursera/example2.txt", "r") as readfile:
    with open("coursera/example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

with open("coursera/example2.txt", "r") as testreadfile:
    print(testreadfile.read())            
print("hello world")
print("hello")
number = list(range(5,30,5))
print(number[2])
words = ["hello","world","spame","eggs"]
# counter = 0
# max_index = len(words) - 1
# while counter <= max_index:
#     word = words[counter]
#     print(word + "!")
# #     counter = counter + 1
# for word in words:
#     print(word + "!")
# for i in range(10):
#     print("hello")
# print("*", end="---")
# print("*")
# for i in range(10):
#     test = "*" * i
#     print(test)
row = 1
while row <= 9:
    col = 1
    while col <= row:
        #num = col * row
        print("%d * %d = %d " % (col,row,col * row), end="\t")
        col += 1
    print("")
    row += 1

class Test2:
    def divition(first, second):
        return first // second


with open("text files/documentary", mode="r") as s_files:
    words = ""
    for line in s_files.readlines():
        words += line
    print(words)
print("completed")
pass




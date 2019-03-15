wordArr = []
userInput = ""
i = 0 

while (userInput != "x"):
    print("Enter word", end=" ")
    print(i, end=" ")
    userInput = input(": ")
    i += 1
    if ( i > 1):
        if userInput in wordArr:
            print("",userInput," alreay exists in the array.")
        else:
            wordArr.append(userInput)
        

wordArr.remove('x')

print("Here is the list of unique words: ")
for elem in wordArr:
    print(elem)

def solution(s):
    theStack = []

    # place the base string that will eventually be returned
    theStack.append([""])

    repeatNum = ""

    for char in s:
        if char.isdigit():
            repeatNum += char
        elif char == "[":
            print(repeatNum)
            theStack.append(["", int(repeatNum)])
            repeatNum = ""
            print(theStack)
        elif char == "]":
            print(theStack)
            string, repeat = theStack.pop()
            theStack[-1][0] += string * repeat
            print(theStack)
        else:
            theStack[-1][0] += char
            print(char, theStack)

    return theStack[-1][0]

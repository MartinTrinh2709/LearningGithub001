#implement a function that takes a string and returns a list of all the substrings that contain only number.
#The function should also remove any leading or trailing white space from the substrings.
def find_numbers(string):
    result = []
    temp = ''
    for i in string:
        if i.isdigit():
            temp += i
        elif temp:
            result.append(temp)
            temp = ''
    if temp:
        result.append(temp)
    return result
print(find_numbers("abc123def456ghi789jkl")) #['123', '456', '789']
print(find_numbers("abc123def456ghi789jkl123")) #['123', '456', '789', '123']
print(find_numbers("abc123def456ghi789jkl123abc")) #['123', '456', '789', '123']

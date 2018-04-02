def camel_case(string):
    array = string.split()
    finalStr = ''
    for word in array:
        finalStr += word.capitalize()
    return finalStr
def Reverse_1(string):
    print(string[::-1])

def Reverse_2(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    print(reversed_string)


string = input("Enter String : ")
Reverse_1(string)
Reverse_2(string)
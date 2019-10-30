#Solution to reversing a string in Python

#By Rafael Perez

x_str = "Hello Everyone"

def reverse_str(tar):
    new_str = ""
    for x in range(len(tar)):
        new_str+=(tar[-1 + (-1* x)])
    print(new_str)

reverse_str(x_str)
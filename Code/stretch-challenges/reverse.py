#string reversal using a for loop
def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str

string = "red fish blue fish one fish two fish"

if __name__ == "__main__":

    print(reverse(string))
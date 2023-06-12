def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False


loop = True
while loop:
    strInput = input(
        "Enter the string to test for palindrome or enter 'exit' to close: "
    )
    strInput = strInput.lower()

    if strInput == "exit":
        run = False
        break

    newStrInput = ""
    for x in strInput:
        if x.isalnum():
            newStrInput += x

    print("Palindrome Test:" + str(isPalindrome(strInput)))

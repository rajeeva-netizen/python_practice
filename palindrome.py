def checkPalindrome(a):
    temp = a
    rev = 0
    while(a>0):
        dig = a%10
        rev = rev*10+dig
        a = a//10
    if(temp == rev):
        print("number is palindrome")
    else:
        print("number is not palindrome")



checkPalindrome(1341)
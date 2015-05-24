# Problem 1: Write a method that determines whether a string is a palindrome or not 

def isPalindrome (str) :
    strArr = str.split()
    strlen = len(strArr)
    for i in range(strlen/2) :
        if strArr[i] != strArr[strlen-i-1] :
            return False
    return True
    
# Problem 2: Write a method that returns the *longest* palindrome inside a block of text

def longestPalindrome (str) :
    longest = ""
    for i in range(len(str)) :
        if str[i] == str[i+1] or str[i-1] == str[i+1]:
            tempPalindrome = expandCenter(str, i)
            if len(tempPalindrome) > len(longest) :
                longest = tempPalindrome
    return longest

def expandCenter (str, center) :
    # returns longers string from center
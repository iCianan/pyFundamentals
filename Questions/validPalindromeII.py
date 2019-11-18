def validPalindrome(string):
    i = 0
    j = len(string) -1
    while i < j:
        if string[i] != string[j]:
            return isPalindrome(string, i+1, j) or isPalindrome(string, i, j-1)
        i += 1
        j -= 1
    return True

def isPalindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True



def main():
    word = 'aabba'
    print(validPalindrome(word))


if __name__ == "__main__":
    main()


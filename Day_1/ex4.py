def palindrome(word):
    return word == word[::-1]
        
if palindrome("level"):
    print("là 1 chuỗi palindrome")
else:
    print("không phải là 1 chuỗi palindrome")
# A palindromic string is one which reads the same when it is reversed.
# Checks if string is palindromic


# s[~i] is s[-(i + 1)], which is the the opposite elem as s[i]
# all(): returns true if all is true
def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


# Longer version, but same as above
def is_palindromic_extended(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    
    return True

s = "lol"
# s = "nope"
# s = "holloh"

print(is_palindromic_extended(s))
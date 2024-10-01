from collections import deque

def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalpha())

    d = deque()
    for char in string:
        d.append(char)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    return True

print(is_palindrome("hottor"))
print(is_palindrome("ololo"))

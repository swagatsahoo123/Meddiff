def isPalindrome(n):
    return n == n[::-1]

n =input()
result = isPalindrome(n)

if result:
    print("Yes")
else:
    print("No")
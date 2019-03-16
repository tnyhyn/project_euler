# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def solve():
    max = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            strNum, num = str(i * j), (i * j)
            if strNum == strNum[::-1] and num > max:
                max = num
    print(max)

solve()

# Answer: 906609




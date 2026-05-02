"""
    date: 02.05.2026
    sample input: 5 - 3
    sample output: 19
"""
def rabbits(n,k):
    a,b = 1, 1

    for i in range(n-2):
        a, b = b, b + k * a

    return b
    
print(rabbits(5, 3))
def reverseString(a: list):
    for i in range(len(a)//2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]

def subtractProductAndSum(n):
    Msum = 1
    Asum = 0
    for i in str(n):
        Msum *= int(i)
        Asum += int(i)
    return Msum - Asum

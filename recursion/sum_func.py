import math
#sum of all numbers in the integer
def sum(num):
    if len(str(num)) == 1:
        return num
    else:
        return (num % 10) + sum(math.floor(num/10))

if __name__ == '__main__':
    print(sum(1234))
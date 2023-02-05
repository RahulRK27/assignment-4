# Python program to triple all numbers of a given list of integers.

lst = [1,2,3,4,5,6,7]
def triple(lst):
    return lst * 3
data = list(map(triple,lst))
print("Result:",data)
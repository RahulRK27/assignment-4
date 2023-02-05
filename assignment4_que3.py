# square the elements of a list using map() function.

lst = [4,5,2,9]
def square (lst):
    return lst ** 2
data = list(map(square,lst))
print("Return:",data)
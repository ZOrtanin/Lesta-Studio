# плюсы: локанично, понятно, эфективно O(1)
def isEven(value):
    return value % 2 == 0

# как пришёл к этому решению
# def fun(value):
#     arr = ['' for i in range(value)]
#     mid = value // 2
#     return arr[:mid] == arr[mid:]
#
# def fun(value):#     
#     mid = value // 2
#     return value - mid == mid
#
# Честно зацепился за оператор // когдато давно подобную задачу уже решал но не сам
# или когда разберал алгоритм сортировки

# плюсы: локаничный, эфективный О(1). минус: непонятно зачем?
def isNewEven(value):    
    return value - value // 2 == value // 2


if __name__ == "__main__":
    arr = [2, 3, -3, 2342, 0]
    for item in arr:
        print(item, '-> isNewEven ->', isNewEven(item))
        print(item, '-> isEven ->', isEven(item))
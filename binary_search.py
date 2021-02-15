def binary_search(the_value,target):
    low = 0
    high = len(the_value)-1
    while low <= high:
        mid = (high+low) // 2
        if the_value[mid] == target:
            return True
        elif target < the_value[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
        


l = [1,2,3,4,5,6,7,8,9]
t = int(input("Input number : "))
print(binary_search(l,t))

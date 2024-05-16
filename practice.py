#sort the list
def sorting(list1, list2):
    list3 = list1 + list2
    list3.sort()
    print(list3)

list1 = [1, 2, 4]
list2 = [1, 3, 4]
sorting(list1, list2)

list51= [2,3,5]
list52 = [3,5,6]
sorting(list51,list52)

#remove duplicate key
def remove_duplicate(nums):
    new= list(set(nums))
    k = len(new)
    print("k = ", k , new)
nums = [0,0,1,1,1,2,2,3,3,4]
remove_duplicate(nums)







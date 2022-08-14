    """
    
    we are given a array<arr> and a integer <diff> 
    
    we have to find number of subset possible equal to diff
    
    (subset_1 - subset_2 = diff)
    
    so Approach is 
    
    subset_1 - subset_2 = diff ---------------(1)
    subset_1 + subset_2 = total ---------------(2)
    
    adding eq1 and eq2
    
    so new eq ==
    
    2*(subset_1) = diff+total
    subset_1 = (diff+total)/2
    
    so our problem reduced to find a subset which is equal to (diff+total)/2
    
    """


def count_subset_of_given_diff(arr,n,sub1,target):
    
    if sub1 == target:
        return 1
    
    if n == 0:
        return 0
    
    consider = count_subset_of_given_diff(arr, n-1, sub1+arr[n-1],target)
    not_consider = count_subset_of_given_diff(arr,n-1,sub1,target)
    
    if arr[n-1]>=target:
        return consider+not_consider
    else:
        return not_consider



arr = [1,1,2,3]
n = 4

total = sum(arr)

diff = 1

target = (diff+total)//2

print(count_subset_of_given_diff(arr,n,0,target))
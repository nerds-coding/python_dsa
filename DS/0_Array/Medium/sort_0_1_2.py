# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1/?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions#


    """
    -> we are using Dutch National Flag Algorithm
    
    where we keep mid(1) and low(0) initially at zero 
    
    then we iterate through using the mid 
    where we always try to keep one index ahead of 1 
    
    and low at the last 0 index 
    
    and high at the 1 index previous of 2's 
    
    """
def sort012(arr,n):
        low = mid = 0
        high = n-1
        
        while(mid<=high):
            
        """
            As mid will always be on the one index ahead of 1 variable 
            and low will always be on the first index of 1

            so wherever we encouter 0 for arr[i]

            we simply put the first 1 at the mid(where we found the 0)

            and bring 0 at the low(where it was on the 1 index of the 1) 
        """
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                mid+=1
                low+=1
            # when we ecounter 1 then move mid by 1 so we alway 1 index ahead of it
            elif arr[mid] == 1:
                mid+=1
            
            # swapping with first index -1 (where 2 start)
            
            else:
                arr[high],arr[mid] = arr[mid],arr[high]
                high-=1
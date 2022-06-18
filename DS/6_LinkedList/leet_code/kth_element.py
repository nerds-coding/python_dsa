# https://practice.geeksforgeeks.org/problems/find-nk-th-node-in-linked-list/1/?page=1&curated[]=8&sortBy=submissions#

"""

as we have find n/kth element on 1 based index of

thus 

List also return the 1 based indexing where simply divide 


len(ans) by k and then -1 


    
"""

def fractionalNodes(head,k): 
    n = 0
    temp = head
    ans = list()
    while temp:
        n+=1
        ans.append(temp)
        temp = temp.next
    
    
    n = ceil((n)/k)
    
    return ans[-(-len(ans)//k)-1]
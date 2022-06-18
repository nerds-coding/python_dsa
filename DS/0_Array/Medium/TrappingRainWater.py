# problem -> https://leetcode.com/problems/container-with-most-water/

# explanation -> https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
def maxArea(height):

    i, j = 0, len(height)-1

    water = 0

    while(i < j):
        water = max(water, (j-i)*min(height[i], height[j]))
        if(height[i] < height[j]):
            i += 1
        else:
            j -= 1
    return water

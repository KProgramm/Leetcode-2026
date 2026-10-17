class Solution:
    def trap(self, height: List[int]) -> int:
        left_tallest = [0]
        right_tallest = [0]*len(height)
        total = 0

        #make the loop calculating the tallest wall on the left of each index:
        curr = 0
        for i in range(1, len(height)):
            # if height[i-1]> curr:
            #     curr = height[i-1]
            #     left_tallest.append(curr)
            # else:
            #     left_tallest.append(curr)

            curr = max(height[i-1], curr)
            left_tallest.append(curr)
        
        #same thing, loop calc the tallest wall on the right of each index:
        curr = 0
        for i in range(len(height)-2, -1, -1):
            # if height[i+1]>curr:
            #     curr = height[i+1]
            #     right_tallest[i] = curr
            # else:
            #     right_tallest[i] = curr

            curr = max(height[i+1], curr)
            right_tallest[i] = curr

        for i in range(len(height)):
            if height[i] > min(left_tallest[i], right_tallest[i]):
                continue
            water = min(left_tallest[i], right_tallest[i])
            total += water - height[i]
        return total
            

            
        
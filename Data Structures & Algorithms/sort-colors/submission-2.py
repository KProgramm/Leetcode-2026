class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        red = 0
        blue = len(nums)-1

        while s<=blue:
            if nums[s] == 1:
                s+=1
            elif nums[s] == 2:
                # temp = nums[s]
                # nums[s] = nums[blue]
                # nums[blue] = temp
                nums[s], nums[blue] = nums[blue], nums[s]
                blue -=1
            elif nums[s] == 0:
                # temp = nums[s]
                # nums[s] = nums[red]
                # nums[red] = temp
                nums[s], nums[red] = nums[red], nums[s]
                s +=1
                red +=1




        
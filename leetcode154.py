nums=[3,4,5,1,2]
def findMin(numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[right] > numbers[mid]:
                right = mid
            else :
                if numbers[right] < numbers[mid]:
                    left = mid + 1
                else:
                    right -= 1
        return numbers[left]
num=findMin(nums)
#for i in range(0,len(nums)):
#    print(nums[i])
print(num)
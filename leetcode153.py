nums=[3,4,5,1,2]
def findMin( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: #处理0个元素
            return 0
        if len(nums) == 1: #处理1个元素
            return nums[0]

        if nums[0] < nums[-1]: #没发生旋转
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if mid + 1< len(nums): #mid 不是最后一位
                if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]: #找到了
                    return nums[mid]
            else:
                if nums[mid - 1] > nums[mid]: # mid 是最后一位
                    return nums[mid]

            if nums[mid] < nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
num=findMin(nums)
#for i in range(0,len(nums)):
#    print(nums[i])
print(num)
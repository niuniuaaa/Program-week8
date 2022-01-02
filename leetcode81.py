nums=[4,5,6,7,0,1,2]
def search( nums, target) :
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return False

    n = len(nums)
    if n == 1:
        return nums[0] == target

    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        if nums[l] == nums[mid] and nums[mid] == nums[r]:
            l += 1
            r -= 1
        elif nums[l] <= nums[mid]:
            if nums[l] <= target and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target and target <= nums[n - 1]:
                l = mid + 1
            else:
                r = mid - 1

    return False
num=search(nums, 0)
for i in range(0,len(nums)):
    print(nums[i])
print(num)
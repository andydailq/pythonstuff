class Solution:
    """
    Rotated Sorted Array
    RC O(log(n))
    """
    def search(self, nums: List[int], target: int) -> int:
        floor_index = 0
        ceiling_index = len(nums) - 1

        while floor_index <= ceiling_index:
            mid_index = floor_index + (ceiling_index - floor_index) // 2
            if nums[mid_index] == target:
                return mid_index
            # if sorted half of array is on the left of the middle index
            if nums[floor_index] <= nums[mid_index]:
                if nums[floor_index] <= target < nums[mid_index]:
                    ceiling_index = mid_index - 1
                else:
                    floor_index = mid_index + 1
            # if sorted half of array is on the right side of the middle index
            else:
                if nums[mid_index] < target <= nums[ceiling_index]:
                    floor_index = mid_index + 1
                else:
                    ceiling_index = mid_index - 1
        # if the algorithm does not catch the target at the middle,
        # then the target is not in the array
        return -1

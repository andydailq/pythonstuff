class Solution:
    # RC O(n)
    # SC O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make left array and then right array then multiply for answer array
        length = len(nums)

        left = [None] * length
        left[0] = 1

        right = [None] * length
        right[len(nums) - 1] = 1

        ans = [None] * length
        # left array
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        # right array, have to go backwards because 1 is at last index position for right array
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            ans[i] = left[i] * right[i]

        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea is to use one array (ans[]) to make left array then right
        # to keep in constant space complexity
        # RC O(n)
        # SC O(1)

        length = len(nums)

        ans = [None] * length
        ans[0] = 1

        # make left array
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        # make complete answer array by multiplying right array index value to left array
        Rarray = 1

        for i in reversed(range(length)):
            ans[i] *= Rarray
            Rarray *= nums[i]
        return ans
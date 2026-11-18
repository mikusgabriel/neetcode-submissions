class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 2
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count_zero -= 1
                if count_zero == 0:
                    return [0] * len(nums)
                continue
            
            product *= nums[i]

        output = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                output = [0] * len(nums)
                output[i] = product
                return output
            output.append(product//nums[i])

        return output
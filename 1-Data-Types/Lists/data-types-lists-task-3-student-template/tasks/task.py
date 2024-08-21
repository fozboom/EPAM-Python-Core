from typing import List


def foo(nums: List[int]) -> List[int]:
    result = []
    multiplication = 1
    for value in nums:
        multiplication *= value
    for i in range(len(nums)):
        product = multiplication // nums[i]
        result.append(product)
    return result
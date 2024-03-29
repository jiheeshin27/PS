# My Solution (Brute-Force)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]
                
# Sol2) in을 이용한 탐색
class Solution(object):
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# Sol3) 첫 번째 수를 뺀 결과 키 조회 (dict이용)
class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if (target-num in nums_map) and (i != nums_map[target-num]):
                return [i, nums_map[target-num]]
            
# Sol4) 투 포인터 이용. 단, 배열이 정렬되어있다는 가정 하에
class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로 
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
            
                
                     
        
                
        

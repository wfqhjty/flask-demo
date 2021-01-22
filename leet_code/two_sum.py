class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        dict_nums={}
        for i in range(len(nums)):
            if (len(dict_nums)>0 and nums[i] in dict_nums):
                result=[dict_nums[nums[i]],i]
                return result
            else:
                dict_nums[target-nums[i]]=i
        return []
        
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target=9
    solution=Solution()
    print(solution.twoSum(nums,target))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        sum_=0
        max_=0
        map_idx={}
        for i in range(len(s)):
            ch = s[i]
            if ch in map_idx:
                idx = map_idx[ch]
                if idx>=start:
                    sum_=i-idx
                    start=idx+1
                    map_idx[ch]=i
                else:
                    map_idx[ch]=i
                    sum_+=1
            else:
                map_idx[ch]=i
                sum_+=1
            max_=max(sum_,max_)
        return max_
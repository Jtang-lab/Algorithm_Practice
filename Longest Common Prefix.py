# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resultStr = strs[0]
        lenResult = len(strs[0])
        while(lenResult>=0):
            for i in range(0, len(strs[0])-lenResult):
                subString = strs[0][i:lenResult+1]
                for j in range(1, len(strs)):
                    if(subString not in strs[j]):
                        resultStr = ""
                        continue
                    else:
                        resultStr = subString
                if(resultStr != ""):
                    resultStr = subString
                    return resultStr
            lenResult = lenResult -1
        return resultStr


strs = ["reflower","flow","flight"]

print(Solution().longestCommonPrefix(strs))
                
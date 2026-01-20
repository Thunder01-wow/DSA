class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        pre_len=len(prefix)

        for i in strs[1:]:
            while prefix != i[0:pre_len]:
                pre_len-=1
                if pre_len==0:
                    return ""
                prefix=prefix[0:pre_len]
        return prefix

        
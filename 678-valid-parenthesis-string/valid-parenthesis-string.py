class Solution:
    def checkValidString(self, s: str) -> bool:
        Leftmin , Leftmax = 0 , 0

        for i in s:
            if i =="(":
                Leftmin += 1
                Leftmax += 1
            elif i == ")":
                Leftmin -= 1
                Leftmax -= 1
            else:
                Leftmin -= 1
                Leftmax += 1

            if Leftmin < 0:
                Leftmin = 0

            if Leftmax < 0:
                return False
        
        return Leftmin == 0
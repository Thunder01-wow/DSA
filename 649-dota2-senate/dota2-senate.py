class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D , R = deque() , deque()
        for i , n in enumerate(senate):
            if n == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r > d:
                D.append(d + len(senate))
            else:
                R.append(r + len(senate))
        
        if R:
            return "Radiant"
        else:
            return "Dire"

        
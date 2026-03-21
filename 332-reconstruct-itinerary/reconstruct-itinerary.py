class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        stack = ["JFK"]
        res = []

        for src , dst in sorted(tickets,reverse = True):
            adj[src].append(dst)

        while stack:
            if adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            else:
                res.append(stack.pop())
            
        return res[::-1]





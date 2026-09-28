class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q=deque()
        ans=[]
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q[0]==i-k:
                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop()

            q.append(i)
            ans.append(nums[q[0]])    
        return ans                

            
                
                        


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
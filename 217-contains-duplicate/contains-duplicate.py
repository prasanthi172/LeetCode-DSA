class Solution(object):
    def containsDuplicate(self, nums):
        
            
            fre=Counter(nums)
            if max(fre.values()) > 1:
                return True
            else:
                return False  
            
          


        
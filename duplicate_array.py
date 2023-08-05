class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checker = set()
        for ele in nums:
            if ele in checker:
                return True
            else:
                checker.add(ele)
        return False


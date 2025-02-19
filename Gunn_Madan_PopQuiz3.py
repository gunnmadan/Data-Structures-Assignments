class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1 and not trust:
            return 1

        trusts = [0] * (n+1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1        
    
# Edge case: If there's only one person and no trust relationships,
#that person is considered the judge by default. 
    
#Initialize arrays to count how many people each person trusts and
# how many people trust each person.
    
# Populate the arrays based on the trust relationships given in the input.
# For each trust relationship [a, b]:
# - Increment trusts[a] since person 'a' trusts someone.
# - Increment trusted_by[b] since person 'b' is trusted by person 'a'.

# Check each person to see if they meet the criteria to be the judge.
    # The judge must:
    # - Trust nobody (trusts[i] == 0)
    # - Be trusted by exactly n - 1 people (trusted_by[i] == n - 1)

    # If no person meets the criteria to be the judge, return -1.
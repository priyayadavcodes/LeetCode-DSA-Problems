class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        ls = list(st)

        if ls[0] == "-":
            return False
        else:
            for i in range(len(ls)//2):
                temp = ls[len(ls)-1-i]
                ls[len(ls)-1-i] = ls[i]
                ls[i] = temp

        s = "".join(ls)
        xnum = int(s)

        if x == xnum:
            return True
        else:
            return False
        
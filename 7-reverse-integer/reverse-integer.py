class Solution:
    def check_32_bit_signed_range(self,n):
        return -2**31 <= n <= 2**31 - 1

    def reverse(self, x: int) -> int:        
        st = str(x)
        ls = list(st)
        
        if ls[0] == "-":
            ls.remove("-")
            for i in range(len(ls)//2):
                temp = ls[len(ls)-1-i]
                ls[len(ls)-1-i] = ls[i]
                ls[i] = temp
            ls.insert(0,"-")
            
        else:
            for i in range(len(ls)//2):
                temp = ls[len(ls)-1-i]
                ls[len(ls)-1-i] = ls[i]
                ls[i] = temp
        
        listToStr = ''.join(map(str, ls))
        num = int(listToStr)
        if not self.check_32_bit_signed_range(num):
            return 0
        else:
            return num

    




  

        
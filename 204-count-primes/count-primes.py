class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean array "is_prime[0..n-1]" and initialize
        # all entries it as true. A value in is_prime[i] will
        # finally be false if i is Not a prime, true otherwise.
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as False starting from i*i
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count all prime numbers
        return sum(is_prime)


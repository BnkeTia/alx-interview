#!/usr/bin/python3
def iswinner(x, nums):
    def sieve(n):
        """
        Generate a list of primes up to nusing the sieve of Eratosthene
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False

            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    def play_game(n):
        available_numbers = list(range(1, n + 1))
        prime_set = set(primes)
        current_turn = 0 # 0 for maria 1 for Ben

        while True:
            made_move = False
            for p in primes:
                if p > n:
                    break
                if p in available_numbers:
                    # Remove p and its multiples
                    available_numbers = [num for num in available_numbers if num % p !=0]
                    made_move = True
                    current_turn = 1 - current_turn # switch turns
                break
            if not made_move:
                break

        return "Maria" if current_turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        winner = play_games(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

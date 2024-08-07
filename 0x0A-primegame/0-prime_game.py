#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of x rounds of a prime-number-based game.

    Parameters:
    x (int): The number of game rounds.
    nums (list): A list of integers, each representing the maximum
                 number in the set for each round.

    Returns:
    str: The name of the player with the most wins ('Maria' or 'Ben').
         If there is no clear winner, return None.
    """
    if x <= 0 or not nums:
        return None

    def sieve(n):
        """
        Return a list of prime numbers up to n using the
        Sieve of Eratosthenes.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    def play_game(n):
        """Simulate the game for a given n and return the winner."""
        primes = sieve(n)
        if not primes:
            return "Ben"  # No primes means Ben wins automatically
        current_player = "Maria"
        while primes:
            p = primes.pop(0)  # Maria picks the smallest prime
            # Remove multiples of p
            primes = [x for x in primes if x % p != 0]
            if not primes:
                return current_player
            current_player = "Ben" if current_player == "Maria" else "Maria"
        return "Ben" if current_player == "Maria" else "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
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

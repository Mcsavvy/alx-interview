#!/usr/bin/python3
"""prime game"""


PlayerID = int
PlayerName = str


def isPrime(n: int) -> bool:
    """checks if a number is a prime number."""
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return True
    for i in range(3, (n // 2), 2):
        if n % i == 0:
            return False
    return True


def playRound(r: int) -> PlayerID:
    """Play a round of primegame

    Args:
        r: the number range for this round
    """
    player: PlayerID = 0
    number_range = list(range(1, r + 1))

    def switch(player: PlayerID) -> PlayerID:
        if player == 0:
            return 1
        return 0

    # we need to map numbers booleans indicating if they
    # are prime numbers. This would help us avoid making multiple
    # calls to `isPrime`.
    prime_map = {n: isPrime(n) for n in number_range}

    while 1:
        # print(f"Current Player: {player}")
        prime = 0
        for n in number_range:
            if prime_map[n]:
                prime = n
                break
        if not prime:
            return switch(player)
        # print(f"Selected Prime {prime}")
        for n in tuple(number_range):
            if n % prime == 0:
                # print(f"Removing {n}")
                number_range.remove(n)
        player = switch(player)


def isWinner(x: int, nums: 'list[int]') -> 'PlayerName | None':
    """Detect who wins a game of prime numbers.

    Args:
        x: the numbers of rounds in the game
        nums: a list containing the number-range for each round

        NOTE: len(nums) == x
    """
    player_names: tuple[str, str] = ("Maria", "Ben")
    winners: list[PlayerID] = []
    if x != len(nums):
        return None
    for i in range(x):
        # print(f"Round {i + 1}")
        winner = playRound(nums[i])
        # print(f"Winner For Round {i + 1}: '{winner}'")
        winners.append(winner)
    ones = 0
    zeros = 0
    for w in winners:
        if w == 1:
            ones += 1
        else:
            zeros += 1
    if ones == zeros:
        return None
    elif ones > zeros:
        return player_names[1]
    return player_names[0]

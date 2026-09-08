# 12981

def solution(n, words):
    used = [words[0]]
    prev = words[0]

    for idx, curr in enumerate(words[1:], start=1): # enumerate from words[1], starting idx also from 1
        if (curr[0] != prev[-1]) or curr in used:
            person = idx % n + 1
            turn = idx // n + 1
            return [person, turn]

        used.append(curr)   
        prev = curr

    return [0, 0]
    

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
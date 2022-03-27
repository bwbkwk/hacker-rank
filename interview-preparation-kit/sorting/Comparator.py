from functools import cmp_to_key

def get_sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    return -1

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "Player("+self.name+","+self.score+")"
    def comparator(a, b):
        # get_sign just for consistency purposes
        # the score_factor will work fine just without it
        score_factor = get_sign(b.score - a.score)
        if b.score != a.score:
            return score_factor
        name_factor = 1 if a.name > b.name else 0 if a.name == b.name else -1
        return name_factor
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

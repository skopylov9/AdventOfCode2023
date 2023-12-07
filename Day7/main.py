from collections import Counter

def cardToNum(card, joker=False):
    cardToNumMap = { 'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 1 if joker else 11, 'T' : 10 }

    if card in cardToNumMap:
        return cardToNumMap[card]
    
    return int(card)

def cardToNumJoker(card):
    return cardToNum(cardToNum(card, joker=True))

def calcRunk(hand, joker=False):
    cardMap = Counter(hand)

    if joker and 'J' in cardMap and len(cardMap) > 1:
        jCount = cardMap.pop('J')
        key, _ = max(cardMap.items(), key=lambda item: item[1])
        cardMap[key] = cardMap[key] + jCount

    statToRunkMap = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]

    return statToRunkMap.index(tuple(sorted(cardMap.values())))

hands = open('input.txt').read().split('\n')
hands = [(handAndBid.split(' ')[0], int(handAndBid.split(' ')[1])) for handAndBid in hands]

handsPart1 = [([calcRunk(hand[0])] + list(map(cardToNum, hand[0])), hand[1]) for hand in hands]
handsPart1 = sorted(handsPart1, key=lambda hand: hand[0])

handsPart2 = [([calcRunk(hand[0], joker=True)] + list(map(cardToNumJoker, hand[0])), hand[1]) for hand in hands]
handsPart2 = sorted(handsPart2, key=lambda hand: hand[0])

print('Part 2: {}'.format(sum([(idx + 1) * hand[1] for idx, hand in enumerate(handsPart2)])))   # 249666369
print('Part 1: {}'.format(sum([(idx + 1) * hand[1] for idx, hand in enumerate(handsPart1)])))   # 249204891

def strToIntNums(nums):
    return [int(num) for num in nums.split(' ') if num]

cards = open('input.txt').read().split('\n')
cards = [(idx, card[card.index(':') + 2 : card.index('|')], card[card.index('|') + 2 :]) for idx, card in enumerate(cards)]
cards = [(idx, strToIntNums(winNums), strToIntNums(haveNums)) for idx, winNums, haveNums in cards]

scores = [sum([1 if winNum in haveNums else 0 for winNum in winNums]) for _, winNums, haveNums in cards]
points = [2 ** (score - 1) if score else 0 for score in scores]

copies = [1 for _ in cards]
for cardIdx, winNums, haveNums in cards:
    for winNumIdx in range(scores[cardIdx]):
        if len(copies) <= (cardIdx + winNumIdx + 1):
            continue
        copies[cardIdx + winNumIdx + 1] += copies[cardIdx]

print('Part 1: {}'.format(sum(points)))     # 20855
print('Part 2: {}'.format(sum(copies)))     # 5489600
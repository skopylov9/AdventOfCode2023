steps = open('input.txt').read().replace('\n', '').split(',')

def customHash(value, seek = 0):
    return customHash(value[1:], (seek + ord(value[0])) * 17 % 256) if value else seek

boxes = [[] for _ in range(256)]
for step in steps:
    label = step.split('-' if '-' in step else '=')[0]
    boxIdx = customHash(label)
    labelIdx = next((idx for idx, lens in enumerate(boxes[boxIdx]) if label == lens[0]), None)

    if '-' in step and labelIdx is not None:
        boxes[boxIdx] = boxes[boxIdx][:labelIdx] + boxes[boxIdx][labelIdx + 1:]

    if '=' in step:
        focalLength = int(step[-1])
        if labelIdx is not None:
            boxes[boxIdx] = boxes[boxIdx][:labelIdx] + [(label, focalLength)] + boxes[boxIdx][labelIdx + 1:]
        else:
            boxes[boxIdx].append((label, focalLength))

part1Summ = sum([customHash(step) for step in steps])
part2Summ = sum([(boxIdx + 1) * (lensIdx + 1) * lens[1] for boxIdx, box in enumerate(boxes) for lensIdx, lens in enumerate(box)])

print('Part 1: {}'.format(part1Summ))   # 495972
print('Part 2: {}'.format(part2Summ))   # 245223

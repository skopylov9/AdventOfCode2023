from functools import reduce
from operator import mul

lines = open('input.txt').read().splitlines()
lines = [ line.split(' -> ') for line in lines ]
modules = { srcModule[1:] : (srcModule[0], dstModules.split(', ')) for srcModule, dstModules in lines }
modules['broadcaster'] = modules.pop('roadcaster')
states = { module : False for module in modules }
conjunctionStates = { module : {} for module, (mType, _) in modules.items() if '&' == mType }
for module, (_, dstModules) in modules.items():
    for dstModule in dstModules:
        if dstModule in conjunctionStates:
            conjunctionStates[dstModule][module] = False

# Flip-flop modules (prefix %) are either on or off; they are initially off.
# If a flip-flop module receives a high pulse, it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse, it flips between on and off.
# If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules;
# they initially default to remembering a low pulse for each input. When a pulse is received,
# the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs,
# it sends a low pulse; otherwise, it sends a high pulse.

# There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all of its destination modules.

# Here at Desert Machine Headquarters, there is a module with a single button on it called, aptly, the button module.
# When you push the button, a single low pulse is sent directly to the broadcaster module.

eventQueue = []

lowPulses = 0
hightPulses = 0

stat = {}
def addToStat(idx, srcModule, pulse):
    if srcModule not in stat:
        stat[srcModule] = ([], [])
    
    stat[srcModule][int(pulse)].append(idx)

def calcPart1(idx):
    global lowPulses
    global hightPulses
    global eventQueue

    if not eventQueue:
        return

    srcModule, dstModule, pulse = eventQueue.pop(0)

    if pulse:
        hightPulses += 1
    else:
        lowPulses += 1

    if dstModule not in modules:
        calcPart1(idx)
        return

    mType, dstModules = modules[dstModule]

    if 'b' == mType:
        addToStat(idx, dstModule, pulse)
        for module in dstModules:
            eventQueue.append((dstModule, module, pulse))
    elif '%' == mType and not pulse:
        states[dstModule] = not states[dstModule]
        addToStat(idx, dstModule, states[dstModule])
        for module in dstModules:
            eventQueue.append((dstModule, module, states[dstModule]))
    elif '&' == mType:
        conjunctionStates[dstModule][srcModule] = pulse
        addToStat(idx, dstModule, not all(conjunctionStates[dstModule].values()))
        for module in dstModules:
            eventQueue.append((dstModule, module, not all(conjunctionStates[dstModule].values())))

    calcPart1(idx)

for i in range(1000):
    eventQueue.append(('btn', 'broadcaster', False))
    calcPart1(i + 1)


stat = {}
conjunctionStates = { module : {} for module, (mType, _) in modules.items() if '&' == mType }
for module, (_, dstModules) in modules.items():
    for dstModule in dstModules:
        if dstModule in conjunctionStates:
            conjunctionStates[dstModule][module] = 0

def calcPart2(srcModule, pulse):
    if srcModule not in stat:
        stat[srcModule] = []
    stat[srcModule].append(pulse)

    srcType, dstModules = modules.get(srcModule, ('', []))

    for module in dstModules:
        if module not in modules or 'b' == modules[module][0]:
            calcPart2(module, pulse)
        elif '%' == modules[module][0] and pulse[0] == 0:
            if module not in stat or len(stat[module]) < 2:
                calcPart2(module, (0, pulse[1] * 2, pulse[2] * 2))
                calcPart2(module, (1, pulse[1], pulse[2] * 2))
        elif '&' == modules[module][0]:
            if 0 == pulse[0]:
                calcPart2(module, (1, pulse[1], pulse[2]))
            else:
                conjunctionStates[module][srcModule] = pulse[1]
                if all(conjunctionStates[module].values()):
                    if '%' == srcType:
                        calcPart2(module, (0, sum(conjunctionStates[module].values()), pulse[2]))
                    elif '&' == srcType:
                        calcPart2(module, (0, reduce(mul, conjunctionStates[module].values()), pulse[2]))
                else:
                    calcPart2(module, (1, pulse[1], pulse[2]))

calcPart2('broadcaster', (0, 1, 1))


print('Part 1:', lowPulses * hightPulses)                                   # 817896682
print('Part 2:', [pulse for pulse in stat['rx'] if pulse[0] == 0][0][1])    # 250924073918341

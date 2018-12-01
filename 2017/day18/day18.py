from collections import defaultdict
instructions = [
'set i 31',
'set a 1',
'mul p 17',
'jgz p p',
'mul a 2',
'add i -1',
'jgz i -2',
'add a -1',
'set i 127',
'set p 826',
'mul p 8505',
'mod p a',
'mul p 129749',
'add p 12345',
'mod p a',
'set b p',
'mod b 10000',
'snd b',
'add i -1',
'jgz i -9',
'jgz a 3',
'rcv b',
'jgz b -1',
'set f 0',
'set i 126',
'rcv a',
'rcv b',
'set p a',
'mul p -1',
'add p b',
'jgz p 4',
'snd a',
'set a b',
'jgz 1 3',
'snd b',
'set f 1',
'add i -1',
'jgz i -11',
'snd a',
'jgz f -16',
'jgz a -19']

# instructions = [
        # 'set a 1',
# 'add a 2',
# 'mul a a',
# 'mod a 5',
# 'snd a',
# 'set a 0',
# 'rcv a',
# 'jgz a -1',
# 'set a 1',
# 'jgz a -2']

def run(instructions):
    registers = defaultdict(int)
    sound = ''
    recovered_sound = ''
    i = 0
    while i < len(instructions):
    #for i in range(len(instructions)):
        instr = instructions[i].split()
        if instr[0] == 'snd':
            sound = registers[instr[1]]
        elif instr[0] == 'set':
            X = instr[1]
            Y = instr[2]
            if Y.isdigit():
                registers[X] = int(Y)
            else:
                registers[X] = registers[Y]
        elif instr[0] == 'add':
            X = instr[1]
            Y = instr[2]
            if Y[-1].isdigit():
                registers[X] = registers[X] + int(Y)
            else:
                registers[X] = registers[X] + registers[Y]
        elif instr[0] == 'mul':
            X = instr[1]
            Y = instr[2]
            if Y[-1].isdigit():
                registers[X] = registers[X] * int(Y)
            else:
                registers[X] = registers[X] * registers[Y]
        elif instr[0] == 'mod':
            X = instr[1]
            Y = instr[2]
            if Y[-1].isdigit():
                registers[X] = registers[X] % int(Y)
            else:
                registers[X] = registers[X] % registers[Y]
        elif instr[0] == 'rcv':
            if registers[instr[1]] is not 0:
                recovered_sound = sound
                break
        elif instr[0] == 'jgz':
            if registers[instr[1]] > 0:
                jump = int(instr[2])
                i += jump
                continue
        print(i)
        i += 1
    print(recovered_sound)


run(instructions)

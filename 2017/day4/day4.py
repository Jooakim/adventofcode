def is_valid(passphrase):
    keys = set()
    for l in passphrase.split():
        if ''.join(sorted(l)) in keys:
            return False
        else: 
            keys.add(''.join(sorted(l)))
    return True

with open('input', 'r') as f:
    s = 0
    for line in f.readlines():
        if is_valid(line):
            s += 1
    print(s)



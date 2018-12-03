import md5
import re

def crack_pass(num_of_chars, key):
    found = 0
    i = 0
    password = ''
    while found < num_of_chars:
        m = md5.new(key + str(i))
        if (re.match('^0{5}',m.hexdigest())):
            password += m.hexdigest()[5]
            found += 1
        i += 1

    return password

def crack_pass_2(num_of_chars, key):
    found = 0
    i = 0
    password = {}
    while found < num_of_chars:
        m = md5.new(key + str(i))
        if (re.match('^0{5}',m.hexdigest())):
            if (re.match('[0-7]', m.hexdigest()[5]) and not password.has_key(int(m.hexdigest()[5]))):
                password[int(m.hexdigest()[5])] = m.hexdigest()[6]
                found += 1
        i += 1

    return password

password = crack_pass_2(8, 'wtnhxymk')
print(str(password))


def brain_luck(code, input):
    parser = 0
    byte = 0
    register = 0
    data = [0]
    output = []
    brackets = {}

    start = {}
    level = []

    for index,char in enumerate(code):            # {    find matching bracket pairs
        if char == '[':
            level.append(index)
        elif char == ']':
            start[index] = level.pop()

    end = {v: k for k, v in start.items()}        # }


    while parser < len(code):
        if code[parser] == '+':
            data[register] += 1
            if data[register] > 255: data[register] = 0
        elif code[parser] == '-':
            data[register] -= 1
            if data[register] < 0: data[register] = 255

        elif code[parser] == ',':
            data[register] = ord(input[byte])
            byte += 1
        elif code[parser] == '.':
            output.append(chr(data[register]))

        elif code[parser] == ']':
            if data[register] != 0:
                parser = start[parser]
        elif code[parser] == '[':
            if data[register] == 0:
                parser = end[parser]

        elif code[parser] == '>':
            register += 1
            if register == len(data):
                data.append(0)
        elif code[parser] == '<':
            register -= 1
      
        parser += 1
    return ''.join(output)



def main():
    print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars')
    print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9))==chr(72))
######################012345678901234567890123456789012
######################----------11111111112222222222333


if __name__ == "__main__": main()
"""

cd data && wget https://github.com/lang-uk/ukrainian-word-stress-dictionary/raw/master/stress.txt

Format: 

ба|аб+а
абы|аб+ы
аб|+аб
абе|аб+е
абам|аб+ам
абу|аб+у
абой|аб+ой

"""

def replace_accents(x):
    chars = list(x.encode('utf-8').replace(b'\xcc\x81', b'+').decode('utf-8'))

    final_chars = []
    for i, c in enumerate(chars):
        if c == '+':
            try:
                tmp = final_chars[i - 1]

                final_chars.pop()
                final_chars.append('+')
                final_chars.append(tmp)
            except IndexError:
                final_chars.append(c)
        else:
            final_chars.append(c)

    return ''.join(final_chars)


with open('data/stress.dict', 'w') as w:
    with open('data/stress.txt') as f:
        for line in f:
            line = line.strip().lower()
            stressed = replace_accents(line)
            clean = stressed.replace('+', '')

            print(line)
            print(stressed)
            print(clean)
            print()

            w.write(f'{clean}|{stressed}\n')

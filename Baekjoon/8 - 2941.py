words = input()
croatia_alphabet = []

if 'c=' in words:
    for i in range(words.count('c=')):
        croatia_alphabet.append('c=')
    words = words.replace('c=', '*')  # 잘못된 삭제 방지를 위한 코드. 그냥 공백으로 처리하니 예제 입력3에서 잘못된 값이 생겼다.
if 'c-' in words:
    for i in range(words.count('c-')):
        croatia_alphabet.append('c-')
    words = words.replace('c-', '*')
if 'dz=' in words:
    for i in range(words.count('dz=')):
        croatia_alphabet.append('dz=')
    words = words.replace('dz=', '*')
if 'd-' in words:
    for i in range(words.count('d-')):
        croatia_alphabet.append('d-')
    words = words.replace('d-', '*')
if 'lj' in words:
    for i in range(words.count('lj')):
        croatia_alphabet.append('lj')
    words = words.replace('lj', '*')
if 'nj' in words:
    for i in range(words.count('nj')):
        croatia_alphabet.append('nj')
    words = words.replace('nj', '*')
if 's=' in words:
    for i in range(words.count('s=')):
        croatia_alphabet.append('s=')
    words = words.replace('s=', '*')
if 'z=' in words:
    for i in range(words.count('z=')):
        croatia_alphabet.append('z=')
    words = words.replace('z=', '*')

words = words.replace('*', '')
print(len(words) + len(croatia_alphabet))
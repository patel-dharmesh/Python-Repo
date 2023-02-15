def freq(str):
    str = str.split()
    str2 = []

    for s in str:
        if s not in str2:
            str2.append(s)
    
    for i in range(0, len(str2)):
        print('Freq ', str2[i], ':', str.count(str2[i]))
    
    #counter = collections.Counter(str).most_common(3)
    #print(counter)

def main():
    str = 'd a b c a a c b b d d d d'
    freq(str)

main()
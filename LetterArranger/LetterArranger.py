def CountWords(word):
    words = permutation(word)
    words = list(set(words))
    words[:] = (l for l in words if not isVowel(l[0]))
    words[:] = (l for l in words if not hasConsecutive(l))
    print(words)
    print(len(words))

def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]  
 
        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]
 
        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append(m + ''.join(p))
    return l
 
def isVowel(letter):
    vowels = "AEIOU"
    return letter in vowels

def hasConsecutive(word):
    return any((isVowel(c1) and isVowel(c2)) or (not isVowel(c1) and not isVowel(c2)) for c1, c2 in zip(word, word[1:]))
    #return any(c1 == c2 for c1, c2 in zip(word, word[1:]))

# Driver program to test above function
#data = list('123')
#for p in permutation(data):
#    print (p)

CountWords("CABAY")

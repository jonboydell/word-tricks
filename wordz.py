ad_name = 'Ark St Giles Academy'
ss_name = 'St Giles'

WORDS = ['Primary', 'School']
words = list(map(lambda w: w.lower(), WORDS))


def homogenise_string(s: str):
    t = s.replace(',','')
    return t.lower().split(' ')
    

def remove_words(s: [], t: []):
    b = list(filter(lambda c: c not in t, s))
    return b
    

def match_words(s: [], t: []):
    b = list(map(lambda c: c in s, t))
    return b
    
    
def count_matches(a: []):
    return a.count(True)
    

def score_match(s: str, t: str, w: []):
    left = remove_words(homogenise_string(s), w)
    right = remove_words(homogenise_string(t), w)
    d = match_words(left, right)
    c = count_matches(d)
    return d, c, c / len(left), c / len(right)


matches, match_count, l, r = score_match(ad_name, ss_name, words)

print(matches)
print(match_count)
print(l)
print(r)

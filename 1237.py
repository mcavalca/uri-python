from difflib import SequenceMatcher
while True:
    try:
        pa = input()
        pb = input()
        sub = SequenceMatcher(None, pa, pb)
        m = sub.find_longest_match(0, len(pa), 0, len(pb))
        print(m.size)

    except EOFError:
        break

def is_palindrome(motherAge, daughterAge):
    motherAge = str(motherAge)
    daughterAge = str(daughterAge)
    difference = len(motherAge) - len(daughterAge)
    daughterAge = daughterAge.zfill(len(motherAge))
    motherAge = motherAge[::-1]
    if motherAge == daughterAge:
        return True
    else:
        return False

count = 0
previousDiffAge = 0
for motherAge in range (15, 120):
    for daughterAge in range(1, 100):
        diffAge = motherAge - daughterAge
        if is_palindrome(motherAge, daughterAge) and diffAge == previousDiffAge:
            count = count + 1
            if count == 6:
                print(motherAge)
                print(daugtherAge)
    previousDiffAge = diffAge

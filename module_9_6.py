def all_variants(text):
    k = 0
    for _ in range(len(text)):
        j = 0
        for _ in range(len(text)-k):
            yield text[j:j+k+1]
            j += 1
        k += 1


a = all_variants("abc")
for i in a:
    print(i)

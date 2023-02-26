#build up a dictionary and assign each key with value.
dic = {}
phrase = "The lazy dog jumped over the curious cat."
for i in phrase:
    if i.isalpha():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

for I in sorted(dic):
    print(f"{I} {dic[I]}")
    



from collections import Counter
import pandas as pd

tt = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked " \
     "a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked "

ttl = tt.split()

for i in range(len(ttl)):
    ttl[i] = ttl[i].lower()

ttl.sort()

ttc = Counter(list(ttl))

ttd = dict(ttc)

for k, v in list(ttd.items()):
    if v < 2:
        ttd.pop(k)

df = pd.DataFrame.from_dict(ttd, orient='index', columns=['COUNT'])
df = df.rename_axis("WORD", axis="columns")

print(df)

import gzip
import pandas as pd
from tqdm import tqdm

file = "clinvar.vcf.gz"

rows = []

with gzip.open(file, "rt", encoding="utf-8") as f:

    for line in tqdm(f):

        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")

        chr = parts[0]
        pos = int(parts[1])
        ref = parts[3]
        alt = parts[4]

        info = parts[7]

        clnsig = None

        for field in info.split(";"):
            if field.startswith("CLNSIG="):
                clnsig = field.split("=")[1]

        rows.append([chr,pos,ref,alt,clnsig])

df = pd.DataFrame(rows,columns=["chr","pos","ref","alt","clnsig"])

print("Toplam varyant:",len(df))

df.to_csv("clinvar_raw.csv",index=False)
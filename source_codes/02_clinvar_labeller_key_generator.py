import pandas as pd

clinvar = pd.read_csv("clinvar_raw.csv", low_memory=False)

pathogenic_terms = {
    "Pathogenic",
    "Likely_pathogenic",
    "Pathogenic/Likely_pathogenic"
}

benign_terms = {
    "Benign",
    "Likely_benign",
    "Benign/Likely_benign"
}

def make_label(x):
    if pd.isna(x):
        return None
    
    x = str(x).strip()
    
    if x in pathogenic_terms:
        return 1
    
    if x in benign_terms:
        return 0
    
    return None

clinvar["label"] = clinvar["clnsig"].apply(make_label)
clinvar = clinvar.dropna(subset=["label"])

# Key oluştur
clinvar["chr"] = clinvar["chr"].astype(str)
clinvar["pos"] = clinvar["pos"].astype(int)
clinvar["ref"] = clinvar["ref"].astype(str)
clinvar["alt"] = clinvar["alt"].astype(str)

clinvar["key"] = clinvar["chr"] + "_" + clinvar["pos"].astype(str) + "_" + clinvar["ref"] + "_" + clinvar["alt"]

clinvar.to_csv("clinvar_all_chrs_with_keys.csv", index=False)

print(len(clinvar))
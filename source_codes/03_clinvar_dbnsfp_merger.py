import pandas as pd
from tqdm import tqdm
import numpy as np

# ClinVar verisi
clinvar = pd.read_csv("clinvar_all_chrs_with_keys.csv", usecols=["key","label"])
clinvar_keys = set(clinvar["key"])

feature_cols = [
    "#chr","pos(1-based)","ref","alt","genename",

    "SIFT_score","Polyphen2_HDIV_score","MutationTaster_score",
    "MutationAssessor_score","VEST4_score","MetaSVM_score","MetaLR_score",
    "M-CAP_score","REVEL_score","MutPred2_score","gMVP_score",
    "BayesDel_addAF_score","BayesDel_noAF_score","CADD_phred","DANN_score",
    "fathmm-XF_coding_score","Eigen-raw_coding","Eigen-phred_coding","MisFit_D_score",

    "AlphaMissense_score","AlphaMissense_rankscore","ESM1b_score","popEVE_score",

    "GERP++_RS","GERP_92_mammals","phyloP100way_vertebrate",
    "phyloP470way_mammalian","phastCons100way_vertebrate","phastCons470way_mammalian",

    "gnomAD4.1_joint_AF","gnomAD4.1_joint_POPMAX_AF","dbNSFP_POPMAX_AF",

    "MANE"
]

chunksize = 50000
results = []

chromosomes = [str(i) for i in range(1,23)] + ["X","Y","M"]

for chr in chromosomes:

    file = f"dbNSFP/dbNSFP5.3.1a_variant.chr{chr}.gz"
    print(f"\nProcessing chromosome {chr}: {file}")

    for chunk in tqdm(pd.read_csv(file,
                                  sep="\t",
                                  usecols=feature_cols,
                                  compression="gzip",
                                  chunksize=chunksize,
                                  low_memory=False)):

        chunk["key"] = chunk["#chr"].astype(str) + "_" + \
                       chunk["pos(1-based)"].astype(str) + "_" + \
                       chunk["ref"] + "_" + chunk["alt"]

        matched = chunk[chunk["key"].isin(clinvar_keys)]

        if len(matched) > 0:
            results.append(matched)

dataset = pd.concat(results, ignore_index=True)

dataset = pd.merge(dataset, clinvar, on="key", how="inner")
dataset = dataset.drop(columns=["key"])

# ----------------------------
# MULTIVALUE KOLON TESPİTİ
# ----------------------------

score_cols = [c for c in dataset.columns if c not in ["#chr","pos(1-based)","ref","alt","label","genename", "MANE"]]

multivalue_cols = []

for col in score_cols:

    sample = dataset[col].astype(str)

    if sample.str.contains(";").any():
        multivalue_cols.append(col)

print("Multivalue columns:")
print(multivalue_cols)

# ----------------------------
# SCORE PROCESSING
# ----------------------------

def process_scores(values_str):

    if pd.isna(values_str) or values_str == ".":
        return np.nan, np.nan, np.nan, 0

    vals = [v for v in str(values_str).split(";") if v not in [".",""]]

    try:

        vals_float = [float(v) for v in vals]

        if len(vals_float) == 0:
            return np.nan, np.nan, np.nan, 0

        return (
            max(vals_float),
            np.mean(vals_float),
            np.std(vals_float),
            len(vals_float)
        )

    except:
        return np.nan, np.nan, np.nan, 0


# ----------------------------
# MULTIVALUE KOLONLAR
# ----------------------------

for col in tqdm(multivalue_cols, desc="Processing multivalue columns"):

    max_list = []
    mean_list = []
    std_list = []
    count_list = []

    for val in dataset[col]:

        mx, mn, sd, ct = process_scores(val)

        max_list.append(mx)
        mean_list.append(mn)
        std_list.append(sd)
        count_list.append(ct)

    dataset[f"{col}_max"] = max_list
    dataset[f"{col}_mean"] = mean_list
    dataset[f"{col}_std"] = std_list
    dataset[f"{col}_count"] = count_list


# ----------------------------
# SINGLE VALUE KOLONLAR
# ----------------------------

single_cols = [c for c in score_cols if c not in multivalue_cols]

for col in single_cols:
    dataset[col] = pd.to_numeric(dataset[col], errors="coerce")


# Orijinal multivalue kolonları silebiliriz
dataset = dataset.drop(columns=multivalue_cols)

dataset.to_csv("variant_dataset.csv", index=False)

print(f"\nFinal dataset length: {len(dataset)}")
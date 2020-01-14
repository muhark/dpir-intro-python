#!/usr/bin/env python3

# This script contains the commands used to create the BES data subsets we use
# for this week's lecture from the original data download.
# It's in the repo for future reference, or in case you were curious where the
# files actually come from.

import pandas as pd
import re

# Reading in source data file, in stata format >:(
df = pd.read_stata("../materials/bes_f2f_2017_v1.3.dta")

# Choosing subset of columns for week 2.
cols = df.columns.tolist()
subset = cols[0:1] + \
         [col for col in cols if re.match(re.compile(r"a[0-9]{2}"), col)] + \
         cols[337:346]+cols[354:356]

# Creating a new dataframe with just these columns.
week2 = df[subset].copy()

# Saving to `csv`, `json`, `feather`; `hdf` requires too many dependencies
week2.to_csv("bes_data_subset_week2.csv", index=False)
week2.to_json("bes_data_subset_week2.json")
week2.to_feather("bes_data_subset_week2.feather")
# week2.to_hdf("bes_data_subset_week2.hdf", key="a_meta")

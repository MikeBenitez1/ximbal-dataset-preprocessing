import pandas as pd
from io import StringIO
import numpy as np
import time
import datetime

raw_dataset = ("/Users/miguelangelbenitezgarcia/Downloads/Datasets_Ximbal/Dataset2_30min.csv")
clean_dataset = ("/Users/miguelangelbenitezgarcia/Downloads/Datasets_Ximbal/Dataset2_30min_clean.csv")

step1 = pd.read_csv(raw_dataset, skiprows = 1)

step1.to_csv(clean_dataset, index=False)

step2 = pd.read_csv(clean_dataset, sep=';', usecols = ["TIME", "FUEL_LEVEL", "ENGINE_LOAD" , "ENGINE_RPM", "FUEL_TYPE", "SPEED", "Short Term Fuel Trim Bank 1", "ENGINE_RUNTIME"])

step2.to_csv(clean_dataset, index=False)

step3 = pd.read_csv(clean_dataset)

step3.rename(columns={'Short Term Fuel Trim Bank 1':'SHORT_TERM_FUEL_TRIM_BANK_1'}, inplace=True)

step3.to_csv(clean_dataset, index=False)

step4 = pd.read_csv(clean_dataset)

step4['TIME'] = pd.to_datetime(step4['TIME'], unit='ms')

step4.to_csv(clean_dataset, index=False)
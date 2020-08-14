import pandas as pd
import numpy as np

#Loading the dataset
raw_dataset = ("/Users/miguelangelbenitezgarcia/Downloads/Datasets_Ximbal/Dataset2_30min.csv")
#Saving the dataset
clean_dataset = ("/Users/miguelangelbenitezgarcia/Downloads/Datasets_Ximbal/Dataset2_30min_clean.csv")

#Deleting the 1st row with unnecessary data header
step1 = pd.read_csv(raw_dataset, skiprows = 1)
step1.to_csv(clean_dataset, index=False)

#Deleting non required columns and only loading necessary columns
names_changed=["TIME", "FUEL_LEVEL", "ENGINE_LOAD" , "ENGINE_RPM", "FUEL_TYPE", "SPEED", "Short Term Fuel Trim Bank 1", "ENGINE_RUNTIME"]
step2 = pd.read_csv(clean_dataset, sep=';', usecols = names_changed)
step2.to_csv(clean_dataset, index=False)

#Renaming some headers as required
step3 = pd.read_csv(clean_dataset)
step3.rename(columns={'Short Term Fuel Trim Bank 1':'SHORT_TERM_FUEL_TRIM_BANK_1_%', 'FUEL_LEVEL': "FUEL_LEVEL_%", 'ENGINE_LOAD': "ENGINE_LOAD_%", 'SPEED': "SPEED_KM/H"}, inplace=True)
step3.to_csv(clean_dataset, index=False)

#Converting the epoch time to a date
step4 = pd.read_csv(clean_dataset)
step4['TIME'] = pd.to_datetime(step4['TIME'], unit='ms')
step4.to_csv(clean_dataset, index=False)

#Deleting rows with null and empty values
step5 = pd.read_csv(clean_dataset)
step5 = step5.replace(to_replace='NODATA' or '-' or 'null', value=np.nan).dropna()
step5.to_csv(clean_dataset, index=False)

#Delete %, RPM and km/h strings from data
step6 = pd.read_csv(clean_dataset)
selected_columns = step6[['FUEL_LEVEL_%', 'ENGINE_LOAD_%', 'ENGINE_RPM', 'SPEED_KM/H', 'SHORT_TERM_FUEL_TRIM_BANK_1_%']]
step6[['FUEL_LEVEL_%', 'ENGINE_LOAD_%', 'ENGINE_RPM', 'SPEED_KM/H', 'SHORT_TERM_FUEL_TRIM_BANK_1_%']] = selected_columns.replace(r'[^0-9.-]+', '', regex=True)
step6.to_csv(clean_dataset, index=False)


import pandas as pd

file = input("Filename:")

sheet = input("Sheetname:")
sheet_names = [sheet]

for sheet_name in sheet_names:	
	date = input("Period_Ending_Date:")
	df = pd.read_excel(file,sheet_name)
	data = df.where(df['Period_Ending_Date'] == date)
	data = data.dropna()
	
	# Saved to a new file
	new_fn = (date + ".xlsx")
	data.to_excel(new_fn,index=False)


	# Joining to an existing file
	f1 = pd.read_excel(new_fn)
	join_to_fn = input("Existing_filename:")
	existing_sheet = input("Sheet_name:")
	f2 = pd.read_excel(join_to_fn,sheet_name= existing_sheet)

	newData = pd.concat([f2,f1])

	newData.to_excel("join_sample.xlsx",index=False)




	

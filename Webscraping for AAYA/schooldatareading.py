import pandas as pd

privschools = pd.read_csv("schools_data\privschool.csv")
pubschools = pd.read_csv("schools_data\pubschool.csv")
pubschooldistrict = pd.read_csv("schools_data\pubschooldistrict.csv")

newdf = pd.DataFrame()

websites = []
print(pubschooldistrict)

for i in range(len(pubschooldistrict["County Code"])):
    if pubschooldistrict["County Name"][i] == "BERGEN" or pubschooldistrict["County Name"][i] == "SOMMERSET" or pubschooldistrict["County Name"][i] == "UNION" or pubschooldistrict["County Name"][i] == "MIDDLESEX" or pubschooldistrict["County Name"][i] == "PASSAIC" or pubschooldistrict["County Name"][i] == "MORRIS":
        websites.append(pubschooldistrict["Website"][i])

# print(newdf)

for i in range(len(privschools["County Code"])):
    if privschools["County Code"][i] == '="04"' or privschools["County Code"][i] == '="36"' or privschools["County Code"][i] == '="40"' or privschools["County Code"][i] == '="24"' or privschools["County Code"][i] == '="32"' or privschools["County Code"][i] == '="28"':
        websites.append(privschools["School Name"][i])
newdf["websites"] = websites
print(newdf)
newdf.to_csv('schoolwebsitelist.csv', index=False)
import pandas as pd

#### NOTE: the dataset is too big to be uploaded on github
# it can be found here: http://whgi.wmflabs.org/snapshot_data/2019-11-04/property_indexes/ (from http://whgi.wmflabs.org/)
df = pd.read_csv("../../data/gender-index-data-2019-11-04.csv") 

# take only those that have a wikipedia page in english
df_en = df[df.site_links.str.contains("enwiki", na=False)]

# filter and take only males or females
MALE = "Q6581097|"
FEMALE = "Q6581072|"

# df_gender = df_en[(df_en.gender == MALE) | (df_en.gender == FEMALE)]
# filter the NaN gender (where we have no info)
df_gender = df_en[df_en.gender.notnull()]

# convert gender and occupation to array
df_gender['gender'] = df_gender['gender'].str.split('|').map(lambda x: x[:-1])

df_gender['occupation'] = df_gender['occupation'].apply(lambda d: d if isinstance(d, str) else "")
df_gender['occupation'] = df_gender['occupation'].str.split('|').map(lambda x: x[:-1])

# save the code and the gender to a new csv
df_gender[["qid", "gender", "occupation"]].to_csv("../data/qid_people_wikidata.csv")

print(df_gender[["qid", "gender"]].head())

# woohoo!
print("!!!!!!!!!!!!!!!")

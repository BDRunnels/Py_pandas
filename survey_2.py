import pandas as pd

data = pd.read_csv("survey_results_public.csv", index_col="ResponseId")
# print(data)

# survey_data = pd.read_csv("survey_results_schema.csv", index_col="qname")
# print(survey_data)
# q1 = survey_data.loc["TBranch"].question
# print(q1)

data["YearsCodePro"] = pd.to_numeric(data["YearsCodePro"], errors="coerce")
q = data.query('ConvertedCompYearly > 100000 & Country == "India" & RemoteWork == "Remote" & YearsCodePro > 12')
print(q["LanguageHaveWorkedWith"].value_counts(), end="\n-----------\n")
print(q["WebframeHaveWorkedWith"].value_counts(), end="\n-----------\n")
print(q["PlatformHaveWorkedWith"].value_counts())

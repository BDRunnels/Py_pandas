import pandas as pd

#   survey_results_public is Stack Overflow 2023 Dev Survey

data = pd.read_csv("survey_results_public.csv")
# print(data.shape)
# print(data.info())

# print(data.head(20))    # first 20 entries
# print(data.tail(20))    # last 20 entries

# pd.set_option("display.max_columns", 85)

# print(data.Employment.value_counts())
# print(data["OpSysProfessional use"].value_counts())

# print(data.Employment[89182])
# print(data.DevType.value_counts())


    # Devs who only use MacOS
macOs_dev = data[data["OpSysProfessional use"] == "MacOS"]
print(macOs_dev)
print("*" * 100)

    # Devs from USA
usa_dev = data[data["Country"] == "United States of America"]
print(usa_dev)
print(usa_dev["Age"].value_counts())
print("*" * 100)

    # Devs from India
india_dev = data[data["Country"] == "India"]
print(india_dev)
print(india_dev["Age"].value_counts())
print("*" * 100)

    # How many India devs interested in coding as hobby as full time employee?
india_coding_act = data[(data["Country"] == "India") & (data["CodingActivities"] == "Hobby") & (data["Employment"] == "Employed, full-time")]
print(india_coding_act)
print("*" * 100)

data_filter = ((data["Country"] == "India") &
               (data["RemoteWork"] == "Remote") &
               (data["ConvertedCompYearly"] > 100_000))

print(data[data_filter].WebframeHaveWorkedWith.value_counts())

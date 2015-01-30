import pandas as pd

df = pd.read_excel(io="input/tmall-surface.xlsx", sheet_name="Sheet1")

collect = []
record = []
for index, row in df.iterrows():
    print(index)
    if index % 2 == 0:
        record = [row[3]]
        if row[4] != "nan":
            record.append(row[4])
            print(str(row[4]).split("\n"))
        else:
            record.append(None)
    else:
        record.append(row[10])
        collect.append(record)

# from pprint import pprint
# pprint(collect)

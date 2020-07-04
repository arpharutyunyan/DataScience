import pandas as pd

person = {
    "name": ["Anna", "Ani", "Karen"],
    "surname": ["Sargsyan", "Petrosyan", "Tigranyan"],
    "email": ["anna@gmail.com", "ani@gmail.com", "karen@gmail.com"]
}

data = pd.DataFrame(person)
# print(data)
data.loc[2, ["name", "surname"]]=["Mike", "Smith"]
filt = (data["email"] == "anna@gmail.com")
data.at[filt, "name"] = "Lucy"
print(data)
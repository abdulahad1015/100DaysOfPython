import csv
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240705.csv")
gray_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Colour":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels,red_squirrels,black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel.csv")

import argparse
import csv
import os

parser = argparse.ArgumentParser()


parser.add_argument("-e", "--yearly_max_temp", help="Will show the max temperature in that specific year YYYY")
parser.add_argument("-a", "--average", help="Will show the average temaparature of the month YYYY/MM")
parser.add_argument("path", help="expects path in the argument after flag")


args = parser.parse_args()

months = {1:"Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

def collect_respective_files(folder_path, year):
    all_files = os.listdir(folder_path)
    matching_files = []
    for file in all_files:
        if f"{year}" in file:
            matching_files.append(file)
    print(matching_files)


def read_weather_file(file_path):
    data = {"date":[], "mean_temp":[], "humidity":[]}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)   # Reads file line by line
            for row in reader:
                if row['Max TemperatureC'] and row['Min TemperatureC']:  #
                    data["date"].append(row["GST"])
                    data["mean_temp"].append(int(row["Mean TemperatureC"]))
                    data["humidity"].append(int(row[" Mean Humidity"])) if row[" Mean Humidity"] else None
            
        return data
    except FileNotFoundError:
        print("File not found!")
        return None

def year_data_reader(file_path):
    pass

def Average_temp(path, year):
    print("This is the average temperature")
    print(path)
    collect_respective_files(path, year)
    # data = read_weather_file(path)
    # print(data)

    # max_temp = max(data["mean_temp"])
    # min_temp = min(data["mean_temp"])
    # average_humidity = sum(data["humidity"])/len(data["humidity"])

    # print(f"Highest Average : {max_temp}°C\nLowest Average : {min_temp}°C\nAverage Humidity : {average_humidity}%")




def yearly_max_temp(path):
    print("This is the yearly max temperature")
    print(path)
    print(type(path))

# 5. Logic to call functions based on flags
if args.average:
    if "/" in args.average:
        year, month = args.average.split("/")
        Average_temp(args.path, year)
    else:
        print("You are supposed to give YYYY/MM in the argument")

if args.yearly_max_temp:
    yearly_max_temp(args.path)
    if "/" in args.average:
        year, month = args.average.split("/")


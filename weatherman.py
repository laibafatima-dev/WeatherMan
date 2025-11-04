import argparse
import csv
import os

parser = argparse.ArgumentParser()

#-------------steps against each flag is defined here------------------

parser.add_argument("-e", "--yearly_max_temp", help="Will show the max temperature in that specific year YYYY")
parser.add_argument("-a", "--average", help="Will show the average temaparature of the month YYYY/MM")
parser.add_argument("-c", "--draw_chart", help="Will show the average temaparature of the month YYYY/MM")
parser.add_argument("-c2", "--combined_chart", help="Will show the average temaparature of the month YYYY/MM")
parser.add_argument("path", help="expects path in the argument after flag")


args = parser.parse_args()

eng_months = {1:"Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


#-------------Function to find yearly report------------------

def max_min_temp_max_humidity(folder_path, year):
    """
    folder_path = The path of the folder files
    year = taked the year for which we are finding info
    return = a dict with max min temp and max humidity value with date for each
    """
    all_files = os.listdir(folder_path)
    matching_files = []
    for file_name in all_files:
        if f"{year}" in file_name:
            matching_files.append(file_name)


    data = {"max_temp": {"temp": 0, "date": ""}, "min_temp" : {"temp" : 10000, "date": ""}, "humidity": {"temp": 0, "date": ""}}
    for file in matching_files:
        try:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file_data:
                headers = csv.DictReader(file_data)
                for each_row in headers:
                    if each_row["Max TemperatureC"] and each_row["Min TemperatureC"] and each_row["Max Humidity"]:
                        if int(each_row["Max TemperatureC"]) >= data["max_temp"]["temp"]:
                            data["max_temp"]["temp"] = int(each_row["Max TemperatureC"])
                            data["max_temp"]["date"] = each_row["GST"]

                        if int(each_row["Min TemperatureC"]) <= data["min_temp"]["temp"]:
                            data["min_temp"]["temp"] = int(each_row["Min TemperatureC"])
                            data["min_temp"]["date"] = each_row["GST"]

                        if int(each_row["Max Humidity"]) > data["humidity"]["temp"]:
                            data["humidity"]["temp"] = int(each_row["Max Humidity"])
                            data["humidity"]["date"] = each_row["GST"]
        except Exception as a:
            pass

    return data

def yearly_max_temp(path, year):
    """
    path = takes the complete path given in argument
    year = takes the year user asked data for
    """


    data = max_min_temp_max_humidity(path, year)

    print(f'Highest = {data["max_temp"]["temp"]}°C on {data["max_temp"]["date"]}\n Lowest = {data["min_temp"]["temp"]}°C on {data["min_temp"]["date"]}\n Humid = {data["humidity"]["temp"]}% on {data["min_temp"]["date"]}')



#-----------function to find monthly report--------------

def monthly_report(file_path, year, month):
    """
    file_path = gives the path of the respective folder
    year = from which year do you need data
    month = from with month do you need data

    return = dictionary of the data from respective file
    """

    all_files = os.listdir(file_path)
    matching_file = None
    for file_name in all_files:
        if f"{year}_{eng_months[int(month)]}" in file_name:
            matching_file = file_name



    data = {"date":[], "mean_temp":[], "humidity":[]}
    try:
        file_ = os.path.join(file_path, matching_file)
        with open(file_, 'r') as file:
            reader = csv.DictReader(file)   
            for row in reader:
                if row['Mean TemperatureC']:  
                    data["date"].append(row["GST"])
                    data["mean_temp"].append(int(row["Mean TemperatureC"]))
                    data["humidity"].append(int(row[" Mean Humidity"])) if row[" Mean Humidity"] else None
            
        return data
    except FileNotFoundError:
        print("File not found!")
        return None



def Average_temp(path, year, month):

    """
    file_path = gives the path of the respective folder
    year = from which year do you need data
    month = from with month do you need data

    """
    
    data = monthly_report(path, year, month)

    max_temp = max(data["mean_temp"])
    min_temp = min(data["mean_temp"])
    average_humidity = sum(data["humidity"])/len(data["humidity"])

    print(f"Highest Average : {max_temp}°C\nLowest Average : {min_temp}°C\nAverage Humidity : {average_humidity}%")


# ------------- draw bar chart of a single day ----------
def draw_bar_chart(file_path, year, month):
    """
    file_path = gives the path of the respective folder
    year = from which year do you need data
    month = from with month do you need data

    return = dictionary of the data from respective file
    """

    all_files = os.listdir(file_path)
    matching_file = None
    for file_name in all_files:
        if f"{year}_{eng_months[int(month)]}" in file_name:
            matching_file = file_name



    data = {"date":[], "mean_temp":[], "humidity":[]}
    try:
        file_ = os.path.join(file_path, matching_file)
        with open(file_, 'r') as file:
            reader = csv.DictReader(file)   
            for row in reader:
                if row['Max TemperatureC'] and row['Min TemperatureC']:
                    print(row["GST"]+"\n", int(row['Max TemperatureC'])*"+",row['Max TemperatureC'],"°C\n",int(row['Min TemperatureC'])*"+",row['Min TemperatureC'],"°C\n" )
            
        return data
    except FileNotFoundError:
        print("File not found!")
        return None


#-----------------combined chart-----------------------

def draw_combined_chart(file_path, year, month):
    """
    file_path = gives the path of the respective folder
    year = from which year do you need data
    month = from with month do you need data

    return = dictionary of the data from respective file
    """

    all_files = os.listdir(file_path)
    matching_file = None
    for file_name in all_files:
        if f"{year}_{eng_months[int(month)]}" in file_name:
            matching_file = file_name



    data = {"date":[], "mean_temp":[], "humidity":[]}
    try:
        file_ = os.path.join(file_path, matching_file)
        with open(file_, 'r') as file:
            reader = csv.DictReader(file)   
            for row in reader:
                if row['Max TemperatureC'] and row['Min TemperatureC']:
                    print(row["GST"]+"\n", int(row['Max TemperatureC'])*"+",int(row['Min TemperatureC'])*"=",row['Max TemperatureC'],"°C - ", row['Min TemperatureC'],"°C\n" )
            
        return data
    except FileNotFoundError:
        print("File not found!")
        return None



# ----------------calling of respective function according to the flags------------------

if args.average:
    if "/" in args.average:
        year, month = args.average.split("/")
        Average_temp(args.path, year, month)
    else:
        print("You are supposed to give YYYY/MM in the argument")

if args.yearly_max_temp:

    if "/" in args.yearly_max_temp:
        year, month = args.yearly_max_temp.split("/")
        yearly_max_temp(args.path, year)
    else:
        year = args.yearly_max_temp
        yearly_max_temp(args.path, year)

if args.draw_chart:
    if "/" in args.draw_chart:
        year, month = args.draw_chart.split("/")
        draw_bar_chart(args.path, year, month)
    else:
        print("You are supposed to give YYYY/MM in the argument")

if args.combined_chart:
    if "/" in args.combined_chart:
        year, month = args.combined_chart.split("/")
        draw_combined_chart(args.path, year, month)
    else:
        print("You are supposed to give YYYY/MM in the argument")
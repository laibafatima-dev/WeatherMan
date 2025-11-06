import argparse
import csv
import os

eng_months = {1:"Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

class Yearly_Report:
    def __init__(self, path, year):
        """
        folder_path = The path of the folder files
        year = taked the year for which we are finding info
        """
        self.folder_path = path
        self.year = year

    def yearly_max_temp(self):
        """
        print yearly reported data
        """


        data = self.max_min_temp_max_humidity()

        print(f'Highest = {data["max_temp"]["temp"]}°C on {data["max_temp"]["date"]}\n Lowest = {data["min_temp"]["temp"]}°C on {data["min_temp"]["date"]}\n Humid = {data["humidity"]["temp"]}% on {data["min_temp"]["date"]}')


    def max_min_temp_max_humidity(self):
        """
        return = a dict with max min temp and max humidity value with date for each
        """
        all_files = os.listdir(self.folder_path)
        matching_files = []
        for file_name in all_files:
            if f"{self.year}" in file_name:
                matching_files.append(file_name)


        data = {"max_temp": {"temp": 0, "date": ""}, "min_temp" : {"temp" : 10000, "date": ""}, "humidity": {"temp": 0, "date": ""}}
        for file in matching_files:
            try:
                file_path = os.path.join(self.folder_path, file)
                with open(file_path, 'r') as file_data:
                    headers = csv.DictReader(file_data)
                    for each_row in headers:
                        if each_row["Max TemperatureC"] and each_row["Min TemperatureC"]:
                            if int(each_row["Max TemperatureC"]) > data["max_temp"]["temp"]:
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


#-----------class to find monthly report--------------


class Monthly_report:

    def __init__(self, path, year, month):
        """
        file_path = gives the path of the respective folder
        year = from which year do you need data
        month = from with month do you need data
        """

        self.file_path = path
        self.year = year
        self.month = month

    def fetch_file(self, file_path, year, month):
        """
        return = file from the folder
        """

        all_files = os.listdir(file_path)
        matching_file = None
        
        for file_name in all_files:
            if f"{year}_{eng_months[int(month)]}" in file_name:
                matching_file = file_name
        return matching_file

    def monthly_report(self, matching_file):
        """
        return = dictionary of the data from respective file
        """

        matching_file = self.fetch_file(self.file_path, self.year, self.month)

        data = {"date":[], "mean_temp":[], "humidity":[]}
        try:
            file_ = os.path.join(self.file_path, matching_file)
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


    def Average_temp(self):

        """
        file_path = gives the path of the respective folder
        year = from which year do you need data
        month = from with month do you need data

        """

        path = self.fetch_file(self.file_path, self.year, self.month)
        data = self.monthly_report(path)

        max_temp = max(data["mean_temp"])
        min_temp = min(data["mean_temp"])
        average_humidity = sum(data["humidity"])/len(data["humidity"])

        print(f"Highest Average : {max_temp}°C\nLowest Average : {min_temp}°C\nAverage Humidity : {average_humidity}%")


# ------------- draw bar chart of a single day ----------

class Bar_chart(Monthly_report):
    def __init__(self, path, year, month):
        """
        file_path = gives the path of the respective folder
        year = from which year do you need data
        month = from with month do you need data
        """
        super().__init__(path, year, month)
        self.file_path = path
        self.year = year
        self.month = month

    def draw_bar_chart(self, func):
        """
        return = dictionary of the data from respective file
        """

        matching_file = self.fetch_file(self.file_path, self.year, self.month)


        data = {"date":[], "mean_temp":[], "humidity":[]}
        try:
            file_ = os.path.join(self.file_path, matching_file)
            with open(file_, 'r') as file:
                reader = csv.DictReader(file)   
                for row in reader:
                    if row['Max TemperatureC'] and row['Min TemperatureC']:
                        func(row)
            return data
        except FileNotFoundError:
            print("File not found!")
            return None

    def printing_bar(self, row):
        print(row["GST"]+"\n", int(row['Max TemperatureC'])*"+",row['Max TemperatureC'],"°C\n",int(row['Min TemperatureC'])*"+",row['Min TemperatureC'],"°C\n" )




#-----------------combined chart-----------------------

class Combined_chart(Bar_chart):
    def __init__(self, path, year, month):
        """
        file_path = gives the path of the respective folder
        year = from which year do you need data
        month = from with month do you need data
        """
        
        super().__init__(path, year, month)
        self.file_path = path
        self.year = year
        self.month = month


    def draw_combined_chart(self):
        """
        return = prints the chart
        """
        self.draw_bar_chart(self.printing_bar)

    def printing_bar(self, row):
        print(row["GST"]+"\n", int(row['Max TemperatureC'])*"+",int(row['Min TemperatureC'])*"=",row['Max TemperatureC'],"°C - ", row['Min TemperatureC'],"°C\n" )




#-------------steps against each flag is defined here------------------

parser = argparse.ArgumentParser()

if __name__ == "__main__":

    parser.add_argument("-e", "--yearly_max_temp", help="Will show the max temperature in that specific year YYYY")
    parser.add_argument("-a", "--average", help="Will show the average temaparature of the month YYYY/MM")
    parser.add_argument("-c", "--draw_chart", help="Will show the average temaparature of the month YYYY/MM")
    parser.add_argument("-c2", "--combined_chart", help="Will show the average temaparature of the month YYYY/MM")
    parser.add_argument("path", help="expects path in the argument after flag")


    args = parser.parse_args()



    # ----------------calling of respective function according to the flags------------------

    if args.average:
        if "/" in args.average:
            year, month = args.average.split("/")
            monthly_report_instance = Monthly_report(args.path, year, month)
            monthly_report_instance.Average_temp()
        else:
            print("You are suppose to give YYYY/MM in the argument")

    if args.yearly_max_temp:

        if "/" in args.yearly_max_temp:
            year, month = args.yearly_max_temp.split("/")
            year_report = Yearly_Report(args.path, year)
            year_report.yearly_max_temp()
        else:
            year = args.yearly_max_temp
            year_report = Yearly_Report(args.path, year)
            year_report.yearly_max_temp()

    if args.draw_chart:
        if "/" in args.draw_chart:
            year, month = args.draw_chart.split("/")
            bar_chart_instance = Bar_chart(args.path, year, month)
            bar_chart_instance.draw_bar_chart(bar_chart_instance.printing_bar)
        else:
            print("You are suppose to give YYYY/MM in the argument")

    if args.combined_chart:
        if "/" in args.combined_chart:
            year, month = args.combined_chart.split("/")
            cobmbined_chart_instance = Combined_chart(args.path, year, month)
            cobmbined_chart_instance.draw_combined_chart()
        else:
            print("You are suppose to give YYYY/MM in the argument")

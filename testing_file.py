import os
import csv
from oop_weatherman import Yearly_Report, Monthly_report, Bar_chart, Combined_chart   # change 'main' to your filename


# ---------------- Setup fake data ----------------
os.makedirs("temp", exist_ok=True)

# Sample CSV data for 2024_Jan
data = [
    ["GST", "Max TemperatureC", "Min TemperatureC", "Mean TemperatureC", "Max Humidity", " Mean Humidity"],
    ["2024-01-01", "30", "15", "22", "80", "70"],
    ["2024-01-02", "32", "12", "25", "85", "75"],
    ["2024-01-03", "29", "10", "20", "78", "65"]
]

with open("temp/weather_2024_Jan.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


# ---------------- TEST CASES ----------------

print("========== TESTING STARTED ==========\n")

# 1️⃣ Test Yearly_Report.max_min_temp_max_humidity()
yr = Yearly_Report("temp", 2024)
result = yr.max_min_temp_max_humidity()
print("Yearly_Report.max_min_temp_max_humidity() =>")
print(result, "\n")

# 2️⃣ Test Yearly_Report.yearly_max_temp()
print("Yearly_Report.yearly_max_temp() =>")
yr.yearly_max_temp()
print()

# 3️⃣ Test Monthly_report.fetch_file()
mr = Monthly_report("temp", 2024, 1)
file_name = mr.fetch_file(mr.file_path, mr.year, mr.month)
print("Monthly_report.fetch_file() =>", file_name, "\n")

# 4️⃣ Test Monthly_report.monthly_report()
data_dict = mr.monthly_report(file_name)
print("Monthly_report.monthly_report() =>")
print(data_dict, "\n")

# 5️⃣ Test Monthly_report.Average_temp()
print("Monthly_report.Average_temp() =>")
mr.Average_temp()
print()

# 6️⃣ Test Bar_chart.draw_bar_chart() and printing_bar()
print("Bar_chart.draw_bar_chart() =>")
bc = Bar_chart("temp", 2024, 1)
bc.draw_bar_chart(bc.printing_bar)
print()

# 7️⃣ Test Combined_chart.draw_combined_chart()
print("Combined_chart.draw_combined_chart() =>")
cc = Combined_chart("temp", 2024, 1)
cc.draw_combined_chart()
print()


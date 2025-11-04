# WeatherMan Problem
Weatherman is a Python command-line tool that reads historical Country's weather data from `.txt` files and provides:

- Highest/Lowest Temperature & Humidity of a given **year**
- Average temperature and humidity of a **specific month**
- Temperature **bar charts** (High & Low) on the terminal
- **Combined charts** showing high (`+`) and low (`=`) temperatures together

## Project Structure

/home/dev/Documents/python_basics/<br>
│<br>
├── venv/ # Your virtual environment folder<br>
│<br>
├── Dubai_weather/ # Project root folder<br>
│ ├── weatherman.py # Main Python script (CLI tool)<br>
│ ├── README.md # Documentation file<br>
│ └── data/ # Folder containing weather data files<br>
│ ├── Dubai_weather_2004_Jul.txt<br>
│ ├── Dubai_weather_2004_Aug.txt<br>
│ ├── Dubai_weather_2005_Jan.txt<br>
│ ├── Dubai_weather_2005_Feb.txt<br>
│ └── ... (more files) ...<br>


---

## Installation & Setup

### Clone or move into the project directory:

Create & activate a virtual environment:
python3 -m venv venv
source venv/bin/activate      

### Install dependencies:

pip install -r requirements.txt

Note: You only use built-in libraries (argparse, csv, os), so requirements.txt may just contain:


python>=3.8
#### How to Run the Program

python3 weatherman.py [FLAG] YYYY/MM or YYYY /path/to/Dubai_weather

#### 1- Yearly Report (-e) — Highest temp, lowest temp, highest humidity of a year:

python3 weatherman.py -e 2015 /home/dev/Documents/python_basics/venv/Dubai_weather
#### Output:

Highest = 25°C on 2007-3-29
Lowest = 1°C on 2007-3-4
Humid = 100% on 2007-3-4

#### 2- Monthly Averages (-a) — Average temperature & humidity for a month:

python3 weatherman.py -a 2014/12 /home/dev/Documents/python_basics/venv/Dubai_weather

#### Output:

Highest Average : 12°C
Lowest Average : 2°C
Average Humidity : 28.22%

#### 3- Monthly Temperature Chart (-c) — Bar graph (high & low temps per day):

python3 weatherman.py -c 2014/12 /home/dev/Documents/python_basics/venv/Dubai_weather

#### Output:

2014-12-1
 ++++++++++++++++ 16 °C
 ++++++ 6 °C

2014-12-2
 +++++++++++++++++ 17 °C
 ++++++ 6 °C
...


#### 4- Combined Chart (-c2) — High (+) and Low (=) temperature on same line:

python3 weatherman.py -c2 2014/12 /home/dev/Documents/python_basics/venv/Dubai_weather

#### Output 

2014-12-1
 ++++++++++++++++ ====== 16 °C -  6 °C

2014-12-2
 +++++++++++++++++ ====== 17 °C -  6 °C
...

### Available Flags Overview
Flag	Description	Example
-e or --yearly_max_temp	Yearly max/min temperature and humidity	-e 2015
-a or --average	Monthly average temperature & humidity	-a 2014/12
-c or --draw_chart	Temperature chart (+ for max, + for min)	-c 2014/12
-c2 or --combined_chart	Combined (+ and =) temp chart	-c2 2014/12

### Imp Note
Weather files must follow this format:
Dubai_weather_YYYY_Mon.txt (e.g., Dubai_weather_2014_Dec.txt)

Works only with Dubai weather dataset (CSV inside TXT files)

Tested on Python 3.8+

No external libraries required.


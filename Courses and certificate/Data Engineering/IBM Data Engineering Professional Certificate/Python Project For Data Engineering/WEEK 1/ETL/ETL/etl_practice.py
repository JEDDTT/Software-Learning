import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime

# logfile = "/log.txt"
unifiedDataFile = "transformed.csv"


# LogEvent
class etl_event:
    from datetime import datetime

    timestamp_format = "%Y-%h-%d-%H:%M:%S"  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    targetFile = "C:/Users/emman/Desktop/ETL/log.txt"

    def __init__(self) -> None:
        pass

    def extraction_event(self):
        with open(self.targetFile, "a") as file:
            file.write(
                self.timestamp
                + ", "
                + "The Extraction of all files have been fulfilled"
                + "\n"
            )

    def transform_event(self):
        with open(self.targetFile, "a") as file:
            file.write(
                self.timestamp + ", " + "The transformation have been fulfilled" + "\n"
            )

    def loading_event(self):
        with open(self.targetFile, "a") as file:
            file.write(
                self.timestamp
                + ","
                + "The laod of all files have been fulfilled"
                + "\n"
            )


##Alternative but not recommended for log event function
# def logEvent():
#     timestamp_format = "%Y-%h-%d-%H:%M:%S"  # Year-Monthname-Day-Hour-Minute-Second
#     now = datetime.now()
#     timestamp = now.strftime(timestamp_format)
#     with open(logfile, "a") as file:
#         file.write(timestamp + "," + "File loaded" + "\n")


def extract_from_csv(file):
    """This funciton serves to read csv file"""
    df = pd.read_csv(file)
    return df


def extract_from_json(file):
    """This funciton serves to read json file"""
    df = pd.read_json(file, lines=True)
    return df


def extract_from_xml(file):
    """This funciton serves to read xml file"""
    df = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file)
    root = tree.getroot()
    for car in root:
        model = car.find("car_model").text
        year = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    [
                        {
                            "car_model": model,
                            "year_of_manufacture": year,
                            "price": price,
                            "fuel": fuel,
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )
    return df


# Extracting all csv, json, and xml file in the current directory
def extraction():
    """This function is used to extract all csv, json and xml file and unite them into one file"""
    extracted_data = pd.DataFrame(
        columns=["car_model", "year_of_manufacture", "price", "fuel"]
    )
    log = etl_event()
    # Retrive all csv file
    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True
        )
    # Retrieve all json file
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_json(jsonfile))],
            ignore_index=True,
        )
    # Retrieve all xml file
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True
        )

    # return a file that has all data from csv, json and xml
    log.extraction_event()
    return extracted_data


# Transform data to specified internal standard, in case we need to round the price
def transform(extracted_data):
    """Transform extracted data to specified internal standard, in case we need to round the price"""
    log = etl_event()
    # Round the price to two decimals
    extracted_data["price"] = round(extracted_data.price, 2)
    unname_column = extracted_data.columns[
        extracted_data.columns.str.contains("Unnamed ")
    ]
    extracted_data.drop(unname_column, inplace=True)
    log.transform_event()
    return extracted_data


def load(unifiedDataFile, transformedDF):
    log = etl_event()
    transformedDF.to_csv(unifiedDataFile)
    log.loading_event()


# Testing
data = extraction()
transform(data)
# print(data)
load(unifiedDataFile, data)
df = pd.read_csv(unifiedDataFile)
print(df)

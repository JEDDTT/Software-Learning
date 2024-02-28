import pandas as pd
import xml.etree.ElementTree as ET

xmlfile = "used_car_prices1.xml"


def extract_from_xml(xmlfile):
    """This funciton serves to read xml file"""
    df = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for car in root:
        model = car.find("car_model").text
        year = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        row = pd.DataFrame(
            {
                "car_model": model,
                "year_of_manufacture": year,
                "price": price,
                "fuel": fuel,
            }
        )
        df = pd.concat(
            [df, row],
            ignore_index=True,
        )
    return df


data = extract_from_xml(xmlfile)
print(data)

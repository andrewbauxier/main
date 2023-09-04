"""
Project Name:   
Module Name:    
Author:         Andrew Auxier
Company:        UMGC, SDEV 300 6383 Building Secure Python Applications (2235) 
Description: 

    This project serves several functions as listed below:
"""
import pandas

POP_DATA_FILE = "data/PopChange.csv"
HOUSING_DATA_FILE = "data/Housing.csv"


def load_population_data():
    """Loads CSV"""
    return pandas.read_csv(POP_DATA_FILE)


def load_housing_data():
    """Loads CSV"""
    return pandas.read_csv(HOUSING_DATA_FILE)

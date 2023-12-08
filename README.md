# DAB111 Group Project - Google Play Store Data

## Overview

This repository contains the Python code for the DAB111 group project, focusing on Google Play Store data. The project involves collecting, processing, and presenting data through a Flask website. The data is stored in an SQLite database.

## Project Structure

- **main folder**
  - **data processing**
    - refer the [data_processing.ipynb](https://github.com/KarthikeyanBaskaran/DAB111_Final_Project_Group_4/blob/main/data_processing.ipynb) file
  - **database**
    - refer to the [database.ipynb](https://github.com/KarthikeyanBaskaran/DAB111_Final_Project_Group_4/blob/main/database.ipynb) file
  - **website**
    - refer to the [website.py](https://github.com/KarthikeyanBaskaran/DAB111_Final_Project_Group_4/blob/main/website.py) file
  - **requirements.txt**
    - Find a list of necessary packages for running the code in [requirements.txt](https://github.com/KarthikeyanBaskaran/DAB111_Final_Project_Group_4/blob/main/requirements.txt) file

## Data Processing

The Google Play Store dataset is processed and loaded into an SQLite database named "AppDB.db."

## Flask Website

The Flask website serves the data from the SQLite database and includes three main routes:

- `/`: Homepage
- `/about`: About page
- `/data`: Data page displaying Google Play Store data.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the main folder.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Execute the Flask application by running `python website.py` in the terminal.

Access the website at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).


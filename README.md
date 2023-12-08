# DAB111 Group Project - Google Play Store Data

## Overview

This repository contains the Python code for the DAB111 group project, focusing on Google Play Store data. The project involves collecting, processing, and presenting data through a Flask website. The data is stored in an SQLite database.

## Project Structure

- **main folder**
  - **data processing**
    - *Include any scripts or notebooks related to data processing.*
  - **database**
    - *Scripts for creating the SQLite database and inserting data.*
  - **website**
    - *Flask application and related files.*
  - **Readme.md**
    - *Project description and setup instructions.*
  - **requirements.txt**
    - *List of necessary packages for running the code.*

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
4. Execute the Flask application by running `python app.py` in the terminal.

Access the website at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).


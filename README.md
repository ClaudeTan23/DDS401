# Data and AI Essentials – Retail Sales Data Analysis

## Overview

This project demonstrates the use of **Python and NumPy** for basic data processing and analysis of retail sales data.

The project is developed as part of the **Data and AI Essentials** assignment. The dataset represents a small retail organisation and contains information about products, prices, quantities sold, stock levels, and discounts.

The analysis focuses on using data processing techniques to support **retail sales and inventory planning**.

## Project Objectives

The objectives of this project are to:

- Read and process a retail sales dataset using Python.
- Identify and use appropriate Python data types.
- Create and manipulate NumPy arrays.
- Create and process two-dimensional NumPy arrays.
- Apply NumPy universal functions for numerical calculations.
- Sort retail products based on sales quantity.
- Interpret the results in relation to retail sales and inventory planning.

## Project Structure

```text
Assignment1/
│
├── data/
│   └── retail_sales_data.csv
│
├── src/
│   ├── 01_read_data.py
│   ├── 02_data_types.py
│   ├── 03_numpy_array.py
│   ├── 04_2d_array.py
│   ├── 05_numpy_computation.py
│   └── 06_sorting.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Dataset

The dataset is stored in:

```text
data/retail_sales_data.csv
```

It contains the following attributes:

| Attribute | Description |
|---|---|
| `Product_ID` | Unique identifier for each product |
| `Category` | Product category |
| `Price` | Product price |
| `Quantity_Sold` | Quantity sold |
| `Stock_Level` | Current stock level |
| `Discount_Percent` | Discount percentage applied |

## Requirements

- Python 3.14 or compatible Python 3.x version
- NumPy

Python's built-in `csv` module is used to read the CSV file.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ClaudeTan23/DDS401.git
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows Command Prompt:

```bash
venv\Scripts\activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Programs

The Python files are located in the `src` directory.

Navigate to the `src` directory:

```bash
cd src
```

Then run each program individually.

### 1. Read Data

```bash
python 01_read_data.py
```

This program reads the CSV dataset using Python's `csv` module and displays the stored retail data.

### 2. Variables and Data Types

```bash
python 02_data_types.py
```

This program demonstrates:

- String variables
- Integer variables
- Floating-point variables
- Conversion of CSV values into appropriate Python data types

### 3. NumPy Array

```bash
python 03_numpy_array.py
```

This program creates a one-dimensional NumPy array containing the quantity sold for each product.


### 4. Two-Dimensional NumPy Array

```bash
python 04_2d_array.py
```

### 5. NumPy Computation

```bash
python 05_numpy_computation.py
```

This program demonstrates NumPy universal functions and calculations such as:

- Multiplication
- Sum
- Mean
- Maximum
- Minimum

### 6. Sorting

```bash
python 06_sorting.py
```

This program sorts products according to their quantity sold from highest to lowest.


## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| NumPy | Numerical computing and array operations |
| CSV | Dataset storage |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Source code repository |
# Assignment 2 – Retail Sales Data Analysis

## 1. Project Overview

This project focuses on analysing retail transaction data using Python. It uses the Online Retail II dataset from the UCI Machine Learning Repository to demonstrate data loading, data inspection, data cleaning, data manipulation, exploratory data analysis and data visualisation.

The project consists of individual Python scripts and a Jupyter Notebook. The Python scripts demonstrate different data analysis techniques, while the notebook provides technical documentation, Python code, corresponding outputs, explanations, findings and recommendations.

The main objective is to transform raw retail transaction data into meaningful information that can support business decision-making.

## 2. Project Objectives

* Load and inspect retail transaction data.
* Examine dataset structure, column names and data types.
* Identify missing values and duplicate records.
* Clean and prepare the dataset for analysis.
* Apply indexing, selection and data transformation techniques.
* Combine datasets and create pivot tables.
* Perform exploratory data analysis (EDA).
* Analyse sales trends and product performance.
* Create visualisations using Matplotlib.
* Interpret analytical findings and provide recommendations.
* Document the complete analysis in a Jupyter Notebook.

## 3. Dataset Description

**Dataset:** Online Retail II

**Source:** UCI Machine Learning Repository

**Dataset URL:** https://archive.ics.uci.edu/dataset/502/online+retail+ii

The Online Retail II dataset contains historical transaction records from a UK-based online retailer covering the period from 1 December 2009 to 9 December 2011.

### Main Variables

| Variable      | Description                      |
| ------------- | -------------------------------- |
| `InvoiceNo`   | Invoice or transaction number    |
| `StockCode`   | Product identification code      |
| `Description` | Product description              |
| `Quantity`    | Number of units purchased        |
| `InvoiceDate` | Date and time of the transaction |
| `UnitPrice`   | Price per unit                   |
| `CustomerID`  | Customer identification number   |
| `Country`     | Customer's country               |

The dataset is provided in Excel format and stored in the `data/` directory. It is used by the Python scripts and Jupyter Notebook for data preparation and analysis.

## 4. Project Structure

```text
Assignment2/
├── data/
│   └── online_retail_II.xlsx
├── notebooks/
│   └── Part_E_Technical Documentation.ipynb
├── outputs/
├── src/
│   ├── 01_load_inspect.py
│   ├── 02_examine_structure.py
│   ├── 03_clean_data.py
│   ├── 04_index_selection.py
│   ├── 05_transform_data.py
│   ├── 06_combine_datasets.py
│   ├── 07_pivot_table.py
│   ├── 08_exploratory_analysis.py
│   ├── 09_line_plot.py
│   ├── 10_scatter_plot.py
│   ├── 11_histogram.py
│   ├── 12_bar_chart.py
│   └── 13_combined_visualizations.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Directory and File Descriptions

| Directory/File     | Description                                                                   |
| ------------------ | ----------------------------------------------------------------------------- |
| `data/`            | Contains the original retail transaction dataset.                             |
| `notebooks/`       | Contains the Jupyter Notebook for Part E technical documentation.             |
| `outputs/`         | Stores generated charts, summaries and other analysis results, if configured. |
| `src/`             | Contains the individual Python scripts for data processing and analysis.      |
| `venv/`            | Local Python virtual environment used during development.                     |
| `.gitignore`       | Specifies files and directories that Git should ignore.                       |
| `README.md`        | Provides project information and setup instructions.                          |
| `requirements.txt` | Lists the Python packages required to run the project.                        |



## 5. Python Scripts

The `src/` directory organises the project into smaller scripts, with each script focusing on a specific data analysis operation.

| Script                          | Description                                                         |
| ------------------------------- | ------------------------------------------------------------------- |
| `01_load_inspect.py`            | Loads the dataset and displays an initial preview.                  |
| `02_examine_structure.py`       | Examines the dataset structure, columns and data types.             |
| `03_clean_data.py`              | Cleans the dataset according to the defined criteria.               |
| `04_index_selection.py`         | Demonstrates indexing and selecting rows or columns.                |
| `05_transform_data.py`          | Performs data transformations and creates derived variables.        |
| `06_combine_datasets.py`        | Combines relevant datasets or data subsets.                         |
| `07_pivot_table.py`             | Summarises data using pivot tables.                                 |
| `08_exploratory_analysis.py`    | Performs exploratory data analysis and summary calculations.        |
| `09_line_plot.py`               | Creates a line plot to examine trends over time.                    |
| `10_scatter_plot.py`            | Creates a scatter plot to examine relationships between variables.  |
| `11_histogram.py`               | Visualises the distribution of numerical data.                      |
| `12_bar_chart.py`               | Compares categories using a bar chart.                              |
| `13_combined_visualizations.py` | Combines multiple visualisations for comparison and interpretation. |

## 6. Technologies Used

* **Python** – Main programming language.
* **Pandas** – Data loading, cleaning, manipulation and aggregation.
* **NumPy** – Numerical operations and array processing.
* **Matplotlib** – Data visualisation.
* **Jupyter Notebook** – Interactive technical documentation and presentation.
* **openpyxl** – Excel file reading support for Pandas.

## 7. Installation and Setup

### Prerequisites

Ensure that Python and Git are installed on your computer.

### Step 1: Clone the Repository

### Step 2: Create a Virtual Environment

Create an isolated Python environment for the project.

```bash
python -m venv venv
```

Activate the environment on Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

Alternatively, activate it using Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

Install the required Python packages from `requirements.txt`.

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Prepare the Dataset

Download the Online Retail II dataset from the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

Place the downloaded Excel file in the `data/` directory and ensure that its filename is:

```text
online_retail_II.xlsx
```

Check that the worksheet names and file paths in the Python scripts match the downloaded dataset.

### Step 5: Run the Python Scripts

Execute the scripts from the project root directory so that relative file paths resolve correctly.

For example:

```bash
python src/01_load_inspect.py
python src/02_examine_structure.py
python src/03_clean_data.py
python src/04_index_selection.py
python src/05_transform_data.py
python src/06_combine_datasets.py
python src/07_pivot_table.py
python src/08_exploratory_analysis.py
python src/09_line_plot.py
python src/10_scatter_plot.py
python src/11_histogram.py
python src/12_bar_chart.py
python src/13_combined_visualizations.py
```

Each script may require input files or intermediate results produced by earlier scripts. Run them in the appropriate order and confirm that the required paths and dependencies are available.

### Step 6: Open the Jupyter Notebook

From the project root directory, start Jupyter Notebook:

```bash
jupyter notebook
```

Open the following notebook:

```text
notebooks/Part_E_Technical Documentation.ipynb
```

Execute the notebook cells in order to reproduce the analysis, view the corresponding outputs and review the explanations and findings.


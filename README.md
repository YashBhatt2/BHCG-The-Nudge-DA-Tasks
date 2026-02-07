# Water Quality Analysis & Employee Data Tasks

Set of scripts for data processing, ML classification, and database integration for the club project. 

## 1. Prerequisites
- Python 3.10+
- MySQL Server
- Virtualenv (recommended)

## 2. Installation
Clone the repo and install the requirements via pip.

we'll set up a virtual environment, and then install pandas in it. because many times installs conflict with global permissions on users' computers. Many times projects require different versions of dependencies, so thats why this is a requirement.
but it should run fine on any system with pandas
```bash
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt
'''

### TASK- 1:
once the data set is fixed, with the target variable given for some part of the data, I will implement the Gaussian naive bayes algorithm. ( Right now i dont have i dont have data to train the model on ).

### TASK - 2:
As per the task, I made a commented program that replaces all NaNs in the salary column with the department-wise median.

***Why is Grouped Imputation better than Global Imputation?***
IN a company people are paid differently in each department, if we replace all null values to the median of the entire slary column,    we will underestimate the salary of a Project Mangager and overestimate the salary of a janitor,
so thats why I took the median of the salary department wise, that way the null values will be replaced more accurately

###TASK -3:
I first converted the timestamp from string to date-time so that i can sort by it as mentioned in the task, then i found and counted the number of duplicates in transaction id, stored it in a series, so that i can just give the length of series to tell how many duplicates there were, this wasnt in the task but it seems like valuable info. then i sorted the dataframe according to timestamp and removed all duplicates except the last.

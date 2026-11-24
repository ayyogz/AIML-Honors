# AIML Honors Assignments - Revised from Student Repository Comparison

These five programs were rewritten using recurring ideas found in the submitted student repositories. They are original implementations, not copied files.

## Assignment overview

1. **Assignment 1 - Multi-Gateway Payment Processing:** Abstract payment method, Razorpay and Stripe payment classes, separate payment factories, aggregator classes, gateway factory, Card/UPI selection, and processing fee (2% Razorpay / 2.9% Stripe).
2. **Assignment 2 - Pandas + CSV Employee CRUD:** Uses a Pandas DataFrame and `employee.csv` to add, display, search, update and delete employee records.
3. **Assignment 3 - SQLite Employee CRUD:** Uses an `Employee` class and SQLite table to add, display, search, update and delete employee records.
4. **Assignment 4 - Pandas + SQLite Employee CRUD:** Uses Pandas `DataFrame`, `to_sql()` and `read_sql()` with an SQLite employee table. SQL is used for update/delete.
5. **Assignment 5 - Output Decorator:** Shows the output decorator with both a function that does not return a value and one that returns a value.

## Requirements

- Python 3
- Assignment 2 and 4: `pip install pandas`
- Assignment 1, 3 and 5: Python standard library only

## Run

Run each file from its own assignment folder:
`python filename.py`

The CSV and database files are created automatically in the current working directory.

## Comparison notes

Repositories inspected included:
- AlhamdaSadiq/AIML-HONORS
- DiyaJambhulkar/AIML_HONOR
- 25banerjees-beep/AIML-HONOUR
- trisha10-ui/AIML-HONOR
- toshita-nawaghare/Honors_Assignments
- 25katrea-maker/Assignments
- vermabhavika1910-lab/Aiml_Honour
- Rhea07895/AIML-HONOUR
- 25manear-sys/AIML-HONOR
- 16prasiddhi/16prasiddhi-Prasiddhi-Tawani-AIML-Assignment

The most repeated patterns were the payment factory hierarchy; menu-driven employee CRUD; Pandas/CSV; SQLite; and the output decorator. Assignment 3 was most commonly SQLite in the inspected sample. Assignment 4 varied between Pandas/CSV, Pandas+SQLite, and MySQL, so this version follows the Pandas+SQLite approach found in multiple submissions. Check the instructor's exact Assignment 4 wording before final submission.

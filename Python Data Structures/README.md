# Python Data Structures — University of Michigan (Coursera)

This repository contains my programming assignments and exercises from the course **Python Data Structures**, part of the **Python for Everybody Specialization** offered by the University of Michigan on Coursera.  

Course link:    
https://www.coursera.org/learn/python-data  

The course focuses on using Python built-in data structures to process and analyze data from files and structured text sources.  

---  

# Repository Structure

Python Data Structures  
│  
├── Assignment6.5.py  
├── Assignment7.1.py  
├── Assignment7.2.py  
├── Assignment8.4.py  
├── Assignment9.4.py  
├── Assignment10.2.py  
└── README.md

Each script corresponds to a programming assignment from the course.  

---  

# Course Overview

**Python Data Structures** introduces the core data structures of the Python programming language and demonstrates how they can be used to perform increasingly complex data analysis tasks.  

Key topics include:  

- Reading and processing data from files  
- String manipulation  
- Lists and loops  
- Dictionaries for frequency counting  
- Tuples for sorting structured data  
- Basic error handling  

These concepts are fundamental for data processing and serve as a foundation for later courses in web data access and database programming.  

---  

# Assignments

## Assignment 6.5 — Word Frequency Counter

This program reads a text file and counts how often each word appears.  

Key features:  

- File reading  
- String splitting  
- Dictionary frequency counting  

Example concept:  

```python
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

---

## Assignment 7.1 — Division with Error Handling

This script demonstrates Python exception handling.

Features:

- User input

- Numeric conversion

- Handling invalid input using `try / except`

Example concept:

```python
try:  
    result = int(a) / int(b)  
except:  
    print("Invalid input")
```

---

## Assignment 7.2 — File Reader (Uppercase)

This program:

1. Prompts the user for a filename

2. Opens the file

3. Prints each line in uppercase

Concepts practiced:

- File I/O

- String transformation

- Iteration through file objects

---

## Assignment 8.4 — Email Domain Counter

Processes a mailbox file and extracts email addresses from lines starting with `"From "`.

The program:

- Extracts the email address

- Counts occurrences of each domain

Concepts demonstrated:

- String parsing

- Dictionaries

- Data aggregation

---

## Assignment 9.4 — Word Frequency Analysis

This program analyzes word usage in a text file.

Steps:

1. Read the file

2. Normalize words

3. Count occurrences using dictionaries

4. Display results

Key learning points:

- Text processing

- Dictionary operations

- Loop-based aggregation

---

## Assignment 10.2 — Most Prolific Email Sender

This assignment analyzes a mailbox dataset to determine which email address sent the most messages.

Steps:

1. Read mailbox file line by line

2. Identify lines beginning with `"From "`

3. Extract email addresses

4. Count frequency with a dictionary

5. Find the email with the maximum count

Example logic:

```python
bigcount = None  
bigword = None

for word, count in counts.items():  
 if bigcount is None or count > bigcount:  
 bigword = word  
 bigcount = count
```

Output example:

`cwen@iupui.edu 5`

---

# Skills Demonstrated

This project demonstrates several core programming concepts.

### Python Fundamentals

- Variables and expressions

- Conditional statements

- Loops

### Data Structures

- Lists

- Dictionaries

- Tuples

### File Processing

- Reading text files

- Parsing structured text

- Processing log-style data

### Error Handling

- Handling invalid input

- Preventing runtime errors

---

# Technologies Used

- Python 3

- Standard Python libraries

- Text file processing

---

# Running the Programs

Example:

`python Assignment10.2.py`

Some assignments require input files such as:

`mbox-short.txt`

Make sure the data file is located in the same directory as the Python script.

---

# Related Courses in the Specialization

This course is part of the **Python for Everybody Specialization**, which includes:

1. Programming for Everybody (Getting Started with Python)

2. Python Data Structures

3. Using Python to Access Web Data

4. Using Databases with Python

5. Capstone: Retrieving, Processing, and Visualizing Data with Python

The specialization introduces programming fundamentals and progresses toward web data processing and database applications.

---

# Author

**GitHub:**  
[yangzkang · GitHub](https://github.com/yangzkang)

This repository documents my learning progress in Python programming and data processing.

# Python Data Structures Course Projects

**Course:** Python Data Structures  
**Specialization:** Python for Everybody  
**University:** University of Michigan  
**Platform:** Coursera

---

## Overview

**Python Data Structures** is a course in the *Python for Everybody Specialization* offered by the University of Michigan on Coursera.

The course introduces the core data structures of the Python programming language and builds on basic procedural programming concepts. It focuses on using built-in data structures such as **lists, dictionaries, and tuples**, along with **file operations and text processing**.

Through a series of programming assignments, the course emphasizes:

- Reading and processing text files

- Organizing data using Python data structures

- Writing programs that analyze structured and semi-structured data

- Handling runtime errors gracefully

This repository contains my solutions to selected programming assignments completed during the course.

---

# Completed Assignments

## Assignment 6.5 — Word Frequency Count

Reads a text file, splits each line into words, and counts how often each word appears.

The program:

- Parses the file line by line

- Splits lines into individual words

- Uses a dictionary to store word frequencies

- Outputs the most common words and their counts

This exercise demonstrates **string processing, loops, and dictionary-based data aggregation**.

---

## Assignment 7.1 — Division with Error Handling

Prompts the user for two numbers and computes their quotient.

The program uses `try/except` to handle:

- Invalid numeric input

- Division by zero errors

Concepts demonstrated:

- Basic arithmetic operations

- Input conversion (`int` / `float`)

- Python exception handling

---

## Assignment 7.2 — File Reader (Uppercase)

Prompts the user for a filename, opens the file, and reads its contents.

The program:

- Reads the file line by line

- Converts each line to uppercase

- Prints the result to the console

Concepts demonstrated:

- File I/O (`open`, `read`)

- Looping through file lines

- String transformation (`upper()`)

---

## Assignment 8.x — Email Domain Counter

Processes a mailbox file and extracts the sender’s email domain (the part after `@`).

The program:

- Reads each line of the mailbox file

- Extracts email addresses

- Splits the domain from the address

- Uses a dictionary to count occurrences

Concepts demonstrated:

- String splitting

- Text parsing

- Dictionary counting

---

## Assignment 9.4 — Structured Data Parsing

Reads structured data (such as JSON or formatted text) and counts specific elements.

Typical tasks include:

- Parsing JSON structures

- Extracting values

- Counting occurrences of specific items

Concepts demonstrated:

- Working with structured data

- Data extraction

- Iteration over nested structures

---

## Assignment 10.2 — Most Prolific Email Sender

This assignment processes a mailbox file such as `mbox-short.txt`.

The program:

1. Reads the mailbox file line by line

2. Identifies lines starting with `"From "`

3. Extracts the sender’s email address

4. Counts the number of messages sent by each address using a dictionary

5. Finds and prints the email address with the highest message count

Concepts demonstrated:

- Text parsing

- Dictionary frequency counting

- Iterating over key-value pairs

- Finding the maximum value in a dataset

---

# Technical Skills Demonstrated

These projects highlight core Python skills and fundamental computer science concepts.

## File I/O

Opening and reading text files line by line using:

`open()`
`for line in file`

Used in nearly every assignment, including reading email logs and word lists.

---

## String Processing

Common operations include:

- Splitting lines into words (`split()`)

- Converting text (`upper()`)

- Extracting substrings (such as domains after `@`)

---

## Data Structures

Key Python data structures used:

- **Lists** — collecting and sorting items

- **Dictionaries** — counting frequencies using key/value pairs

- **Tuples** — sometimes used when sorting dictionary items

---

## Control Flow

Programs rely on:

- Loops (`for`, `while`)

- Conditional statements (`if`)

- Error handling (`try / except`)

These control structures allow programs to process files, analyze data, and produce meaningful output.

---

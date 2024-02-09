### tabulato

`tabulato` is a Python package that provides functionality for generating tabulated representations of data with customizable colors and formatting options. It offers a user-friendly interface for creating visually appealing tables in terminal output.

With `tabulato`, you can easily format your data into tables with specified headers, apply different colors to headers and rows, and customize the appearance of your tabulated data. Whether you're working on command-line applications, data analysis scripts, or any other project that requires presenting data in a tabular format, `tabulato` can help streamline the process and enhance the visual presentation of your data.

### Table of Contents

- [tabulato](#tabulato)
- [Table of Contents](#table-of-contents)
- [Key features of tabulato include:](#key-features-of-tabulato-include)
- [Installation](#installation)
- [Example](#example)
  - [Arguments](#arguments)
  - [Defaults](#defaults)
  - [Types](#types)
  - [Description](#description)

### Key features of tabulato include:

- Generating tables with customizable colors for headers, even rows, and odd rows.
- Specifying required columns to ensure important data is always displayed.
- Option to make headers bold for emphasis.
- User-friendly API for straightforward integration into your Python projects.

> tabulato simplifies the task of formatting and presenting tabular data in terminal environments, making it an essential tool for developers and data scientists working with command-line interfaces.

### Installation

To install tabulato, you can use pip:

```bash
pip install tabulato
```

### Example

In the following examples shows you how you can use

```py
from tabulato import colorful_tabulate

headers = ["Name", "Student Number", "DOB", "Email Address"]

data = [
    ["John Doe", "S12345", "1995-07-15", "john@example.com"],
    ["Alice Smith", "S67890", "1998-03-22", "alice@example.com"],
    ["Bob Johnson", "S54321", "1997-11-10", "bob@example.com"],
    ["Emma Brown", "S98765", "1996-09-18", "emma@example.com"],
    ["Michael Lee", "S24680", "1999-05-30", "michael@example.com"],
    ["Sophia Wang", "S13579", "1994-12-05", "sophia@example.com"],
    ["David Chen", "S75310", "1992-04-08", "david@example.com"],
    ["Olivia Kim", "S36924", "1993-10-25", "olivia@example.com"],
]

colorful_tabulate(headers=headers, data=data, colorful=True, bold_header=True)
```

```shell
+-------------+----------------+------------+---------------------+
| Name        | Student Number | DOB        | Email Address       |
+-------------+----------------+------------+---------------------+
| John Doe    | S12345         | 1995-07-15 | john@example.com    |
| Alice Smith | S67890         | 1998-03-22 | alice@example.com   |
| Bob Johnson | S54321         | 1997-11-10 | bob@example.com     |
| Emma Brown  | S98765         | 1996-09-18 | emma@example.com    |
| Michael Lee | S24680         | 1999-05-30 | michael@example.com |
| Sophia Wang | S13579         | 1994-12-05 | sophia@example.com  |
| David Chen  | S75310         | 1992-04-08 | david@example.com   |
| Olivia Kim  | S36924         | 1993-10-25 | olivia@example.com  |
+-------------+----------------+------------+---------------------+
```

The `colorful_tabulate` is a useful function for visually enhancing tabulated data in terminal output by applying colors and styling.

#### Arguments

| Argument           | Type            | Default    | Description                                                       |
| ------------------ | --------------- | ---------- | ----------------------------------------------------------------- |
| `headers`          | `list[str]`     |            | A list of strings representing the headers of the table.          |
| `data`             | `list[list]`    |            | A list of lists representing the data rows of the table.          |
| `required_columns` | `list[str]`     |            | A list of strings representing the required columns in the table. |
| `colorful`         | `bool`          | `True`     | A boolean indicating whether to colorize the output.              |
| `bold_header`      | `bool`          | `True`     | A boolean indicating whether to make the header bold.             |
| `header_color`     | `COLOR_LITERAL` | `"BLUE"`   | The color of the header.                                          |
| `even_row_color`   | `COLOR_LITERAL` | `"GREEN"`  | The color of even-numbered rows.                                  |
| `odd_row_color`    | `COLOR_LITERAL` | `"YELLOW"` | The color of odd-numbered rows.                                   |

#### Defaults

- `colorful`: `True`
- `bold_header`: `True`
- `header_color`: `"BLUE"`
- `even_row_color`: `"GREEN"`
- `odd_row_color`: `"YELLOW"`

#### Types

- `list[str]`: List of strings
- `list[list]`: List of lists
- `bool`: Boolean
- `COLOR_LITERAL`: String representing color (e.g., `"BLUE"`, `"GREEN"`, `"YELLOW"`)

#### Description

The `colorful_tabulate` function generates a tabulated representation of data with customizable colors and formatting options. It takes the following arguments:

- `headers`: A list of strings representing the headers of the table.
- `data`: A list of lists representing the data rows of the table.
- `required_columns`: A list of strings representing the required columns in the table.
- `colorful` (optional, default=`True`): A boolean indicating whether to colorize the output.
- `bold_header` (optional, default=`True`): A boolean indicating whether to make the header bold.
- `header_color` (optional, default=`"BLUE"`): The color of the header.
- `even_row_color` (optional, default=`"GREEN"`): The color of even-numbered rows.
- `odd_row_color` (optional, default=`"YELLOW"`): The color of odd-numbered rows.

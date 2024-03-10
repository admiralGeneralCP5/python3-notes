
## Table of Contents:

1. [Tabulate](#tabulate)
2. [Pretty Table](#pretty-table)
3. [Table 2 ASCII](#table-2-ascii)
4. [Table 2 ASCII with Headers](#table-2-ascii-with-headers)

<br>

## Tabulate

[PyPi Documentation](https://pypi.org/project/tabulate/)

Install command:
```
pip install tabulate
```

Example code:
```py
from tabulate import tabulate

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # x values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # y values

combined = []
for number in numbers:
    row = []
    for letter in letters:
        combined_value = str(number) + letter
        row.append(combined_value)
    combined.append(row)


print(tabulate(combined, tablefmt="rounded_grid"))
```

Output:
```txt
╭─────┬─────┬─────┬─────┬─────┬─────┬─────╮
│ 1A  │ 1B  │ 1C  │ 1D  │ 1E  │ 1F  │ 1G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2A  │ 2B  │ 2C  │ 2D  │ 2E  │ 2F  │ 2G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3A  │ 3B  │ 3C  │ 3D  │ 3E  │ 3F  │ 3G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4A  │ 4B  │ 4C  │ 4D  │ 4E  │ 4F  │ 4G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5A  │ 5B  │ 5C  │ 5D  │ 5E  │ 5F  │ 5G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6A  │ 6B  │ 6C  │ 6D  │ 6E  │ 6F  │ 6G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 7A  │ 7B  │ 7C  │ 7D  │ 7E  │ 7F  │ 7G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 8A  │ 8B  │ 8C  │ 8D  │ 8E  │ 8F  │ 8G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 9A  │ 9B  │ 9C  │ 9D  │ 9E  │ 9F  │ 9G  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 10A │ 10B │ 10C │ 10D │ 10E │ 10F │ 10G │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 11A │ 11B │ 11C │ 11D │ 11E │ 11F │ 11G │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 12A │ 12B │ 12C │ 12D │ 12E │ 12F │ 12G │
╰─────┴─────┴─────┴─────┴─────┴─────┴─────╯
```

---

<br>

## Pretty Table

[PyPi Documentation](https://pypi.org/project/prettytable/)

Install Command:
```
pip install prettytable
```

Example Code:
```py
from prettytable import PrettyTable

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # x values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # y values

combined = []
for number in numbers:
    row = []
    for letter in letters:
        combined_value = str(number) + letter
        row.append(combined_value)
    combined.append(row)


table = PrettyTable()
table.add_rows(combined)
print(table)
```

Output:
```txt
+---------+---------+---------+---------+---------+---------+---------+
| Field 1 | Field 2 | Field 3 | Field 4 | Field 5 | Field 6 | Field 7 |
+---------+---------+---------+---------+---------+---------+---------+
|    1A   |    1B   |    1C   |    1D   |    1E   |    1F   |    1G   |
|    2A   |    2B   |    2C   |    2D   |    2E   |    2F   |    2G   |
|    3A   |    3B   |    3C   |    3D   |    3E   |    3F   |    3G   |
|    4A   |    4B   |    4C   |    4D   |    4E   |    4F   |    4G   |
|    5A   |    5B   |    5C   |    5D   |    5E   |    5F   |    5G   |
|    6A   |    6B   |    6C   |    6D   |    6E   |    6F   |    6G   |
|    7A   |    7B   |    7C   |    7D   |    7E   |    7F   |    7G   |
|    8A   |    8B   |    8C   |    8D   |    8E   |    8F   |    8G   |
|    9A   |    9B   |    9C   |    9D   |    9E   |    9F   |    9G   |
|   10A   |   10B   |   10C   |   10D   |   10E   |   10F   |   10G   |
|   11A   |   11B   |   11C   |   11D   |   11E   |   11F   |   11G   |
|   12A   |   12B   |   12C   |   12D   |   12E   |   12F   |   12G   |
+---------+---------+---------+---------+---------+---------+---------+
```

---

<br>

## Table 2 ASCII

[PyPi Documentation](https://pypi.org/project/table2ascii/)

[Additional Documentation](https://table2ascii.readthedocs.io/en/stable/)

Install Command:
```
pip install table2ascii
```

Example Code:
```py
from table2ascii import table2ascii

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # x values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # y values

combined = []
for number in numbers:
    row = []
    for letter in letters:
        combined_value = str(number) + letter
        row.append(combined_value)
    combined.append(row)


print(table2ascii(body=combined))
```

Output:
```txt
╔═════════════════════════════════════════╗
║ 1A    1B    1C    1D    1E    1F    1G  ║
║ 2A    2B    2C    2D    2E    2F    2G  ║
║ 3A    3B    3C    3D    3E    3F    3G  ║
║ 4A    4B    4C    4D    4E    4F    4G  ║
║ 5A    5B    5C    5D    5E    5F    5G  ║
║ 6A    6B    6C    6D    6E    6F    6G  ║
║ 7A    7B    7C    7D    7E    7F    7G  ║
║ 8A    8B    8C    8D    8E    8F    8G  ║
║ 9A    9B    9C    9D    9E    9F    9G  ║
║ 10A   10B   10C   10D   10E   10F   10G ║
║ 11A   11B   11C   11D   11E   11F   11G ║
║ 12A   12B   12C   12D   12E   12F   12G ║
╚═════════════════════════════════════════╝
```

---

<br>

## Table 2 ASCII with Headers

[PyPi Documentation](https://pypi.org/project/table2ascii/)

[Additional Documentation](https://table2ascii.readthedocs.io/en/stable/)

Install Command:
```
pip install table2ascii
```

Example Code:
```py
from table2ascii import table2ascii

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # x values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # y values

combined = []
for number in numbers:
    row = []
    for letter in letters:
        combined_value = str(number) + letter
        row.append(combined_value)
    combined.append(row)


letters_header = letters.copy()  # makes a copy of letters
letters_header.insert(0, '')  # inserts an empty string at the beginning

with_headers = combined[:]  # makes a copy of combined
for index, row in enumerate(with_headers):  # inserts the corresponding value in numbers to the beginning of each row
    row.insert(0, numbers[index])

print(table2ascii(body=with_headers, header=letters_header, first_col_heading=True))
```

Output:
```txt
╔════╦═════════════════════════════════════════╗
║    ║  A     B     C     D     E     F     G  ║
╟────╫─────────────────────────────────────────╢
║ 1  ║ 1A    1B    1C    1D    1E    1F    1G  ║
║ 2  ║ 2A    2B    2C    2D    2E    2F    2G  ║
║ 3  ║ 3A    3B    3C    3D    3E    3F    3G  ║
║ 4  ║ 4A    4B    4C    4D    4E    4F    4G  ║
║ 5  ║ 5A    5B    5C    5D    5E    5F    5G  ║
║ 6  ║ 6A    6B    6C    6D    6E    6F    6G  ║
║ 7  ║ 7A    7B    7C    7D    7E    7F    7G  ║
║ 8  ║ 8A    8B    8C    8D    8E    8F    8G  ║
║ 9  ║ 9A    9B    9C    9D    9E    9F    9G  ║
║ 10 ║ 10A   10B   10C   10D   10E   10F   10G ║
║ 11 ║ 11A   11B   11C   11D   11E   11F   11G ║
║ 12 ║ 12A   12B   12C   12D   12E   12F   12G ║
╚════╩═════════════════════════════════════════╝
```

# getable

Parse HTML table to a 2d-array-like data structure.

## Installation

```bash
pip install getable
```

## Example

```python
from getable import TableParser

html = """
<table id="table">
    <thead>
        <tr><th>Name</th><th>Age</th></tr>
    </thead>
    <tbody>
        <tr><td>Alpha</td><td>10</td></tr>
        <tr><td>Bravo</td><td>20</td></tr>
    </tbody>
</table>
"""
    
parser = TableParser()
table = parser.parse(source=html, locator="#table")
for row in table:
    for cell in row:
        print(cell.text)
```



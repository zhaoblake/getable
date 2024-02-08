# getable
<p>
<a href="https://github.com/zhaoblake/getable/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/zhaoblake/getable/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/zhaoblake/getable" > 
 <img src="https://codecov.io/gh/zhaoblake/getable/graph/badge.svg?token=E14F3M0CM9"/> 
 </a>
<a href="https://pypi.org/project/getable" target="_blank">
    <img src="https://img.shields.io/pypi/v/getable?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/getable" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/getable.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

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



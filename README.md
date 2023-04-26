# getable

A simple tool to parse HTML table to a 2d-array-like data structure.

## Installation

```bash
pip install getable
```

## Usage

Now we get a standard HTML table like below, let's see what we can do with getable.
<table id="standardTable">
        <thead>
        <tr>
            <th>House</th>
            <th>Region</th>
            <th>Seat</th>
            <th>Words</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>Targaryen</td>
            <td>Crownlands</td>
            <td>Dragonstone</td>
            <td>Fire and Blood</td>
        </tr>
        <tr>
            <td>Stark</td>
            <td>North</td>
            <td>Winterfell</td>
            <td>Winter is Coming</td>
        </tr>
        <tr>
            <td>Lannister</td>
            <td>Westerlands</td>
            <td>Casterly Rock</td>
            <td>Hear Me Roar</td>
        </tr>
        <tr>
            <td>Greyjoy</td>
            <td>Iron Islands</td>
            <td>Pyke</td>
            <td>We Do Not Sow</td>
        </tr>
        </tbody>
    </table>

```python
from getable import TableParser

source = """
<table id="standardTable">
    <thead>
        <tr><th>House</th><th>Region</th><th>Seat</th><th>Words</th></tr>
    </thead>
    <tbody>
        <tr><td>Targaryen</td><td>Crownlands</td><td>Dragonstone</td><td>Fire and Blood</td></tr>
        <tr><td>Stark</td><td>North</td><td>Winterfell</td><td>Winter is Coming</td></tr>
        <tr><td>Lannister</td><td>Westerlands</td><td>Casterly Rock</td><td>Hear Me Roar</td></tr>
        <tr><td>Greyjoy</td><td>Iron Islands</td><td>Pyke</td><td>We Do Not Sow</td></tr>
    </tbody>
</table>
"""

table_parser = TableParser()
table = table_parser.parse(source=source, locator="#standardTable")

print(table.head)  # House, Region, Seat, Words
print(table.head[0].text)  # House

print(table.body)
"""
Targaryen, Crownlands, Dragonstone, Fire and Blood
Stark, North, Winterfell, Winter is Coming
Lannister, Westerlands, Casterly Rock, Hear Me Roar
Greyjoy, Iron Islands, Pyke, We Do Not Sow
"""

print(table.body[-1][-1].text)  # We Do Not Sow
print(table[-1][-1].text)  # We Do Not Sow
```

## License

This project is licensed under the terms of the MIT license.



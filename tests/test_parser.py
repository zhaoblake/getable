import os
from functools import lru_cache

from getable.parser import TableParser


def test_parse_standard_table():
    table_parser = TableParser()
    table = table_parser.parse(source=get_source_html(), locator="#standardTable")
    assert len(table) == 4
    assert len(table.head) == 4
    assert len(table.body) == 4
    assert table.head[0].text == "House"
    assert table.head[1].text == "Region"
    assert table.head[2].text == "Seat"
    assert table.head[3].text == "Words"

    for row in table:
        assert len(row) == 4

    assert table[0][0].text == "Targaryen"
    assert table[1][1].text == "North"
    assert table[2][2].text == "Casterly Rock"
    assert table[3][3].text == "We Do Not Sow"

    assert str(table) == ("House, Region, Seat, Words\n"
                          "Targaryen, Crownlands, Dragonstone, Fire and Blood\n"
                          "Stark, North, Winterfell, Winter is Coming\n"
                          "Lannister, Westerlands, Casterly Rock, Hear Me Roar\n"
                          "Greyjoy, Iron Islands, Pyke, We Do Not Sow")


def test_ignore_invisible_rows():
    table_parser = TableParser(ignore_invisible_rows=False)
    table = table_parser.parse(get_source_html(), locator="#tableWithInvisibleRow")
    assert len(table) == 4

    table_parser = TableParser(ignore_invisible_rows=True)
    table = table_parser.parse(get_source_html(), locator="#tableWithInvisibleRow")
    assert len(table) == 2


def test_ignore_incomplete_rows():
    table_parser = TableParser(ignore_incomplete_rows=False)
    table = table_parser.parse(get_source_html(), locator="#tableWithIncompleteRow")
    assert len(table) == 4

    table_parser = TableParser(ignore_incomplete_rows=True)
    table = table_parser.parse(get_source_html(), locator="#tableWithIncompleteRow")
    assert len(table) == 2


def test_tbody_data_tag():
    table_parser = TableParser(tbody_data_tag="td>input")
    table = table_parser.parse(get_source_html(), locator="#tableWithTbodyInputDataTag")
    assert len(table) == 4

    for row in table:
        assert len(row) == 4

    assert table[0][0].text == "Targaryen"
    assert table[1][1].text == "North"
    assert table[2][2].text == "Casterly Rock"
    assert table[3][3].text == "We Do Not Sow"


@lru_cache(1)
def get_source_html() -> str:
    html_path = os.path.join(os.path.dirname(__file__), "resources", "table.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

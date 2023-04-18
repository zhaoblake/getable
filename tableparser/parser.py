from pyquery import PyQuery as PyqElement

from tableparser.models import (
    Table,
    TableBody,
    TableCell,
    TableContent,
    TableHead,
    TableRow,
)
from tableparser.utils import is_visible


class TableParser:
    def __init__(
        self,
        *,
        thead_tag: str = "thead",
        tbody_tag: str = "tbody",
        trow_tag: str = "tr",
        thead_data_tag: str = "th",
        tbody_data_tag: str = "td",
        ignore_invisible_rows: bool = True,
        ignore_incomplete_rows: bool = True,
    ):
        self.thead_tag = thead_tag
        self.tbody_tag = tbody_tag
        self.trow_tag = trow_tag
        self.thead_data_tag = thead_data_tag
        self.tbody_data_tag = tbody_data_tag
        self.ignore_invisible_rows = ignore_invisible_rows
        self.ignore_incomplete_rows = ignore_incomplete_rows

    def parse(self, source: str, locator: str) -> Table:
        table_element = PyqElement(source)
        if table_element[0].tag != "table":
            table_element = table_element.find(locator)

        thead_element = table_element.find(self.thead_tag)
        thead_locator = f"{locator}>{self.thead_tag}"
        head = TableHead(element=thead_element, locator=thead_locator, rows=[])
        self._parse_content(table_content=head, data_tag=self.thead_data_tag)

        tbody_element = table_element.find(self.tbody_tag)
        tbody_locator = f"{locator}>{self.tbody_tag}"
        body = TableBody(element=tbody_element, locator=tbody_locator, rows=[])
        self._parse_content(table_content=body, data_tag=self.tbody_data_tag)

        if self.ignore_invisible_rows:
            body.rows = [row for row in body.rows if is_visible(row.element)]

        if self.ignore_incomplete_rows:
            body.rows = [row for row in body.rows if len(row) >= len(head)]

        return Table(element=table_element, locator=locator, head=head, body=body)

    def _parse_content(self, table_content: TableContent, data_tag: str):
        row_elements = table_content.element.find(self.trow_tag).items()
        for row_index, row_element in enumerate(row_elements, start=1):
            row_locator = (
                f"{table_content.locator}>{self.trow_tag}:nth-child({row_index})"
            )
            row = TableRow(element=row_element, locator=row_locator, cells=[])

            cell_elements = row_element.find(data_tag).items()
            for cell_index, cell_element in enumerate(cell_elements, start=1):
                if not is_visible(cell_element):
                    continue

                cell_locator = f"{row_locator}>{data_tag}:nth-child({cell_index})"
                cell_text = cell_element.text() or cell_element.val()

                cell = TableCell(
                    element=cell_element, locator=cell_locator, text=cell_text
                )
                row.cells.append(cell)

            table_content.rows.append(row)

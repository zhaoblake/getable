import typing as t
from dataclasses import dataclass

from pyquery import PyQuery as PyqElement


@dataclass
class TableCell:
    element: PyqElement

    locator: str
    text: str

    def __repr__(self):
        return self.text


@dataclass
class TableRow:
    element: PyqElement

    locator: str
    cells: t.List[TableCell]

    def __getitem__(self, index):
        return self.cells[index]

    def __len__(self):
        return len(self.cells)

    def __repr__(self):
        return ", ".join([repr(cell) for cell in self.cells])


@dataclass
class TableContent:
    element: PyqElement

    locator: str
    rows: t.List[TableRow]

    def __getitem__(self, index):
        return self.rows[index]

    def __repr__(self):
        return "\n".join([repr(row) for row in self.rows])


class TableHead(TableContent):
    def __getitem__(self, index):
        return self.rows[0][index]

    def __len__(self):
        return len(self.rows[0])


class TableBody(TableContent):
    def __len__(self):
        return len(self.rows)


@dataclass
class Table:
    element: PyqElement

    locator: str
    head: TableHead
    body: TableBody

    def __len__(self):
        return len(self.body)

    def __getitem__(self, index):
        return self.body[index]

    def __repr__(self):
        return f"{self.head!r}\n{self.body!r}"

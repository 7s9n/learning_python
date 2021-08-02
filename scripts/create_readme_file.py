from abc import ABCMeta , abstractmethod
from enum import Enum


class Text:
    """Represents a base text tag"""
    def __init__(self , text):
        self._text = text

    def render(self):
        return self._text

class Cell:
    def __init__(self , wrapped):
        self._wrapper = wrapped

    @property
    def text(self):
        return self._wrapper.render()

    @text.setter
    def text(self , value):
        self._wrapper = Text(value)

    def render(self):
        return f" {self._wrapper.render()} |"

    def __str__(self):
        return f"{self.text}"

class Row:
    def __init__(self , row):
        self._cells = self.construct(row)

    def construct(self , row):
        r = []
        for content in row:
            r.append( self._construct_one_cell(content) )
        return r

    def _construct_one_cell(self , content):
        return Cell( Text( content ) )

    def append(self , data):
        return self._cells.append( self._construct_one_cell(data) )

    def render(self):
        return '|' + ''.join( c.render() for c in self._cells )

    def __len__(self):
        return len(self._cells)

    def __getitem__(self , idx):
        if not ( idx < len(self) ):
            raise IndexError('Index out of bound')
        return self._cells[idx]

class Header:
    class Alignment(Enum):
        LEFT_ALIGN = ':---'
        RIGHT_ALIGN = '---:'
        CENTER_ALIGN = ':---:'

    def __init__(self , columns):
        self._columns = Row(columns)

    def append(self , data):
        return self._columns.append(data)

    def render(self):
        header = self._columns.render() + '\n'
        header += Row([self.Alignment.CENTER_ALIGN.value]*len(self._columns)).render()
        return header

    def __len__(self):
        return len(self._columns)

class Body:
    def __init__(self , rows):
        self._rows = self.construct(rows)

    @property
    def rows(self):
        return self._rows

    def construct(self , rows):
        body = []
        for row in rows:
            body.append( Row( row ) )
        return body

    def append(self , row):
        self._rows.append( Row(row) )

    def render(self):
        return '\n'.join( r.render() for r in self._rows )

    def __iter__(self):
        idx = 0
        r_len = len(self._rows)
        while idx < r_len:
            yield self._rows[idx]
            idx += 1

    def __getitem__(self , idx):
        return self.rows[idx]


class Table:
    def __init__(self , columns , rows):
        self._header = Header(columns=columns)
        self._body = Body(rows=rows)

    @property
    def columns(self):
        return self._header

    @property
    def rows(self):
        return self._body

    def normalize(self):
        h_len = len(self._header)
        for row in self._body:
            r_len = len(row)
            if r_len < h_len:
                for _ in range(h_len - r_len):
                    row.append('')

    def render(self):
        return f"{self._header.render()}\n{self._body.render()}"

    def __getitem__(self , idx):
        return self.rows[idx]

class Emphasis(metaclass=ABCMeta):
    def __init__(self , wrapped):
        self._wrapper = wrapped

    @abstractmethod
    def render(self):
        pass

class BoldWrapper(Emphasis):
    def __init__(self , wrapped):
        super(BoldWrapper , self).__init__(wrapped)

    def render(self):
        return f"**{self._wrapper.render()}**"
class ItalicWrapper(Emphasis):
    def __init__(self , wrapped):
        super(ItalicWrapper , self).__init__(wrapped)

    def render(self):
        return f"*{self._wrapper.render()}*"


if __name__ == '__main__':
    c = ['Name' , 'Age' , 'Score']
    r = [
        ['Hussein' , 22 , 'non'] ,
        ['Moataz' , 21 , 'non'],
    ]
    table = Table(
        columns = c,
        rows = r,
    )
    table.columns.append('s')
    table.rows.append([0 , 2 , 3])
    table.normalize()
    print(table.render())

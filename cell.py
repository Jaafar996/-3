class GameCell:
    def __init__(self, cell_type='empty'):
        self.cell_type = cell_type  # 'empty', 'i', 'p', 'o', 'r', 'purple', 'gray'

    def __str__(self):
        if self.cell_type == 'empty':
            return '.'
        elif self.cell_type == 'i':
            return 'I'
        elif self.cell_type == 'p':
            return 'P'
        elif self.cell_type == 'o':
            return 'O'
        elif self.cell_type == 'r':
            return 'R'
        elif self.cell_type == 'purple':
            return 'U'
        elif self.cell_type == 'gray':
            return 'G'
        return ' '

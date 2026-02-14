class CellUpdateError(Exception):
    def __str__(self):
        return "Invalid attempt to modify the next or leap attribute!"

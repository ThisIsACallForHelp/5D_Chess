class TimeLine:
    """
    a specific timeline with a specific position 
    in a specific time in the universe
    """
    def __init__(self, TimeLineID, ParentID, CreationTurn, BoardToCopy):
        self.TimeLineID = TimeLineID
        self.ParentID = ParentID
        self.CreationTurn = CreationTurn
        self.BoardToCopy = BoardToCopy
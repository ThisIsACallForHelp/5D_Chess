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

    @classmethod
    def BuildTesseract(cls, TimeLineID, Position_String):
        instance = cls(timeline_id)
        Positions = Position_String.split("-")
        for x in range(4):
            for y in range(4):
                for z in range(4):

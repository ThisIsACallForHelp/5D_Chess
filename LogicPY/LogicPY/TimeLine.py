import pygame
class TimeLine:
    """
    a specific timeline with a specific position 
    in a specific time in the universe
    """
    def __init__(self, TimeLineID, ParentID, CreationTurn, BoardToCopy):
        self.TimeLineID = TimeLineID
        self.ParentID = ParentID
        self.CreationTurn = CreationTurn
        self.TesseractBoard = BoardToCopy

    @classmethod
    def BuildTesseract(self, TimeLineID, screen, Position_Dict = None):
        SQUARE_SIZE = 45
        BOARD_MARGIN = SQUARE_SIZE * 4 + 20 
        #each board is 4 by 4 squares, so the whole board is 180 pixels
        #and add a 20 pixel margin 
        self.TimeLineID = TimeLineID
        self.TesseractBoard = Position_Dict
        for w in range(4):
            for x in range(4):
                SquareCounter = 0
                for y in range(4):
                    for z in range(4):
                        x_axis_pixel = y * SQUARE_SIZE
                        y_axis_pixel = z * SQUARE_SIZE
                        BoardSquare = pygame.Rect(x_axis_pixel, y_axis_pixel, SQUARE_SIZE, SQUARE_SIZE)
                        color = (240, 217, 181) if (y + z) % 2 == 0 else (181, 136, 99)
                        pygame.draw.rect(screen, color, BoardSquare)
                        SquareCounter += 1


                    



                    
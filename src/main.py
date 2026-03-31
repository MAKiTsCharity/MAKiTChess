from tkinter import *
from data import Pieces
from PIL import ImageTk,Image
import math

from MoveSolver import validMoves, movePiece


turn = True
selectedPiece = -1
selectedValidMoves = []
# def CheckMove(move):




def updateBoard():
    for x in range(10):
        for y in range(10):
            colours = ["#aa6611","#d2aa99","#8b6f4d","#c7b8b2", "#da4070", "#ecd052"]
            canvas.create_rectangle((x*boardSize/10, y*boardSize/10), ((x+1)*boardSize/10, (y+1)*boardSize/10), fill=((colours[(x+y)%2] if (x%9) and (y%9) else colours[(x+y)%2+2]) if selectedPiece<0 else (colours[4] if x==Pieces[selectedPiece]["pos"][0] and y==Pieces[selectedPiece]["pos"][1] else (colours[(x+y)%2] if (x%9) and (y%9) else colours[(x+y)%2+2]))) if [x,y] not in selectedValidMoves else colours[5])

    for piece in Pieces:
        canvas.create_image(
        (boardSize/10*piece["pos"][0] + boardSize/20,boardSize/10*piece["pos"][1] + boardSize/20),
        image=pieceImages["".join([piece["piece"],"W" if piece["player"] else "B"])]
    )

def on_left_click(event):
    global selectedPiece
    global selectedValidMoves
    global turn
    global Pieces

    squareX = math.floor(event.x/(boardSize/10))
    squareY = math.floor(event.y/(boardSize/10))

    if [squareX,squareY] in selectedValidMoves:
        Pieces = movePiece(Pieces, selectedPiece, [squareX,squareY])
        turn = not turn
    else:
        for piece in Pieces:
            if piece["pos"][0] == squareX and piece["pos"][1] == squareY:
                selectedPiece = piece["id"]
                break

    if selectedPiece >= 0:
        selectedValidMoves = validMoves(Pieces, Pieces[selectedPiece], turn)

    updateBoard()

def MoveCommit():
    print(f"Commited move: {manMove.get()}")

    updateBoard()






root = Tk()
root.title('MAKiT Chess')

root.bind("<Button-1>", on_left_click)

paned_InputMove = PanedWindow(root, orient=HORIZONTAL)
paned_InputMove.pack(fill='both', expand=1)

manMoveLabel = Label(root, text="Manual move")
manMove = Entry(root)

paned_InputMove.add(manMoveLabel)
paned_InputMove.add(manMove)

commitMove = Button(root, text="Commit move", width=25, command=MoveCommit)
exitButton = Button(root, text="Halt", width=25, command=root.destroy)

commitMove.pack()
exitButton.pack()

boardSize = 600

canvas = Canvas(root, width=boardSize, height=boardSize, bg='white')
canvas.pack()

pieceImage = Image.open('./src/Chess_Pieces_Sprite.svg.png').convert("RGBA")

pieceImageSize = 640



pieceImages = {"KW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*0,pieceImageSize*0,pieceImageSize*1,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "QW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*1,pieceImageSize*0,pieceImageSize*2,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "BW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*2,pieceImageSize*0,pieceImageSize*3,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "NW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*3,pieceImageSize*0,pieceImageSize*4,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "RW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*4,pieceImageSize*0,pieceImageSize*5,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "PW":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*5,pieceImageSize*0,pieceImageSize*6,pieceImageSize*1]).resize((int(boardSize/10),int(boardSize/10)))),
               "KB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*0,pieceImageSize*1,pieceImageSize*1,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10)))),
               "QB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*1,pieceImageSize*1,pieceImageSize*2,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10)))),
               "BB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*2,pieceImageSize*1,pieceImageSize*3,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10)))),
               "NB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*3,pieceImageSize*1,pieceImageSize*4,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10)))),
               "RB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*4,pieceImageSize*1,pieceImageSize*5,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10)))),
               "PB":ImageTk.PhotoImage(pieceImage.crop([pieceImageSize*5,pieceImageSize*1,pieceImageSize*6,pieceImageSize*2]).resize((int(boardSize/10),int(boardSize/10))))}


updateBoard()

root.mainloop()
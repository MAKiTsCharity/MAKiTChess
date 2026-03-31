def getPiece(Pieces, position):
    for piece in Pieces:
        if piece["pos"] == position:
            return piece
    
    return False


def validMoves(Pieces, piece, turn):

    retVal = []

    if turn ^ piece["player"]:
        return retVal

    match piece["piece"]:
        case "P":
            if not getPiece(Pieces,[piece["pos"][0],piece["pos"][1]+(1 if piece["player"] else -1)]):
                retVal.append([piece["pos"][0],piece["pos"][1]+(1 if piece["player"] else -1)])

            if not getPiece(Pieces,[piece["pos"][0],piece["pos"][1]+(2 if piece["player"] else -2)]) and (not piece["hasDoubled"]) and not getPiece(Pieces,[piece["pos"][0],piece["pos"][1]+(1 if piece["player"] else -1)]):
                retVal.append([piece["pos"][0],piece["pos"][1]+(2 if piece["player"] else -2)])

            if getPiece(Pieces,[piece["pos"][0]+1,piece["pos"][1]+(1 if piece["player"] else -1)]):
                retVal.append([piece["pos"][0]+1,piece["pos"][1]+(1 if piece["player"] else -1)])

            if getPiece(Pieces,[piece["pos"][0]-1,piece["pos"][1]+(1 if piece["player"] else -1)]):
                retVal.append([piece["pos"][0]-1,piece["pos"][1]+(1 if piece["player"] else -1)])
        case _:
            print("(´･ω･`)?")


    return retVal



def movePiece(Pieces, selectedPiece, move):

    retPieces = []

    ids = 0

    for piece in Pieces:
        if piece["id"] == selectedPiece:
            piece["pos"] = move
            piece["id"] = ids
            retPieces.append(piece)
        elif piece["pos"] != move:
            piece["id"] = ids
            retPieces.append(piece)
        else:
            ids -= 1

        ids += 1


    return retPieces
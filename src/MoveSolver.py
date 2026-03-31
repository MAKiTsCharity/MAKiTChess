def getPiece(Pieces, position):
    for piece in Pieces:
        if piece["pos"] == position:
            return piece
    
    return False

def removeMoves(moves, indicesToRemove):
    retVal = []
    
    for i in range(len(moves)):
        if i not in indicesToRemove:
            retVal.append(moves[i])

    return retVal

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
        case "R":
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                curPos = [piece["pos"][0],piece["pos"][1]]
                while (curPos[0]+direction[0] >= 0) and (curPos[0]+direction[0] <= 9) and (curPos[1]+direction[1] >= 0) and (curPos[1]+direction[1] <= 9):
                    curPos[0] += direction[0]
                    curPos[1] += direction[1]
                    if not getPiece(Pieces, curPos):
                        retVal.append([curPos[0],curPos[1]])
                    elif getPiece(Pieces, curPos)["player"] ^ piece["player"]:
                        retVal.append([curPos[0],curPos[1]])
                        break
                    else:
                        break
        case "N":

            directions = [[2,1],[2,-1],[1,2],[-1,2],[-2,1],[-2,-1],[1,-2],[-1,-2]]

            for direction in directions:
                testPos = [piece["pos"][0]+direction[0],piece["pos"][1]+direction[1]]
                if (testPos[0] >= 0) and (testPos[0] <= 9) and (testPos[1] >= 0) and (testPos[1] <= 9):
                    if not getPiece(Pieces, testPos):
                        retVal.append([testPos[0],testPos[1]])
                    elif getPiece(Pieces, testPos)["player"] ^ piece["player"]:
                        retVal.append([testPos[0],testPos[1]])
        case "B":
            directions = [[1,1],[1,-1],[-1,-1],[-1,1]]
            for direction in directions:
                curPos = [piece["pos"][0],piece["pos"][1]]
                while (curPos[0]+direction[0] >= 0) and (curPos[0]+direction[0] <= 9) and (curPos[1]+direction[1] >= 0) and (curPos[1]+direction[1] <= 9):
                    curPos[0] += direction[0]
                    curPos[1] += direction[1]
                    if not getPiece(Pieces, curPos):
                        retVal.append([curPos[0],curPos[1]])
                    elif getPiece(Pieces, curPos)["player"] ^ piece["player"]:
                        retVal.append([curPos[0],curPos[1]])
                        break
                    else:
                        break

        case "Q":
            directions = [[1,1],[1,-1],[-1,-1],[-1,1],[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                curPos = [piece["pos"][0],piece["pos"][1]]
                while (curPos[0]+direction[0] >= 0) and (curPos[0]+direction[0] <= 9) and (curPos[1]+direction[1] >= 0) and (curPos[1]+direction[1] <= 9):
                    curPos[0] += direction[0]
                    curPos[1] += direction[1]
                    if not getPiece(Pieces, curPos):
                        retVal.append([curPos[0],curPos[1]])
                    elif getPiece(Pieces, curPos)["player"] ^ piece["player"]:
                        retVal.append([curPos[0],curPos[1]])
                        break
                    else:
                        break

        case "K":
            directions = [[1,1],[1,-1],[-1,-1],[-1,1],[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                curPos = [piece["pos"][0]+direction[0],piece["pos"][1]+direction[1]]
                if (curPos[0] >= 0) and (curPos[0] <= 9) and (curPos[1] >= 0) and (curPos[1] <= 9):
                    if not getPiece(Pieces, curPos):
                        retVal.append([curPos[0],curPos[1]])
                    elif getPiece(Pieces, curPos)["player"] ^ piece["player"]:
                        retVal.append([curPos[0],curPos[1]])
        case _:
            print("(´･ω･`)?")

    forbiddenMoves = []

    if piece["pos"][0] == 0 or piece["pos"][0] == 9 or piece["pos"][1] == 0 or piece["pos"][1] == 9:
        for i in range(len(retVal)):
            if retVal[i][0] == 0 or retVal[i][0] == 9 or retVal[i][1] == 0 or retVal[i][1] == 9:
                forbiddenMoves.append(i)

    retVal = removeMoves(retVal, forbiddenMoves)

    print(f"FINAL: {retVal}")

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
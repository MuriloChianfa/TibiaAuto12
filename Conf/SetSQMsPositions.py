from Core.GetPlayerPosition import GetPlayerPosition

SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Player = [0, 0]
gameWindow = [0, 0, 0, 0]
SQMsSizes = [0, 0]


def SetSQMs():
    if gameWindow[0] and gameWindow[1] != 0:
        SQMsSizes[0] = int((gameWindow[2] - gameWindow[0]) / 15)
        SQMsSizes[1] = int((gameWindow[3] - gameWindow[1]) / 11)
        print(f"Size of Your SQM [Width: {SQMsSizes[0]}px, Height: {SQMsSizes[1]}px]")
        print('')
    else:
        print("Setting Window Size...")
        print('')
        Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[
            3] = GetPlayerPosition()
        SetSQMs()

    if Player[0] and Player[1] != 0 and SQMsSizes[0] and SQMsSizes[1] != 0:
        SQMs[0] = Player[0] - SQMsSizes[0]
        SQMs[1] = Player[1] + SQMsSizes[1]
        SQMs[2] = Player[0]
        SQMs[3] = Player[1] + SQMsSizes[1]
        SQMs[4] = Player[0] + SQMsSizes[0]
        SQMs[5] = Player[1] + SQMsSizes[1]
        SQMs[6] = Player[0] - SQMsSizes[0]
        SQMs[7] = Player[1]
        SQMs[8] = Player[0]
        SQMs[9] = Player[1]
        SQMs[10] = Player[0] + SQMsSizes[0]
        SQMs[11] = Player[1]
        SQMs[12] = Player[0] - SQMsSizes[0]
        SQMs[13] = Player[1] - SQMsSizes[1]
        SQMs[14] = Player[0]
        SQMs[15] = Player[1] - SQMsSizes[1]
        SQMs[16] = Player[0] + SQMsSizes[0]
        SQMs[17] = Player[1] - SQMsSizes[1]
        return SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], \
               SQMs[7], SQMs[8], SQMs[9], SQMs[10], SQMs[11], SQMs[12], SQMs[13], \
               SQMs[14], SQMs[15], SQMs[16], SQMs[17]
    else:
        print("Setting Player Position...")
        Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[
            3] = GetPlayerPosition()
        SetSQMs()


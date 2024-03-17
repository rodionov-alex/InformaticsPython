with open('26.txt') as f:
    lots_count, participant_count, bets_count = tuple(map(int, f.readline().split()))
    bets = sorted([tuple(map(int, x.split())) for x in f], key=lambda x: (x[0], x[2]))
    lot_bets = dict()
    lots_sold = []

    for lot, participant, bet in bets:
        if lot in lot_bets:
            lot_bets[lot].append(bet)
        else:
            lot_bets[lot] = [bet]

    for key in lot_bets.keys():
        if len(lot_bets[key]) > 1:
            lots_sold.append(lot_bets[key][-2])

    print(len(lots_sold), sum(lots_sold), sep='\t')

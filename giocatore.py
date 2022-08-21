import dado

class giocatore: 
    #nome
    dadi = []
    d1 = dado()
    d2 = dado()
    d3 = dado()
    d4 = dado()
    d5 = dado()
    dadi.append(d1)
    dadi.append(d2)
    dadi.append(d3)
    dadi.append(d4)
    dadi.append(d5)

    def lancio():
        for x in dadi:
         x.new_value()
    
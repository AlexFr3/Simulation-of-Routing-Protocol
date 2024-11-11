class Nodo:
    def __init__(self, id_nodo):
        self.id_nodo = id_nodo
        self.vicini = {}  # Distanza ai nodi vicini
        self.tabella_routing = {id_nodo: (0, id_nodo)}  # Distanza a se stesso

    def aggiungi_vicino(self, vicino, distanza):
        self.vicini[vicino.id_nodo] = distanza
        self.tabella_routing[vicino.id_nodo] = (distanza, vicino.id_nodo)

    def aggiorna_tabella(self, tabelle_vicine):
        cambiato = False
        for nodo_vicino, tabella in tabelle_vicine.items():
            distanza_vicino = self.vicini[nodo_vicino]
            for destinazione, (distanza, next_hop) in tabella.items():
                nuova_distanza = distanza_vicino + distanza
                if (destinazione not in self.tabella_routing or 
                    nuova_distanza < self.tabella_routing[destinazione][0]):
                    self.tabella_routing[destinazione] = (nuova_distanza, nodo_vicino)
                    cambiato = True
        return cambiato

# Creazione dei nodi e della rete
nodi = [Nodo(i) for i in range(5)]
nodi[0].aggiungi_vicino(nodi[1], 1)
nodi[1].aggiungi_vicino(nodi[2], 1)
nodi[2].aggiungi_vicino(nodi[3], 1)
nodi[3].aggiungi_vicino(nodi[4], 1)
nodi[4].aggiungi_vicino(nodi[0], 1)  # Anello

# Simulazione
for step in range(10):  # Massimo 10 cicli
    cambiato = False
    for nodo in nodi:
        tabelle_vicine = {vicino: nodi[vicino].tabella_routing for vicino in nodo.vicini}
        if nodo.aggiorna_tabella(tabelle_vicine):
            cambiato = True
    if not cambiato:
        break
    print(f"Ciclo {step + 1}:")
    for nodo in nodi:
        print(f"Nodo {nodo.id_nodo} tabella: {nodo.tabella_routing}")

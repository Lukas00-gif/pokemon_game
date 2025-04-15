# Estrutura para as telas
class Tela:
    def __init__(self, mapa, pokemons_disponiveis):
        self.mapa = mapa
        self.pokemons_disponiveis = pokemons_disponiveis

# Mapas das telas
mapa_tela1 = [
    ["solo", "solo", "solo", "solo", "solo"],
    ["solo", "grama", "agua", "grama", "solo"],
    ["solo", "grama", "grama", "grama", "solo"],
    ["solo", "grama", "agua", "grama", "solo"],
    ["solo", "solo", "solo", "solo", "solo"],
]
pokemons_tela1 = ["bulbasaur", "charmander", "squirtle"]

mapa_tela2 = [ # Cima
    ["montanha", "montanha", "montanha", "montanha", "montanha"],
    ["solo", "caverna", "caverna", "caverna", "solo"],
    ["solo", "grama", "grama", "grama", "solo"],
    ["solo", "solo", "solo", "solo", "solo"],
    ["solo", "solo", "solo", "solo", "agua"],
]
pokemons_tela2 = ["bulbasaur", "charmander", "squirtle", "gastly", "mewtwo"]

mapa_tela3 = [ # Direita
    ["floresta", "montanha", "montanha", "montanha", "montanha"],
    ["floresta", "grama", "grama", "grama", "grama"],
    ["floresta", "solo", "solo", "solo", "solo"],
    ["floresta", "mansao assombrada", "grama", "grama", "estacao de trem"],
]
pokemons_tela3 = ["charmander", "bulbasaur", "gastly", "mewtwo"]

mapa_tela4 = [ # Baixo 
    ["solo", "solo", "solo", "solo", "solo"],
    ["jardim", "jardim", "solo", "agua", "agua"],
    ["praia", "praia", "praia", "praia", "praia"],
    ["praia", "rio", "rio", "rio", "praia"],
]
pokemons_tela4 = ["squirtle"]

mapa_tela5 = [ # Esquerda
    ["montanha_gelada", "montanha_gelada", "montanha_gelada", "montanha_gelada", "montanha_gelada"],
    ["solo", "floresta", "cemiterio", "floresta", "solo"],
    ["solo", "floresta", "cemiterio", "floresta", "solo"],
    ["solo", "floresta", "cemiterio", "floresta", "solo"],
    ["solo", "solo", "solo", "solo", "solo"],
]
pokemons_tela5 = ["charmander", "bulbasaur","gastly"]

# Dicionário para armazenar as telas (sem alterações)
telas = {
    1: Tela(mapa_tela1, pokemons_tela1),
    2: Tela(mapa_tela2, pokemons_tela2),
    3: Tela(mapa_tela3, pokemons_tela3),
    4: Tela(mapa_tela4, pokemons_tela4),
    5: Tela(mapa_tela5, pokemons_tela5),
}


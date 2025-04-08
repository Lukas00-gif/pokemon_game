import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 1200
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pokémon")

# Cores
VERDE = (0, 128, 0) # grama
VERDE_ESCURO = (70,163,100) # floresta
VERDE_MEIO = (5,163,13) # jardim
AZUL = (150, 150, 255) # agua
AZUL_ESCURO = (17, 5, 252) #rio
AZUL_CLARO = (124, 129, 237)# montanha gelada
AMARELO_CLARO = (230, 242, 63) #praia 
AMARELO_SHINY = (255, 102, 0) # enconrtar shiny
MARROM = (139, 69, 19) #montanha
ROXO = (100, 50, 100) # cemiterio
CINZA_ESCURO = (80, 80, 80) #caverna
BEGE = (191,201,114) # solo
BRANCO_CLARO = (235, 230, 234) # estaçao de trem
PRETO_CLARO = (53,54,54) # mansao assombrada
PRETO = (0, 0, 0)
CINZA_CLARO = (220, 220, 220)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

'''criar outros biomas, 
bioma - criar rio (deferente da agua, que seria maior), pokes tipo agua e gelo
bioma - criar um jardim pokemons veneno e fada
bioma - criar uma praia(areia) pokemons tipo dragao e psquico


tipo escuro e fantasma encontrados em - mansao assombrada e cemiterio
tipo metal e eletrico encontrados em -  estacao de trem
tipo inseto, veneno, voador encontrados em - florestas
tipo pedra encontrados em - montanhas e cavernas
tipo solo e lutador encontrado no - solo
tipo gelo(lendarios de gelo) - montanha gelada e no rio
tipo grama - encontados em - gramas
tipo normal em qualquer lugar?(mudar isso)


add pokemons de acordo com o tipo de raridade
comum | incomum | raro | super raro | mitico | extintos |lendario
90%  |   85%   |  60% |     45%    |   20%  |    10%    |  3%   

o jogador ganha dinheiro capturando pokemons e um npc deve aparecer no mapa com itens
inclicive pokebolas e itens de evoluçao aleatorio os itens

add inventario
add pokedex com os numeros do pokemons como base

add banco um possivel banco de dados
'''

# Dicionário para armazenar os sprites redimensionados
pokemon_sprites = {}
bioma_sprites = {} # Novo dicionário para sprites de bioma
sprite_tamanho_padrao = (96, 96)
sprite_encontro_tamanho = (128, 128)

# Fontes
fonte_normal = pygame.font.Font(None, 36)
fonte_bioma = pygame.font.Font(None, 40)
fonte_botao = pygame.font.Font(None, 24)
fonte_shiny = pygame.font.Font(None, 20)

# Carregar sprite do jogador
player_sprite_sheet = pygame.image.load("player_and_npc/player_front_andando_mapa.png").convert_alpha()
player_frame_width = 32
player_frame_height = 32
player_scale = 2
player_width = player_frame_width * player_scale
player_height = player_frame_height * player_scale
player_frame_index = 0
player_num_frames = 1

# Função para obter o frame do jogador
def get_player_frame(frame_index):
    frame = player_sprite_sheet
    return pygame.transform.scale(frame, (player_width, player_height))

# Função para carregar um sprite
def carregar_sprite(caminho, tamanho):
    try:
        sprite = pygame.image.load(caminho).convert_alpha()
        return pygame.transform.scale(sprite, tamanho)
    except pygame.error as e:
        print(f"Erro ao carregar sprite {caminho}: {e}")
        return None

# Função para carregar e redimensionar sprites de bioma
def carregar_bioma_sprite(caminho, tamanho_tile):
    try:
        sprite = pygame.image.load(caminho).convert_alpha()
        # Redimensionar para o tamanho do tile
        return pygame.transform.scale(sprite, (tamanho_tile, tamanho_tile))
    except pygame.error as e:
        print(f"Erro ao carregar sprite de bioma {caminho}: {e}")
        return None

pokemon_sprites = {}

def obter_sprite_pokemon(nome_pokemon, eh_shiny=False, para_encontro=False):
    data = pokemon_data.get(nome_pokemon.lower())
    if data:
        nome_arquivo = data["sprite_shiny"] if eh_shiny and data.get("sprite_shiny") else data["sprite"]
        caminho = f"sprites/{nome_arquivo}"
        sprite_carregado = pokemon_sprites.get(caminho)
        tamanho = sprite_encontro_tamanho if para_encontro else sprite_tamanho_padrao
        if sprite_carregado is None or sprite_carregado.get_size() != tamanho:
            sprite_carregado = carregar_sprite(caminho, tamanho)
            pokemon_sprites[caminho] = sprite_carregado
        return sprite_carregado
    return None

# Carregar sprites iniciais de Pokémon
pokemon_sprites["bulbasaur_front.png"] = carregar_sprite(f"sprites/bulbasaur_front.png", sprite_tamanho_padrao)
pokemon_sprites["charmander_front.png"] = carregar_sprite(f"sprites/charmander_front.png", sprite_tamanho_padrao)
pokemon_sprites["squirtle_front.png"] = carregar_sprite(f"sprites/squirtle_front.png", sprite_tamanho_padrao)
pokemon_sprites["gastly_front.png"] = carregar_sprite(f"sprites/gastly_front.png", sprite_tamanho_padrao)
pokemon_sprites["mewtwo_front.png"] = carregar_sprite(f"sprites/mewtwo_front.png", sprite_tamanho_padrao)

# Dados dos Pokémon (sem alterações)
pokemon_data = {
    "bulbasaur": {
        "tipo": ["grama"],
        "fraquezas": ["voador", "fogo", "psiquico", "gelo"],
        "resistencias": ["lutador", "agua", "grama", "eletrico", "fada"],
        "imunidades": [],
        "raridade": "comum",
        "taxa_captura": 0.8,
        "number": "0001",
        "biomas": ["floresta", "grama"],
        "sprite": "bulbasaur_front.png",
        "sprite_shiny": "shiny_bulbasaur_front.png",
        "nivel": 5,
        "shiny": False,
    },

    "charmander": {
        "tipo": ["fogo"],
        "fraquezas": ["solo", "pedra", "agua"],
        "resistencias": ["inseto", "metal", "fogo", "grama", "gelo", "fada"],
        "imunidades": [],
        "raridade": "comum",
        "taxa_captura": 0.8,
        "number": "0004",
        "biomas": ["montanha", "solo"],
        "sprite": "charmander_front.png",
        "sprite_shiny": "shiny_charmander_front.png",
        "nivel": 5,
        "shiny": False,
    },
    "squirtle": {
        "tipo": ["agua"],
        "fraquezas": ["grama", "eletrico"],
        "resistencias": ["metal", "fogo", "agua", "gelo"],
        "imunidades": [],
        "raridade": "comum",
        "taxa_captura": 0.85,
        "number": "0007",
        "biomas": ["agua"],
        "sprite": "squirtle_front.png",
        "sprite_shiny": "shiny_squirtle_front.png",
        "nivel": 5,
        "shiny": False,
    },
    "gastly": {
        "tipo": ["fantasma", "veneno"],
        "fraquezas": ["fantasma", "psiquico", "escuro"],
        "resistencias": ["veneno", "inseto", "grama", "fada"],
        "imunidades": ["normal", "lutador", "solo"],
        "raridade": "raro",
        "taxa_captura": 0.4,
        "number": "0092",
        "biomas": ["caverna", "cemiterio",],
        "sprite": "gastly_front.png",
        "sprite_shiny": "shiny_gastly_front.png",
        "nivel": 10,
        "shiny": False,
    },
    "mewtwo": {
        "tipo": ["psiquico"],
        "fraquezas": ["inseto", "fantasma", "escuro"],
        "resistencias": ["lutador", "psiquico"],
        "imunidades": [],
        "raridade": "lendario",
        "taxa_captura": 0.05,
        "number": "0150",
        "biomas": ["montanha"],
        "sprite": "mewtwo_front.png",
        "sprite_shiny": "shiny_mewtwo_front.png",
        "nivel": 70,
        "shiny": False,
    },
}

# Estrutura para as telas (sem alterações)
class Tela:
    def __init__(self, mapa, pokemons_disponiveis):
        self.mapa = mapa
        self.pokemons_disponiveis = pokemons_disponiveis

# Mapas das telas (sem alterações)
mapa_tela1 = [
    ["solo", "solo", "solo", "solo", "solo"],
    ["solo", "grama", "agua", "grama", "solo"],
    ["solo", "grama", "grama", "grama", "solo"],
    ["solo", "grama", "agua", "grama", "solo"],
    ["solo", "solo", "solo", "solo", "solo"],
]
pokemons_tela1 = ["charmander", "squirtle"]

mapa_tela2 = [ # Cima
    ["montanha", "montanha", "montanha", "montanha", "montanha"],
    ["solo", "caverna", "caverna", "caverna", "solo"],
    ["solo", "grama", "grama", "grama", "solo"],
    ["solo", "solo", "solo", "solo", "solo"],
    ["solo", "solo", "solo", "solo", "agua"],
]
pokemons_tela2 = ["charmander","squirtle","gastly", "mewtwo"]

mapa_tela3 = [ # Direita
    ["floresta", "montanha", "montanha", "montanha", "montanha"],
    ["floresta", "grama", "grama", "grama", "grama"],
    ["floresta", "solo", "solo", "solo", "solo"],
    ["floresta", "mansao assombrada", "grama", "grama", "estacao de trem"],
]
pokemons_tela3 = ["charmander", "bulbasaur"]

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

# Tela atual (sem alterações)
tela_atual = 1
mapa_atual = telas[tela_atual].mapa
pokemons_disponiveis_atual = telas[tela_atual].pokemons_disponiveis

# Posição do jogador (sem alterações)
jogador_x = largura // 2
jogador_y = altura // 2
velocidade_jogador = 42

# Variável de controle de encontro (sem alterações)
pokemon_encontrado_atual = None

# Botão de correr (sem alterações)
botao_correr_rect = pygame.Rect(largura // 4 + 20, 280, 150, 40)
cor_botao = (200, 200, 200)
cor_texto_botao = (0, 0, 0)

# Função para encontrar Pokémon (sem alterações)
def encontrar_pokemon(bioma):
    possiveis_pokemon = [nome for nome in pokemons_disponiveis_atual if bioma in pokemon_data[nome]["biomas"] or "qualquer" in pokemon_data[nome]["biomas"]]
    if not possiveis_pokemon:
        return None
    chance_encontro = random.random()
    if chance_encontro < 0.2:
        pokemon_encontrado = random.choice(possiveis_pokemon)
        if random.random() < 0.1:
            pokemon_data[pokemon_encontrado]["shiny"] = True
            sprite_shiny = carregar_sprite(f"sprites/shiny_{pokemon_encontrado}_front.png", sprite_encontro_tamanho)
            if sprite_shiny:
                pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = sprite_shiny
            else:
                pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = None
        else:
            pokemon_data[pokemon_encontrado]["shiny"] = False
            pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = None
        return pokemon_encontrado
    return None

# Loop principal
rodando = True
clock = pygame.time.Clock()

# Carregar o sprite da floresta (agora fora do loop para carregar apenas uma vez)
floresta_sprite = carregar_bioma_sprite("biomas/floresta.png", largura // len(mapa_atual[0])) # Usando a largura do tile como base
agua_sprite = carregar_bioma_sprite("biomas/agua.png", largura // len(mapa_atual[0]))
grama_sprite = carregar_bioma_sprite("biomas/grama.png", largura // len(mapa_atual[0]))
solo_sprite = carregar_bioma_sprite("biomas/solo.png", largura // len(mapa_atual[0]))
cemiterio_sprite = carregar_bioma_sprite("biomas/cemiterio.png", largura // len(mapa_atual[0]))
montanha_sprite = carregar_bioma_sprite("biomas/montanha.png", largura // len(mapa_atual[0]))
montanha_gelada_sprite = carregar_bioma_sprite("biomas/montanha_gelada.png", largura // len(mapa_atual[0]))
estacao_de_trem_sprite = carregar_bioma_sprite("biomas/estacao_de_trem.jpg", largura // len(mapa_atual[0]))
mansao_assombrada_sprite = carregar_bioma_sprite("biomas/mansao_assombrada.jpg", largura // len(mapa_atual[0]))
rio_sprite = carregar_bioma_sprite("biomas/rio.jpg", largura // len(mapa_atual[0]))
praia_sprite = carregar_bioma_sprite("biomas/praia.jpg", largura // len(mapa_atual[0]))
jardim_sprite = carregar_bioma_sprite("biomas/jardim.jpg", largura // len(mapa_atual[0]))
caverna_sprite = carregar_bioma_sprite("biomas/caverna.jpg", largura // len(mapa_atual[0]))


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if pokemon_encontrado_atual is None:
                # Lógica de movimento do jogador (sem alterações)
                if evento.key == pygame.K_RIGHT:
                    jogador_x += velocidade_jogador
                elif evento.key == pygame.K_LEFT:
                    jogador_x -= velocidade_jogador
                elif evento.key == pygame.K_DOWN:
                    jogador_y += velocidade_jogador
                elif evento.key == pygame.K_UP:
                    jogador_y -= velocidade_jogador

                # Tentar encontrar Pokémon (sem alterações)
                tile_largura = largura // len(mapa_atual[0])
                tile_altura = altura // len(mapa_atual)
                coluna_jogador_atual = int(jogador_x // tile_largura)
                linha_jogador_atual = int(jogador_y // tile_altura)
                if 0 <= linha_jogador_atual < len(mapa_atual) and 0 <= coluna_jogador_atual < len(mapa_atual[0]):
                    bioma_atual = mapa_atual[linha_jogador_atual][coluna_jogador_atual]
                    print(f"Bioma Atual (Movimento): {bioma_atual}")
                    print(f"Pokémons Disponíveis (Movimento): {pokemons_disponiveis_atual}")
                    pokemon_encontrado = encontrar_pokemon(bioma_atual)
                    if pokemon_encontrado:
                        print(f"Pokémon Encontrado (Movimento): {pokemon_encontrado}")
                        pokemon_encontrado_atual = pokemon_encontrado

                # Lógica de mudança de tela (sem alterações)
                if jogador_x + player_width // 2 > largura and mapa_atual[linha_jogador_atual][len(mapa_atual[0]) - 1] == "solo": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_x, pokemon_encontrado_atual = 3, telas[3].mapa, telas[3].pokemons_disponiveis, player_width // 2, None
                elif jogador_x - player_width // 2 < 0 and mapa_atual[linha_jogador_atual][0] == "solo": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_x, pokemon_encontrado_atual = 5, telas[5].mapa, telas[5].pokemons_disponiveis, largura - player_width // 2, None
                elif jogador_y + player_height // 2 > altura and mapa_atual[len(mapa_atual) - 1][coluna_jogador_atual] == "solo": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_y, pokemon_encontrado_atual = 4, telas[4].mapa, telas[4].pokemons_disponiveis, player_height // 2, None
                elif jogador_y - player_height // 2 < 0 and mapa_atual[0][coluna_jogador_atual] == "solo": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_y, pokemon_encontrado_atual = 2, telas[2].mapa, telas[2].pokemons_disponiveis, altura - player_height // 2, None
                elif tela_atual == 2 and jogador_y + player_height // 2 > altura and mapa_atual[len(mapa_atual) - 1][coluna_jogador_atual] == "solo": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_y, pokemon_encontrado_atual = 1, telas[1].mapa, telas[1].pokemons_disponiveis, player_height // 2, None
                elif tela_atual == 3 and jogador_x - player_width // 2 < 0 and mapa_atual[linha_jogador_atual][0] == "floresta": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_x, pokemon_encontrado_atual = 1, telas[1].mapa, telas[1].pokemons_disponiveis, largura - player_width // 2, None
                elif tela_atual == 4 and jogador_y - player_height // 2 < 0 and mapa_atual[0][coluna_jogador_atual] == "agua": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_y, pokemon_encontrado_atual = 1, telas[1].mapa, telas[1].pokemons_disponiveis, altura - player_height // 2, None
                elif tela_atual == 5 and jogador_x + player_width // 2 > largura and mapa_atual[linha_jogador_atual][len(mapa_atual[0]) - 1] == "cemiterio": tela_atual, mapa_atual, pokemons_disponiveis_atual, jogador_x, pokemon_encontrado_atual = 1, telas[1].mapa, telas[1].pokemons_disponiveis, player_width // 2, None

                jogador_x = max(player_width // 2, min(jogador_x, largura - player_width // 2))
                jogador_y = max(player_height // 2, min(jogador_y, altura - player_height // 2))

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and pokemon_encontrado_atual:
                if botao_correr_rect.collidepoint(evento.pos):
                    print(f"Você correu de {pokemon_encontrado_atual}!")
                    pokemon_encontrado_atual = None

    player_current_frame = get_player_frame(player_frame_index)

    tela.fill(VERDE)

    tile_largura = largura // len(mapa_atual[0])
    tile_altura = altura // len(mapa_atual)
    for y, linha in enumerate(mapa_atual):
        for x, tile in enumerate(linha):
            cor = (100, 200, 100) if tile == "grama" else \
                  AZUL if tile == "agua" else \
                  MARROM if tile == "montanha" else \
                  CINZA_ESCURO if tile == "caverna" else \
                  ROXO if tile == "cemiterio" else \
                  VERDE_ESCURO if tile == "floresta" else \
                  BEGE if tile == "solo" else \
                  AZUL_CLARO if tile == "montanha gelada" else \
                  BRANCO_CLARO if tile == "estacao de trem" else \
                  PRETO_CLARO if tile == "mansao assombrada" else \
                  AZUL_ESCURO if tile == "rio" else \
                  AMARELO_CLARO if tile == "praia" else \
                  VERDE_MEIO # jardim

            # Desenhando os sprites dos biomas
            if tile == "floresta" and floresta_sprite:
                tela.blit(floresta_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "agua" and agua_sprite:
                tela.blit(agua_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "grama" and grama_sprite:
                tela.blit(grama_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "solo" and solo_sprite:
                tela.blit(solo_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "montanha" and montanha_sprite:
                tela.blit(montanha_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "cemiterio" and cemiterio_sprite:
                tela.blit(cemiterio_sprite, (x * tile_largura, y * tile_altura))
            elif tile == "montanha_gelada" and montanha_gelada_sprite:
                tela.blit(montanha_gelada_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("estacao de trem") and estacao_de_trem_sprite:
                tela.blit(estacao_de_trem_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("mansao assombrada") and mansao_assombrada_sprite:
                tela.blit(mansao_assombrada_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("rio") and rio_sprite:
                tela.blit(rio_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("praia") and praia_sprite:
                tela.blit(praia_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("jardim") and jardim_sprite:
                tela.blit(jardim_sprite, (x * tile_largura, y * tile_altura))
            elif tile == ("caverna") and caverna_sprite:
                tela.blit(caverna_sprite, (x * tile_largura, y * tile_altura))
            # elif colocar os outros biomas aki
            else:
                pygame.draw.rect(tela, cor, (x * tile_largura, y * tile_altura, tile_largura, tile_altura))
        
            # ---------------

            if x == 0 and y >= 0 and y < len(mapa_atual):
                pygame.draw.rect(tela, PRETO, (x * tile_largura, y * tile_altura, 5, tile_altura))
            if x == len(mapa_atual[0]) - 1 and y >= 0 and y < len(mapa_atual):
                pygame.draw.rect(tela, PRETO, (x * tile_largura + tile_largura - 5, y * tile_altura, 5, tile_altura))
            if y == 0 and x >= 0 and x < len(mapa_atual[0]):
                pygame.draw.rect(tela, PRETO, (x * tile_largura, y * tile_altura, tile_largura, 5))
            if y == len(mapa_atual) - 1 and x >= 0 and x < len(mapa_atual[0]):
                pygame.draw.rect(tela, PRETO, (x * tile_largura, y * tile_altura + tile_altura - 5, tile_largura, 5))

    tela.blit(player_current_frame, (jogador_x - player_width // 2, jogador_y - player_height // 2))

    # Mostrar o bioma atual (sem tentar encontrar Pokémon aqui)
    coluna_jogador = int(jogador_x // tile_largura)
    linha_jogador = int(jogador_y // tile_altura)
    if 0 <= linha_jogador < len(mapa_atual) and 0 <= coluna_jogador < len(mapa_atual[0]):
        bioma_atual = mapa_atual[linha_jogador][coluna_jogador]
        bioma_atual_texto = fonte_bioma.render(bioma_atual.capitalize(), True, BRANCO)
        bioma_rect = bioma_atual_texto.get_rect(center=(largura // 2, 50))
        tela.blit(bioma_atual_texto, bioma_rect)

    if pokemon_encontrado_atual:
        pygame.draw.rect(tela, CINZA_CLARO, (largura // 4, altura // 4 - 50, largura // 2, 350))
        texto_encontro = fonte_normal.render(f"Um {pokemon_encontrado_atual} selvagem apareceu!", True, PRETO)
        texto_rect = texto_encontro.get_rect(center=(largura // 2, altura // 4 - 20))
        tela.blit(texto_encontro, texto_rect)

        pokemon_para_desenhar = obter_sprite_pokemon(pokemon_encontrado_atual.lower(), pokemon_data[pokemon_encontrado_atual.lower()]["shiny"], para_encontro=True)

        if pokemon_para_desenhar:
            tela.blit(pokemon_para_desenhar, (largura // 2 - pokemon_para_desenhar.get_width() // 2, altura // 4 + 30))

        shiny_text = ""
        if pokemon_data[pokemon_encontrado_atual.lower()]["shiny"]:
            shiny_text = "(Shiny!)"
        texto_shiny = fonte_shiny.render(shiny_text, True, AMARELO_SHINY)
        texto_shiny_rect = texto_shiny.get_rect(center=(largura // 2, altura // 4 + sprite_encontro_tamanho[1] // 2 + 85))
        tela.blit(texto_shiny, texto_shiny_rect)

        pygame.draw.rect(tela, cor_botao, botao_correr_rect)
        texto_correr = fonte_botao.render("Correr", True, cor_texto_botao)
        texto_rect_correr = texto_correr.get_rect(center=botao_correr_rect.center)
        tela.blit(texto_correr, texto_rect_correr)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
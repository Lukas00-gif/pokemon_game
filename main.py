import pygame
import random

from data.pokemon_data import pokemon_data
from maps.game_maps import telas
from sprites_data.sprites_loader import obter_sprite_pokemon, carregar_sprite, carregar_todos_bioma_sprites, sprite_encontro_tamanho, bioma_sprites, pokemon_sprites

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

'''
* agua - pokemons tipo agua
* rio - pokemons tipo agua(pokes diferente do bioma agua) e gelo
* jardim - pokemons tipo veneno e fada
* praia - pokemons tipo dragao e psiquico
* mansao assombrada e cemiterio - pokemons tipo escuro e fantasma
* estaçao de trem - pokemons metal e eletrico
* florestas - pokemons tipo veneno(pokes diferente do bioma jardim), voador e inseto 
* montanhas e cavernas  - pokemons tipo pedra
* solo - pokemons tipo solo e lutador
* montanha gelada e o rio - pokemons de gelo
* grama - pokemons tipo grama
* qualquer? - pokemons tipo normal

'''

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


# Carregar sprites iniciais de Pokémon
pokemon_sprites = {}
pokemon_sprites["bulbasaur_front.png"] = carregar_sprite(f"sprites/bulbasaur_front.png", (96,96))
pokemon_sprites["charmander_front.png"] = carregar_sprite(f"sprites/charmander_front.png", (96,96))
pokemon_sprites["squirtle_front.png"] = carregar_sprite(f"sprites/squirtle_front.png", (96,96))
pokemon_sprites["gastly_front.png"] = carregar_sprite(f"sprites/gastly_front.png", (96,96))
pokemon_sprites["mewtwo_front.png"] = carregar_sprite(f"sprites/mewtwo_front.png", (96,96))


# Carregar todos os sprites de bioma UMA VEZ
tamanho_base_bioma = 216 # Um tamanho base razoável para carregar todos os biomas inicialmente
bioma_sprites_cache = carregar_todos_bioma_sprites(tamanho_base_bioma)

# Tela atual (sem alterações)
tela_atual = 1
mapa_atual = telas[tela_atual].mapa
pokemons_disponiveis_atual = telas[tela_atual].pokemons_disponiveis

# Posição do jogador (sem alterações)
jogador_x = largura // 2
jogador_y = altura // 2
velocidade_jogador = 44

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
    if chance_encontro < 0.1:
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

    # bioma_sprites = load_bioma_sprites(tile_largura)

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

            
            # Desenhando os sprites dos biomas (agora usando o cache carregado)
            if tile in bioma_sprites_cache and bioma_sprites_cache[tile]:
                scaled_bioma_sprite = pygame.transform.scale(bioma_sprites_cache[tile], (tile_largura, tile_altura))
                tela.blit(scaled_bioma_sprite, (x * tile_largura, y * tile_altura))
            else:
                pygame.draw.rect(tela, cor, (x * tile_largura, y * tile_altura, tile_largura, tile_altura))


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
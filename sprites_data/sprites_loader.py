import pygame
import random

from data.pokemon_data import pokemon_data


bioma_sprites = {} # Inicializar aqui para ser acessível depois da função
pokemon_sprites = {}

# Dicionário para armazenar os sprites redimensionados
pokemon_sprites = {}
bioma_sprites = {} # Novo dicionário para sprites de bioma
sprite_tamanho_padrao = (96, 96)
sprite_encontro_tamanho = (128, 128)

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


def carregar_todos_bioma_sprites(tamanho_base):
    sprites = {}
    sprites["floresta"] = carregar_bioma_sprite("./biomas/floresta.png", tamanho_base)
    sprites["agua"] = carregar_bioma_sprite("./biomas/agua.png", tamanho_base)
    sprites["grama"] = carregar_bioma_sprite("./biomas/grama.png", tamanho_base)
    sprites["solo"] = carregar_bioma_sprite("./biomas/solo.png", tamanho_base)
    sprites["cemiterio"] = carregar_bioma_sprite("./biomas/cemiterio.png", tamanho_base)
    sprites["montanha"] = carregar_bioma_sprite("./biomas/montanha.png", tamanho_base)
    sprites["montanha_gelada"] = carregar_bioma_sprite("./biomas/montanha_gelada.png", tamanho_base)
    sprites["estacao de trem"] = carregar_bioma_sprite("./biomas/estacao_de_trem.jpg", tamanho_base)
    sprites["mansao assombrada"] = carregar_bioma_sprite("./biomas/mansao_assombrada.jpg", tamanho_base)
    sprites["rio"] = carregar_bioma_sprite("./biomas/rio.jpg", tamanho_base)
    sprites["praia"] = carregar_bioma_sprite("./biomas/praia.jpg", tamanho_base)
    sprites["jardim"] = carregar_bioma_sprite("./biomas/jardim.jpg", tamanho_base)
    sprites["caverna"] = carregar_bioma_sprite("./biomas/caverna.jpg", tamanho_base)
    return sprites


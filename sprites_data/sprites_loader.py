import pygame
import random

from data.pokemon_data import pokemon_data


# Dicionário para armazenar os sprites redimensionados
pokemon_sprites = {}
bioma_sprites = {} # Novo dicionário para sprites de bioma
sprite_tamanho_padrao = (96, 96)
sprite_encontro_tamanho = (128, 128)

# comum - 10%
# incomum - 8%
# raro - 5%
# super raro - 3%
# extinto - 2%
# mitico - 1%
# lendario - 0.9%

#diminuir draticamente ja que e toda hora q aparece aki e a chance normal
# e fazer os teste se esta tudo ok
raridade_chance = {
    "comum": 0.10,
    "incomum": 0.08,
    "raro": 0.05,
    "super raro": 0.03,
    "extinto": 0.02,
    "mitico": 0.01,
    "lendario": 0.009,
}


def encontrar_pokemon(bioma, pokemons_disponiveis):
    possiveis_pokemon = [nome for nome in pokemons_disponiveis if bioma in pokemon_data[nome]["biomas"] or "qualquer" in pokemon_data[nome]["biomas"]]
    if not possiveis_pokemon:
        return None

    pokemon_raro = random.choice(possiveis_pokemon)
    raridade = pokemon_data[pokemon_raro]["raridade"]
    #chance normal de ver um pokemon = 10%
    chance_encontro_base = raridade_chance.get(raridade, 0.001)

    if random.random() < chance_encontro_base:
        pokemon_encontrado = pokemon_raro
        #original 0.001 = 0.1%
        if random.random() < 0.001:
            pokemon_data[pokemon_encontrado]["shiny"] = True
            sprite_shiny = carregar_sprite(f"sprites/shiny_{pokemon_encontrado.lower()}_front.png", sprite_encontro_tamanho)
            if sprite_shiny:
                pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = sprite_shiny
            else:
                pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = None
        else:
            pokemon_data[pokemon_encontrado]["shiny"] = False
            pokemon_data[pokemon_encontrado]["sprite_shiny_carregado"] = None
        return pokemon_encontrado
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


def carregar_todos_bioma_sprites(tamanho_base):
    sprites = {}
    sprites["floresta"] = carregar_bioma_sprite("./biomas/floresta.png", tamanho_base)
    sprites["agua"] = carregar_bioma_sprite("./biomas/agua.png", tamanho_base)
    sprites["grama"] = carregar_bioma_sprite("./biomas/grama.png", tamanho_base)
    sprites["solo"] = carregar_bioma_sprite("./biomas/solo.png", tamanho_base)
    sprites["cemiterio"] = carregar_bioma_sprite("./biomas/cemiterio.png", tamanho_base)
    sprites["montanha"] = carregar_bioma_sprite("./biomas/montanha.png", tamanho_base)
    sprites["montanha gelada"] = carregar_bioma_sprite("./biomas/montanha_gelada.png", tamanho_base)
    sprites["estacao de trem"] = carregar_bioma_sprite("./biomas/estacao_de_trem.jpg", tamanho_base)
    sprites["mansao assombrada"] = carregar_bioma_sprite("./biomas/mansao_assombrada.jpg", tamanho_base)
    sprites["rio"] = carregar_bioma_sprite("./biomas/rio.jpg", tamanho_base)
    sprites["praia"] = carregar_bioma_sprite("./biomas/praia.jpg", tamanho_base)
    sprites["jardim"] = carregar_bioma_sprite("./biomas/jardim.jpg", tamanho_base)
    sprites["caverna"] = carregar_bioma_sprite("./biomas/caverna.jpg", tamanho_base)
    return sprites


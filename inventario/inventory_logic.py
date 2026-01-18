# inventory/inventory_logic.py

import pygame
from sprites_data.sprites_loader import carregar_sprite

def inicializar_inventario(largura, altura):
    # --- Estado do Inventário ---
    inventario = {
        "aberto": False,
        "aba_ativa": "pokebolas",
        
        "pokebolas_data": {
            "pokeball": 5,
            "greatball": 5,
            "ultraball": 5,
            "masterball": 5,
            "premierball": 5,
        },
        "pokemon_capturados": [],
        "party_atual": [],
    }

    # --- Carregamento de Sprites ---
    # Usamos um dicionário para organizar as sprites
    sprites = {
        "pokeball": carregar_sprite("sprites/pokebolas/pokeball.png", (32, 32)),
        "greatball": carregar_sprite("sprites/pokebolas/greatball.png", (32, 32)),
        "ultraball": carregar_sprite("sprites/pokebolas/ultraball.png", (32, 32)),
        "masterball": carregar_sprite("sprites/pokebolas/masterball.png", (32, 32)),
        "premierball": carregar_sprite("sprites/pokebolas/premierball.png", (32, 32)),
    }

    # --- Configurações Visuais (Rects) ---
    rect_fundo = pygame.Rect(largura // 4, altura // 4, largura // 2, altura // 2)
    
    largura_aba = rect_fundo.width // 3
    altura_aba = 40
    
    rects_abas = {
        "pokebolas": pygame.Rect(rect_fundo.left, rect_fundo.top, largura_aba, altura_aba),
        "pokedex": pygame.Rect(rect_fundo.left + largura_aba, rect_fundo.top, largura_aba, altura_aba),
        "pokemon": pygame.Rect(rect_fundo.left + 2 * largura_aba, rect_fundo.top, largura_aba, altura_aba)
    }

    return inventario, sprites, rect_fundo, rects_abas
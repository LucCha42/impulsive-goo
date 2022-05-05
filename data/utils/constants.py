from typing import Tuple, List

import pygame.image
from numpy import array, ndarray
from pygame import Surface


def tupint(v: ndarray) -> Tuple[int, int]:
    """
    Converts a numpy vector to a tuple of ints.
    It's needed because some pygame functions require tuples of ints.

    :param v: 2D numpy array
    :return: tuple of ints
    """
    return int(v[0]), int(v[1])


# screen
RESOLUTIONS: ndarray = array(((1920, 1080), (1280, 720), (960, 540)))
SCREEN_SIZE: ndarray = RESOLUTIONS[0]  # select resolution

# world grid
GRID_SIZE: ndarray = array((32, 18))  # world size in tiles
GRID_WIDTH: int = GRID_SIZE[0]
GRID_HEIGHT: int = GRID_SIZE[1]

# tile
TILE_EDGE: int = SCREEN_SIZE[0] // GRID_WIDTH
TILE_SIZE: ndarray = array((TILE_EDGE, TILE_EDGE))
TILE_IMG: Surface = pygame.image.load("resources/sprites/test.png")
TILE_SPRITE: Surface = pygame.transform.scale(TILE_IMG, tupint(TILE_SIZE))

# goal tile
GOAL_SIZE: ndarray = TILE_SIZE
GOAL_IMAGES: List[Surface] = [
    pygame.image.load("resources/sprites/goal_1.png"),
    pygame.image.load("resources/sprites/goal_2.png"),
    pygame.image.load("resources/sprites/goal_3.png"),
]
GOAL_SPRITES: List[Surface] = list(map(
    lambda img: pygame.transform.scale(img, tupint(GOAL_SIZE)),
    GOAL_IMAGES
))

# player
PLAYER_SIZE: ndarray = TILE_SIZE * 3/4
PLAYER_IMG: Surface = pygame.image.load("resources/sprites/player.png")
PLAYER_SPRITE: Surface = pygame.transform.scale(PLAYER_IMG, tupint(PLAYER_SIZE))
PLAYER_MAX_V: int = TILE_SIZE[0] - 1

# cursor
CURSOR_SIZE: ndarray = TILE_SIZE * 3/4
CURSOR_IMG: Surface = pygame.image.load("resources/sprites/cursor.png")
CURSOR_SPRITE: Surface = pygame.transform.scale(CURSOR_IMG, tupint(CURSOR_SIZE))

# physics
FPS: int = 60
GRAVITY: ndarray = array((0, PLAYER_MAX_V / 75))

# beam physics
BEAM_STRENGTH: float = PLAYER_MAX_V / 4  # beam impulse velocity length
BEAM_DURATION: float = 0.3  # beam duration in seconds
BEAM_DECREASE: float = 1 / (BEAM_DURATION * FPS)
BEAM_VECTOR_STEP: float = TILE_EDGE / 3

# colors
WHITE: ndarray = array((255, 255, 255))
BLACK: ndarray = array((0, 0, 0))
GREY: ndarray = array((128, 128, 128))
BLUE: ndarray = array((0, 0, 255))
RED: ndarray = array((250, 0, 0))

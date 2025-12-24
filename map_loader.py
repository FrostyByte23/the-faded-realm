import pygame
import json

with open("start.json") as f:
    data = json.load(f)

tiles = data["tiles"]

tile_images = {

}
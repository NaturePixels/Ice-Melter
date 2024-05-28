import pygame
import json


class Animation:
    def __init__(self):
        self.frame_index = 0
        self.frame_duration_passed = 0

    def load_anim(self, path):
        cfgf = open(f"{path}/config.json", "r")
        cfg = json.loads(cfgf.read())
        cfgf.close()
        frames = []
        for f in range(cfg["frame_quantity"]):
            frames.append(pygame.image.load(f"{path}/{f}.png"))
        for frame in frames:
            frame.set_colorkey(0)
        return frames, cfg

    def play_anim(self, anim_config):
        self.frame_duration_passed += anim_config["frame_rate"]
        if self.frame_duration_passed > 1:
            if anim_config["frame_quantity"] - 1 > self.frame_index:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.frame_duration_passed = 0


class entity:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = [0, 0]
        self.collision_types = {
            "left": False,
            "right": False,
            "top": False,
            "bottom": False,
        }

    def move(self, tiles):
        self.collision_types = {
            "left": False,
            "right": False,
            "top": False,
            "bottom": False,
        }
        self.rect.x += self.speed[0]

        for t in tiles:
            if t.colliderect(self.rect):
                if self.speed[0] > 0:
                    self.rect.right = t.left
                    self.collision_types["left"] = True
                if self.speed[0] < 0:
                    self.rect.left = t.right
                    self.collision_types["right"] = True
        self.rect.y += self.speed[1]

        for t in tiles:
            if t.colliderect(self.rect):
                if self.speed[1] > 0:
                    self.rect.bottom = t.top
                    self.collision_types["top"] = True
                if self.speed[1] < 0:
                    self.rect.top = t.bottom
                    self.collision_types["bottom"] = True

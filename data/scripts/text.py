import pygame


def clip(s, x, y, w, h):
    return s.subsurface(pygame.Rect(x, y, w, h))


class Font:
    def __init__(self, font_img):
        self.char_order = list(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
            + "1234567890()"
            + "'"
            + '"=+?!.,/-:@'
        )
        self.char_index = 0

        self.font = {}
        ccw = 0
        for x in range(font_img.get_width()):
            if font_img.get_at((x, 1)) == (127, 127, 127):
                self.font[self.char_order[self.char_index]] = clip(
                    font_img, x - ccw, 0, ccw, font_img.get_height()
                )
                self.char_index += 1
                ccw = 0
            else:
                ccw += 1

    def RenderText(self, txt, x, y, surf, color):
        x_offset = 0
        y_offset = 0
        for char in txt:
            if char != " " and char != "\n":
                new_char = pygame.Surface(self.font[char].get_size())
                self.font[char].set_colorkey(-1)
                new_char.fill(color)
                new_char.blit(self.font[char], (0, 0))
                new_char.set_colorkey(0)
                surf.blit(new_char, (x + x_offset, y + y_offset))

                x_offset += new_char.get_width() + 1

            if char == " ":
                x_offset += new_char.get_width() + 1
            if char == "\n":
                y_offset += new_char.get_height() + 1
                x_offset = 0

import pygame, random

import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type

        # Tải các khung hình cho hoạt ảnh
        self.frames = [
            pygame.image.load(f"Graphics/chicken/c{frame}.png") for frame in range(1, 8)
        ]
        self.current_frame = 0  # Bắt đầu từ khung hình đầu tiên
        self.frame_duration = 10  # Số lần cập nhật trước khi chuyển frame
        self.frame_counter = 0  # Đếm số lần cập nhật

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        # Di chuyển alien
        self.rect.x += direction

        # Tăng bộ đếm và chuyển frame nếu cần
        self.frame_counter += 1
        if self.frame_counter >= self.frame_duration:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        img = pygame.image.load("Graphics/boss/Boss1.png")
        self.image = pygame.transform.scale(img, (40, 40))

        # x la toa do di chuyen random tu canh trai den phai
        x = random.choice([self.offset / 2, self.screen_width + self.offset - self.image.get_width()])
        if x == self.offset / 2:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft=(x, 90))


    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset / 2:
            self.kill()
        elif self.rect.left < self.offset / 2:
            self.kill()

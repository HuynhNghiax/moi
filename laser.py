import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, is_alien_laser=False):
        super().__init__()

        self.is_alien_laser = is_alien_laser
        self.image = self.load_image()
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height
        self.is_broken = False
        self.break_timer = None

    def load_image(self):
        if self.is_alien_laser:
            img = pygame.image.load('Graphics/egg/egg.png')
            return pygame.transform.scale(img, (15, 15))
        else:
            img = pygame.image.load('Graphics/laser_lv1.png')
            return pygame.transform.scale(img, (8, 15))

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 13 or self.rect.y < 5:
            self.speed = 0
            if self.is_alien_laser:
                if not self.is_broken:
                    self.break_egg()
                    self.break_timer = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - self.break_timer >= 1000:
                    self.kill()
            else:
                self.kill()

    def break_egg(self):
        """Chuyển đổi hình ảnh trứng thành trứng vỡ"""
        self.image = pygame.image.load('Graphics/egg/bokenegg.png')  # Hình ảnh trứng vỡ
        self.is_broken = True

import pygame

class LevelManager(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game  # Tham chiếu đến đối tượng Game
        self.current_level = 1
        self.level_data = {}  # Dữ liệu cho từng cấp

    def load_level_data(self):
        # Tạo thông tin cấu hình cho các cấp độ
        self.level_data = {
            1: {"alien_rows": 3, "alien_speed": 1},
            2: {"alien_rows": 4, "alien_speed": 1.2},
            3: {"alien_rows": 5, "alien_speed": 1.5},
            # Thêm các cấp độ khác
        }

    def setup_level(self, level):
        # Thiết lập dữ liệu cho cấp độ hiện tại
        self.current_level = level
        level_config = self.level_data.get(level, {})
        alien_rows = level_config.get("alien_rows", 5)
        alien_speed = level_config.get("alien_speed", 3)

        self.game.aliens_group.empty()  # Xóa tất cả alien hiện tại
        self.game.create_aliens(rows=alien_rows)  # Tạo alien theo cấp
        self.game.alien_shoot_laser(speed=alien_speed)  # Tăng tốc độ alien
        self.game.create_obstacles()

    def next_level(self):
        self.current_level += 1
        self.setup_level(self.current_level)

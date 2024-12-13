import pygame

# Định nghĩa màu sắc
GREY = (29, 29, 27)
YELLOW = (243, 216, 63)


class Menu:
    def __init__(self, screen, screen_width, screen_height, offset):
        # Màn hình hiển thị và kích thước
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset

        # Font chữ
        self.font = pygame.font.Font("Font/monogram.ttf", 40)
        self.title_font = pygame.font.Font("Font/monogram.ttf", 60)

        # Tùy chọn menu
        self.options = ["NEW GAME", "RESUME", "EXIT"]
        self.selected = 0

        # Màu sắc cho text menu
        self.highlight_color = YELLOW
        self.default_color = GREY

        # Tải background
        bg_image = pygame.image.load("Graphics/backgroud.jpg")
        self.background = pygame.transform.scale(bg_image, (
        self.screen_width + self.offset, self.screen_height + 2 * self.offset))

        # Tải tiêu đề
        self.title_image = pygame.image.load("Graphics/HeadTitle.png")

        # Tải và thiết lập nút
        self.button_image = pygame.image.load("Graphics/ButtonBackgroundImage.png")
        self.button_image = pygame.transform.scale(self.button_image, (200, 60))  # Điều chỉnh kích thước nút
        self.button_rect = self.button_image.get_rect()

    def draw(self):
        """Hiển thị giao diện menu."""
        # Vẽ background
        self.screen.blit(self.background, (0, 0))

        # Vẽ tiêu đề
        title_x = self.screen_width / 2 - self.title_image.get_width() / 2
        self.screen.blit(self.title_image, (title_x, self.offset))

        # Hiển thị các tùy chọn trong menu
        for index, option in enumerate(self.options):
            # Tính toán vị trí button
            button_x = self.screen_width // 2 - self.button_rect.width // 2
            button_y = 300 + index * (self.button_rect.height + 20)

            # Vẽ nút nền
            self.button_rect.topleft = (button_x, button_y)
            self.screen.blit(self.button_image, self.button_rect)

            # Đổi màu text dựa trên việc có được chọn hay không
            color = self.highlight_color if index == self.selected else self.default_color

            # Render text và căn giữa nó trong nút
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=self.button_rect.center)
            self.screen.blit(text_surface, text_rect)

    def handle_input(self, event):
        """ Xử lý tương tác bàn phím trên menu. """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)  # Đi lên, quay vòng khi đạt đỉnh
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)  # Đi xuống, quay vòng khi đạt đáy
            elif event.key == pygame.K_RETURN:  # Nhấn Enter
                return self.options[self.selected]

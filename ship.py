import pygame

class Ship():
    """Инициализируем корабль и задает его изначальную позицию."""
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Каждый новый корабль появляется у нижнего края экрана
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 
        
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учётом флага."""
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

         # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
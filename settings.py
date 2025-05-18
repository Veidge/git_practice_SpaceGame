class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализируем настройки игры."""
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля        
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        
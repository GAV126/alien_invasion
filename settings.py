class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        self.ship_speed = 1    # get error when use "self.ship.speed = 1"
# add bullet
        self.bullet_speed =1.0
        self.bullet_width =3
        self.bullet_height=15
        self.bullet_colour = (60,60,60)
        self.bullets_allowed = 3

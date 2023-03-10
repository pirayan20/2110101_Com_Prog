import pygame as pg
import random
from os import path

from pygame.sprite import spritecollide

img_dir = path.join('source/img')

# define screen resolution [width 480 , height 600 , FPS 60 ]
width = 480
height = 600
FPS = 60
# define colors
white = (255, 255, 255)
black = (0, 0, 0)

# initialize pg and create window
pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("ShipSpace!")
clock = pg.time.Clock()
duration_tracker = 0
cooldown_tracker = 0

# load game graphics
bg = pg.image.load(path.join(img_dir, "space.png")).convert()
bg_rect = bg.get_rect()
ship_img = pg.image.load(path.join(img_dir, "Ship.png")).convert()
meteor_img = pg.image.load(path.join(img_dir, "meteor_med.png")).convert()
bullet_img = pg.image.load(path.join(img_dir, "red_bullet.png")).convert()
shield_img = pg.image.load(path.join(img_dir, 'barrier-circle.png')).convert()

#################################################################################################
# Class ที่เพิ่มเข้ามาใหม่ -> Ship , Meteor , Bullet ; Function ที่เพิ่มเข้ามาใหม่ -> newmeteor()

# Class ของผู้เล่นภายในมี method __init__ , update , shoot
class Ship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.inv = False
        self.image = pg.transform.scale(ship_img, (50, 38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.inv:
            self.image = pg.transform.scale(shield_img, (50, 50))
            self.image.set_colorkey(black)
        else:
            self.image = pg.transform.scale(ship_img, (50, 38))
            self.image.set_colorkey(black)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def invicible(self):
        self.inv = True


# Class ของของหินภายในมี method __init__ , update
class Meteor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Class ของลูกกระสุนภายในมี method __init__ , update
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # ทำลายลูกกระสุนทิ้งถ้าลูกกระสุนออกจากหน้าจอ
        if self.rect.bottom < 0:
            self.kill()

# function ที่สร้างหินขึ้นมา 1 ก้อน
def newmeteor():
    m = Meteor()
    all_sprites.add(m)
    meteors.add(m)
#################################################################################################

new_game = True

cooldown_tracker = 6000
while True:

    # set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม
    clock.tick(FPS)
    if new_game:
        new_game = False

        #################################################################################################
        # TO DO 1-1 : สรา้ง sprite Group ให้กับ all_sprites, meteors, bullets, ship

        all_sprites = pg.sprite.Group()
        meteors = pg.sprite.Group()
        bullets = pg.sprite.Group()

        # TO DO 1-2 : สร้าง Object ให้กับ ship
        myShip = Ship()

        # TO DO 1-3 : เพิ่ม ship ลงใน all_sprites
        all_sprites.add(myShip)

        #################################################################################################
        # TO DO 2 : สร้าง Object Meteor ขึ้นมา 8 ก้อนโดยผ่านการเรียกใช้ฟังก์ชัน newmeteor()
        for i in range(8):
            newmeteor()

        #################################################################################################
    
    if not myShip.inv: 
        cooldown_tracker += clock.get_time()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        #################################################################################################
        # TO DO 3 : ตรวจสอบว่าถ้ามีการกดปุ่ม spacebar (K_SPACE) ให้ ship เรียกฟังก์ชั่นสำหรับการยิงกระสุน
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            myShip.shoot()

        if cooldown_tracker > 6000:
            if keystate[pg.K_LSHIFT]:
                myShip.invicible()
                cooldown_tracker = 0

        #################################################################################################

    # Update
    all_sprites.update()

    #################################################################################################
    # TO DO 5 : ตรวจสอบว่าลูกกระสุนชนหินหรือไม่
    # ถ้าชนให้สร้างหินขึ้นมาใหม่เท่ากับจำนวนที่ถูกชนไป
    hits = pg.sprite.groupcollide(bullets,meteors,True,True)
    if len(hits) > 0:
        for i in range(len(hits)):
            newmeteor()

    #################################################################################################
    # TO DO 6 : ตรวจสอบว่าหินชนยานผู้เล่นหรือไม่
    # ถ้าชนให้เริ่มเกมใหม่
    if not myShip.inv:
        hits = pg.sprite.spritecollide(myShip,meteors,True)
        if hits:
            new_game = True
    else:
        duration_tracker += clock.get_time()
        if duration_tracker > 3000:
            myShip.inv = False
            duration_tracker = 0
            font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
            font = pg.font.Font(font_name, 250)  # กำหนดขนาด font
            text_surface = font.render("BNK48", True, white)  # กำหนด Text และ สี
            text_rect = text_surface.get_rect()  # แปลง Surface เป็น object
            text_rect.midtop = (width/2, height/4)  # ระบุตำแหน่งของ text
            screen.blit(text_surface, text_rect)  # เอา Text ใส่ลงใน object ของ Text นั้น

    #################################################################################################
    # TO DO 4 : clear screen ด้วยสีดำ จากนั้น เอา bg ใส่ใน bg_rect
    screen.fill(black)
    screen.blit(bg,bg_rect)

    #################################################################################################
    # TO DO 7 : วาด element ใน all_sprites ลงใน screen
    all_sprites.draw(screen)
    #################################################################################################
    # after drawing everything, flip the display
    pg.display.flip()

pg.quit()

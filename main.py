def on_on_created(sprite):
    sprite.set_velocity(-50, 0)
    sprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
    music.change_tempo_by(10)
    music.set_tempo(90)
sprites.on_created(SpriteKind.enemy, on_on_created)

music.play_melody("", 90)
music.ba_ding.play()
def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 5 5 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 2 2 2 2 . . 2 2 2 2 . . . . 
                    . 2 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . 2 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 . . . . 
                    . . . 2 2 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 . . . . . . 
                    . . . . . 2 2 2 2 . . . . . . . 
                    . . . . . . 2 2 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 5 5 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        50,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
    sprite.start_effect(effects.star_field)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

enemySprite: Sprite = None
projectile: Sprite = None
music.ba_ding.loop()
mySprite: Sprite = None
mySprite2: Sprite = None
for index in range(11):
    mySprite2 = sprites.create(img("""
            . . . . . c c . . . . . . c c . 
                    . c c . . c 3 c . . c c . c 3 c 
                    . c 3 c c 3 3 c . . c 3 c 6 3 c 
                    . c 3 3 c 3 6 c . . c 3 6 3 3 c 
                    c c c 6 3 6 6 c . c c 3 3 3 c c 
                    3 3 c c 6 6 c 6 c 6 c 6 3 3 c c 
                    6 3 3 c c c 3 6 c 3 3 c c 6 c c 
                    3 6 3 3 6 3 3 c c c 3 c 3 6 c 6 
                    3 c 6 3 3 3 c c 3 c 3 c 3 3 c 3 
                    c c c 3 3 c 3 6 3 3 3 c c 3 6 3 
                    c c c 6 3 c 3 3 6 3 c 6 c 6 3 3 
                    6 3 c 6 3 6 c 3 3 3 c 3 3 c 3 6 
                    6 3 3 6 6 6 3 c 6 3 6 c 3 3 3 c 
                    c 6 3 3 6 3 c c c 3 6 c c 6 3 c 
                    c c 6 6 6 c c 6 c 6 3 c 6 6 6 c 
                    c c c 6 6 c c 6 6 6 c c 6 6 c c
        """),
        SpriteKind.player)
    mySprite2.set_position(16 * index, 100)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999999999999999999999999999999999999dd999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddd99999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddd99999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999ddddd9999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999999999999999999999999999999999ddddddd9999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999999999999999999999999999999999ddddddd9999999999999999999999999999999999999999999999999999999999dddddddddd99
        dd999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd99999999999999999999999999999999999999999999999999999999ddddddddddddd
        ddddd999999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd9999999999999999999999999999999999999999999999999999999dddddddddddddd
        dddddd99999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd9999999999999999999999999999999999999999999999999999999dddddddddddddd
        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd9999999999999999999999999999999999999999999999999999999dddddddddddddd
        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd999999999999999999999999999999999999999999999999ddddddddddddddddddddd
        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd99999999999999999999999999999999999999999999999dddddddddddddddddddddd
        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999ddddddddd999999999999999999999999999999999999999999999ddddddddddddddddddddddd
        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999ddddddddd999999999999999999999999999999999999999999999ddddddddddddddddddddddd
        ddddddd999999999999999999999999999999999ddd9999999999999999999999999999999999999999ddddddddd999999999999999999999999999999999999999999999dd7777777777777dddddddd
        ddddddd999999999999999999999999999999ddddddd999999999999999999999999999999999999999dddddddddd999999999999999999999999999999999999999977777777777777777777ddddddd
        ddddddd9999999999999999999999999999ddddddddd999999999999999999999999999999999999999dddddddddd9999999999999999999999999999999999999777777777777777777777777dddddd
        ddddddd99999999999999999999999999dddddddddddd99999999999999999999999999999999999999ddddddddddd999999999999977777777777777777777777777777777777777777777777dddddd
        ddddddd9999999999999999999999999ddddddddddddd9999999999999999999999999999999999999dddddddddddd977777777777777777777777777777777777777777777777777777777777dddddd
        ddddddd999999999999999999999999dddddddddddddd999999999999999999999999999999999999ddddddddddddd977777777777777777777777777777777777777777777777777777777777dddddd
        ddddddd999999999997999999999999dddddddddddddd999999999999999999999999999999999999ddddddddddddd777777777777777777777777777777777777777777777777777777777777dddddd
        ddddddd999997777777799999999999dddddddddddddd999999999999999999999999dd999999999dddddddddddddd777777777777777777777777777777777aa7777777777777777777777777dddddd
        ddddddd997777777777799999999999ddddddddddddddd9999999999999999999999ddddddd9999ddddddddddddddd77777777777777777777777777777777aaaaaa7777777777777777777777dddddd
        ddddddd77777777777779999999999dddddddddddddddd999999999999999999999dddddddddd99ddddddddddddddd7777777777777777777777777777777aaaaaaa7777777777777777777777dddddd
        ddddddd77777777777779999999999dddddddddddddddd999999999999999999999ddddddddddddddddddddddddddd7777777777777777777777777777777aaaaaaa7777777777777777777777dddddd
        ddddddd77777777777777999999999dddddddddddddddd999999999999999999999ddddddddddddddddddddddddddd777777777777777777777777777777aaaaaaaa7777777777777777777777dddddd
        ddddd7777777777777777999999999dddddddddddddddd99999999999999999999ddddddddddddddddddddddddddd777777777777777777777777777777aaaaaaaaa7777777777777777777777dddddd
        dddd77777777777777777999999ddddddddddddddddddd99999999999999999999ddddddddddddddddddddddddddd77777777777777777777777777777aaaaaaaaa77777777777777777777777dddddd
        dddd77777777777777777ddddddddddddddddddddddddd99ddd999999999999999ddddddddddddddddddddddddddd77777777777777777777777777777aaaaaaaa777777777777777777777777dddddd
        ddd777777777777777777ddddddddddddddddddddddddd99dddd99999999999999ddddddddddddddddddddddddddd7777777777777777777777777777aaaaaaaa7777777777777777777777777dddddd
        ddd777777777777777777dddddddddddddddddddddddddddddddd9999999999999dddddddddddddddddddddddddd7777777777777777777777777777aaaaaaaa777777777777777777777777777ddddd
        dd7777777777777777777ddddddddddddddddddddddddddddddddd999999999999dddddddddddddddddddddddddd777777777777777777777777777aaaaaaa77777777777777777777777777777ddddd
        dd7777777777777777777ddddddddddddddddddddddddddddddddd99999999999ddddddddddddddddddddddddddd77777777777777777777777777aaaaaaaaa7777777777777777777777777777ddddd
        d77777777777777777777ddddddddddddddddddddddddddddddddd99999999999dddddddddddddddddddddddddd777777777777777777777777777aaaaaaaaa7777777777777777777777777777ddddd
        d77777777777777777777ddddddddddddddddddddddddddddddddd99999999999ddddddddddddddddddddddddd777777777777777777777777777aaaaaaaaaa77777777777777777777777777777dddd
        d77777777777777777777dddddddddddd77777dddddddddddddddd99999999999dddddddddddddddddddddddd77777777777777777777777777777aaaaaaaaaa777777aaaaa77777777777777777dddd
        7777777777777777777777ddddddddddd7777777dddddddddddddd99999999999ddddddddddddddddddddddd777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaa777777777777777777
        7777777777777777777777dddddddddd77777777dddddddddddddd9999999999dddddddddddddddd77777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaa777777777777777777
        77777777777777777777777ddddddd77777777777dddddddddddddddddddddd9dddddddddddddd7777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa77777777777777777
        7777777777777777777777777dddd777777777777dddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        77777777777777777777777777777777777777777dddddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        77777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddddd7777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        77777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        7777777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        77777777777777777777777777777777777777777777777ddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        7777777777777777777777777777777777777777777777777dddddddddddddddddddddddddd77777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaa7777777777777777
        777777777777777777777777777777777777777777777777777dddddddddddddddddddddddd77777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaa7777777777777777
        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd77777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa77777777777777777
        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaa7777777777777777777777
        77777777777777777777777777777777777777777777777777777dddddddddddddddddddddd777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaa77777777777777777777
        77777777777777777777777777777777777777777777777777777777dddddddddddddddddd7777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaa7777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777dddddd7777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777777
        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777777
        ffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaa777777777777777777
        ffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaa7777777777777777777
        fffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaa77777777777777777777
        fffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaa7777777777777777777777
        fffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaa777777777777777777777
        fffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaa7777777777777777777
        ffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaa77777777777777777
        ffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        fffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        ffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaa7777777777777777
        ffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaa77777777777777777
        ffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaa7777777777777777777777777777777
        fffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaaaaaaaaaaaa7a7777777777777777777777777777
        fffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aa7777777777aaa7777777777777777777777777777
        ffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa777777777777777777777777777
        fffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa777777777777777777777777777
        ffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa777777777777777777777777777
        fffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa777777777777777777777777777
        ffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa777777777777777777777777777
        fffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa777777777777777777777777777
        ffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa77777777777777777777777777
        fffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa77777777777777777777777777
        ffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aa777777777777777777777777777
        ffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aa777777777777777777777777777
        ffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aa777777777777777777777777777
        ffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa77777777777777777777777777
        ffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa7777777777777777777777777
        ffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaa7777777777777777777777777
        ffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaa7777777777777777777777777
        ffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaaa7777777777777777777777777
        fffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa7777777777777777777777777
        fffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaaa7777777777777777777777777
        fffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777aaa77777777777777777777777777
"""))
mySprite = sprites.create(img("""
        ........................
            ......ffff..............
            ....fff22fff............
            ...fff2222fff...........
            ..fffeeeeeefff..........
            ..ffe222222eef..........
            ..fe2ffffff2ef..........
            ..ffffeeeeffff..........
            .ffefbf44fbfeff.........
            .fee41fddf14eef.........
            fdfeeddddd4eff..........
            fbffee444edd4e..........
            fbf4f2222edde...........
            fcf.f22cccee............
            .ff.f44cdc4f............
            ....fffddcff............
            .....fddcff.............
            ....cddc................
            ....cdc.................
            ....cc..................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.set_background_color(9)

def on_update_interval():
    global enemySprite
    enemySprite = sprites.create(img("""
            . . . f f f c c c . . . . . 
                    . f f 5 5 5 5 5 5 f f . . . 
                    . f 5 5 5 5 5 5 5 5 5 f . . 
                    f 5 5 5 5 5 5 5 5 5 5 5 c . 
                    f 5 5 b d 5 5 5 5 5 5 5 c . 
                    f 5 d 4 4 b 5 5 5 5 5 5 5 f 
                    f 5 b 4 4 4 c c 5 5 5 5 5 f 
                    f f f 4 4 c b c b 5 5 5 b f 
                    . f f d d c 1 e b b b b b c 
                    . . f d d d d 4 f b b b b c 
                    . . f 4 4 4 e e e 4 b b c . 
                    . . f 9 9 9 e d d 4 f f . . 
                    . . f 9 9 9 e d d e f . . . 
                    . f 3 3 b 3 b e e b f . . . 
                    . f f 3 b 3 b 3 b f f . . . 
                    . . . f f b b f f . . . . .
        """),
        SpriteKind.enemy)
    enemySprite.set_position(randint(0, 160), randint(0, 120))
game.on_update_interval(500, on_update_interval)

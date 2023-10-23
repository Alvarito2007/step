def on_gesture_shake():
    global paso
    paso += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

paso = 0
basic.show_string("Hey! Es hora de caminar tu meta de hoy son 20 pasos.")

def on_forever():
    basic.show_number(paso)
    if paso == 0:
        basic.pause(200)
        basic.show_string("Que pasa? dale tu puedes con !ANIMOS!")
        basic.pause(200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(200)
    if paso == 5:
        basic.pause(200)
        basic.show_string("Vamos tu puedes")
        basic.pause(200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            # # # # #
            """)
        basic.pause(200)
    if paso == 10:
        basic.pause(200)
        basic.show_string("Ya casiii")
        basic.pause(200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            # # # # #
            # # # # #
            """)
        basic.pause(200)
    if paso == 20:
        basic.pause(200)
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(200)
        music.play(music.string_playable("A B C5 A G A B C5 ", 120),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(200)
        basic.show_string("Epaa, has terminado tu meta diaria sigue asi :")
        basic.pause(200)
        if paso <= 20:
            basic.clear_screen()
basic.forever(on_forever)

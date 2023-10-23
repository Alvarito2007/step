input.onGesture(Gesture.Shake, function () {
    paso += 1
    led.stopAnimation()
})
let paso = 0
basic.showString("Hey! Es hora de caminar tu meta de hoy son 20 pasos.")
basic.forever(function () {
    basic.showNumber(paso)
    if (paso == 0) {
        basic.pause(200)
        basic.showString("Que pasa? dale tu puedes con !ANIMOS!")
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(200)
    }
    if (paso == 5) {
        basic.pause(200)
        basic.showString("Vamos tu puedes")
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            # # # # #
            `)
        basic.pause(200)
    }
    if (paso == 10) {
        basic.pause(200)
        basic.showString("Ya casiii")
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            # # # # #
            # # # # #
            `)
        basic.pause(200)
    }
    if (paso == 20) {
        basic.pause(200)
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(200)
        music.play(music.stringPlayable("A B C5 A G A B C5 ", 120), music.PlaybackMode.UntilDone)
        basic.pause(200)
        basic.showString("Epaa, has terminado tu meta diaria sigue asi :")
        basic.pause(200)
        if (paso <= 20) {
            basic.clearScreen()
        }
    }
})

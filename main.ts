let rand = 0
let players = 0
let current_player = 0
let step = -1
input.onPinPressed(TouchPin.P0, function start_game() {
    
    players = 2
    current_player = 1
    step = 0
    basic.showNumber(players)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (players > 2 && step == 0) {
        players = players - 1
        basic.showNumber(players)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (step == 0) {
        players = players + 1
        basic.showNumber(players)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    step += 1
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    if (step > 0) {
        if (current_player == 1) {
            basic.showString("Round:" + ("" + step))
        }
        
        basic.showString("Player:" + ("" + current_player))
        rand = randint(0, 1)
        if (rand) {
            basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # . . . #
            `)
        } else {
            basic.showLeds(`
            . # # # .
            . # . # .
            . # . # .
            # # # # #
            # . . . #
            `)
        }
        
        if (current_player < players) {
            current_player = current_player + 1
        } else {
            current_player = 1
            step = step + 1
        }
        
    }
    
})
function animation() {
    basic.clearScreen()
    let leds_xy = [[4, 2], [4, 3], [3, 4], [2, 4], [1, 4], [0, 3], [0, 2], [0, 1], [1, 0], [2, 0], [0, 3], [4, 1]]
}


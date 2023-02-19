rand = 0
players = 0
current_player = 0
step = -1

def start_game():
    global players, current_player, step
    players = 2
    current_player = 1
    step = 0
    basic.show_number(players)

input.on_pin_pressed(TouchPin.P0, start_game)

def on_button_pressed_a():
    global players, step
    if players > 2 and step == 0:
        players = players -1
        basic.show_number(players)

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global players, step
    if step == 0:
        players = players +1 
        basic.show_number(players)

input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global step
    step += 1 

input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global rand, players, current_player, step
    if step > 0:
        if current_player == 1:
            basic.show_string("Round:" + str(step))
        basic.show_string("Player:" + str(current_player))
        rand = randint(0, 1)
        animation
        if rand: 
            basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # . . . #
            """)
        else:
            basic.show_leds("""
            . # # # .
            . # . # .
            . # . # .
            # # # # #
            # . . . #
            """)
        if current_player < players:
            current_player = current_player + 1
        else:
            current_player = 1
            step = step + 1

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def animation():
    basic.clear_screen()
    leds_xy = [[4,2], [4,3], [3,4],
               [2,4], [1,4], [0,3],
               [0,2], [0,1], [1,0],               
               [2,0], [3,0], [4,1]]
    for xy in leds_xy:
        led.plot(xy[0], xy[1])
    for i in range(3):
        for xy1 in leds_xy:
            led.unplot(xy1[0], xy1[1])
            basic.pause(200)
            led.plot(xy1[0], xy1[1])

animation()
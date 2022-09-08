from sense_hat import SenseHat
from time import sleep
sense = SenseHat()


# Hiermee zeg je dat de leds op wit moeten staan en dat hij begint op positie 4 van de Y as van boven naar onder)
# Dus White heeft de RGB kleuren code 255, 255, 255 gekregen, ja het staat in RGB en het kan bijvoorbeeld ook in HSL. Meer kan je hier vinden. https://htmlcolorcodes.com/
white = (255, 255, 255)
blue = (0, 0, 255)
bat_y = 4

# Ook weer een variabel, dit keer is het met een INDEX
ball_position = [3, 3]
ball_velocity = [1, 1]
ball_colour = blue

# Deze functie maakt het streepje. (dE BaT)
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

# Deze functie verplaats het streepje naar BOVEN wanneer je op de joystick naar BOVEN DRUKT.
def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

sense.stick.direction_up = move_up

# Deze functie verplaats het streepje naar BENEDEN. wanneer je op de joystick naar BENEDEN DRUKT.
def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1


sense.stick.direction_down = move_down

# Dexe functie creeërt de bal. De kleur is blauw.
def draw_ball():
    # Hiermee zet ik de posite van de bal, in dit geval staat hij in het midden van het LED display.
    sense.set_pixel(ball_position[0], ball_position[1], blue)

    # += betekend dat ball_velocity de positie doorgeeft.toevoegd aan ball_position. += wil eigenlijk zeggen dat alles van de rechterkant van de OPERATOR wordt bijgevoegd aan de linkerkant van de OPERATOR.
    ball_position[0] += ball_velocity[0]

# Als positie van de bal gelijk is aan 7 of als balpositie gelijk is aan 0 dan... dan keert bal achteruit.
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]

# Velocity wordt toegevoegd aan de ball_position, met andere woorden de bal beweegt.
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]

# Dit is een loop, zolang het TRUE IS blijft
# hij de functies uitvoeren die er onder staan.
while True:
    draw_bat()
    sleep(0.25)
    sense.clear(0, 0, 0)
    draw_ball()
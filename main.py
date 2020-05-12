from time import sleep
import random

room_1_right_wall_broken = False
room_2_right_wall_broken = False
room_2_left_enemy_killed = False
npc_house_npc_killed = False
room_2_right_wall_hp = 3
player_hp = 5
room_2_left_enemy_hp = 2
boss_hp = 12
player_dmg = 1
player_move = ""
player_reaction_move = ""
dodged = None
word_delay = 0.#05
current_room = ""

def create_save():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    current_room = "start_game"
    save_1 = open(f"saves\\save_1.txt", "w")

    save_1.write("room_1_right_wall_broken:" + str(room_1_right_wall_broken) + " \n")
    save_1.write("room_2_right_wall_broken:" + str(room_2_right_wall_broken) + " \n")
    save_1.write("npc_house_npc_killed:" + str(npc_house_npc_killed) + " \n")
    save_1.write("player_hp:" + str(player_hp) + " \n")
    save_1.write("player_dmg:" + str(player_dmg) + " \n")
    save_1.write("current_room:" + str(current_room) + " \n")
    save_1.close()
    start_game()

def save_game():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    save_1 = open(f"saves\\save_1.txt", "w")

    save_1.write("room_1_right_wall_broken:" + str(room_1_right_wall_broken) + " \n")
    save_1.write("room_2_right_wall_broken:" + str(room_2_right_wall_broken) + " \n")
    save_1.write("npc_house_npc_killed:" + str(npc_house_npc_killed) + " \n")
    save_1.write("player_hp:" + str(player_hp) + " \n")
    save_1.write("player_dmg:" + str(player_dmg) + " \n")
    save_1.write("current_room:" + str(current_room) + " \n")
    save_1.close()

def load_game():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    save_1 = open(f"saves\\save_1.txt", "r")
    saved_variables = save_1.readlines()
    for i in saved_variables:
        if "room_1_right_wall_broken:" in i:
            room_1_right_wall_broken = eval(i[25:])
        elif "room_2_right_wall_broken:" in i:
            room_2_right_wall_broken = eval(i[25:])
        elif "npc_house_npc_killed:" in i:
            npc_house_npc_killed = eval(i[21:])
        elif "player_hp:" in i:
            player_hp = int(i[10:])
        elif "player_dmg:" in i:
            player_dmg = float(i[11:])
        elif "current_room:" in i:
            current_room = i[13:]
    save_1.close()
    eval(current_room)()

def play_game():
    choice = valid_input("What would you like to do?\n Start New Save\n Load a Save", ["new", "load", "start"]).lower()
    if "new" in choice or "start" in choice:
        create_save()
    else:
        load_game()

def available_commands():
    global current_room
    global npc_house_npc_killed
    if current_room == "npc_house" and "npc_house_npc_killed" == False:
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Talk\n Exit to Title\n Help")
        current_room()
    elif current_room == "room_3_town":
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Enter House\n Exit to Title\n Help")
        current_room()
    else:
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Exit to Title\n Help")
        current_room()

def exit_to_title():
    global current_room
    answer = valid_input("Are you sure you want to exit the game?\n Yes\n No", ["yes", "no"])
    if "yes" in answer:
        save_game()
        title_screen()
    else:
        delayed_print_words(f"goes to {current_room}")
        eval(current_room)()

def delayed_print_words(text):
    for char in text:
        sleep(word_delay)
        print(char, end="")
    sleep(0.5)
    print("")
    return ""

def valid_input(input_text, options=[]):
    while True:
        sleep(word_delay)
        response = input(delayed_print_words(input_text)).lower()
        for option in options:
            if option in response:
                return response
        delayed_print_words("That isn't a response i know what to do with. \nPlease check your spelling and try again.")
        delayed_print_words("For a list of Commands enter Help")

def title_screen():
    delayed_print_words("Title Screen:")
    choice = valid_input("What would you like to do?\n Play Game\n Settings\n Close Game", ["play", "play game", "settings", "close", "close game"]).lower()
    if  "play" in choice:
        play_game()
    elif "settings" in choice:
        settings()
    else:
        exit()

def is_float(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    return True

def settings():
    delayed_print_words("Settings:")
    choice = valid_input("What would you like to do?\n Change The Text Speed\n Exit to the Title Screen", ["text", "speed", "exit"]).lower()
    if "text" in choice or "speed" in choice:
        set_text_speed()
    else:
        title_screen()

def set_text_speed():
    global word_delay
    delayed_print_words("Please input the text speed you want:")
    text_speed = input()
    if text_speed > 2:
        delayed_print_words("That number is to High")
        set_text_speed()
    elif is_float(text_speed):
        word_delay = float(text_speed)
        settings()
    else:
        delayed_print_words("That isn't a number.\nPlease enter a number.")
        set_text_speed()

def room_1():
    global current_room
    current_room = "room_1"
    delayed_print_words("Room 1 Description")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to room 1 left")
        room_1_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to room 1 right")
        room_1_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("Goes to room 1 left")
        room_1_left()
    elif "right" in action:
        delayed_print_words("goes to room 1 right with wall unbroken")
        room_1_right()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 1")
        room_1()
    elif "exit" in action:
        exit_to_title()
    else:
        delayed_print_words("Swings nail, goes to room 1")
        room_1() 

def room_1_left():
    global current_room
    current_room = "room_1_left"
    delayed_print_words("room 1 left description")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("faceplants wall goes to room 1 left")
        room_1_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to room 1")
        room_1()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("Walks into wall goes to room 1 left")
    elif "right" in action:
        delayed_print_words("goes to room 1")
        room_1()
    elif "jump" in action:
        delayed_print_words("Jumps, goes to room 1 left")
        room_1_left()
    elif "exit" in action:
        exit_to_title()
    else:
        delayed_print_words("Swings nail, goes to room 1 left")
        room_1_left()

def room_1_right():

    global room_1_right_wall_broken
    global current_room
    current_room = "room_1_right" 

    if room_1_right_wall_broken == False:
        delayed_print_words("room 1 right description with wall unbroken")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "right", "left", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("jumps to room 1")
            room_1()
        elif "right" in action and "jump" in action:
            delayed_print_words("faceplants wall goes to room 1 right")
            room_1_right()
        elif "help" in action:
            available_commands()
        elif "right" in action:
            delayed_print_words("walks into wall goes to room 1 right")
            room_1_right()
        elif "left" in action:
            delayed_print_words("Goes to room 1")
            room_1()
        elif "jump" in action:
            delayed_print_words("Jumps, goes to room 1 right")
            room_1_right()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("Swings nail, goes to room 1 right with wall broken")
            room_1_right_wall_broken = True
            room_1_right()

    if room_1_right_wall_broken == True:
        delayed_print_words("room 1 right description with wall broken")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("jumps to room 1")
            room_1()
        elif "right" in action and "jump" in action:
            delayed_print_words("jumps, goes to room 1 right")
            room_1_right()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to room 1")
            room_1()
        elif "jump" in action:
            delayed_print_words("Jumps, goes to room 1 right")
            room_1_right()
        elif "attack" in action:
            delayed_print_words("swings nail, goes to room 1 right")
            room_1_right()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("goes to room 2 far left")
            room_2_far_left()
            
def room_2_far_left():
    global current_room
    current_room = "room_2_far_left"
    if room_2_left_enemy_killed == False:
        delayed_print_words("room 2 far left description with enemy alive")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("jumps slightly to the left goes to room 2 far left")
            room_2_far_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("jumps slightly to the right goes to room 2 far left")
            room_2_far_left()
        elif "help" in action:
            available_commands()
        elif "right" in action:
            delayed_print_words("goes to room 2 left")
            room_2_left()
        elif "left" in action:
            delayed_print_words("goes to room 1 right")
            room_1_right()
        elif "jump" in action:
            delayed_print_words("jumps, goes to room 2 far left")
            room_2_far_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("Swings Nail, goes to room 2 far left")
            room_2_far_left()
    else:
        delayed_print_words("room 2 far left description with enemy killed")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("jumps slightly to the left goes to room 2 far left")
            room_2_far_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("jumps slightly to right goes to room 2 far left")
            room_2_far_left()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to room 1 right")
            room_1_right()
        elif "right" in action:
            delayed_print_words("goes to room 2 left with enemy killed")
            room_2_left()
        elif "jump" in action:
            delayed_print_words("jumps, goes to room 2 far left")
            room_2_far_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("Swings nail, goes to room 2 far left")
            room_2_far_left()
    
def room_2_left():
    global current_room
    current_room = "room_2_left"
    delayed_print_words("room 2 left description")
    if room_2_left_enemy_killed == False:
        first_combat_players_turn()
        delayed_print_words("goes to room 2 left")
        room_2_left()
    else:
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("jumps slightly to the left goes to room 2 left")
            room_2_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("jumps slightly to right goes to room 2 left")
            room_2_left()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to room 2 far left")
            room_2_far_left()
        elif "right" in action:
            delayed_print_words("goes to room 2 right")
            room_2_right()
        elif "jump" in action:
            delayed_print_words("Jumps, goes to room 2 left")
            room_2_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("Swings nail, goes to room 2 left")
            room_2_left()

def first_combat_players_turn():
    global player_dmg
    global player_hp
    global room_2_left_enemy_hp
    global room_2_left_enemy_killed
    global player_move
    global current_room
    current_room = "first_combat_players_turn"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title screen")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif room_2_left_enemy_hp <= 0:
        delayed_print_words("Describe enemy death, goes to room 2 left with enemy killed")
        room_2_left_enemy_killed = True
        room_2_left()
    delayed_print_words("Describe enemy")
    delayed_print_words(f"Your HP:{player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to room 2 far left")
        player_move = "jump"
        first_combat_enemies_turn()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to in pit")
        in_pit()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 2 far left")
        room_2_far_left()
    elif "right" in action:
        delayed_print_words("takes 1 damage")
        delayed_print_words("it becomes enemies turn with player move set to right")
        player_hp -= 1
        player_move = "right"
        first_combat_enemies_turn()
    elif "jump" in action:
        delayed_print_words("Jumps out of way, it becomes enemies turn with player move set to jump")
        player_move = "jump"
        first_combat_enemies_turn()
    elif "attack" in action:
        delayed_print_words("Deal 1 damage to enemy and it becomes enemies turn with player move set to attack")
        room_2_left_enemy_hp -= player_dmg
        player_move = "attack"
        first_combat_enemies_turn()
    else:
        exit_to_title()
      
def first_combat_enemies_turn():

    global player_hp
    global room_2_left_enemy_hp
    global room_2_left_enemy_killed
    global player_move

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif room_2_left_enemy_hp <= 0:
        delayed_print_words("Describe enemy death, goes to room 2 left with enemy killed")
        room_2_left_enemy_killed = True
        room_2_left()
    if player_move == "attack":
        delayed_print_words("Describe enemy as dazed, goes to first combat players turn with both hp unchanged")
        first_combat_players_turn()
    elif player_move == "jump":
        delayed_print_words("Describe player jumping out of way, goes to first combat players turn with both hp unchanged")
        first_combat_players_turn()
    else:
        delayed_print_words("describe enemy damaging player, goes to first combat players turn with players hp -= 1 and enemy hp unchanged")
        player_hp -= 1
        first_combat_players_turn()

def room_2_right():
    global current_room
    current_room = "room_2_right"
    delayed_print_words("room 2 right description with pit")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("goes to room 2 left with enemy killed")
        room_2_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("goes to room 2 far right")
        room_2_far_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 2 left")
        room_2_left()
    elif "right" in action:
        delayed_print_words("goes to in pit")
        in_pit()
    elif "jump" in action:
        delayed_print_words("Jumps, goes to room 2 right")
        room_2_right()
    elif "attack" in action:
        delayed_print_words("Attacks, goes to room 2 right")
        room_2_right()
    else:
        exit_to_title()

def in_pit():
    global current_room
    current_room = "in_pit"
    delayed_print_words("pit description")
    if room_2_right_wall_broken == False: 
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("goes to room 2 right")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("goes to room 2 far right")
            room_2_far_right()
        if "left" in action:
            delayed_print_words("walks into edge of pit goes to in pit")
            in_pit()
        elif "right" in action:
            delayed_print_words("walks into edge of pit goes to in pit")
            in_pit()
        elif "help" in action:
            available_commands()
        elif "jump" in action:
            delayed_print_words("jumps, goes to in pit")
            in_pit()
        elif "attack" in action:
            delayed_print_words("swings nail, goes to in pit")
            in_pit()
        else:
            exit_to_title()

def room_2_far_right():

    global room_2_right_wall_hp
    global room_2_right_wall_broken
    global current_room
    current_room = "room_2_far_right"

    if room_2_right_wall_broken == False:
        if room_2_right_wall_hp == 0:
            room_2_right_wall_broken = True
            room_2_far_right()
        delayed_print_words("room 2 right description with wall unbroken")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "jump" in action and "left" in action:
            delayed_print_words("jumps, goes to room 2 right")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("faceplants wall deals 1 damage to wall goes to room 2 far right")
            room_2_right_wall_hp -= 1
            room_2_far_right()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to in pit")
            in_pit()
        elif "right" in action:
            delayed_print_words("walks into wall goes to room 2 far right")
            room_2_far_right()
        elif "jump" in action:
            delayed_print_words("jumps, goes to room 2 far right")
            room_2_far_right()
        elif "attack" in action:
            delayed_print_words("attacks wall with nail, deals 1 damage to wall, goes to room 2 far right")
            room_2_right_wall_hp -= 1
            room_2_far_right()
        else:
            exit_to_title()
    else:
        delayed_print_words("room 2 right description with wall broken")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "right", "left", "jump", "attack", "exit"])
        if "jump" in action and "left" in action:
            delayed_print_words("jumps, goes to room 2 right")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("goes to room 3 cliff")
            room_3_cliff()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to in pit")
            in_pit()
        elif "right" in action:
            delayed_print_words("goes to room 3 cliff")
            room_3_cliff()
        elif "jump" in action:
            delayed_print_words("jumps, goes to room 2 far right")
            room_2_far_right()
        elif "attack" in action:
            delayed_print_words("swings nail, goes to room 2 far right")
            room_2_far_right()
        else:
            exit_to_title()

def room_3_cliff():
    global current_room
    current_room = "room_3_cliff"

    delayed_print_words("room 3 cliff description")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("goes to room 2 far right")
        room_2_far_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("goes to room 3 left")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 2 far right")
        room_2_far_right()
    elif "right" in action:
        delayed_print_words("goes to room 3 left")
        room_3_left()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 3 cliff")
        room_3_cliff()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 3 cliff")
        room_3_cliff()
    else:
        exit_to_title()

def room_3_left():
    global current_room
    current_room = "room_3_left"

    delayed_print_words("room 3 left description")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("faceplants wall goes to room 3 left")
        room_3_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 3 left")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("walks into wall goes to room 3 left")
        room_3_left()
    elif "right" in action:
        delayed_print_words("goes to room 3 town")
        room_3_town()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 3 left")
        room_3_left()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 3 left")
        room_3_left()
    else:
        exit_to_title()

def room_3_town():
    global current_room
    current_room = "room_3_town"

    delayed_print_words("room 3 town description")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit", "go into", "enter", "house"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps slightly to the left goes to room 3 town")
        room_3_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 3 town")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 3 left")
        room_3_left()
    elif "right" in action:
        delayed_print_words("goes to room 3 right")
        room_3_right()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 3 town")
        room_3_town()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 3 town")
        room_3_town()
    elif "enter" in action or "go into" in action or "house" in action:
        delayed_print_words("goes to npc house")
        npc_house()
    else:
        exit_to_title()

def npc_house():
    global npc_house_npc_killed
    global player_dmg
    global current_room
    current_room = "npc_house"
    if npc_house_npc_killed == False:
        delayed_print_words("npc house description with npc alive")
        action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit", "talk", "speak"])
        if "left" in action and "jump" in action:
            delayed_print_words("hits head goes to npc house")
            npc_house()
        elif "right" in action and "jump" in action:
            delayed_print_words("hits head, goes to npc house")
            npc_house()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to room 3 town")
            room_3_town()
        elif "right" in action:
            delayed_print_words("walks into wall of house, goes to npc house")
            npc_house()
        elif "jump" in action:
            delayed_print_words("hits head, goes to npc house")
            room_3_town()
        elif "attack" in action:
            delayed_print_words("kills npc, goes to npc house")
            npc_house_npc_killed = True
            npc_house()
        elif "talk" in action or "speak" in action and player_dmg == 1:
            delayed_print_words("talks to npc, npc gives better weapon, goes to npc house")
            player_dmg = 1.5
            npc_house()
        elif "talk" in action or "speak" in action:
            delayed_print_words("npc tells player they have nothing more to give, goes to npc house")
            npc_house()
        else:
            exit_to_title()
    else:
        delayed_print_words("npc house description with npc dead")
        action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("hits head goes to npc house")
            npc_house()
        elif "right" in action and "jump" in action:
            delayed_print_words("hits head, goes to npc house")
            npc_house()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("goes to room 3 town")
            room_3_town()
        elif "right" in action:
            delayed_print_words("walks into wall of house, goes to npc house")
            npc_house()
        elif "jump" in action:
            delayed_print_words("hits head, goes to npc house")
            room_3_town()
        elif "attack" in action:
            delayed_print_words("swings nail, goes to npc house")
            npc_house()
        else:
            exit_to_title()

def room_3_right():
    global current_room
    current_room = "room_3_right"

    delayed_print_words("room 3 right description")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps slightly to the left, goes to room 3 right")
        room_3_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right, goes to room 4 left")
        room_4_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 3 town")
        room_3_town()
    elif "right" in action:
        delayed_print_words("goes to room 4 left")
        room_4_left()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 3 right")
        room_3_right()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 3 right")
        room_3_right()
    else:
        exit_to_title()

def room_4_left():
    global current_room
    current_room = "room_4_left"

    delayed_print_words("room 4 left description")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left, goes to room 3 right")
        room_3_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 4 left")
        room_4_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 3 right")
        room_3_right()
    elif "right" in action:
        delayed_print_words("goes to room 4 boss room")
        room_4_boss_room()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 4 left")
        room_4_left()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 4 left")
        room_4_left()
    else:
        exit_to_title()

def room_4_boss_room():
    global current_room
    current_room = "room_4_boss_room"

    delayed_print_words("room 4 boss room description")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left, goes to room 4 boss room")
        room_4_boss_room()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 4 boss room")
        room_4_boss_room()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 4 left")
        room_4_left()
    elif "right" in action:
        delayed_print_words("goes to room 4 boss fight")
        room_4_boss_fight()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 4 boss room")
        room_4_boss_room()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 4 boss room")
        room_4_boss_room()
    else:
        exit_to_title()

def room_4_boss_fight():
    delayed_print_words("boss fight starting description")
    boss_fight_players_turn_boss_right()

def boss_fight_players_turn_boss_right():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_players_turn_boss_right"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen() 
    delayed_print_words("boss on right description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("takes 1 damage, goes to boss turn player on left")
        player_hp -= 1
        boss_fight_boss_turn_player_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "right" in action:
        delayed_print_words("takes 1 damage, goes to boss turn player on left")
        player_hp -= 1
        boss_fight_boss_turn_player_left()
    elif "jump" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "attack" in action:
        delayed_print_words("boss takes player damage goes to boss turn player on left")
        boss_hp -= player_dmg
        boss_fight_boss_turn_player_left()
    else:
        exit_to_title()

def boss_fight_players_turn_boss_left():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_players_turn_boss_left"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on left description")
    delayed_print_words(f"Reads Player Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("player takes 1 damage, goes to boss turn player right")
        player_hp -= 1
        boss_fight_boss_turn_player_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("player takes 1 damage, goes to boss turn player right")
        player_hp -= 1
        boss_fight_boss_turn_player_right()
    elif "right" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "jump" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "attack" in action:
        delayed_print_words("boss takes player damage goes to boss turn player on right")
        boss_hp -= player_dmg
        boss_fight_boss_turn_player_right()
    else:
        exit_to_title()

def boss_fight_boss_turn_player_left():
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global dodged
    global player_reaction_move

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()

    boss_move = random.choice(["Slam", "Jump Crush"])
    if boss_move == "Slam":
        delayed_print_words("boss winds up slam")
        dodged = boss_fight_player_reaction_boss_right()
        if dodged:
            boss_fight_players_turn_boss_right()
        else:
            player_hp -= 1
            boss_fight_players_turn_boss_right()
    else:
        delayed_print_words("boss jumps above player")
        dodged = boss_fight_player_reaction_boss_in_air()
        if dodged:
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()

def boss_fight_boss_turn_player_right():
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global dodged
    global player_reaction_move

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()

    boss_move = random.choice(["Slam", "Jump Crush"])
    if boss_move == "Slam":
        delayed_print_words("boss winds up slam")
        dodged = boss_fight_player_reaction_boss_left()
        if dodged:
            boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            boss_fight_players_turn_boss_left()
    else:
        delayed_print_words("boss jumps above player")
        dodged = boss_fight_player_reaction_boss_in_air()
        if dodged:
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()

def boss_fight_player_reaction_boss_in_air():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global player_reaction_move
    current_room = "boss_fight_player_reaction_boss_in_air"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss in air description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        player_reaction_move = "left"
        return False
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        player_reaction_move = "right"
        return False
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        player_reaction_move = "left"
        return True
    elif "right" in action:
        delayed_print_words("goes right")
        player_reaction_move = "right"
        return True
    elif "jump" in action:
        delayed_print_words("jumps")
        player_reaction_move = "under"
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        player_reaction_move = "under"
        return False
    else:
        exit_to_title()

def boss_fight_player_reaction_boss_left():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_player_reaction_boss_left"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on left winding up slam attack description")
    delayed_print_words(f"Reads Player Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        return False
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        return True
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        return False
    elif "right" in action:
        delayed_print_words("goes right")
        return True
    elif "jump" in action:
        delayed_print_words("jumps")
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        return False
    else:
        exit_to_title()

def boss_fight_player_reaction_boss_right():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_player_reaction_boss_right"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on right winding up slam attack description")
    delayed_print_words(f"Reads Player Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        return True
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        return False
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        return True
    elif "right" in action:
        delayed_print_words("goes right")
        return False
    elif "jump" in action:
        delayed_print_words("jumps")
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        return False
    else:
        exit_to_title()

def start_game():
    delayed_print_words("reads intro")#"You fall into the unknown, all you know is your mission is to kill some large beast plagueing this land."
    delayed_print_words("continues intro")#"Suddenly you hit the ground, Hard, but weirdly you don't feel any pain."
    delayed_print_words("finishes intro")#"You notice something a bit heavy hanging at your side, you look down and see what looks to be a nail around the size of a sword.\nInspecting this nail closer reveals that it has a few imperfections but you think you should be able to use it if you have to defend yourself."
    delayed_print_words("goes to room 1")
    room_1()

title_screen()
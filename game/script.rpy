# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Unknown = Character("Unknown")

screen test:
    text "Dah selesai" at muncul:
        xalign 0.5
        yalign 0.5

transform terkenaserang:
    zoom 1.0
    xalign 0.5
    yalign 1.0
    block:
        ease 0.05 zoom 1.02
        yalign 1.01
        xalign 0.51
        ease 0.05 zoom 1.0
        yalign 1.0
        xalign 0.5
        repeat 2

transform hilang:
    linear .5 alpha 0.0

transform muncul:
    linear .5 alpha 1.0 

transform mantul:
    ease_bounce 0.5 zoom 1.5
    ease_expo 1.0 zoom 0.5
    ease_bounce 0.5 zoom 1.0

transform melayang:
    parallel:
        easein 5 yoffset -1500
    parallel:
        linear .1 rotate 360 
        rotate 0
        repeat

transform muncul2:
    parallel:
        linear .5 alpha 1.0 
    parallel:
        easein 5 yoffset 1500 

transform muncul3:
    subpixel True
    linear .5 alpha 1.0 
    #yoffset 100
    parallel:
        easein 5 yalign 1.0 zoom 1.1
    parallel:
        linear 5 rotate 0
    parallel:
        ease 5 zoom 5 
    parallel:
        ease 5 yoffset 3500 xalign 0.35 

transform terkenaserang2:
        ease 0.05 zoom 5.1
        yoffset 3550
        xalign 0.351
        ease 0.05 zoom 5.0
        yoffset 3500
        xalign 0.35
        repeat 2

transform mati:
    parallel:
        ease 0.05 zoom 5.1
        xalign 0.351
        ease 0.05 zoom 5.0
        xalign 0.35
        repeat 
    parallel:
        ease 8 yoffset 7000
    
    
image serang1:
    zoom 0.5
    yalign 0.5
    "serangan1.1.gif"
    pause 0.1
    "serangan1.2.gif"
    pause 0.1
    "serangan1.3.gif"
    pause 0.1
    "serangan1.4.gif"
    pause 0.1
    "serangan1.5.gif"
    pause 0.1
    "serangan1.6.gif"
    pause 0.1
    repeat    


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    Unknown "Hello"

    window hide

    show unknown base at terkenaserang

    show serang1:
        xalign 0.5
        zoom 1.5

    pause 0.5

    hide serang1

    # These display lines of dialogue.

    pause 0.2

    Unknown "Ouch"

    show unknown base at hilang

    Unknown "Aku menghilang"

    show unknown base at muncul

    Unknown "Aku muncul"

    show unknown base at mantul

    Unknown "Hehe"

    show unknown base at melayang

    Unknown "Haha"
        
    show unknown base at muncul2

    Unknown "LOL"

    show unknown base at muncul3

    Unknown "Aku Kembali"

    Unknown "Satu satunya manusia yang hidup di bumi ini adalah Impusm!"

    show unknown base at terkenaserang2

    show serang1:
        xalign 0.5
        zoom 1.5

    pause 0.5

    hide serang1

    # These display lines of dialogue.

    pause 0.2

    Unknown "Dahla"
    
    show unknown base at mati

    "Musuh mu mati"

    window hide

    centered "Dah selesai" with dissolve

    # This ends the game.

    return

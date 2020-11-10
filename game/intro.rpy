init python:
    for i in range(1, 13):
        renpy.image("intro_" + str(i), "/images/Intro/Prolog/" + str(i) + ".jpg")

screen toprightmenu:

    #key "c" action Show("scr_settings")
    #key "r" action ShowMenu("gallery")

    #imagebutton:
        #idle "p corrupt[v_corruption]_idle" hover "p corrupt[v_corruption]_hover" xalign 0.98 yalign 0.01 action [Show("scr_settings"),renpy.restart_interaction]
    imagebutton:
        xpos 1775
        ypos 5
        focus_mask True
        idle Transform("images/buttons/stat_idle.png", zoom=1)
        hover Transform("images/buttons/stat_hover.png", zoom=1)
        clicked Jump("info_1")
    #imagebutton:
        #idle "p_stat_l" xalign 0.97 yalign 0.26
    #imagebutton:
        #idle "p progress" xalign 0.01 yalign 0.01
    #imagebutton:
        #idle "btn options_0" hover "btn options_1" xalign 0.01 yalign 0.01 action ShowMenu("save")
    #imagebutton:
        #idle "b_button_idle" hover "b_button_hover" xalign 0.98 yalign 0.28 action ShowMenu("gallery")
    #text "Day [v_days]" xalign 0.065 yalign 0.035

label intro:
    $ can_hide_windows = True
    stop music
    scene black with dissolve
    $ mc = renpy.input(
        "Ana karakterin ismi Josh'dur, isterseniz bunu değiştirebilirsiniz, istediğiniz ismi girin:",
        default="Josh"
        ).strip().title()

    scene intro_1 with dissolve
    play music "sfx/Intro_music.mp3"
    if incest == True:
        "Your name is [mc] and you're a young uncle who's looking after his niece Milly."
    if incest == False:
        "Your name is [mc] and you're a guy taking care of a friend's daughter, her name is Milly."
    scene intro_2 with dissolve
    "This is Milly. She's a shy, but lovely, girl."
    "Due to job obligations, Milly's parents relocated overseas."
    "Not wanting her to have to start over completely in a foreign country, her parents wanted to her to stay in the place she knew well, the place where she has roots. The place where she has friends and family."
    "Her parents asked if she could stay with you, if you would look after her and follow her education, and you agreed to let her stay with you."
    "While following Milly's studies, you met someome special."
    scene intro_3 with dissolve
    "Milly's teacher, Linda."
    "Your relationship with Linda was kept secret, even from Milly, to keep Milly from facing any repercussions because her uncle and her teacher were in an intimate relationship."
    scene intro_4 with dissolve
    "After a while, Milly returned to her parents. She's sad to be without you."
    scene intro_5 with dissolve
    "With Milly's absence, the relationship between you and Linda became pretty serious. Linda would even sleep over at your place on occasion."
    "Until..."
    scene intro_6 with dissolve
    $ renpy.pause (2)
    stop music
    play music "sfx/Music1.mp3"
    scene intro_7 with dissolve
    mc "{i}(Always the same news...){/i}"
    play sound "sfx/Door-bell.mp3"
    "{i}Door bells{/i}"
    mc "???"
    mc "{i}(Is that Linda?){/i}"
    scene intro_8
    mc "{i}(It's unusual for her to come by at this time of day.){/i}"
    scene intro_9
    menu:
        "Open the door":
            play sound "sfx/Door_Open.mp3"
            stop music
            play music "sfx/Music2.mp3"
            scene intro_10 with dissolve
            $ renpy.pause (2)
            mc "{i}(Oh!){/i}"
            mc "M-Milly?!"
            scene intro_11
            if incest == True:
                ml "Hey, Uncle! It's so nice to see you again. I've missed you!"
            if incest == False:
                ml "Hey, [mc]! It's so nice to see you again. I've missed you!"
            scene intro_10
            mc "I've missed you too, Milly! I wasn't expecting you at all. In fact... what are you doing here?"
            menu:
                "Come on in":
                    mc "Come on in, Milly, don't stay outside."
                    scene intro_12
                    if incest == True:
                        ml "Oh, thank you, Uncle."
                    if incest == False:
                        ml "Oh, thank you, [mc]."
                    jump d01_intro_comein

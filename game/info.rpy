image info_1 = "images/buttons/info_1.jpg"

screen info_1:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1800
        ypos 25
        focus_mask True
        idle Transform("images/buttons/exit_info_idle.png")
        hover Transform("images/buttons/exit_info_hover.png")
        clicked Rollback()

    imagebutton:
        xpos 100
        ypos 250
        focus_mask True
        idle Transform("images/buttons/Milly_info_idle.png")
        #hover Transform("images/game_gui/Ary_info_hover.png")
        #clicked Jump("info_Ary")

    python:
        ml_friendship = ml_attr.get_friendship()
        ml_love = ml_attr.get_love()

    vbox:
        xpos 300
        ypos 300

        text _("{b}Friendship: {b}[ml_friendship]")size 40
        text _("{b}Love: {b}[ml_love]")size 40

    if Linda == True:
        imagebutton:
            xpos 100
            ypos 500
            focus_mask True
            idle Transform("images/buttons/Linda_info_idle.png")
            #hover Transform("images/game_gui/Ary_info_hover.png")
            #clicked Jump("info_Ary")

        python:
            ld_friendship = ld_attr.get_friendship()
            ld_love = ld_attr.get_love()

        vbox:
            xpos 300
            ypos 550

            text _("{b}Friendship: {b}[ld_friendship]")size 40
            text _("{b}Love: {b}[ld_love]")size 40


label info_1:
    $ can_hide_windows = False
    hide screen date1
    hide screen date2
    hide screen displayTextScreen
    hide screen toprightmenu
    scene info_1 with dissolve
    call screen info_1

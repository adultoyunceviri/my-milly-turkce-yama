image day2 = "/images/buttons/day2.jpg"
init python:
    for i in range(1, 44):
        renpy.image("d02_mcbed1_" + str(i), "/images/Day02/d02_mcbed1_" + str(i) + ".jpg")
image d02_mcbed1_44 = Movie (play="/images/Day02/d02_mcbed1_44.mpg")
image d02_mcbed1_45 = Movie (play="/images/Day02/d02_mcbed1_45.mpg")
image d02_mcbed1_46 = Movie (play="/images/Day02/d02_mcbed1_46.mpg")
init python:
    for i in range(47, 52):
        renpy.image("d02_mcbed1_" + str(i), "/images/Day02/d02_mcbed1_" + str(i) + ".jpg")

define flash = Fade(.90, 1, .50, color="#fff")

screen date2:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 20
        ypos 10
        focus_mask True
        idle Transform("images/buttons/day2.png")

label d02_mcroom1_1:
    hide screen toprightmenu
    hide screen date1
    stop music
    scene day2 with dissolve
    $ renpy.pause (2)
    scene d02_mcbed1_1 with dissolve
    show screen date2
    show screen toprightmenu
    mc "zzzz...zzzz..."
    scene d02_mcbed1_2 with dissolve
    play sound "sfx/Phone_Ringing.mp3" loop
    "{i}Smartphone rings{/i}"
    menu:
        "Answer the call":
            mc "{i}(Better answer...){i}"
            scene d02_mcbed1_13
            mc "{i}(Oh, it's Linda!){i}"
            stop sound
            scene d02_mcbed1_15
            mc "Hello, Linda. Is everything alright?"
            scene d02_mcbed1_14
            ld "Hello, love! Just calling you to talk for a bit. I won't be able to come by today, I have so much work to do, so I'll be at work until late."
            scene d02_mcbed1_15
            mc "Don't worry, I have plenty of work to do myself. We'll see each other tomorrow."
            scene d02_mcbed1_14
            mc "{i}(Phew, dodged a bullet there since Milly's here. I have to make sure Linda doesn't get suspicious of anything. I hope Milly won't be staying here for very long.){i}"
            ld "Okay, I look forward to being with you."
            scene d02_mcbed1_15
            mc "Me too. I'll talk to you later."
            scene d02_mcbed1_14
            ld "I can't wait see you again, love."
            scene d02_mcbed1_15
            mc "Me too, bye."
            scene d02_mcbed1_14
            mc "{i}(I should get a little more sleep.){i}"
            scene black with dissolve
            "A FEW MINUTES LATER"
            scene d02_mcbed1_1 with dissolve
            $ renpy.pause (1)
            play sound "sfx/Door-bell.mp3"
            "{i}Door bells{/i}"
            mc "zzzz...uhm??"
            play sound "sfx/Door-bell.mp3"
            "{i}Door bells{/i}"
            stop sound
            mc "Yaaawn..."
            scene d02_mcbed1_3
            mc "{i}(Who will be ringing the bell in the morning?){i}"
            jump d02_mcroom1_2

        "Don't answer the call":
            "zzzz....zzzzz..."
            stop sound
            scene black with dissolve
            "A FEW MINUTES LATER"
            scene d02_mcbed1_1 with dissolve
            $ renpy.pause (1)
            play sound "sfx/Door-bell.mp3"
            "{i}Door bells{/i}"
            mc "zzzz...uhm??"
            play sound "sfx/Door-bell.mp3"
            "{i}Door bells{/i}"
            stop sound
            mc "Yaaawn..."
            scene d02_mcbed1_3
            mc "{i}(Who will be ringing the bell in the morning?){i}"
            jump d02_mcroom1_3

label d02_mcroom1_2:
    scene d02_mcbed1_4 with dissolve
    play sound "sfx/Door_Open.mp3"
    scene d02_mcbed1_5 with dissolve
    $ Linda = True
    ld "Surprise!"
    play sound "sfx/Disco.wav"
    scene d02_mcbed1_6
    play music "sfx/Music5.mp3"
    mc "Linda...what are you doing here?"
    scene d02_mcbed1_5
    ld "I wanted to give you a little surprise before going to work."
    scene d02_mcbed1_6
    mc "Oh, thank you!"
    mc "{i}(I hope she doesn't find out that Milly's here.){i}"
    scene d02_mcbed1_11
    ld "You won't let me in?"
    scene d02_mcbed1_12
    mc "Oh! Sure, though I was just about to leave..."
    scene d02_mcbed1_11
    ld "Don't worry, I'm not staying long, I have to go to work."
    scene d02_mcbed1_16 with dissolve
    $ renpy.pause (1)
    scene d02_mcbed1_18 with dissolve
    mc "Do you want something?"
    scene d02_mcbed1_17
    ld "In fact I would like something..."
    scene d02_mcbed1_20
    ld "...I want you!"
    scene d02_mcbed1_21
    mc "What?"
    scene d02_mcbed1_20
    ld "Don't be silly, you know what I mean."
    scene d02_mcbed1_19
    mc "{i}(Oh no, what if Milly wakes up? She would be shocked!){i}"
    mc "{i}(But if I refuse, Linda might get suspicious...){i}"
    jump d02_mcroom1_4

label d02_mcroom1_3:
    scene d02_mcbed1_4 with dissolve
    play sound "sfx/Door_Open.mp3"
    scene d02_mcbed1_7 with dissolve
    $ Linda = True
    play sound "sfx/Disco.wav"
    mc "Linda?"
    scene d02_mcbed1_8
    play music "sfx/Music5.mp3"
    ld "Why didn't you answer the phone?"
    scene d02_mcbed1_7
    mc "Ehm...I hadn't heard the phone ring."
    mc "What are you doing here?"
    scene d02_mcbed1_8
    ld "I wanted to see if you weren't doing anything else."
    scene d02_mcbed1_7
    mc "What?"
    scene d02_mcbed1_10
    ld "Can I come in? Or are you hiding something?"
    scene d02_mcbed1_9
    mc "No, come in."
    mc "{i}(Let's hope she doesn't notice Milly's presence.){i}"
    scene d02_mcbed1_10
    ld "Well..."
    scene d02_mcbed1_16 with dissolve
    $ renpy.pause (1)
    scene d02_mcbed1_18 with dissolve
    mc "Do you want something?"
    scene d02_mcbed1_17
    ld "In fact I would like something..."
    scene d02_mcbed1_20
    ld "...I want you!"
    scene d02_mcbed1_21
    mc "What?"
    scene d02_mcbed1_20
    ld "Don't be silly, you know what I mean."
    scene d02_mcbed1_19
    mc "{i}(Oh no, what if Milly wakes up? She would be shocked!){i}"
    mc "{i}(But if I refuse, Linda might get suspicious...){i}"
    jump d02_mcroom1_4

label d02_mcroom1_4:
    scene d02_mcbed1_19
    menu:
        "Accept":
            scene d02_mcbed1_29
            play music "sfx/Music4.mp3"
            mc "Okay, you've piqued my interest..."
            scene d02_mcbed1_30
            ld "Yes..."
            scene d02_mcbed1_31
            ld "...very..."
            scene d02_mcbed1_32
            ld "...interesting."
            scene d02_mcbed1_33 with dissolve
            ld "Wow [mc]! Every time I see your cock, I'm impressed."
            scene d02_mcbed1_35
            mc "Being with you always gets me excited."
            scene d02_mcbed1_34
            ld "Me, too. Unfortunately, we have little time. I have to go to work soon."
            scene d02_mcbed1_35
            mc "Don't worry."
            scene d02_mcbed1_44 with dissolve
            $ renpy.pause (2)
            mc "oooh...yes..."
            ld "I like having your hard cock in my hand."
            scene d02_mcbed1_45 with dissolve
            $ renpy.pause (2)
            ld "I want your cum."
            scene d02_mcbed1_46 with dissolve
            $ renpy.pause (2)
            mc "AAAH...I'm cumming."
            with flash
            $ renpy.pause (0.5)
            with flash
            scene d02_mcbed1_39 with dissolve
            mc "OOOH...Fuck..."
            scene d02_mcbed1_40
            mc "Wow..."
            scene d02_mcbed1_41
            ld "mmm..."
            scene d02_mcbed1_42
            ld "*yum*"
            scene d02_mcbed1_48
            ld "Your cum tastes very good."
            scene d02_mcbed1_47
            mc "Thanks, Linda. That felt great."
            scene d02_mcbed1_48
            ld "Now I have to go, see you."
            scene d02_mcbed1_47
            mc "Bye, I'll talk to you later."
            $ ld_attr.set_friendship(+1)
            $ ld_attr.set_love(+1)
            scene black with dissolve
            "A FEW MINUTES LATER"
            scene d02_mcbed1_28 with dissolve
            mc "{i}(It was really very nice; luckily Milly didn't hear us.){i}"
            scene d02_mcbed1_49
            mc "{i}(I was lucky. I should wake Milly up now. We have a lot to do today.){i}"
            jump d02_lvroom1_1

        "Refuse":
            scene d02_mcbed1_25
            play music "sfx/Music3.mp3"
            ld "What is wrong with you?"
            scene d02_mcbed1_24
            mc "Sorry, Linda, but I have things to do."
            scene d02_mcbed1_26
            ld "Well, then I'm going to work. See you later."
            scene d02_mcbed1_27 with dissolve
            $ renpy.pause (1)
            scene d02_mcbed1_28 with dissolve
            mc "{i}(Shit! I made her mad... but, perhaps it's better that way.){i}"
            mc "{i}(Luckily, she didn't wake Milly up...){i}"
            scene d02_mcbed1_49
            mc "{i}(I should wake Milly up now. We have a lot to do today.){i}"
            jump d02_lvroom1_1

label d02_lvroom1_1:
    scene d02_mcbed1_49
    if incest == True:
        ml "Good morning, Uncle!"
    if incest == False:
        ml "Good morning, [mc]!"
    stop music
    play sound "sfx/Disco.wav"
    mc "{i}(What?){i}"
    scene d02_mcbed1_50
    mc "Good morning, Milly..."
    play music "sfx/Music2.mp3"
    scene d02_mcbed1_51
    ml "Sorry if I woke up late..."
    scene d02_mcbed1_50
    mc "No problem."
    mc "{i}(I hope the doorbell didn't wake her up.){i}"
    "END VERSION V0.2"

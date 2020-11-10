init python:
    for i in range(1, 4):
        renpy.image("d01_intro_comein_" + str(i), "/images/Day01/intro_comein" + str(i) + ".jpg")
init python:
    for i in range(1, 5):
        renpy.image("d01_intro_kissher_" + str(i), "/images/Day01/intro_kiss" + str(i) + ".jpg")
init python:
    for i in range(1, 5):
        renpy.image("d01_intro_hughher_" + str(i), "/images/Day01/intro_hugh" + str(i) + ".jpg")
init python:
    for i in range(1, 9):
        renpy.image("d01_intro_apartment_" + str(i), "/images/Day01/intro_apartment" + str(i) + ".jpg")
init python:
    for i in range(1, 10):
        renpy.image("d01_intro_mlroom_" + str(i), "/images/Day01/intro_mlroom" + str(i) + ".jpg")
init python:
    for i in range(1, 6):
        renpy.image("d01_bag_" + str(i), "/images/Day01/d01_bag" + str(i) + ".jpg")
init python:
    for i in range(1, 7):
        renpy.image("d01_bag_panty_" + str(i), "/images/Day01/d01_bag_panty" + str(i) + ".jpg")
init python:
    for i in range(1, 8):
        renpy.image("d01_bathroom1_" + str(i), "/images/Day01/d01_bathroom1_" + str(i) + ".jpg")
init python:
    for i in range(1, 37):
        renpy.image("d01_kitchen1_" + str(i), "/images/Day01/d01_kitchen1_" + str(i) + ".jpg")
init python:
    for i in range(1, 40):
        renpy.image("d01_living1_" + str(i), "/images/Day01/d01_living1_" + str(i) + ".jpg")
init python:
    for i in range(1, 74):
        renpy.image("d01_living2_" + str(i), "/images/Day01/d01_living2_" + str(i) + ".jpg")
init python:
    for i in range(1, 40):
        renpy.image("d01_mcbed1_" + str(i), "/images/Day01/d01_mcbed1_" + str(i) + ".jpg")
init python:
    for i in range(1, 5):
        renpy.image("d01_mcbed2_" + str(i), "/images/Day01/d01_mcbed2_" + str(i) + ".jpg")
init python:
    for i in range(1, 4):
        renpy.image("d01_mlroom1_" + str(i), "/images/Day01/d01_mlroom1_" + str(i) + ".jpg")
screen date1:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 20
        ypos 10
        focus_mask True
        idle Transform("images/buttons/day1.png")

label d01_intro_comein:
    scene d01_intro_comein_1 with dissolve
    ml "I see it's stayed the same since I left."
    scene d01_intro_comein_3 with dissolve
    show screen toprightmenu
    show screen date1
    menu:
        "Kiss her":
            jump d01_intro_kissher

        "Hug her":
            jump d01_intro_hughher

label d01_intro_kissher:
    scene d01_intro_kissher_1 with dissolve
    $ renpy.pause (2)
    scene d01_intro_kissher_2
    if incest == True:
        ml "Uncle, what are you doing?"
    if incest == False:
        ml "[mc], what are you doing?"
    scene d01_intro_kissher_1
    mc "I'm sorry, Milly. I didn't mean to..."
    scene d01_intro_kissher_4
    ml "I'm not a little girl anymore..."
    scene d01_intro_kissher_3
    mc "You're right. I'm sorry, Milly."
    mc "{i}(What the fuck was I doing...){/i}"
    jump d01_intro_apartment

label d01_intro_hughher:
    $ ml_attr.set_friendship(+1)
    scene d01_intro_hughher_1 with dissolve
    mc "I really missed you, Milly."
    scene d01_intro_hughher_2
    if incest == True:
        ml "I missed you too, Uncle."
    if incest == False:
        ml "I missed you too, [mc]."
    scene d01_intro_hughher_4
    mc "We'll have a lot to talk about."
    scene d01_intro_hughher_2
    ml "Yes! I have so many things to tell you."
    jump d01_intro_apartment

label d01_intro_apartment:
    scene d01_intro_apartment_1
    ml "Sorry that I didn't tell you I was coming."
    scene d01_intro_apartment_2
    menu:
        "It was a nice surprise":
            $ ml_attr.set_friendship(+1)
            scene d01_intro_apartment_2
            mc "It's fine, Milly! I'm really glad you're here."
            scene d01_intro_apartment_3
            if incest == True:
                ml "It's great to see you too, Uncle."
            if incest == False:
                ml "It's good to be back."
            scene d01_intro_apartment_4
            mc "{i}(I'm really glad to have Milly back here with me again.){i}"
            jump d01_intro_apartment1

        "Well, you should have warned me":
            if ml_attr.friendship == 0:
                scene d01_intro_apartment_2
                mc "You could have warned me. You were lucky to find me at home."
                scene d01_intro_apartment_5
                if incest == True:
                    ml "I'm sorry, Uncle! I just wanted to surprise you."
                if incest == False:
                    ml "I'm sorry, [mc]! I just wanted to surprise you."
                scene d01_intro_apartment_6
                mc "{i}(Maybe I went too far with the reprimand. She's a good girl.){i}"
                jump d01_intro_apartment1

            if ml_attr.friendship >= 0:
                $ ml_attr.set_friendship(-1)
                scene d01_intro_apartment_2
                mc "You could have warned me. You were lucky to find me at home."
                scene d01_intro_apartment_5
                if incest == True:
                    ml "I'm sorry, Uncle! I just wanted to surprise you."
                if incest == False:
                    ml "I'm sorry, [mc]! I just wanted to surprise you."
                scene d01_intro_apartment_6
                mc "{i}(Maybe I went too far with the reprimand. She's a good girl.){i}"
                jump d01_intro_apartment1

label d01_intro_apartment1:
    scene d01_intro_apartment_7
    menu:
        "Take her to her room":
            scene d01_intro_apartment_7
            mc "Imagine you must be tired from the trip."
            scene d01_intro_apartment_8
            ml "Yes, thank you. It's been a long trip."
            jump d01_intro_mlroom

label d01_intro_mlroom:
    stop music
    play music "sfx/Music1.mp3"
    scene d01_intro_mlroom_1 with dissolve
    $ renpy.pause (2)
    ml "Wow! It's just like I remembered. You kept everything the same!"
    scene d01_intro_mlroom_3
    ml "Thanks for keeping all my stuff."
    scene d01_intro_mlroom_2
    mc "You don't have to thank me. I wanted to keep all your things, so I could have some memories of our time together."
    jump d01_intro_mlroom1

label d01_intro_mlroom1:
    scene d01_intro_mlroom_2
    menu:
        "Suggest a hot shower":
            mc "You've had a long trip. Why don't you go take a shower while I take your bag to your room and make you something to eat?"
            scene d01_intro_mlroom_3
            ml "You're right, a good shower would be nice. I'll see you later."
            scene d01_intro_mlroom_9
            $ renpy.pause (2)
            jump d01_bag

label d01_bag:
    scene d01_bag_1
    mc "{i}(All right, let's get to work!){i}"
    scene d01_bag_2 with dissolve
    menu:
        "Open":
            play sound "sfx/Zipper-sound.mp3"
            scene d01_bag_3 with dissolve
            $ renpy.pause (2)
            mc "{i}(What?){i}"
            mc "{i}(Milly's always been messy...){i}"
            mc "{i}(...these panties are cute, though. I can tell Milly has grown up over the years.){i}"
            scene d01_bag_4
            $ renpy.pause (2)
            jump d01_bag1

label d01_bag1:
    menu:
        "Smell the panties":
            mc "{i}(It smells so good...){i}"
            scene d01_bag_panty_1
            mc "{i}*Smelling*{i}"
            mc "{i}(These panties smell great.){i}"
            scene d01_bag_panty_2
            ml "mmm..."
            scene d01_bag_panty_3
            ml "{i}(I forgot to get something out of my suitcase.){i}"
            scene d01_bag_panty_4
            stop music
            play sound "sfx/Disco.wav"
            ml "{i}(What?){i}"
            scene d01_bag_panty_5
            play music "sfx/Music3.mp3"
            if incest == True:
                ml "{i}(My uncle's sniffing my panties.){i}"
            if incest == False:
                ml "{i}([mc] sniffing my panties.){i}"
            scene d01_bag_panty_6
            ml "{i}(I didn't think he's so perverse.){i}"
            ml "{i}(I better go back to the bathroom and wash up.){i}"
            scene d01_bag_panty_1
            mc "{i}(Better get back to work...){i}"
            scene d01_bag_3 with dissolve
            $ renpy.pause (2)
            scene black with dissolve
            stop music
            "FINISHED PUTTING HER CLOTHES AWAY..."
            if ml_attr.friendship == 0:
                jump d01_bag2
            if ml_attr.friendship >= 0:
                $ ml_attr.set_friendship(-1)
                jump d01_bag2

        "Finish arranging the clothes":
            mc "{i}(What am I doing?){i}"
            mc "{i}(Why would I think of sniffing her panties? Anyway, I should put Milly's clothes away.){i}"
            scene d01_bag_3 with dissolve
            $ renpy.pause (2)
            scene black with dissolve
            "FINISHED PUTTING HER CLOTHES AWAY..."
            jump d01_bag2

label d01_bag2:
    scene d01_bag_5 with dissolve
    play music "sfx/Music1.mp3"
    $ renpy.pause (2)
    mc "{i}(Great! The clothes are in place. Let's go make lunch.){i}"
    jump d01_bath1_1

label d01_bath1_1:
    scene d01_bathroom1_1 with dissolve
    mc "{i}(???){i}"
    mc "{i}(The bathroom door is semi closed.){i}"
    scene d01_bathroom1_2
    jump d01_bath1_2

label d01_bath1_2:
    menu:
        "Peek":
            jump d01_bath1_3

        "Don't peek":
            mc "{i}(Better go make something to eat.){i}"
            jump d01_kitchen1_1

label d01_bath1_3:
    scene d01_bathroom1_3
    play music "sfx/Music4.mp3"
    $ renpy.pause (2)
    mc "{i}(Wow...but she grew up good.){i}"
    mc "{i}(Let's hope she doesn't notice I'm here.){i}"
    menu:
        "Continue peeking":
            mc "{i}(I can't stop looking at her.){i}"
            scene d01_bathroom1_4 with dissolve
            $ renpy.pause (2)
            scene d01_bathroom1_5 with dissolve
            stop music
            play sound "sfx/Disco.wav"
            ml "*GASP!*"
            scene d01_bathroom1_6
            play music "sfx/Music3.mp3"
            if incest == True:
                ml "Uncle! Go away! I'm half-naked! I'm not a child anymore."
            if incest == False:
                ml "[mc]! Go away! I'm half-naked! I'm not a child anymore."
            scene d01_bathroom1_7
            mc "Sorry, it's not what you think..."
            scene d01_bathroom1_6
            ml "Close the door!"
            scene d01_bathroom1_7
            mc "Ok."
            mc "{i}(What a fool I made. Better go make something to eat.){i}"
            if ml_attr.friendship == 0:
                play music "sfx/Music1.mp3"
                jump d01_kitchen1_1
            if ml_attr.friendship >= 0:
                $ ml_attr.set_friendship(-1)
                play music "sfx/Music1.mp3"
                jump d01_kitchen1_1

        "Stop peeking":
            $ ml_attr.set_friendship(+1)
            mc "{i}(Better go make something to eat.){i}"
            play music "sfx/Music1.mp3"
            jump d01_kitchen1_1

label d01_kitchen1_1:
    scene d01_kitchen1_1 with dissolve
    mc "{i}(I'll have to change some of my habits with Milly staying here.){i}"
    $ renpy.pause (2)
    play sound "sfx/Phone_Ringing.mp3" loop
    "{i}Smartphone rings{/i}"
    mc"???"
    scene d01_kitchen1_2
    mc "{i}(It's Linda. Better answer her.){i}"
    menu:
        "Answer the call":
            scene d01_kitchen1_2
            $ renpy.pause (1)
            stop sound
            scene d01_kitchen1_3 with dissolve
            mc "Hello, Linda."
            ld "Hi [mc], how are you?"
            mc "Well, how about you?"
            ld "I'm correcting today's audits."
            mc "Interesting!"
            ld "Yes! ahahaha"
            ld "I was wondering if you wanted to stay over at my place tonight?"
            scene d01_kitchen1_4
            mc "{i}(Oh, God! What do I tell her? I can't leave Milly alone. She just got here. What am I gonna tell her?){i}"
            ld "[mc]! Are you there? Are you going to answer me?"
            scene d01_kitchen1_3
            mc "Yeah, sorry..."
            mc "...but I have to finish a job by tomorrow, so this evening is no good."
            ld "Okay, then I'll see you tomorrow."
            mc "Okay, I'll see you then."
            ld "Bye, my love."
            scene d01_kitchen1_1 with dissolve
            mc "{i}(What do I tell her? I don't think she'll be happy to know that Milly's back.){i}"
            mc "{i}(Better make something to eat.){i}"
            menu:
                "Make food":
                    jump d01_kitchen1_2

label d01_kitchen1_2:
    scene d01_kitchen1_5 with dissolve
    mc "{i}(Let's get to work...){i}"
    scene black with dissolve
    "A few minutes later..."
    scene d01_kitchen1_6 with dissolve
    play music "sfx/Music2.mp3"
    $ renpy.pause (1)
    scene d01_kitchen1_7
    if incest == True:
        ml "Here I am, Uncle."
    if incest == False:
        ml "Here I am, [mc]."
    scene d01_kitchen1_8
    mc "???"
    scene d01_kitchen1_9
    $ renpy.pause (1)
    mc "{i}(Shit! I must say, she's grown up well!){i}"
    scene d01_kitchen1_10
    ml "Wow, just in time. I'm getting hungry."
    scene d01_kitchen1_12
    mc "Ehehehe, I figured you had worked up an appetite."
    scene d01_kitchen1_11
    ml "What are you making?"
    scene d01_kitchen1_12
    mc "{i}(Oh, God, what did she like?){i}"
    menu:
        "Salad":
            mc "Healthy salad!"
            scene d01_kitchen1_15
            ml "Wow! I see you haven't forgotten what I like!"
            scene d01_kitchen1_16
            if incest == True:
                mc "How can I forget my niece's favorite things?"
            if incest == False:
                mc "How can I forget my favorite things about my favorite friend?"
            $ ml_attr.set_friendship(+1)
            jump d01_kitchen1_3

        "Cheeseburger":
            mc "A great Cheeseburger!"
            scene d01_kitchen1_13
            ml "You know that's not what I like."
            ml "Don't you know I like vegetables?"
            scene d01_kitchen1_14
            mc "I'm sorry, Milly. I had other things on my mind."
            if ml_attr.friendship == 0:
                jump d01_kitchen1_3
            if ml_attr.friendship >= 0:
                $ ml_attr.set_friendship(-1)
                jump d01_kitchen1_3

label d01_kitchen1_3:
    scene d01_kitchen1_11
    ml "Okay, I'm gonna sit at the table."
    scene d01_kitchen1_12
    mc "Okay, food will be ready soon."
    scene d01_kitchen1_17
    ml "{i}(I'm very glad to be back. It's like my home here.){i}"
    scene d01_kitchen1_18
    if incest == True:
        ml "{i}(And my uncle has always been considerate of me. He treated me like a daughter.){i}"
    if incest == False:
        ml "{i}(And [mc] has always been considerate of me. He treated me like a daughter.){i}"
    scene d01_kitchen1_19
    ml "{i}(Last year was hell at my parents' house. They were always away and I didn't have any friends.){i}"
    scene d01_kitchen1_20
    mc "{i}(It's ready to eat.){i}"
    scene d01_kitchen1_21
    mc "Milly, your plate's ready."
    scene d01_kitchen1_22
    mc "Is everything all right?"
    scene d01_kitchen1_23
    ml "Yeah, I was just thinking about something."
    scene d01_kitchen1_22
    mc "Ok."
    scene d01_kitchen1_24
    jump d01_kitchen1_4

label d01_kitchen1_4:
    scene d01_kitchen1_24
    menu:
        "Ask her why she came to see you" if D01_answ1 == False:
            mc "Why did you come to see me?"
            scene d01_kitchen1_25
            ml "Because I missed you.."
            scene d01_kitchen1_24
            mc "*giggle* Don't joke!"
            scene d01_kitchen1_26
            ml "ahahaha"
            scene d01_kitchen1_27
            ml "Anyway, it's the truth."
            scene d01_kitchen1_28
            mc "Other than that, what made you come back here?"
            scene d01_kitchen1_25
            ml "I'm going to study at the university. I want to be a doctor."
            scene d01_kitchen1_24
            mc "Really? Wonderful! I'm very happy for you."
            scene d01_kitchen1_27
            ml "Thanks."
            $ D01_answ1 = True
            jump d01_kitchen1_4

        "Ask her about the time she spent away" if D01_answ2 == False:
            mc "How did you spend this time being back with your parents?"
            scene d01_kitchen1_25
            ml "Pretty good. Although I've missed being here a lot. I can't wait to meet my friend."
            scene d01_kitchen1_24
            mc "Are you talking about Sophia?"
            scene d01_kitchen1_30
            ml "Yeah, we haven't talked in a long time."
            scene d01_kitchen1_29
            mc "Don't worry, you'll get to see her again and spend time with her."
            scene d01_kitchen1_27
            ml "Yes, you're right! I can't wait to meet her."
            scene d01_kitchen1_28
            mc "{i}(I figured Milly's stay at her parents' house would make her sad. She spent most of her childhood here.){i}"
            $ D01_answ2 = True
            jump d01_kitchen1_4

        "Reminisce about the past" if D01_answ3 == False:
            mc "It seems like yesterday when you were gone."
            scene d01_kitchen1_30
            ml "Yes, I was very sad that day."
            scene d01_kitchen1_29
            mc "Well, let's not think about it. You're back now."
            scene d01_kitchen1_27
            ml "Yes, we'll have a chance to tell each other the things we've done while I was away."
            scene d01_kitchen1_28
            mc "Remember when I used to drive you to school every day?"
            scene d01_kitchen1_27
            ml "Yeah, then you went and talked to Professor Linda. She asked to see you often to talk about me."
            scene d01_kitchen1_28
            mc "Oh, yeah. She told me I had to be tougher on you in your studies."
            mc "{i}(It was actually an excuse to see us...){i}"
            $ D01_answ3 = True
            jump d01_kitchen1_4

    scene d01_kitchen1_24
    mc "Well, you better eat now."
    scene d01_kitchen1_27
    ml "Yes."
    scene d01_kitchen1_28
    $ renpy.pause (1)
    scene black with dissolve
    "After we finished eating..."
    scene d01_kitchen1_31 with dissolve
    ml "That was really delicious!"
    ml "Now I feel really good!"
    scene d01_kitchen1_32
    mc "*giggle* I saw! You ate everything fast."
    scene d01_kitchen1_31
    ml "*giggle* It's true!"
    scene d01_kitchen1_32
    mc "{i}(Milly has always been a cheerful girl. Seeing her sad earlier worried me.){i}"
    scene d01_kitchen1_33
    if incest == True:
        ml "Hey Uncle! I don't want to be too much trouble. I guess you have a lot of things to do."
    if incest == False:
        ml "Hey [mc]! I don't want to be too much trouble. I guess you have a lot of things to do."
    scene d01_kitchen1_34
    mc "Don't worry, I took the day off today. How could I go to work when you've just arrived and it's been ages since we last saw each other?"
    scene d01_kitchen1_31
    ml "Hey, I have an idea!"
    scene d01_kitchen1_32
    mc "What's on your mind?"
    scene d01_kitchen1_31
    ml "Follow me."
    scene d01_kitchen1_35
    ml "Let's watch TV!"
    scene d01_kitchen1_36
    mc "Good idea. So we can relax a bit."
    scene d01_living1_1
    play music "sfx/Music1.mp3"
    ml "Hahaha, I couldn't wait to jump on the couch!"
    scene d01_living1_2
    mc "Milly!"
    scene d01_living1_3
    ml "That's nice!!!"
    scene d01_living1_4
    mc "Come on now, Milly, don't act like a child..."
    scene d01_living1_5
    ml "I know, but some things I still like to do, even though I'm older."
    scene d01_living1_6
    mc "{i}(It's always the same. I have to be careful, because now she's not a little girl anymore.){i}"
    jump d01_living1_1

label d01_living1_1:
    scene d01_living1_6
    menu:
        "Spank her gently":
            scene d01_living1_7
            mc "You asked for it!"
            scene d01_living1_8
            "SPANK!"
            scene d01_living1_9
            ml "*giggle* Okay, I'll move."
            jump d01_living1_2

        "Tell her to move":
            scene d01_living1_6
            mc "Move over so I can sit down."
            scene d01_living1_5
            ml "No, I want the whole couch for me."
            scene d01_living1_6
            mc "{i}(How stubborn.){i}"
            jump d01_living1_1

label d01_living1_2:
    scene d01_living1_10
    ml "*giggle* Don't be too hard on me."
    scene d01_living1_11
    ml "Sit down! I want to watch TV with you."
    scene d01_living1_12
    mc "I can see you're very anxious."
    mc "Don't you feel tired? After all, you've had a long trip."
    scene d01_living1_11
    ml "I'm not tired!"
    scene d01_living1_13
    ml "YAWN!"
    mc "HAHAHAHA!"
    mc "You should go to bed..."
    scene d01_living1_15
    ml "But I'd love to watch a movie!"
    scene d01_living1_14
    mc "Maybe another time, when you're not tired..."
    scene d01_living1_16
    ml "You're right! Better zap the TV."
    scene d01_living1_18 with dissolve
    "AFTER SOME TIME..."
    scene d01_living1_19 with dissolve
    mc "{i}(I can't believe she likes to see these anime.){i}"
    scene d01_living1_20
    mc "{i}(But I must admit that the protagonist is very sexy!){i}"
    mc "{i}(Let's see if she...){i}"
    scene d01_living1_21
    play music "sfx/Music2.mp3"
    mc "{i}(What?){i}"
    mc "{i}(As I imagined, she fell asleep.){i}"
    mc "{i}(It's so sweet to see her sleeping...){i}"
    scene d01_living1_22
    mc "{i}(Maybe I should wake her up and send her to bed?){i}"
    menu:
        "Wake her up":
            play music "sfx/Music1.mp3"
            mc "Milly!"
            mc "Milly! Wake up!"
            jump d01_living1_4

        "Look at her tits":
            mc "{i}(Her shirt went down a little...){i}"
            scene d01_living1_23
            play music "sfx/Music4.mp3"
            mc "{i}(...She's grown a lot over the years.){i}"
            if incest == True:
                mc "{i}(Oh, God, what am I doing? I'm attracted to my niece!){i}"
            if incest == False:
                mc "{i}(Oh, God, what am I doing? I'm attracted to her!){i}"
            mc "{i}(Better wake her up.){i}"
            play music "sfx/Music1.mp3"
            jump d01_living1_3

label d01_living1_3:
    scene d01_living1_22
    mc "Milly!"
    mc "Milly! Wake up!"

label d01_living1_4:
    scene d01_living1_24
    ml "mmmph..."
    scene d01_living1_25
    mc "You were asleep, go to bed you'll be more comfortable."
    scene d01_living1_27
    ml "mmm...I'm sorry; I'm really tired..."
    scene d01_living1_26
    mc "You don't have to apologize."
    mc "Just go to bed..."
    scene d01_living1_27
    ml "Ok..."
    scene d01_living1_28 with dissolve
    ml "???"
    scene d01_living1_29 with dissolve
    ml "GASP! OH MY GOD!"
    scene d01_living1_30
    mc "What happened?"
    scene d01_living1_31
    ml "My shirt came down!"
    scene d01_living1_32
    mc "I didn't want to fix it for you..."
    scene d01_living1_33
    ml "I'm used to wearing the same clothes at home, but I'm not a kid anymore."
    scene d01_living1_34
    mc "If you want, we can go dress shopping tomorrow."
    scene d01_living1_35
    if incest == True:
        ml "Thanks Uncle! I'm going to sleep now, see you later."
    if incest == False:
        ml "Thanks [mc]! I'm going to sleep now, see you later."
    scene d01_living1_36
    mc "Have a good sleep."
    scene d01_living1_37 with dissolve
    mc "{i}(Well, I better go to my room and finish the work on the computer.){i}"
    scene d01_living1_38
    mc "{i}(Better turn off the TV.){i}"
    scene d01_living1_39 with dissolve
    $ renpy.pause (1)
    scene d01_mcbed1_1 with dissolve
    mc "{i}(Let's see if I got any emails.){i}"
    scene d01_mcbed1_2
    mc "{i}(Great! Maybe I can close this deal.){i}"
    mc "{i}(I have to think about what to write in the e-mail...){i}"
    scene d01_mcbed1_3
    mc "{i}(Damn it! I can't concentrate.){i}"
    mc "{i}(Maybe a little rest will get these thoughts out of my head.){i}"
    scene d01_mcbed1_4
    mc "{i}(Linda won't be happy when she hears that Milly's back.){i}"
    scene d01_mcbed1_5 with dissolve
    $ renpy.pause (1)
    scene d01_mcbed1_6 with dissolve
    mc "{i}(I wonder why Milly's back.){i}"
    mc "{i}(She should continue her studies where her parents are.){i}"
    mc "{i}(Better get some sleep...){i}"
    scene black with dissolve
    $ renpy.pause (2)
    stop music
    mc "zzz..."
    mc "...zzz..."
    if incest == True:
        ml "Uncle! Wake up!"
    if incest == False:
        ml "[mc]! Wake up!"
    mc "...zzz...???..."
    scene d01_mcbed1_7 with dissolve
    mc "{i}(...But what?){i}"
    scene d01_mcbed1_8
    play music "sfx/Music4.mp3"
    if incest == True:
        ml "Uncle, well awake!"
    if incest == False:
        ml "[mc], well awake!"
    scene d01_mcbed1_9
    mc "But what? Milly, what are you doing?"
    scene d01_mcbed1_8
    ml "I want to wake you up in a nice way."
    scene d01_mcbed1_10
    mc "{i}(Oh, shit!){i}"
    scene black with dissolve
    scene d01_mcbed1_11 with dissolve
    stop music
    play sound "sfx/Disco.wav"
    mc "NO!"
    mc "{i}(It was a dream!){i}"
    play music "sfx/Music3.mp3"
    mc "{i}(I thought that taking a rest might help me...){i}"
    mc "{i}(...and instead nothing. Apparently, thoughts of Milly come to me even when I'm asleep.){i}"
    scene d01_mcbed1_12
    mc "{i}(It's late. Milly's still asleep and I should get dinner ready.){i}"
    menu:
        "Go to Milly's room":
            mc "{i}(Better go wake Milly.){i}"
            jump d01_mlroom1_1

        "Go prepare dinner":
            mc "{i}(Better cook dinner.){i}"
            jump d01_living2_1

label d01_mlroom1_1:
    scene d01_mlroom1_1 with dissolve
    play music "sfx/Music1.mp3"
    mc "{i}(Better knock on the door.){i}"
    "TOC...TOC..."
    mc "Milly, wake up!"
    mc "{i}(No answer.){i}"
    mc "Milly! If you nap for too long, you won't be able to sleep tonight!"
    mc "...."
    mc "{i}(I better go in and wake her up.){i}"
    scene d01_mlroom1_2
    mc "Milly I'm coming in..."
    scene d01_mlroom1_3
    $ renpy.pause (1)
    mc "What?"
    mc "{i}(Is she awake? That's better.){i}"
    mc "{i}(She's usually the one who sleeps the most. I must say, she surprised me.){i}"
    mc "{i}(Better go make dinner.){i}"
    jump d01_living2_1

label d01_living2_1:
    scene d01_living2_1 with dissolve
    stop music
    play sound "sfx/Disco.wav"
    $ renpy.pause (1)
    mc "{i}(Unbelievable!){i}"
    mc "Milly!"
    scene d01_living2_2
    play music "sfx/Music2.mp3"
    if incest == True:
        ml "Hey Uncle, I was just..."
    if incest == False:
        ml "Hey [mc], I was just..."
    scene d01_living2_3
    ml "*GASP!*"
    scene d01_living2_4
    $ renpy.pause (2)
    scene d01_living2_5
    ml "{i}(Oh, no...){i}"
    scene d01_living2_6
    $ renpy.pause (1)
    scene d01_living2_7 with dissolve
    ml "Sorry, I'll pick it up right away."
    scene d01_living2_8 with dissolve
    $ renpy.pause (1)
    scene d01_living2_9 with dissolve
    mc "{i}(Oh, no...again...){i}"
    menu:
        "Look at her ass":
            scene d01_living2_10 with dissolve
            mc "{i}(What a great ass. I have to be careful, she mustn't notice.){i}"
            if ml_attr.friendship == 0:
                jump d01_living2_2
            if ml_attr.friendship >= 0:
                $ ml_attr.set_friendship(-1)
                jump d01_living2_2

        "Don't do anything":
            mc "{i}(Hang on, [mc]!){i}"
            jump d01_living2_2

label d01_living2_2:
    scene d01_living2_11 with dissolve
    $ renpy.pause (2)
    scene d01_living2_12 with dissolve
    ml "Sorry, I wanted to surprise you by making dinner."
    scene d01_living2_13
    mc "Really? That's great, I can't wait to try."
    scene d01_living2_14
    ml "Awesome! I'll get right to work."
    scene d01_living2_15 with dissolve
    $ renpy.pause (2)
    scene d01_living2_16 with dissolve
    mc "Just be careful around the kitchen, don't hurt yourself."
    ml "Don't worry..."
    ml "...OH MY GOD!"
    mc "What's wrong?"
    scene d01_living2_18 with dissolve
    $ renpy.pause (1)
    scene d01_living2_17 with dissolve
    play music "sfx/Music1.mp3"
    ml "I forgot the ingredients!"
    scene d01_living2_19
    ml "{i}(I want to cook something he'll enjoy.){i}"
    mc "Milly, what are you going to cook?"
    scene d01_living2_20 with dissolve
    $ renpy.pause (1)
    scene d01_living2_21 with dissolve
    ml "It's a surprise!"
    scene d01_living2_22
    mc "Really?"
    scene d01_living2_21
    ml "Yeah, close your eyes."
    mc "mmm...ok."
    scene black with dissolve
    $ renpy.pause (1)
    "BACKGROUND SOUND OF POTS"
    mc "Milly, are you ok?"
    scene d01_living2_23 with dissolve
    if incest == True:
        ml "Don't worry uncle, it's okay..."
    if incest == False:
        ml "Don't worry [mc], it's okay..."
    ml "...Keep your eyes closed."
    scene d01_living2_24 with dissolve
    mc "Ok."
    scene black with dissolve
    "A FEW MINUTES LATER"
    scene d01_living2_25 with dissolve
    ml "Dinner is ready!"
    mc "Thanks."
    scene d01_living2_26
    mc "{i}(She cooked something simple, but I appreciate her effort.){i}"
    jump d01_living2_3

label d01_living2_3:
    scene d01_living2_28
    play music "sfx/Music1.mp3"
    menu:
        "Thank you for dinner" if D01_answ4 == False:
            mc "It looks delicious, and the meal, too, of course."
            scene d01_living2_27
            ml "eheheh"
            ml "Don't overdo it. I just cooked some simple sausages."
            scene d01_living2_28
            mc "I thought you only liked vegetables."
            scene d01_living2_27
            ml "I wanted to surprise you. Besides, I don't just eat vegetables, even though it's my favorite food."
            $ D01_answ4 = True
            jump d01_living2_3

        "Ask if she has a boyfriend" if D01_answ5 == False:
            mc "So, Milly, do you have a boyfriend?"
            scene d01_living2_31
            if incest == True:
                ml "Uncle!"
            if incest == False:
                ml "[mc]!"
            mc "Sorry, it's just that a pretty girl like you..."
            scene d01_living2_32
            play music "sfx/Music3.mp3"
            ml "It's not what you think!"
            scene d01_living2_33
            mc "I'm sorry, Milly. Don't worry, I'm sure you could have anyone you wanted."
            scene d01_living2_27
            play music "sfx/Music1.mp3"
            ml "Thank you! You always know exactly what to say."
            $ D01_answ5 = True
            jump d01_living2_3

        "Talk about Sophia" if D01_answ6 == False:
            mc "I can imagine Sophia's face when she sees you again after all this time."
            scene d01_living2_27
            ml "Yeah, I guess she won't even believe it's me."
            scene d01_living2_28
            mc "hehehe, she'll be happy to see you again."
            scene d01_living2_29
            ml "Do you know if she's working or studying?"
            scene d01_living2_31
            ml "I hope she's not mad at me for leaving."
            scene d01_living2_31
            mc "Don't worry, she won't be angry."
            scene d01_living2_27
            if incest == True:
                ml "You're right! Thanks Uncle!"
            if incest == False:
                ml "You're right! Thanks [mc]!"
            $ D01_answ6 = True
            jump d01_living2_3

    scene d01_living2_28
    mc "Well, let's eat now."
    scene d01_living2_34 with dissolve
    $ renpy.pause (0.5)
    scene d01_living2_35 with dissolve
    $ renpy.pause (0.5)
    scene d01_living2_36 with dissolve
    $ renpy.pause (0.5)
    scene d01_living2_37 with dissolve
    play music "sfx/Music5.mp3"
    ml "mmmm..."
    mc "{i}(Wait...What is she doing?){i}"
    scene d01_living2_38
    mc "{i}(Oh no...){i}"
    scene d01_living2_39
    mc "{i}(...what am I thinking! She's just eating a sausage without the cutlery.){i}"
    scene d01_living2_40
    ml "{i}(Why are you watching me?){i}"
    scene d01_living2_41
    ml "Why aren't you eating? Don't you like it?"
    scene d01_living2_42
    mc "Um..."
    mc "{i}(I have to make an excuse.){i}"
    mc "I'm just surprised you eat without using cutlery. You also forgot to bring a drink."
    scene d01_living2_43
    ml "*GASP!* I'm sorry, I forgot."
    scene d01_living2_44
    mc "Don't worry, I'll take care of it."
    scene black with dissolve
    "AFTER YOU FINISH YOUR DINNER"
    scene d01_living2_45 with dissolve
    play music "sfx/Music1.mp3"
    ml "It was nice having dinner with you."
    scene d01_living2_46
    mc "You too. Well, it's getting late."
    scene d01_living2_49
    if incest == True:
        ml "Wait, Uncle!"
    if incest == False:
        ml "Wait, [mc]!"
    scene d01_living2_50
    mc "Yes?"
    scene d01_living2_49
    ml "Would you like to watch TV together before sleepy time?"
    scene d01_living2_50
    mc "mmmm...."
    mc "....Ok!"
    scene d01_living2_47
    ml "Yay! Thank you very much!"
    scene d01_living2_48
    mc "You're welcome."
    jump d01_living2_4

label d01_living2_4:
    scene d01_living2_51 with dissolve
    ml "Let's see what's on TV."
    scene d01_living2_52
    mc "I don't think there's anything interesting on TV today."
    scene d01_living2_53
    $ renpy.pause (0.5)
    scene d01_living2_54
    mc "Did you see that?"
    scene d01_living2_55
    ml "Yeah, it's the usual news."
    ml "But I want to ask you a question..."
    scene d01_living2_56
    mc "eh?"
    scene d01_living2_57 with dissolve
    ml "Have you been alone all this time after I returned to my parents?"
    scene d01_living2_58
    mc "What do you mean?"
    scene d01_living2_59
    mc "{i}(That's a smart look. I know what you're getting at.){i}"
    scene d01_living2_61
    ml "You know what I mean. Have you had any girlfriends?"
    scene d01_living2_60
    mc "Milly, I don't think we should..."
    scene d01_living2_62
    ml "Why? Do you think I'm still too young to know such things?"
    scene d01_living2_63
    mc "No, but..."
    scene d01_living2_64
    ml "AHAHAHA! I'm kidding!"
    mc "*Joking tone* Careful, I can ask you personal questions too."
    scene d01_living2_65
    ml "Oh, No!"
    scene d01_living2_67
    ml "It's confidential."
    scene d01_living2_66
    mc "I was just kidding."
    menu:
        "Kiss her on the forehead" if ml_attr.friendship >= 3:
            scene d01_living2_66
            play music "sfx/Music2.mp3"
            mc "Come here Milly."
            scene d01_living2_68 with dissolve
            $ renpy.pause (0.5)
            scene d01_living2_69 with dissolve
            "SMACK"
            scene d01_living2_70
            ml "???"
            if incest == True:
                ml "{i}(It seems strange to me that my uncle is giving me a kiss on the forehead.){i}"
            if incest == False:
                ml "{i}(It seems strange to me that [mc] is giving me a kiss on the forehead.){i}"
            scene d01_living2_71
            ml "{i}(But I must remain calm. He loves me very much.){i}"
            scene d01_living2_72
            mc "{i}(I had a strange feeling...){i}"
            scene d01_living2_73
            ml "Thank you, I feel better."
            scene d01_living2_72
            mc "Sorry, I didn't mean to make you sad."
            scene d01_living2_73
            ml "Don't worry."
            scene d01_living2_72
            mc "It's getting late. Tomorrow we are going to meet Sophia."
            scene d01_living2_65 with dissolve
            ml "It's true!"
            scene d01_living2_61
            ml "So I'm going to sleep, tomorrow will be a busy day."
            scene d01_living2_60
            mc "Good night, Milly."
            scene d01_living2_61
            if incest == True:
                ml "Good night, Uncle."
            if incest == False:
                ml "Good night, [mc]."
            jump d01_mcroom1_1

        "It's getting late" if ml_attr.friendship <= 2:
            scene d01_living2_66
            mc "It's getting late. Tomorrow we are going to meet Sophia."
            scene d01_living2_65
            ml "It's true!"
            scene d01_living2_61
            ml "So I'm going to sleep, tomorrow will be a busy day."
            scene d01_living2_60
            mc "Good night, Milly."
            scene d01_living2_61
            if incest == True:
                ml "Good night, Uncle."
            if incest == False:
                ml "Good night, [mc]."
            jump d01_mcroom1_2

label d01_mcroom1_1:
    scene d01_mcbed2_1 with dissolve
    mc "{i}(Wow, there were a lot of surprises today. I'd better get to sleep, tomorrow will be a very busy day.{i})"
    scene d01_mcbed2_2 with dissolve
    $ renpy.pause (1)
    scene black with dissolve
    $ renpy.pause (1)
    scene d01_mcbed2_3 with dissolve
    if incest == True:
        ml "{i}(It was a beautiful day. Tomorrow I will have the opportunity to see Sophia again, and spend time together with my uncle.{i})"
    if incest == False:
        ml "{i}(It was a beautiful day. Tomorrow I will have the opportunity to see Sophia again, and spend time together with [mc].{i})"
    scene d01_mcbed2_4
    if incest == True:
        ml "{i}(I felt strange when my uncle kissed me, though it was only a peck on the forehead...{i})"
    if incest == False:
        ml "{i}(I felt strange when [mc] kissed me, though it was only a peck on the forehead...{i})"
    scene d01_mcbed2_3
    ml "{i}(Oh well, I shouldn't worry about that now. I should get some sleep.{i})"
    scene black with dissolve
    jump d02_mcroom1_1

label d01_mcroom1_2:
    scene d01_mcbed2_1 with dissolve
    mc "{i}(It has been a day of great surprises. Better sleep than tomorrow will be a very busy day.{i})"
    scene d01_mcbed2_2 with dissolve
    $ renpy.pause (1)
    scene black with dissolve
    jump d02_mcroom1_1

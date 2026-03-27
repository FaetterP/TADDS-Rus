default jaxpoint = 0
default ragpoint = 0
default ganpoint = 0
default pompoint = 0
default zoopoint = 0
default kingpoint = 0

define j = Character("JAX")
define r = Character("RAGATHA")
define g = Character("GANGLE")
define p = Character("POMNI")
define z = Character("ZOOBLE")
define k = Character("KINGER")
define c = Character("CAINE")
define b = Character("BUBBLE")
define a = Character("[avatar.upper()]")
define zg = Character("ZOOBLE & GANGLE")
define rp = Character ("RAGATHA & POMNI")
define x = Character ("XDDCC")
define n = Character ("NPC")
define m = Character ("MING")
define sb = Character ("SIR BASTION")
define md = Character ("MAID")
define q = Character ("???")
define gq = Character ("GLOINK QUEEN")

# NVL characters are used for the phone texting
define j_nvl = Character("JAX", kind=nvl, image="nighten", callback=Phone_SendSound)
define r_nvl = Character("RAGATHA", kind=nvl, callback=Phone_ReceiveSound)
define g_nvl = Character("GANGLE", kind=nvl, callback=Phone_ReceiveSound)
define p_nvl = Character("POMNI", kind=nvl, callback=Phone_ReceiveSound)
define z_nvl = Character("ZOOBLE", kind=nvl, callback=Phone_ReceiveSound)
define x_nvl = Character("XDDCC", kind=nvl, callback=Phone_ReceiveSound)
define a_nvl = Character("[avatar]", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


# Cg's and other art

image D1gameover = "CGs/D1gameover.png"

image CG_cent2 = "CGs/centipede2 cg.png"
image CG_cent = "CGs/centipede cg.png"
image CG_nap = "CGs/jaxnap cg.png"
image CG_stupid = "CGs/jaxstupid cg.png"
image CG_jfriends = "CGs/jaxfriends cg.png"
image CG_jaxpinh = "CGs/jaxpinh cg.png"
image CG_jaxpintm = "CGs/jaxpintm cg.png"
image CG_jaxpintf = "CGs/jaxpintf cg.png"
image CG_jaxpints = "CGs/jaxpints cg.png"

image CG_bedpicnic = "CGs/rag picnic cg.png"
image CG_softball = "CGs/ragatha softball cg.png"
image CG_ragcry = "CGs/rag cry cg.png"
image CG_ragwalk = "CGs/rag walk cg.png"
image CG_ragpj = "CGs/rag pj cg.png"

image CG_vidgame = "CGs/pomni game cg.png"
image CG_toast = "CGs/toast cg.png"
image CG_libraryf = "CGs/libraryf cg.png"
image CG_librarym = "CGs/librarym cg.png"
image CG_wheel = "CGs/wheel cg.png"

image ganart1 = "images/gangleart1.png"
image ganart2 = "images/gangleart2.png"
image zoobart1 = "images/zoobart1.png"

image CG_ganskirt = "CGs/gangle skirt cg.png"
image CG_ganyaoi = "CGs/gangle yaoi cg.png"
image CG_pocky = "CGs/gangle pocky bg.png"
image CG_ganwalkf = "CGs/gangle walk f cg.png"
image CG_ganwalkm = "CGs/gangle walk m cg.png"
image CG_gangleww = "CGs/gangleww.png"

image CG_zpin = "CGs/zooble pin cg.png"
image CG_swim = "CGs/zooble swim cg.png"
image CG_zparts = "CGs/zooble parts cg.png"
image CG_zfriendsf = "CGs/zooble friends f cg.png"
image CG_zfriendsm = "CGs/zooble friends m cg.png"

image dark = "images/bgs/dark.png"
image CG_wackywatch1 = "CGs/wackywatch1.png"
image CG_wackywatch2 = "CGs/wackywatch2.png"
image censor_bar = "images/censor_bar.png"
image CG_closet_m1 = "CGs/closetm1.png"
image CG_closetm2 = "CGs/closetm2.png"
image CG_closetf1 = "CGs/closetf1.png"
image CG_closetf2 = "CGs/closetf2.png"
image uniformnote = "CGs/uniformnote.png"
image bluebutler = "CGs/blue butler.png"
image DAY1 = "images/DAY1.png"
image DAY1 complete = "images/DAY1 complete.png"
image DAY2 = "images/DAY2.png"
image DAY2 complete = "images/DAY2 complete.png"
image DISCLAIMER = "images/DISCLAIMER.png"

#Transforms and animations
transform top_left:
    xalign 1.0
    yalign 0.0

transform appear_right:
    xalign .85 yalign 1.0
    alpha 0 xoffset 30
    easein .5 alpha 1.0 xoffset 0

transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0


transform myleft:
    xalign 0.2
    yalign 1.0
    
transform myright:
    xalign 0.8
    yalign 1.0

image caine_glitch:
    "images/c1a.png"
    pause .5
    "images/c1b.png"
    pause .1
    "images/c1c.png"
    pause .1
    "images/c1d.png"
    pause .1
    "images/c1e.png"
    pause .1
    "images/c1f.png"
    pause .1
    "images/c1g.png"
    pause .1
    "images/c1h.png"
    pause .1
    "images/c1i.png"
    pause .1
    "images/c1j.png"
    pause .1
    "images/c1k.png"
    pause .1
    "images/c1l.png"
    pause .1
    "images/c1m.png"
    pause .1
    "images/c1n.png"


image fading_chars:
    "images/gansil.png"
    0.9
    "images/jaxsil.png"
    0.9
    "images/ragsil.png"
    0.9
    "images/pomsil.png"
    0.9
    "images/zoobsil.png"
    0.9
    repeat 

#Flags
default uniform_female = False
default uniform_male = False
default choice_taken = False
default jaxtour = False
default jaxprank = False
default ragtour = False
default kinglunch = False
default lunchinvite = False
default ganwalk = False
default zoowalk = False
default ragwalk = False
default pomwalk = False
default jaxwalk = False
default zoobfight = False
default ragtourcomplete = False
default breakfastbetrayal = False
default SheKnows = False
default greatexpectations = False
default snitch = False
default scavenge = False
default zoobpool = False
default zoobfriend = False

define flash = Fade(0.5, 0.5, 0.5, color="#fff")

define gui.dialogue_text_outlines = [ (2, "#2A4A61", 0, 0) ]
define gui.dialogue_outline_scaling = "linear"
define gui.charaters_text_outlines = [ (2, "#2A4A61", 0, 0) ]
define gui.characters_outline_scaling = "linear"
style say_label:
    outlines [ ( 3, "#4890C4", 0, 0) ]
    outline_scaling "linear"

screen uniform():
    imagebutton:
        xalign 0.25
        yalign 0.1

        auto "uni_f_%s.png" action [Hide("uniform"), SetVariable("uniform_female", True), Return()]

    imagebutton:
        xalign 0.75
        yalign 0.1

        auto "uni_m_%s.png" action [Hide("uniform"), SetVariable("uniform_male", True), Return()]


# PHONE CODE
define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define avatar = "[avatar]"
define ragatha = "RAGATHA"
define jax = "JAX"
define gangle = "GANGLE"
define zooble = "ZOOBLE"
define pomni = "POMNI"
define xddcc = "XDDCC"

init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            #draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == avatar:
                $ message_frame = "images/phone/phone_send_frame.png"
            else:
                $ message_frame = "images/phone/phone_received_frame2.png"

            hbox:
                spacing 10
                if d.who == avatar:
                    box_reverse True
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == avatar:
                        $ message_icon = "images/phone/phone_avatar_icon.png"
                    elif d.who == ragatha:
                        $ message_icon = "images/phone/phone_ragatha_icon.png"
                    elif d.who == jax:
                        $ message_icon = "images/phone/phone_jax_icon.png"
                    elif d.who == gangle:
                        $ message_icon = "images/phone/phone_gangle_icon.png"
                    elif d.who == pomni:
                        $ message_icon = "images/phone/phone_pomni_icon.png"
                    elif d.who == zooble:
                        $ message_icon = "images/phone/phone_zooble_icon.png"
                    elif d.who == xddcc:
                        $ message_icon = "images/phone/phone_pomni_icon.png"

                    else:
                        $ message_icon = "images/phone/phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != avatar and previous_d_who != d.who:
                        text d.who

                    frame:
                        padding (20,20)
                        

                        background Frame(message_frame, 23,23,23,23)
                        xsize 350

                        if d.current:
                            if d.who == avatar:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False
                            

                            if d.who == avatar:
                                color "#FFF"
                                text_align 1.0
                                xpos -580
                            else:
                                color "#FFF"

                                
                            id d.what_id
        $ previous_d_who = d.who
                    
style phoneFrame is default

style phoneFrame_frame:
    background Transform("images/phone/phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("images/phone/phone_foreground.png", xcenter=0.5,yalign=0.5)
    
    ysize 550
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True

# The game starts here.

label start:

    stop music fadeout 1.0

    scene dark with fade

    pause 2.0

    play music "audio/Morning.mp3" volume 0.5 fadein 0.5

    scene bg void
    with fade

    show DISCLAIMER with dissolve
    pause

    hide DISCLAIMER with dissolve
    pause 0.5

    show cainexcited with moveinbottom

    c "Welcome to the Amazing Digital Dating Simulator! A slice-of-life styled school setting where anything and everything is possible!"

    hide cainexcited
    show cainmyself

    c "I'm Caine, and I'll be your Principal for the duration of your stay here at the Amazing Digital Academy!"

    show fading_chars
    
    hide cainmyself
    show cainshowoff
    pause (0.1)

    show cainshowoff at right
    with move

    c "Help your classmates, pull pranks on the teacher,"

    hide cainshowoff
    show cainexcited at right 

    c "become a straight A student, or a rule-breaking delinquent!"

    hide cainexcited
    show cainfawn at right

    c "All this while possibly finding love along the way!"

    hide fading_chars

    hide cainfawn

    show cainneutral at right
    pause (0.1)

    show cainneutral at center
    with move

    c "But enough about my wonderful creation!"

    hide cainneutral
    show cainwallbrk 

    c "Let's get you enrolled! First thing's first, what uniform will you be dawning?"

    hide cainwallbrk with moveoutbottom

    call screen uniform
    
    show cainneutral
    
    c "Sounds good! How about your name? What should we call you?"


    label choosename:
        $ avatar = renpy.input("What is your name?", length=20)

        hide cainneutral
        show cainthink

        c "[avatar], huh? Are you sure you like that name?"
    
        menu:
            "Yep! That's my name.":
                jump name_yes
        
            "When you say it that way, I’m not sure…":
                jump choosename

    label name_yes:
        
        hide cainthink
        show cainshowoff

        c "Alrighty then, [avatar]!"
        c "Then let's head inside!"
        jump name_yesdone
        
    label name_yesdone:

    stop music fadeout 1.0

    scene classroom door
    with flash 

    "Hi, my name is [avatar], I’m a transfer student to The Amazing Digital Academy."

    "My parents moved to the countryside after a vague, tragic event that changed the course of our lives."
    
    "After I said goodbye to all my old friends, my parents got my transcripts and packed up the car."

    "Today is my first day at this new school."

    play music "audio/Morning.mp3" volume 0.5 fadein 1.0
    scene homeroom bg
    with flash
    show morning at top_left

    "I glance down at my class schedule. This should be ENGLISH 101 with Mr. Kinger. So where is the teacher?"

    "As I step into the room to let in any other students that might be late to class, someone else hops into the room." 
    
    "The figure looks like a tall white piece from a gaming set. Specifically, he looks like a king in chess."

    "It takes me a moment to put two and two together, but when I do, I almost groan at the pun. Surely his name can’t really be"

    show kingcheerywave with moveinbottom

    k "Hello, my name is Kinger."

    hide kingcheerywave
    show kingcurioussr
    
    k "You must be pleased to meet me!"

    "Mr. Kinger extends a gloved hand, which I shake more out of instinct than out of a genuine sense of excitement."

    hide kingcurioussr
    show kingexcited

    k "Good morning students! On the docket today we have a new student named...!"

    hide kingexcited
    show kingcurioussr 
    
    k "Oh, uh what’s your name again?"

    menu:
        "Hey everyone! I’m [avatar]. I look forward to learning with you all, and I hope we can all be friends.":
            $ ragpoint += 1
            $ ganpoint += 1
            jump day1homeroom

        "I’m [avatar]. Don’t mess with me, and we’ll be good.":
            $ zoopoint += 1
            jump day1homeroom
        
        "I’m [avatar] and I’m always down for a good time.":
            $ jaxpoint += 1
            $ pompoint += 1
            jump day1homeroom

    label day1homeroom:

    hide kingcurioussr
    show kingcheerysr

    k "Righty oh! Go on and take any open seat, [avatar], most of our students don’t bite!"

    "One of the other students, a purple rabbit, seems to grin at this."

    "I take a moment to think of who to sit by."

    label seatchoice:
        menu:
            "I take a seat next to the girl in colorful hat and sailor uniform":
                jump pomsit
            
            "I sit next to the shy-looking girl with a comedy mask and ribbon body":
                jump gansit
            
            "I sit next to the mismatched figure with a bored look on their face":
                jump zoosit

            "I sit down next to the cheery looking ragdoll in front of the class":
                jump ragsit
            
            "I sit down with the mischievous looking purple rabbit":
                jump jaxsit

            "I sit down in the teacher’s chair" if not choice_taken:
                $ choice_taken = True
                jump kingsit

    label jaxsit:

        scene homeroom bg
        show morning at top_left
        with None

        show jaxnonchalant with moveinbottom

        "I sit down next to the purple rabbit. He looks bored by Mr. Kinger’s lecture." 
        "As I take a closer look, I see his name is written on a nameplate on his desk, apparently his name is Jax."
        "As I get a closer look at Jax, I also see he’s working his jaw. Is he chewing gum?"

        "He catches me looking at him, and I almost apologize for staring, but I can see he isn’t offended."

        hide jaxnonchalant
        show jaxmischief2

        "Instead, he grins quietly before putting a finger up to his lips."


        "He takes the chewed gum between his gloved fingers, reaching out towards the girl in front of us."

        show jaxmischief2 at myleft
        with move

        show ganbasicflip at myright
        with moveinright

        "The girl in front of us has a ribbon for a body and a comedy mask for a face." 
    
        "She’s paying close attention to Mr. Kinger’s lecture, and Jax is reaching out with the gum on his hand."

        "Is he going to stick it on her mask?"

        menu:

            "Warn her":
                jump choice1_gan

            "Keep quiet and see what happens":
                jump choice1_jax

    label choice1_gan:

        $ menu_flag = True
        $ ganpoint += 1
        $ jaxpoint -= 1

        a "Hey, what are you trying to do to her?"

        hide ganbasicflip
        show gansurprise at bounce, myright

        hide jaxmischief2
        show jaxcautious at myleft

        g "Huh?"

        "Thanks to your advance notice, the ribbon girl manages to extend her mask forward, turning to face Jax with a panicked expression on her mask."

        "The ragdoll girl seems to notice this exchange as well."

        show ragargue at right
        with moveinright

        r "Jax, leave her alone! I don’t even know why we let you sit behind her."

        "It sounds like this isn’t the first time Jax has tried something like this."
        
        "Mr. Kinger’s attention is drawn by the ragdoll girl shouting at Jax."

        show jaxcautious at center
        with move

        show kingcurioussr at left
        with moveinleft

        k "Where's going on?"

        hide jaxcautious
        show jaxannoyed2

        "A flicker of annoyance crosses Jax’s features, and he narrows his eyes for a moment before grinning in faux-innocence, 
        sticking the gum right back in his mouth without pause."

        hide jaxannoyed2
        show jaxmischief 

        j "Whaaaat?"

        "He draws the word out, rolling his eyes as he looks directly at me."

        hide jaxmischief
        show jaxbored

        j "I guess the newbie just hates fun. "

        "Despite Jax's disapproval, I can't help but notice the masked girl giving me a grateful look. I nod in her direction."

        
        jump seatchoice_done

    label choice1_jax:

        $ menu_flag = False
        $ ganpoint -= 1
        $ jaxpoint += 1

        "Jax reaches forward with practiced stealth, sticking the wet wad of already-been-chewed gum to the ribbon-girl’s mask."

        "The ribbon girl lets out a quiet shriek of discomfort, flailing her arms as she desperately pulls away from Jax."

        hide ganbasicflip
        show ganmortified at bounce, myright

        g "Eeeeew! Jax! What is thaaat? What did you do? Eeeew!"

        "Her whining and desperate flailing is a little funny, even as she feels around blindly behind her mask."
        
        "Her movements attract the attention of Mr. Kinger."

        show jaxmischief2 at center
        with move

        show kingcurious at left
        with moveinleft

        k "Where’s going on?"

        "He seems aware something is going on, but he doesn’t seem to know what. How is this guy teaching us?"

        show zoobirritated at right
        with moveinright

        z "Jax is just picking on Gangle again."

        "The mismatched figure pipes up from next to Gangle, who is evidently the ribbon girl that Jax just stuck his gum to"

        hide zoobirritated
        show zoobbasic at right

        z "Here Gangle, let's go to the bathroom so we can wash it off."

        hide ganmortified
        with moveoutright

        hide kingcurious
        show kingpointing at left

        k " Oh yes, carry on then, Zooble!"

        "Nothing phases this teacher."

        hide kingpointing
        with moveoutleft

        hide zoobbasic
        show zoobangry at right
        
        "Zooble glares daggers into the rabbit as they leave."

        hide zoobangry
        with moveoutright

        hide jaxmischief2
        show jaxmischief at center

        j "What? It was funny, right? Back me up here."

        "Jax turns to face me."

        menu:
            "Yeah, that was hilarious!":
                $ jaxpoint += 1

                hide jaxmischief
                show jaxsidesmirk

                "Jax smirks as I take his side. It was a pretty good prank!"

                j "Heh, you’re not so bad, new kid, maybe you can teach these losers how to grow a sense of humor."

                "I smirk back. Maybe things at this school won’t be so bad."
                jump seatchoice_done

            "I guess it was kinda funny…":
                $ jaxpoint += 1

                hide jaxmischief
                show jaxsidesmirk2

                "Jax offers a thin smile as he leans over to me."

                j "It was very funny. You should try loosening up, new kid, you might have some actual fun."

                "I can’t help but audibly gulp, and hope I haven’t thrown my lot in with the wrong person"
                jump seatchoice_done
        
            "No, Jax, that was mean":
                hide jaxmischief
                show jaxbored

                "Jax barely acknowledges my response, almost cutting me off before I finish saying my peace."

                j "Everyone’s a critic."

                "Jax shrugs."
                jump seatchoice_done


        jump seatchoice_done

    label ragsit:
        scene homeroom bg
        show morning at top_left
        with None

        show ragsmile with moveinbottom

        "I take my seat next to the ragdoll girl in a blue skirt and vest." 
        "She’s paying such close attention to the lecture, I hesitate to introduce myself, not wanting to disrupt her."
        "To my surprise, she takes the initiative once Mr. Kinger pauses to write some english letters on the board, a friendly smile on her face."

        hide ragsmile
        show raghappy

        r "Hey new stuff, my name’s Ragatha!"

        hide raghappy
        show ragcheer

        r "I’m the class representative, so you can talk to me if there’s anything you need, like an extra pencil, or dealing with Jax if he gives you a hard time. Anything at all!"

        "I can tell she’s trying very hard to make me feel comfortable and like part of the class. As a transfer student, I appreciate the effort."

        show jaxsidesmirk2 at left
        with moveinleft 
    
        j "Well that’s not very nice, Raggy, badmouthing me to the new kid."

        "Based on the grin on the purple rabbit’s face, this must be the Jax that Ragatha is talking about."

        hide ragcheer
        show ragembarrassed at bounce, center
        pause (0.1)

        show ragembarrassed at myright
        with move

        r "Jax!"

        "She cries out, exasperated"

        show jaxsidesmirk2 at myleft
        with move

        hide ragembarrassed
        show ragindignant at myright

        r "Don’t sneak up on me like that."

        hide jaxsidesmirk2
        show jaxeyeshut at myleft

        j "Listen newbie, if you want to be the perfect straight A student, you can trust Ragatha to make that happen."

        hide ragindignant
        show ragnervoussmile at myright

        r "Oh, thanks Jax? That’s oddly nice of you"

        hide jaxeyeshut
        show jaxbored at myleft

        j "But you’re gonna bore everyone to tears and nobody’s gonna want to hang out with you."

        hide ragnervoussmile
        show ragannoyed at myright

        "His grin fades to an obstinate smirk as he continues."

        hide jaxbored
        show jaxsidesmirk at myleft
        j "Now, if you wanna have real fun, be cool, and be loved by everyone, I’m the guy to talk to."

        "Ragatha’s frown grows deeper as Jax keeps talking, interrupting him with her own rebuttal"

        hide ragannoyed
        show ragargue at myright

        r "I don’t think [avatar] wants to go around pulling pranks on everyone, and I really don’t think-"

        "Jax interrupts her again. These two must have some sort of history, leaping into any gap in one another’s argument to berate one another."

        hide jaxsidesmirk
        show jaxeyeroll at myleft

        j "Yeah yeah, I bet the new kid wants to spend all day reading textbooks, good one Ragatha."

        "Jax offers a humorless laugh as he mocks her to her face."

        hide ragargue
        show ragdisgust at myright

        r "Well that’s better than being a jerk all the time!"

        "The two keep interrupting and talking over one another. How has nobody noticed the escalating argument at the front of the classroom? Evidently, I’m the only one who wants to end this argument."

        menu:
            "I can enjoy a good prank, Jax":
                $ jaxpoint += 1
                jump jaxpranks1

            "What’s wrong with being a good student?":
                $ ragpoint += 2
                $ ragtour = True

                hide ragdisgust
                show raggrateful at myright

                "Ragatha smiles a friendly smile, turning to me with a look of genuine gratitude before turning to face Jax again."

                hide raggrateful
                show ragsmug at myright

                r " See, Jax? People like [avatar] want to focus on their academics."

                hide jaxeyeroll 
                with moveoutleft

                "Jax rolls his eyes and walks away. If he’s bothered about losing the argument, he hides it well."

                show ragsmug at center
                with move

                "Ragatha leans over to me."

                hide ragsmug
                show ragexcite at center

                r "If you want, can I give you a tour of the school during our lunch break?"

                "She pauses for a moment"

                hide ragexcite
                show ragnervouslaugh

                r "Only if you want to though, I totally get wanting to be left alone on your lunch break!"

                "Well, she may not be the most assertive member of our class, but I can tell her smile and positivity are genuine."

                "A part of me is excited to start our class tour, but another part of me worries that if I tell Ragatha that, her doting on me might start to smother me."

                jump seatchoice_done

        label jaxpranks1:
            
            hide jaxeyeroll
            show jaxsidesmirk at myleft

            hide ragdisgust
            show ragpout at myright

            "Jax smirks, seeing he has won this argument."

            j " See, doll face? The newbie knows what fun is."

            "Ragatha huffs at his rebuke, but accepts defeat, turning back to the lecture."

            hide ragpout
            with moveoutright

            hide jaxsidesmirk
            show jaxshrug at myleft

            j "Normally this is the time our “class rep” would bore you with a tour of the school,"

            hide jaxshrug
            show jaxwink at myleft 
            
            j "I’m feeling generous today. I’ll show you around the place, how’s that sound?"

            "Ragatha lets out another indignant huff, apparently she is still paying some attention to me and Jax."

            menu:
                "Sure, that sounds fun!":
                    $ jaxpoint += 2
                    $ jaxtour = True

                    j "Alright, find me at lunch time."

                    "Jax swaggers back to his desk, savoring his victory. Guess I know what I’m doing for lunch today."
                    jump seatchoice_done

                "Actually I wouldn’t mind taking the tour with Ragatha":
                    $ ragpoint += 2
                    $ ragtour = True

                    show ragnervousexcite at myright
                    with moveinright

                    hide jaxwink
                    show jaxnonchalant at myleft

                    "Ragatha perks up at my response, her friendly smile springing back to her face."

                    "Jax surrenders his grin, but if even cares that I just turned him down, he doesn’t show it."

                    hide jaxnonchalant
                    with moveoutleft

                    r "O-oh really? Well, how about we meet during lunch and I give you the grand tour?"

                    "I glance back at Jax again, but he is already back at his desk." 
                    "If he sees my glance, he doesn’t acknowledge it. I decide to focus on my conversation with Ragatha instead."

                    a "Thanks for offering, that sounds nice."

                    jump seatchoice_done

    label kingsit:
        $ kingpoint += 1

        scene homeroom bg
        show morning at top_left

        show kingneutral 

        "I sit on Kinger’s open seat behind his desk." 
        "The chess piece blinks at me for a moment before surveying the other open desks. He seems content to let me take his seat."

        show kingcurious

        k " I guess you’re the teacher now."

        "The mismatched figure speaks up, raising their hand before calling out to Mr. Kinger."

        show zoobbasic at left
        with moveinleft

        z "Very funny, Kinger. You have to teach the class, now make them pick another seat."

        hide zoobbasic
        with moveoutleft

        "Mr. Kinger looks at me apologetically."

        hide kingcurious
        show kingexplain

        k "Sorry, but them’s the rules kid."

        jump seatchoice

    label gansit:
        scene homeroom bg
        show morning at top_left
        with None
        
        show ganfocus with moveinbottom

        "I sit next to the shy-looking girl with a comedy mask and ribbon body."

        "But even as I sit down and look at my new desk neighbor, she doesn’t seem to have noticed me."

        "Instead, she’s drawing something in her sketchbook. I’m not used to being ignored like this, so I lean over to see what she’s drawing."

        "Once she notices me, she flinches away, blushing furiously."

        hide ganfocus
        show ganembarrassed at bounce, center

        "Oh sorry! I-I didn’t see you there!"

        hide ganembarrassed
        show gannervousblush

        "You’re the new student, right [avatar]? I’m Gangle…"

        "She seems really timid, I’m not sure there’s anything I could do that would make her feel at ease."

        a "Nice to meet you Gangle, what are you working on?"

        hide gannervousblush
        show ganhesitant

        g "Oh these?"

        "Gangle seems surprised by the question but doesn’t shy away from responding"

        hide ganhesitant
        show gannervous

        g "Uhm well, sometimes I just like to sketch, they’re not really good or anything."

        a "That’s cool, so you’re an art student?"

        "Gangle offers me a sheepish smile."

        hide gannervous
        show ganexplain2

        g "That’s right, I guess you could call me an artist."

        "She pauses a moment, seeming to revel in that statement, before timidly correcting herself."

        hide ganexplain2
        show ganapprehensive

        g "I mostly just sketch and stuff. Nothing crazy."

        "Right as I catch a glimpse of her happy demeanor, she retreats back into her own shyness."

        "I’m about to open my mouth to ask about her skittishness when the abstract figure near me speaks up."

        show ganapprehensive at myright
        with move

        show zoobbasic at myleft
        with moveinleft

        z "Gangle’s just being modest." 

        hide zoobbasic
        show zoobneutral2 at myleft
        
        z "She’s actually a really good artist, and the star of our school’s art club."

        hide ganapprehensive
        show gansmallblush at myright

        "Gangle blushes again, giving another one of the shy smiles that seem to be her trademark." 
        "The blush and the smile are kind of cute on her."

        g "Oh, thanks"

        hide gansmallblush
        show ganshy at myright

        g "I think your art is really good too, Zooble!"

        "So that’s what their name is!"

        "Gangle seemed pretty confident talking to Zooble, they must have a history."

        a "So you’re both artists?"

        "Zooble shrugs."

        hide zoobneutral2
        show zoobshrug at myleft

        z "I do a little bit when I have time, I don’t do it as often as Gangle though."

        a "Huh, can I see your art…"

        menu:
            "Gangle?":
                $ ganpoint += 1
                jump ganart

            "Zooble?":
                $zoopoint += 1
                jump zoobart


    label ganart:

        hide zoobshrug
        with moveoutleft

        show ganshy at center
        with move
        
        "I asked Gangle to see her art first."

        hide ganshy
        show ganoh at center

        g " O-oh well maybe uhm..."

        hide ganoh
        show ganfocus

        "She rifles through the papers, taking a few moments to look for one she deems good enough to show."

        hide ganfocus
        show gantimid

        "She timidly hands me the sketch."

        "An anime style sketch, complete with big eyes, small mouth, and a big head."

        "Upon further inspection it kind of looks familiar. Gangle interrupts your thoughts."

        hide gantimid
        show gannervous

        g "It’s kind of a rough sketch…"

        hide gannervous
        show ganunsure 

        "Please don’t look too close."

        "She says the latter phrase under her breath, I'm not sure if she intends for me to hear her or not."

        menu:
            "This is impressive Gangle.":
                $ ganpoint += 1
                $ lunchinvite = True

                hide ganunsure
                show ganshy

                "Gangle smiles and blushes, timidly taking back her sketch and giggling."

                g "Thank you…that’s really nice of you to say…"

                "There’s a lingering warmth in her tone and smile as she goes back to sketching."

                hide ganshy
                show ganbasic

                "I feel like I’m getting along well with Gangle, despite her shyness."

                "I try to pay attention to Mr. Kinger’s lecture, but I can’t help but steal an occasional glance at Gangle’s sketchbook."

                "When class is getting ready to end,  I feel one of her ribbons gently tap my shoulder."

                g "M-me and Zooble usually sit outside in the courtyard during Lunch, you should join us."

                "I can’t deny the offer is very tempting."

                jump seatchoice_done

            "Yeah I can see its pretty rough":
                $ ganpoint -= 1
                $ zoopoint -= 1

                hide ganunsure
                show gansad

                g "Oh..."

                "She takes her sketch back before hiding it under some papers."
                "She’s trying to hide it, but I can see she’s on the verge of tears."

                show zoobangry2 at myleft
                with moveinleft

                show gansad at myright
                with move

                z "You don’t have to be rude about it. Just because you don’t like it doesn’t mean it isn’t good."

                "If looks could kill, Zooble would have made me wither to nothing on the spot." 
                "Still, I don’t know what favors I’m doing anybody by pretending I like Gangle’s art."

                "The two of them ignore me for the rest of the lecture. That suits me fine. All I did was offer my genuine opinion." 
                "Still, I keep my gaze to my own notebook and Mr. Kinger’s lecture until the lunch bell rings."

                jump seatchoice_done

    label zoobart:
       
        "I turned to face Zooble to check out their art. Unlike Gangle, Zooble barely reacted to my request, tossing their notebook on my desk."

        hide ganshy
        with moveoutright

        hide zoobshrug
        show zoobbasic at myleft
        pause (.1)

        show zoobbasic at center
        with move

        "Have fun."

        "I opened their notebook. There’s a sketch of something really intricate, the line work is complex and varied." 
        "From a technical standpoint alone, this is impressive."

        menu:
            "Wow, this is really cool, Zooble!":
                $ zoopoint += 1
                $ lunchinvite = True

                hide zoobbasic
                show zoobshy

                "Zooble doesn’t have a mouth, but what functions for their eyebrows tells me they're pleased by my compliment."

                z "Thanks, [avatar]"

                hide zoobshy
                show zoobneutral

                "Zooble nods, paying attention to the lecture, then adds, as if it were an afterthought,"

                hide zoobneutral
                show zoobbasic

                z "If you want to sit with me and Gangle, you can find us in the courtyard during lunch."

                "There wasn’t a lot of enthusiasm in that invitation, but Zooble doesn’t seem to get excited for anything, so I don’t take it personally."
                "Better than sitting alone like I used to at my old school."

                jump seatchoice_done

            "I’ve seen better":
                $ zoopoint -= 1
                $ ganpoint -= 1

                hide zoobbasic
                show zoobsquint

                "Zooble snatched their notebook back from me, their eyes narrowing."
                "I didn’t think they would be so sensitive about their art."

                hide zoobsquint
                show zoobthreaten

                z "Yeah, I guess I have too."

                "They’re looking directly at my face instead of at my art. Ouch!"

                "As Zooble glares at me, Gangle moves over to soothe their temper."

                show ganhesitant at myright
                with moveinright

                show zoobthreaten at myleft
                with move

                g "I-I think your art is good, Zooble!"

                hide zoobthreaten
                show zoobannoyed at myleft

                "Zooble’s scorn is averted from me as they begins to talk to Gangle. The two of them ignore me for the rest of the lecture." 
                "That suits me fine. Zooble seems a little too easy to offend, all I did was offer my genuine opinion."
                "Still, I keep my gaze to my own notebook and Mr. Kinger’s lecture until the lunch bell rings."

                jump seatchoice_done

    
    label pomsit:

        scene homeroom bg
        show morning at top_left

        "I take a seat next to the girl in the colorful hat."

        show pomcautioussmile with moveinbottom

        p "Oh, um, hi!"

        "She gives me a shy wave, as if she's surprised I want to sit next to her."

        a "Hello there."

        "I squint down at her desk."

        "Written on it is the name XDDCC, though I'm pretty sure I heard another student address her as Pomni."

        a "Uhm, Exduh..."

        a "Exduduch..."

        hide pomcautioussmile
        show pomsweatsmile

        p "I-it's Pomni."

        "She says, covering the plaque on her desk with one of her gloves."

        p "Just Pomni."

        "She lets out a sigh."

        hide pomsweatsmile
        show pomexplain

        p "When I first got here, well, it's a long story...but basically I couldn't remember my name. So Caine tried to make one up for me."

        hide pomexplain
        show pomerm

        p "For the first few days here, I was XDDCC."

        "How did she manage to pronounce that??"

        hide pomerm
        show pomsweatsmile2

        p "But nobody could pronounce that, so we ended up going with the second name he picked out, Pomni."

        "Guess that makes sense."

        "As much sense as anything makes here at least."

        hide pomsweatsmile2
        show pomneutral

        p "Though come to think of it, since you just showed up, I'm officialy {i} not {/i} the newest one around here."

        hide pomneutral
        show pomcheery

        p "So I can show you the ropes, if you're interested."

        "Just as she says that, the ragdoll student at the front of class seems to take notice of us, walking over to our desks."

        show pomcheery  at myleft 
        with move
        hide pomcheery
        show pomheadtilt at myleft 
        with None

        show ragcheer at myright 
        with moveinright

        r "Oh, hi you two!"

        r "Pomni, are you making friends with the new transfer student?"

        hide pomheadtilt
        show pomsweatsmile2 at myleft

        p "Hey Ragatha..."

        p "Yep, just talking to [avatar]."

        "Pomni turns to me."

        hide pomsweatsmile2
        show pomexplain at myleft

        p "Uh, [avatar], this is Ragatha. She's our class president."

        "Ragatha extends a hand towards me."

        hide ragcheer
        show ragconfident at myright

        r "Welcome to our school, [avatar]! If you ever need help with anything at all, I'm your gal!"

        "She beams."

        hide ragconfident
        show ragcheerconfident at myright

        r "I'm happy you and Pomni are getting along, can I tempt you with a tour of the school later?"

        r "Maybe Pomni can come along too, what d'ya think?"

        "Pomni interjects,"

        hide pomexplain
        show pomnervoussmile at myleft

        p "Oh, uh, that's really okay Ragatha. I've been on your tour a few times. I'll er- sit this one out."

        hide ragcheerconfident
        show ragnervousexcite at myright

        r "Oh...you sure? Well okay! What do you say, [avatar]?"

        "She says, leaning towards me."

        menu:
            "A tour sounds great, Ragatha":
                $ ragpoint += 2
                $ ragtour = True
                jump ragacuck

            "Actually, I'd like to keep talking with Pomni.":
                $ pompoint += 2
                jump pomchad
            
            "Can you two jump off my back? I just sat down.":
                $ pompoint -=1
                $ ragpoint -=1
                jump pomragtantrum
        
        label ragacuck:
        
        hide ragnervousexcite
        show ragexcite at myright

        hide pomnervoussmile
        show pomsweatsmile2 at myleft
        
        r "That's just swell, [avatar]!"

        "Ragatha says with a pump of her fist before leaning over to Pomni."

        hide ragexcite
        show ragnervouslaugh at myright

        r "Are you suuuure you don't wanna come along, Pomni?"

        "Pomni looks away."

        hide pomsweatsmile2
        show pomsweatsmile at myleft

        p "N-no, it's okay, you two have fun."

        "Pomni's attention goes back to class, as Ragatha has monopolized my time."

        hide pomsweatsmile with moveoutleft
        show ragnervouslaugh at center with move

        hide ragnervouslaugh
        show ragnervousexcite 

        r "Welp! Guess it's just us this afternoon, [avatar]!"

        "I guess so."

        jump seatchoice_done

        label pomchad:

            hide ragnervousexcite
            show ragnervouslaugh at myright

            hide pomnervoussmile
            show pomcautioussmile at myleft

            p "O-oh? Cool..."

            "Pomni gives me a small smile"

            r "Right, sure thing! I'll leave you two to it, then!"

            "Ragatha seems to take it all in stride."

            hide ragnervouslaugh with moveoutright
            show pomcautioussmile at center with move

            p "It's kind of cool to have someone else new to talk to."

            a "Really?"

            hide pomcautioussmile

            show pomsoft

            p "Yeah, I mean, everyone here treats all the weirdness of the school like its just business as usual."

            hide pomsoft
            show pomgrin

            p "Now I get to see how {i} you {/i} react to all the weirdness for the first time."

            "{i} gulp {/i}"

            "It gets {i} weirder {/i} than this?"

            jump seatchoice_done

        label pomragtantrum:

        hide ragnervousexcite
        show ragembarrassed at myright
        hide pomnervoussmile
        show pomtrauma at myleft

        a "I mean seriously, I can't even catch my breath."

        p "Uh..."

        hide ragembarrassed
        show ragconcern at myright

        r "Oh, that's okay [avatar]."

        r "I didn't mean to overstimulate you."

        "Overstimulate?"

        hide ragconcern
        show ragawkwardblush at myright
       
        r "The offer for a tour is still open, you know, if you're..."

        "She trails off, returning to her desk."

        hide ragawkwardblush with moveoutright

        show pomtrauma at center with move
        hide pomtrauma
        show pomawkward

        p "So, uh, what was that all about?"

        a "I mean I just sat down."

        a "I feel like I was just starting to talk to you, and then she got up in my face, and-"

        hide pomawkward
        show pomdisapproval

        "There's an awkward pause, I may have killed the vibe."

        p "Well Ragatha can get on people's nerves sometimes, but that's no excuse to be so rude to her."

        "Pomni turns away from me."

        "Any attempts I make at conversation are met with one-syllable answers."

        "Yep."

        "I {i} definitely {/i} killed the vibe."
        
        jump seatchoice_done

        label zoosit:

            scene homeroom bg
            show morning at top_left
            with None

            show zoobbasic with moveinbottom

            "I sat down next to the interesting-looking student with mis-matched limbs."

            hide zoobbasic
            show zoobannoyed

            z "{i} Sigh {/i}"

            z "I'm not going to bother asking you your name or backstory if that's what Caine wants."

            a "I'm sorry?"

            hide zoobannoyed
            show zoobeyesclosed

            z "You heard what I said. After a week, Caine is gonna get bored of all this, and you won't even be here anymore."

            "Did I do something to offend them?"

            a "Why do you think I'm going to be gone in just a week?"

            hide zoobeyesclosed
            show zoobexplain
            
            z "Cause that's just how things work around here."

            z "Caine comes up with some new student or adventure,"

            z "Everyone gets excited to know them."

            hide zoobexplain
            show zoobeyesclosed2

            z "Then Caine gets bored, or they move away."

            hide zoobeyesclosed2
            show zoobannoyed

            z "Honestly, I don't even know why I'm telling you all of this."

            "Nothing they say makes any sense."

            "But I'm still offended at being treated like some sort of side act in a circus."

            a "Well I didn't ask to be here."

            a "All I remember is something happened at my old school, and my parents had to move out to the countryside."

            "I huff."
            
            a "That's the only reason I'm here right now."

            hide zoobannoyed
            show zoobirritated

            "Zooble glares back at me, but before we can start to argue, the girl in the colorful hat comes over to us."

            show zoobirritated at myright with move
            show pomneutral at myleft with moveinleft
            show pomneutral with moveinleft


            p "Hey guys, what's going on over here?"

            "She says, looking at us."

            a "Well they-"

            "I point to Zooble."

            a "Just keep saying I'm going to dissappear in a week when principal Caine gets bored of me."

            hide pomneutral
            show pomsweatsmileblush at myleft

            p "Well, that's no good..."

            "She waves her hands, trying to diffuse the situation."

            hide pomsweatsmileblush
            show pombored at myleft

            p "You know how Caine gets when we don't play along, Zooble."

            hide zoobirritated
            show zoobannoyed at myright

            z "How Caine feels about things isn't my problem."

            "To illustrate their point, they kick their feet up on the desk in front of them."

            "Pomni just shakes her head before extending a hand for me to shake."

            hide pombored
            show pomcautioussmile at myleft

            p "Well, anyways, welcome to our class, [avatar]."

            p "Sorry about Zooble, they just don't really like new people...or Caine."

            "I nod."

            a "I can see that."

            hide pomcautioussmile
            show pomheadtiltsmile at myleft

            p "Well, if you want, you can come sit next to me instead?"

            p "I'm sure Kinger won't mind."

            "I cast a glance at Zooble, who is still ignoring me"

            "The invitation is tempting..."

            menu:
                "Sure, I'll sit next to you Pomni.":
                    $ pompoint += 2
                    jump pomswap

                "I think I'll stick it out with Zooble.":
                    $ zoopoint += 2
                    jump zoobsit
            
                "I don't really care where I sit.":
                    jump boringmorning1

            label pomswap:

                hide zoobannoyed
                hide pomheadtiltsmile
                show pomcautioussmile at myleft
                show pomcautioussmile at center with move

                "I take Pomni's hand as she leads me to a desk next to her."

                p "You know, I'm actually the newest one here, so I kind of understand what you're going through."

                "I doubt anyone understands what I'm going through right now, but I appreciate the sentiment."

                a "This place just gets weirder and weirder the more time I spend here."

                hide pomcautioussmile
                show pomsweatsmile2

                p "Yeah I get that."

                "There's an awkward pause between us. In the background, Mr. Kinger continues his lecture on English."

                hide pomsweatsmile2
                show pomconfident

                p "Well, during lunch, I like to go to the library, in case you want to join me?"

                "She looks up at me."

                "I smile back at her. I might just have to take her up on that."

                jump seatchoice_done

             
            label zoobsit:
                $ lunchinvite = True

                hide pomheadtiltsmile
                show pomneutral at myleft
                hide pomneutral with moveoutleft
                
                hide zoobannoyed
                show zoobbasic at myright 
                pause (0.1)
                show zoobbasic at center 
                with move

                z "Suit yourself, don't think this make us friends or anything."

                "I guess not, but I find myself oddly unbothered by Zooble's cool demeanor."

                a "That's fair."

                "I shrug."

                a "I'm sure you have a reason for feeling the way you do."

                "That, oddly, seems to pierce their cool exterior."

                hide zoobbasic
                show zoobsurprise

                z "Huh?" 

                hide zoobsurprise
                show zoobconcern
                
                z "Well, uh, yeah. I-I do..."

                a "I feel like you just really dislike principal Caine?"

                hide zoobconcern
                show zoobeyesclosed3

                z "Well, yeah, dislike is an understatement."

                "They pause."

                hide zoobeyesclosed3
                show zoobsquint

                z "He just keeps trying to come up with new things and acts like we should be falling over ourselves."

                "I shrug."

                a "It's okay, you don't have to like me..."

                hide zoobsquint
                show zoobhesitant

                z "Well, it's not that I don't like you-"

                z "It's just that...nevermind."

                a "It's okay."

                z "For what its worth, I'm sorry I was so harsh on you."

                hide zoobhesitant
                show zoobneutral

                z "Listen, to make it up to you, I usually eat lunch with Gangle in the courtyard. You can tag along if you want. You know, instead of sitting alone."

                "Just as I'm about to respond, Zooble sees something out of the corner of their eye."

                hide zoobneutral
                show zoobangry
                show zoobangry at myleft with move
                show jaxmischief at myright with moveinright
                show ganbigcry at right with moveinright

                z "Leave Gangle alone, Jax!"

                "They say, running off."

                "Oh well."

                "I guess if I want to talk to them later, I know where to find them."

                jump seatchoice_done

            label boringmorning1:

                hide pomheadtiltsmile
                show pomawkward at myleft

                p "Okay, sure thing, [avatar]..."

                hide pomawkward with moveoutleft

                "Pomni walks back to her desk."

                "Zooble just sits there and ignores me."

                "What little attention they do pay in class goes directly to the ribbon-girl on her left."

                show gancheery at right with moveinright

                "{i} Sigh {/i}"

                "Guess its gonna be a quiet morning for me."

                jump seatchoice_done

                
label seatchoice_done:
    
    stop music fadeout 1.0
    scene homeroom bg
    with flash
    show morning at top_left

    "I was just settling into my desk and getting used to this place when something burst into the room."


    show kingcheerysr at left
    with moveinleft

    k "Principal Caine, how exciting to have you in our class today!"

    hide kingcheerysr
    with moveoutleft

    "The new figure turned to address us. At his side was a bubble with razor-sharp teeth." 
    "I don’t think I’ll ever get used to this school."

    play music "audio/Caine-theme.mp3" volume 0.4 fadein 1.0

    show cainexcited at center
    with moveinright

    show bubble at myright
    with moveinright

    c "Kinger! Class! How do you do!"

    hide cainexcited
    show cainwallbrk 

    "Principal Caine extends a hand, gesturing to all of us, before freezing in place."

    hide cainwallbrk
    show cainmouthclosed 

    "With a sound like porcelain grinding against porcelain, his teeth slam shut."

    hide cainmouthclosed
    show caine_glitch 

    "his eyes slowly extrude from his teeth, like they’re not solid objects."

    hide caine_glitch
    show cainmoutheyes 

    c "[avatar]! Wasn't expecting {i} you {/i} here!"

    "Manic enthusiasm suffuses his voice as he points his cane at me."

    hide cainmoutheyes
    show cainpointing 

    c "Maybe you’ll be the secret ingredient to make this school interesting."

    hide cainpointing
    show cainderpthink 

    "He pauses a moment, rubbing the base of his chin in contemplation for a moment."

    show zoobirritated at left with moveinleft

    z "Is there a reason you’re here, Caine?"

    "Zooble speaks to him like they’re addressing an annoying insect instead of the principal of the school."

    hide zoobirritated with moveoutleft

    "Caine perks up."

    hide cainderpthink
    show cainright 

    c "That’s right, the reason I’m here, to make sure we all have an enriching academy experience! One filled with fun, danger, adventure..."

    "He begins to list more and more descriptors, increasing his breakneck speed until I can’t even tell what he’s saying."

    hide cainright
    show cainwallbrk 

    c "And most of all, interesting to our studio audience!"

    "He turns towards the window and stares out of it for a moment."
    "Is he addressing somebody? There doesn’t appear to be anyone outside."

    hide cainwallbrk
    show cainactually3 

    c "However, the numbers are in, students, and it turns out school dramas are just white noise."

    hide cainactually3
    show cainbite 

    c "Normally, this is the time that I’d tell you that means the end of school life as we know it!"

    "Caine bites on his hands in mock horror, the class and Kinger play along, gasping at this revelation. Gangle looks ready to burst into tears."

    hide cainbite
    show cainmyself

    c "However, my sweet-toothed students, your benevolent principal has found a way to bring public interest back to the school in a major way!"

    "At this point, the sharp-toothed bubble next to him pipes up."

    hide bubble
    show bub talk at bounce, myright

    b "How are you bringing interest back to the school, mister President?"

    hide cainmyself
    show cainsquintright 

    "Caine shoots the bubble a confused look, but hits his stride a moment later."

    hide bub talk
    show bubble at myright

    hide cainsquintright
    show cainshrug 

    c "You see my little Tomar emeralds, what’s one thing no academy around here has ever had?"

    show jaxsly at left with moveinleft

    j "A cast of colorful characters?"

    hide jaxsly with moveoutleft

    show zoobannoyed at left with moveinleft

    z "A competent principal?"

    hide zoobannoyed with moveoutleft

    show ragthink at left with moveinleft

    r "Adequate funding?"

    hide ragthink with moveoutleft

    "Caine shakes his head."

    hide cainshrug
    show caincount

    c "Wrong, wrong, and surprisingly right but also not relevant to what I’m talking about!"

    hide caincount
    show cainexcited

    c " No, no school around here has had a culture festival, celebrating the unique talents of its students!"

    hide cainexcited
    show cainshowoff

    c "So I, being your benevolent principal, have decided to put your class in charge of throwing the best culture festival this side of the Pacific ocean!"

    hide cainshowoff
    show caingettem

    c "Make it flashy, we gotta keep the interest of our investors after all!"

    hide caingettem
    show caintime at bounce, center

    c "Egads! I’m almost late for my deep tissue massage!"

    hide caintime
    show cainneutral

    c "Alright Kinger, I'll leave you the list of everyone's responsibilities,"

    hide cainneutral
    show caingettem
    
    c "you all have five days! Break a leg or two!"

    hide bubble with moveoutright
    hide caingettem with moveoutright

    stop music fadeout 1.0

    "As abruptly as he appeared, Caine darted out of the room, disappearing from view as he headed to his appointment."

    play music "audio/Morning.mp3" volume 0.5 fadein 1.0

    show kingneutral at center
    with moveinbottom

    k "Alright class, let's see what roles Caine assigned to each of you for the culture festival."

    "Kinger lifts a paper from his desk and begins to read aloud." 

    hide kingneutral
    show kingpointing
    
    k "Ragatha, as the class representative, I trust you to organize the other students and make sure the festival proceeds with no issues."

    show ragconfident at left 
    with moveinleft

    r "You can count on me!"

    hide ragconfident with moveoutleft

    hide kingpointing
    show kingsquint

    k "Zooble and Gangle, you two will work on art to promote the festival." 

    hide kingsquint
    show kingexplain2
    
    k "We have a pretty big school here, so we’ll need plenty of posters, and some art to display during the festival."

    show ganapprehensive at right 
    with moveinright

    g " I-I don’t know, I still don’t have anything I’m comfortable showing everyone else..."

    show zoobeyesclosed3 at left 
    with moveinleft

    z "..."

    hide zoobeyesclosed3 with moveoutleft
    hide ganapprehensive with moveoutright

    hide kingexplain2
    show kingcurioussr

    k "Pomni and Jax, look up what a culture festival is!"

    show pomconfused at right 
    with moveinright

    p "Shouldn’t we do that before we start making posters?"

    show jaxsidesmirk at left
    with moveinleft

    j "No, I like his idea. Plus, we get to see what Gangle comes up with for her posters. If it’s anything like what she comes up with when she draws Ragatha."

    hide pomconfused
    show gansurprise at right
    with moveinright

    g "Jax!"

    "Gangle interrupts Jax before he can finish his thought, pleading with him to stay quiet."

    hide gansurprise
    hide jaxsidesmirk
    hide kingcurioussr
    with moveoutbottom

    "The class erupts into chaos as Zooble and Gangle argue with Jax, Pomni tries to find out what a culture festival is, and Ragatha tries to salvage what remains of class and get her classmates to pay attention."

    "For his part, Mr. Kinger seems content to let the students bicker amongst themselves, maybe he didn’t have the rest of his lesson planned and is just waiting out the lunch bell."

    play sound "audio/schoolbell.mp3" volume 0.5

    stop music fadeout 1.0

    "As if I had summoned it by thinking of it, the lunch bell sounds. Everyone drops their arguments and files out of the classroom. Time to find out what I’m doing for lunch."

    play music "audio/Afternoon.mp3" volume 0.5 fadein 1.0

    scene lunchroom bg
    with flash
    show afternoon at top_left

    "After my chaotic first half of the day, I had worked up quite the appetite."

    "The cafeteria was bustling with unfamiliar faces. Around me, there was a selection of places to buy lunch, but none of them stood out from one another."

    "I pick up something to eat at the nearest food place and set about deciding where to sit down. Still, as I scan the bustling lunchroom, I don’t recognize anyone from class."

    if jaxtour:
        "Finally, I see a familiar tall figure walking out of the lunch room."

        "I pick up my pace to catch up to him."

        show jaxbored2 with moveinbottom

        a "Jax!"

        a "I don’t think he heard me."

        "Finally, out of breath and panting, I catch up to my new tour guide."

        a "*pant, pant*" 
        
        a "Jax, weren’t you gonna give me a tour of the school?"

        hide jaxbored2
        show jaxwut

        j "Wha?"

        "He looks completely surprised."

        hide jaxwut
        show jaxeyebrow

        j "A tour?"

        hide jaxeyebrow
        show jaxthink

        j "Oh yeah, the tour."

        "Understanding dawns on him, and his surprised expression is quickly covered with a sly grin."

        hide jaxthink
        show jaxsidesmirk

        j "I made it up. Just trying to piss off Ragatha."

        a "Well, I’m here, so what are we going to do?"

        hide jaxsidesmirk
        show jaxnonchalant

        j "We?"

        hide jaxnonchalant
        show jaxnope

        j "There is no {i}“we,”{/i} new kid"

        hide jaxnope
        show jaxthink

        j "But if you’re so desperate to hang out with me, I have an idea."

        hide jaxthink
        show jaxsmile

        j "Let’s go on a little field trip outside."

        a "Are we allowed to do that?"

        hide jaxsmile
        show jaxeyeroll

        "Jax rolls his eyes."

        j "Jeez, you sound like a broken toy. Is that the only thing you say?"

        "I shake my head, I don’t want to disappoint Jax."

        hide jaxeyeroll
        show jaxwink

        j "It doesn’t matter what we’re allowed to do, it matters if we get caught. So keep up, new kid."

        "He finds a door leading to a field, slyly pushing it open before bounding through." 
        "I have to sprint to make it through before the door locks."

        jump jaxlunchD1
    
    label lunchdecision:
        scene lunchroom bg
        show afternoon at top_left

        menu:
            "I could check the library, maybe Pomni or Jax is there trying to find out what a culture festival is" if pompoint >= 2 or jaxpoint >= 2:
                jump libraryD1

            "Didn’t Zooble and Gangle say they ate lunch in the courtyard?" if zoopoint >= 2 or ganpoint >=2:
                jump courtyardD1

            "I think Ragatha wanted to give me a tour of the school" if ragpoint >= 2:
                jump tourlunch

            "I guess I could just take my lunch back to the classroom" if not kinglunch:
                $ kinglunch = True
                jump classroomD1

            "I sat alone, there’s nobody I felt particularly close to":
                jump lonerlunch

    
    label libraryD1:
        scene library bg
        with flash
        show afternoon at top_left

        "I walked into the library with my tray in my hand." 
        "I peered through the rows of dusty, cluttered, shelves, and I saw Jax and Pomni by the tables in the middle of the library."

        "Even from here, I can tell Jax is up to trouble, he’s tapping his foot impatiently and pacing back and forth." 
        "I can barely make out Pomni, craning her neck to peer up into the tall bunny’s yellow eyes."

        "As I gingerly maneuver between the shelves, trying to avoid spilling the creamed corn casserole I brought from the cafeteria, I can make out some words."

        p "Going to…with…Kinger asked us to…"

        "I can’t hear Jax’s response, but I don’t have to, as he mimics Pomni’s mannerisms, tilting his head from side to side."

        "As I get closer, I can hear her trying to reason with the stubborn rabbit."

        show pompout at myright
        with moveinright

        p "We should at least {i}try{/i} to do what he said. I don’t want to be the only one who didn’t do anything to help."

        "Against my better judgement, I creep closer, nearly tripping over a step-stool. I manage to creep into earshot."

        show jaxshrug at myleft
        with moveinleft

        j "Why? This whole thing is pointless, and no one will even notice if we bail, trust me."

        hide jaxshrug
        show jaxeyeroll at myleft

        "Jax crosses his arms, leaning back and letting out an annoyed sigh."

        "As he leans back, he catches sight of me."

        "Oop!"

        hide jaxeyeroll
        show jaxwut at myleft

        j "Hey, new kid!"

        "He calls out to me."

        hide jaxwut
        show jaxwink at myleft

        j "What do you think? We should ditch this dumb culture fair thing, right?"

        hide pompout
        show pomsass at myright

        p "Their name is [avatar], Jax."

        p "Second off, they were in class with the rest of us. I bet they want to stay on Caine’s good side as much as the rest of us."

        hide jaxwink
        show jaxmischief at myleft

        j "I bet they'd rather do something fun like pulling an epic prank."

        hide pomsass
        show pomhope at myright

        "Pomni gives me a meaningful look."

        "Jax shoots me a mischievous grin."

        "I feel like I should choose my response carefully here."

        menu:
            "Pomni’s right, we all have a part to play to make the culture fair a success!":
                $ pompoint += 1
                jump pomlunchD1

            "That sounds fun Jax, I don’t care about the culture fair, let’s go pull a prank!":
                $ jaxpoint += 1
                $ jaxprank = True

                hide jaxmischief
                show jaxsidesmirk at myleft

                hide pomhope
                show pombored at myright

                j "Hah! See Pomni? The new kid's cool."

                hide pombored
                show pomeyesclosed at myright

                p "Alright, well you two have fun then."

                "She turns back to the shelves while Jax ushers me out of the library."

                j "Later, Pom-Pom!"
                
                jump jaxlunchD1
                
        label pomlunchD1:
        
        hide pomhope
        show pomreassure at myright

        hide jaxmischief
        show jaxannoyed2 at myleft

        p "Thank you, [avatar]."

        "She trails off, giving me a nervous but genuine smile."

        "Jax scowls for a moment, but recovers quickly."

        hide jaxannoyed2
        show jaxshrug at myleft

        j " Whatever, see you losers later."

        j "You know, I still have a lot of gum to chew."

        hide jaxshrug
        show jaxsly at myleft

        j "Maybe I’ll find a book about culture festivals and stick all the pages together!"

        hide jaxsly with moveoutleft

        "Jax gives a mischievous grin before strolling out of the library. I hope he wasn’t serious."

        show pomreassure at center
        with move

        hide pomreassure

        show pomunsure 

        p "Ignore him, he probably isn’t going to do that."

        hide pomunsure
        show pomawkward

        "There’s an awkward pause as neither of us seem to know what to say, before Pomni breaks it for us."

        hide pomawkward
        show pomreassure

        "So, it looks like it's up to us new kids to find out what the culture fair is about!"

        "I nod."

        a "How hard could it be to find a book about culture festivals?"

        scene library bg
        show afternoon at top_left

        "We proceed into the depths of the library, I pretty much forget about lunch as we search the shelves." 
        "Each book is so caked with dust, it feels like the library is a forgotten archive."
        "The more we scour the shelves, the more we realize how daunting of a task this actually would be."

        show pomunsure with moveinbottom

        p "These don’t seem to be organized by genre…"

        "She looks over at me."

        a "Yeah and they don’t seem to be in alphabetical order either."

        a "What’s on your shelf?"

        "Pomni lifts up a book with a happy puppy on the front, the title reading “Spot’s day out”."

        hide pomunsure
        show pomtalk 

        p "This was between a book of dessert recipes and a calculus textbook."

        a "So it’s really just random, huh?"

        hide pomtalk
        show pomtrauma

        p "Oh god this could take all day…"

        "Pomni seems to deflate at the prospect."

        a "H-hey! There’s two of us, that’s double the search power!"

        a "We’ll take it one shelf at a time, we got this!"

        hide pomtrauma
        show pomconfused

        "I do my best to reassure her. She looks at me a bit skeptically before nodding."

        hide pomconfused
        show pomsweatsmile2

        p " You’re right."

        hide pomsweatsmile2
        show pomconfident

        p "We can do this!"

        "We both get back to the search, carefully inspecting the spines of every book on the shelves." 
        "Eventually we split to different parts of the library trying to maximize our progress."

        hide pomconfident
        show pomnervoussmile

        p "Uh, little help?"

        "Pomni seems to have found a book she wants, but she’s too short to get to it."

        a " I’m coming, Pomni."

        "I stride between the bookshelves, coming up to her side. She points at a book on the higher shelves, I reach for it but no luck. It’s a bit too high for me as well."

        a "Did you want me to lift you or?"

        "Pomni goes flush at the idea."

        hide pomnervoussmile
        show pomsweatsmileblush

        p "Oh uh no that’s okay…"

        a "It’s alright, I promise I’m stronger than I look. I won’t drop you."

        "I flex my bicep jokingly, flashing a big grin at the jester girl. Pomni chokes an awkward laugh."

        hide pomsweatsmileblush
        show pomnervoussmile

        p "I-it’s not that, it’s just…I just…prefer if you didn’t."

        hide pomnervoussmile
        show pomawkwardsmile

        "She smiles at me timidly as she clutches her arm. It seems Pomni doesn’t want to be touched." 
        "I realize I was pushing a boundary and suddenly backtrack, not meaning to make her uncomfortable."

        a "Oh okay, no worries!"

        hide pomawkwardsmile
        show pomtalk

        p "There has to be a step-stool around here or something…"

        "I remember tripping on a step-stool by some shelves when I entered the library."

        a "Oh! Here!"

        "I dip out quickly to grab the step-stool and return with it."

        a "Ta-dah!"

        "I set the step-stool on the ground for her, she climbs to the top step, however still has to reach a bit. She plucks the book off the shelf."

        hide pomtalk
        show pomgrin

        p "Got it!"

        hide pomgrin
        show pomeyebrowsmirk

        p "Hey, you’re pretty reliable, [avatar]."

        menu:
            "Just happy to help a friend!":
                $ pompoint += 1

                hide pomeyebrowsmirk
                show pomheadtilt

                "Pomni blinks at me."

                p "Friend?"

                "I suddenly feel my stomach sink. I didn’t say that too soon did I?"

                hide pomheadtilt
                show pomcheery

                "Pomni gives me a bright smile."

                p "You’re sweet, [avatar]."

                "We search well beyond the bell signaling lunch, until the bell that signals that classes are over for the day."

                stop music fadeout 1.0

                play sound "audio/schoolbell.mp3" volume 0.5

                "Time seemed to fly by with Pomni. Ah well, guess it's time to grab my things."

                jump walkhomedecision

            "Don’t get used to it.":
                $ pompoint -= 1

                hide pomeyebrowsmirk
                show pomconcern

                "Pomni looks at me, surprised and hurt."

                p "Did I…do something wrong?"

                a "No, I just want to get this over with as quick as possible."

                hide pomconcern
                show pomdisapproval

                p "Well nobody asked you to help me."

                "I decide against trying to clarify what I was trying to say. If Pomni wants to be offended by me, then that’s her fault."

                hide pomdisapproval
                show pomdisappointed

                "Pomni goes back to searching the books."

                "I go back to searching my section as well."

                stop music fadeout 1.0

                "We pass the time without any new requests to help her find a book."

                jump walkhomedecision

        label jaxlunchD1:

            if jaxprank:

                scene stairwell bg with flash
                show afternoon at top_left

                show jaxsly

                j "That Pomni huh? She can be {i}so{/i} needy."

                "Jax smirks, rolling his eyes."

                hide jaxsly 
                show jaxwink

                j "Not like you, huh, new kid?"

                "I’m not sure how to proceed for a moment, but I have a feeling I know what Jax wants me to say."

                a "Y-yeah, I’m down for anything!"

                "I give Jax finger guns, which he scoffs at before grinning at me."

                hide jaxwink
                show jaxcringe

                j " You’re so cringe."

                hide jaxcringe
                show jaxeyeshut

                j "But since you’re so eager to get on my good side, I came up with something fun for us to do!"

                
                hide jaxeyeshut
                show jaxsmile

                j "Let’s go on a little field trip outside."

                a "Are we allowed to do that?"

                hide jaxsmile
                show jaxeyeroll

                "Jax rolls his eyes."

                j "Jeez, you sound like a broken toy. Is that the only thing you say?"

                "I shake my head, I don’t want to disappoint Jax."

                hide jaxeyeroll
                show jaxwink

                j "It doesn’t matter what we’re allowed to do, it matters if we get caught. So keep up, new kid."

                "He finds a door leading to a field, slyly pushing it open before bounding through." 
                "I have to sprint to make it through before the door locks."

            scene softball bg
            show afternoon at top_left

            "The door leads us out onto a softball field. I didn't even know this school had a softball team."

            "Jax gets on all fours, putting his head almost even with the ground as he crawls around."

            "Is he looking for something?"

            a "Jax, did you lose something out here?"

            show jaxannoyed2

            j "Shut up, I’m looking for something."

            "In the few hours I’ve known him, I’ve never seen Jax take anything so seriously."

            "I get down on my hands and knees too, checking each blade of grass for anything remarkable."

            "I’m so focused I forget my surroundings, bumping face-first into the seat of Jax’s pants."

            hide jaxannoyed2
            show jaxconfused

            "He wheels on me."

            hide jaxconfused
            show jaximpatient

            j "Don’t try to get fresh with me, new kid."

            "I blush as I crawl back a few paces."

            a "S-sorry..."

            "Jax shakes his head."

            hide jaximpatient
            show jaxeyeroll

            j "Do you even know what we’re looking for?"

            "I shake my head, I didn’t want to make him angry by asking."

            hide jaxeyeroll
            show jaxshrug

            j "Then how do you think you’re going to find what we’re looking for?"

            "I blush again as I realise he has a valid point."

            a "So what are we looking for?"

            hide jaxshrug
            show jaxmanic

            j "A centipede."

            a "A centipede?"

            hide jaxmanic
            show jaxnonchalant

            "Jax doesn’t look amused that he has to repeat himself."

            j "A centipede."

            "We spent the rest of lunch searching, but just as the bell rings, I find a centipede crawling near a rock pile."

            a "Jax! I found one!"

            hide jaxnonchalant
            show jaxwut

            "I hoist the insect up by its rear end, it flails around as it tries to escape my grasp, its dark legs wriggling in discomfort."

            hide jaxwut
            show jaxmanic

            j "Jackpot!"

            hide jaxmanic
            show jaxsidesmirk

            j "Nice job, [avatar]."

            a "You used my name!"

            hide jaxsidesmirk
            show jaxnonchalant

            j "No, I didn't new kid."

            "I squint at him."

            hide jaxnonchalant
            show jaxshrug

            j "You’re imagining things."

            hide jaxshrug
            show jaxsidesmirk2

            "He puts on an unreadable smirk. Guess I’m not getting him to admit to anything."

            j "But this is one fine specimen."

            a "Okay, what are we doing with this? Are you an insect collector?"

            hide jaxsidesmirk2
            show jaxdisgust

            j "Ew, no."

            "He shakes his head before he drops the centipede into my backpack."

            a "Hey!"

            hide jaxdisgust
            show jaxbored2

            j "Calm down."

            hide jaxbored2
            show jaxmischief2

            j "We’re going to put this in Ragatha’s locker and then hide out and watch her open it."

            a "Why?"

            hide jaxmischief2
            show jaxmischief

            j "Cause Ragatha hates centipedes!"

            "I pause for a moment, not fully understanding why we would do that."

            a "So why are we putting one in her locker?"

            hide jaxmischief
            show jaxshrug

            j "Because it’s funny, new kid, try to keep up."

            "I don’t know if I agree, but this is the happiest I’ve seen Jax since we started hanging out."

            hide jaxshrug
            show jaxsly

            j "Come on, I have a key to let us back inside."

            "He pulls a ring of keys out of his back pocket."
            "How did he get those? It looks like a set of master keys to every door in the school."

            a "Cool..."

            scene stairwell bg
            show afternoon at top_left

            "Jax lets us back in. We sneak our way up the main stairwell, and are almost at Ragatha’s locker, when our class rep herself shows up, strolling down the hallway."

            show ragcurious at myright
            with moveinright

            r "[avatar], what are you doing in the hallway?"

            "She tilts her head, offering me a weary smile."

            hide ragcurious
            show ragunsure at myright

            r "I’ve been looking for you since you didn’t show up to afternoon classes."

            "She notices Jax and her expression sours."

            show jaxsidesmirk at myleft 
            with moveinleft

            hide ragunsure
            show ragindignant at myright

            r "Jax, you better be leaving [avatar] alone."

            hide jaxsidesmirk
            show jaxmischief at myleft

            j "Come on Ragatha,"

            "He offers a cartoonishly wide grin."

            hide jaxmischief
            show jaxwink at myleft

            j "The new kid actually looked for me. We even got lunch together!"

            hide ragindignant
            show ragshock at myright

            "Ragatha looks utterly confused."

            r "[avatar], is that true?"

            "It feels like I should choose my response carefully."

            menu:
                "That’s right, we had lunch together and we’re just trying to get back to class.":
                    $ jaxpoint += 1

                    hide jaxwink
                    show jaxsidesmirk2 at myleft

                    j "See dollface?"

                    hide ragshock
                    show ragpout at myright

                    "Ragatha squints at him, but for some reason, she seems to trust me."

                    r "Fine, but I’m keeping an eye on you Jax."

                    "Ragatha leans over to me, whispering in my ear."

                    hide ragpout
                    show ragnervoussmile at myright

                    r "[avatar], if he’s messing with you now and you don’t feel comfortable talking to me about it, you can find me after class."

                    "She’s so nice I almost feel bad about what we’re going to do."

                    "Almost."

                    jump jaxlocker

                "No, Jax asked me to look for a centipede to put in your locker.":
                    $ ragpoint += 2
                    $ jaxpoint -= 1
                    
                    hide ragshock
                    show ragangryblush at myright

                    hide jaxwink
                    show jaxbored2 at myleft

                    r "Jax! You know that’s the one thing I’m scared of!"

                    "She sounds thoroughly exasperated, like this isn’t the first time."

                    "Ragatha turns to me, interposing her body between myself in Jax, casting a glance at me over her shoulder."

                    hide ragangryblush
                    show ragindignant at myright

                    r " I’m sorry he roped you into one of his plans."

                    "Jax looks unbothered by my response."
                    
                    hide jaxbored2
                    show jaxshrug at myleft

                    j "Well if you wanna be boring, I won’t stand in your way."

                    "He doesn’t seem disappointed or surprised as he walks away."

                    hide jaxshrug with moveoutleft

                    show ragindignant at center
                    with move

                    hide ragindignant
                    show raghappy

                    r "Come with me, [avatar], Kinger actually collects insects!"

                    hide raghappy
                    show ragcheerconfident

                    r "Don’t worry about whatever he told you to do, I’ve gotcha now!"

                    "She takes my hand in hers as she leads me back to class."

                    "Jax’s response was disappointing, but Ragatha’s warm smile makes it worth my moment of weakness."

                    jump walkhomedecision

                "She knows! (Throw the centipede and run.)":
                    $ jaxpoint += 1
                    $ ragpoint -= 1
                    $ SheKnows = True

                    stop music fadeout 1.5

                    hide jaxwink
                    show jaxwut at myleft

                    hide ragshock
                    show ragstiff at myright

                    "My hands fly to my backpack, seizing the terrible black insect, before hurling it directly at our class representative." 
                    "No part of this is voluntary, every movement feeling like a scene out of a horror movie."

                    play music "audio/Caine-theme.mp3" volume 0.4 fadein 0.5

                    window hide

                    show CG_cent2 with flash
                    pause

                    r "Aaaaaah!"

                    "Her one eye bugs out of her head as the centipede lands in the center of her face."

                    "Jax is laughing like a madman next to me."

                    hide CG_cent2 with flash

                    hide jaxwut
                    show jaxlmao at myleft

                    hide ragstiff
                    show ragfear at myright

                    j "Holy sh{image=censor_bar}, new kid, that was amazing!"

                    hide ragfear with moveoutright

                    "Ragatha flails wildly, running back to class with the centipede on her face."

                    r "Kingerrrrr!"

                    "She runs out of earshot as she disappears into our homeroom."

                    "Jax is still laughing, taking a seat on the floor to catch his breath."

                    hide jaxlmao
                    show jaxbiglaugh at myleft

                    j "Jeez, new kid, where did you learn that?"

                    a "I didn’t learn it anywhere, I just panicked!"

                    show jaxbiglaugh at center
                    with move
                    hide jaxbiglaugh
                    show jaxdisbelief

                    stop music fadeout 1.5

                    "Jax finally gets control over his fit of laughter after a few more moments."

                    j "Well if that’s what you do when you panic, I guess I need to keep you on edge."

                    "Jax stands up, putting a hand on my shoulder as he looks me directly in the eye, grinning from ear to ear."

                    hide jaxdisbelief
                    show jaxmischief2

                    j "She hates you for sure now."

                    "I bury my face in my hands."

                    a "Now what?"

                    hide jaxmischief2
                    show jaxshrug

                    j "Well, school's almost over. Guess we should grab our things."

                    jump walkhomedecision

            label jaxlocker:
                scene lockers bg with flash
                show afternoon at top_left

                "Jax and I sneak through the hallways before finding a locker labelled with Ragatha’s name."
                "Pictures of horses and farm animals are pasted on the outside."

                show jaxirony

                j "Come on, new kid, now or never."

                "I gulp."

                menu:
                    "Put the centipede in her locker.":
                        $ jaxpoint += 1

                        "I gingerly pick the centipede up by the sides before setting it just below a slit in her locker."

                        "The creepy crawly centipede slithers right in."

                        "All according to Keikaku."

                        hide jaxirony
                        show jaxsidesmirk

                        j "Nice job, new kid. Now let’s hide out and enjoy your handiwork."

                        hide jaxsidesmirk with moveoutbottom

                        "We hide behind a corner and wait."


                    "Ask Jax to put the centipede in her locker":

                        "I turn to Jax and let out a little whimper."

                        hide jaxirony
                        show jaxconfused

                        j "Seriously? You already picked the centipede up outside!"

                        hide jaxconfused
                        show jaxeyeroll

                        "Despite his complaints he reaches over my shoulder and unzips my backpack and plucks the centipede out, before pushing it into Ragatha’s locker."

                        hide jaxeyeroll
                        show jaxannoyed2

                        j "Next time, I expect you to follow through."

                        "He glares at me for a moment before grinning at his own handiwork, then ushering me behind a nearby corner."

                        hide jaxannoyed2 with moveoutbottom

                scene lockers bg
                show afternoon at top_left

                stop music fadeout 1.5
                
                play sound "audio/schoolbell.mp3" volume 0.5

                "The bell to dismiss class rings a few moments later, we were cutting it close!"

                show ragsmile at myright
                with moveinbottom

                "Ragatha finds her way to her locker, entering her combination."

                "And then"

                play music "audio/Caine-theme.mp3" volume 0.4 fadein 0.5

                window hide

                show CG_cent with flash
                pause

                "Ragatha’s locker springs open, the centipede lands on the front of her uniform, and she looks down, horrified."

                r "Jaaax!!!"

                hide CG_cent with flash

                hide ragsmile
                show ragfear at myright

                show jaxmischief at myleft

                j "What?"

                hide ragfear
                show ragfrustrated at myright

                r "Why would you put a centipede in my locker? You know how much I hate them!"

                hide jaxmischief
                show jaxsly at myleft

                j "Why does it have to be me?"

                r "Because only {i}you{/i} would do something like this."

                hide jaxsly
                show jaxdisbelief at myleft

                "Jax looks away slyly, before taking credit for our prank."

                j "You got me, Raggy, but you shoulda seen the look on your face!"

                hide ragfrustrated
                show ragdisgust at myright

                r "Ugh! You’re terrible."

                hide ragdisgust with moveoutright

                "She storms off."

                "I’m glad Jax took the fall for us as I step out from behind the corner."

                "That wasn’t a very nice thing to do."

                "But Jax seems pretty happy with me right now."

                "So that’s nice."

                stop music fadeout 1.5

                jump walkhomedecision
    
    label courtyardD1:
        scene courtyard bg with flash
        show afternoon at top_left

        if not lunchinvite:
            "I pick up a garden salad from the cafeteria and stride out into the courtyard."

            "Though there are a few tables out here, they’re mostly empty, and it's easy to find Gangle and Zooble."

            "They both look up at me as I approach."

            show ganidle at myright
            show zoobbasic at myleft

            a "Hey...do you mind if I sit with you guys?"

            "They look at each other and then back at me."

            hide ganidle
            show gancheery at myright

            hide zoobbasic
            show zoobexplain at myleft

            zg "No Problem."

            "Did they coordinate that?"

            "Either that, or they’ve just been friends for a long time."

        if lunchinvite:

            "I pick up a garden salad from the cafeteria and stride out into the courtyard."

            "Though there are a half dozen tables out here, they’re mostly empty, and it's easy to find Gangle and Zooble."

            show ganexplain2 at myright
            with moveinright

            "Gangle gives me a big wave with one of her ribbon-arms, her comedy mask showing an expression of cautious excitement."

            show zoobbasic at myleft 
            with moveinleft

            "Zooble lifts up her claw-hand in a friendly wave as well."

            a "Hi guys, thanks for the invite!"

            hide ganexplain2
            show gancheery at myright

            hide zoobbasic
            show zoobexplain at myleft

            zg "No Problem!"

            "Did they coordinate that?"

            "Either that, or they’ve just been friends for a long time."

        hide zoobexplain
        show zoobbasic at myleft

        hide gancheery
        show gancasual at myright

        g "So, [avatar], how are you liking our school so far?"

        a "Well it's pretty different from my old school."

        "I start, Zooble and Gangle waiting on my next words."

        a "But I think I'm starting to like it here."

        hide gancasual
        show gansmallblush at myright

        "Gangle smiles, pushing the tips of her ribbon-hands together with a gentle blush."

        g "I like it here too, I'm really excited for the culture festival."

        "We pass the time in relative silence as we eat our lunches."

        "Zooble is the first to break the silence, pointing at my meal."

        hide zoobbasic
        show zoobeyebrow at myleft

        z "Are you a vegan or something?"

        a "Oh, this?"

        "I gesture to my salad."

        a "Not really, I just grabbed something that looked good before heading out to meet you guys."

        hide gansmallblush
        show ganexplain2 at myright

        g "I think it looks good!"

        hide zoobeyebrow
        show zoobshrug at myleft

        "Zooble shrugs."

        hide zoobshrug
        show zoobeyesclosed2 at myleft

        z "I like to bring food I cook myself, I can’t stand what Caine stocks the cafeteria with."

        hide ganexplain2
        show gantimid at myright

        "Gangle has a gentle smile on her face as she pokes a bit of shrimp tempura with a chopstick." 
        "How she manages to use chopsticks when both of her hands are the tips of red ribbons is honestly very impressive."

        g " I don’t think it's all bad, there’s a lot of traditional Japanese foods in the cafeteria. I never got to eat sushi when I was in high school before!"

        "They go back and forth like this for a bit while I stab at the remnants of my salad." 
        "A hush falls over our table for a moment, then"

        hide gantimid
        show ganexplain2 at myright

        g "So, Zooble, are you going to help me get art done for the culture festival after lunch?"

        "Zooble looks at Gangle pointedly."

        hide zoobeyesclosed2
        show zoobannoyed at myleft

        z "Honestly, I'm tired of talking about the culture festival."

        hide zoobannoyed
        show zoobshrug at myleft

        z "It's just another one of Caine's stupid plans to make us all come together and make him feel good about himself."

        hide zoobshrug
        show zoobthreaten at myleft

        hide ganexplain2
        show gannervous at myright

        z "I mean come on, Gangle, he’s having Pomni look up what a culture festival is."

        hide zoobthreaten
        show zoobannoyed2 at myleft

        z "He doesn’t care about the culture festival at all, it's just something to make us all busy."

        hide zoobannoyed2
        show zoobeyesclosed3 at myleft

        hide gannervous
        show ganunsure at myright

        z "I don’t see why I should put in any more effort than Caine is, you know?"

        stop music fadeout 1.5

        hide ganunsure
        show ganvergenotears at myright

        "There’s a faint tinkle, like something delicate fracturing, and Gangle's smile falters."

        "Gangle's lip starts quivering, tears welling up at the side of her mask."

        "Z-Zooble..."

        hide zoobeyesclosed3
        show zoobconcern2 at myleft

        z "G-Gangle, I didn't mean-"

        hide ganvergenotears
        show ganbigcry at myright

        "But their apology is too late, Gangle's comedy mask has broken and now lies on the table in front of us in two pieces. Gangle is sobbing loudly."

        hide zoobconcern2
        show zoobapology at myleft

        z "I just"

        "They give me a meaningful look"

        z "Come on, [avatar], you understood what I meant, right?"

        menu:
            "I'm sorry Gangle, I promise to help you with your art for the festival.":
                $ ganpoint += 1
                $ zoopoint -=2
                $ zoobfight = True
                jump ganlunchD1

            "Gangle, Zooble is just annoyed at being pulled around by Caine all the time, they didn't mean to hurt your feelings":
                $ zoopoint += 1
                $ zoobfriend = True
                jump zoolunchD1

    label ganlunchD1:

        play music "audio/Tense.mp3" volume 0.5 fadein 1.0

        hide ganbigcry
        show gansniffle at myright

        g "Th-thanks [avatar]."

        "Gangle sniffles, sliding one of her ribbon hands over mine on the table."

        hide zoobapology
        show zoobthreaten at myleft

        "Zooble glares at me."

        z "Come on, [avatar], don’t make me out to be the bad guy here. If you’d been through enough of Caine’s bullsh{image=censor_bar}, you’d be sick of these sorts of things too."

        a "Zooble, it's clear this culture fair means a lot to Gangle. Can't you just put your anger at principal Caine aside for this?"

        hide zoobthreaten
        show zoobfrustrated at myleft

        z "I’m not angry, I’m just frustrated with Caine, and the-"

        "They sigh, standing up, and giving Gangle an apologetic look."

        hide zoobfrustrated
        show zoobregret at myleft

        z "I’m sorry Gangle, I’m gonna go, now."

        hide zoobregret with moveoutleft

        "I almost stop Zooble, and try to get them to reconcile, but Gangle is still crying, and right now she has to take priority."

        show gansniffle at center
        with move
        hide gansniffle
        show ganapprehensivetears

        g "[avatar], did you really mean what you said? About helping me with the art for the festival?"

        a "Of course I do, Gangle!"

        hide ganapprehensivetears
        show ganhopetears 

        "Gangle picks up the remnants of her comedy mask, trying to put on a brave face as she stands up from her half-eaten lunch."

        g "That's really nice of you."

        g "I didn't feel like doing all my work alone..."

        hide ganhopetears
        show gansniffle

        "Gangle sniffles."

        g "And I don't think Zooble wants to hang out with me right now."

        "She sinks deeper into her own sadness, sagging physically with the emotional weight she feels." 
        "I support her as we make our way to the art studio, draping one of her arms over my shoulder as I support her."

        stop music fadeout 1.5

        scene art room bg with flash
        show afternoon at top_left

        play music "audio/Afternoon.mp3" volume 0.5 fadein 1.0

        "Once we step inside, Gangle starts to regain her composure, wiping her face and taking a seat at a table."

        show ganfocustears

        "She gets to work immediately, picking up a pencil and drawing an anime character with a big smile in a cheerleading uniform."

        "The more engrossed she gets in her art, the more she manages to smile, her pain fading as she adds more and more details to her drawing."

        a "Gangle, you're really good at this."

        "She jumps as I finish talking to her, I think she was so engrossed in her drawing she lost track of her surroundings."

        hide ganfocustears
        show gansurprisetears at bounce, center

        g "[avatar]!"

        hide gansurprisetears
        show ganhappysad

        g "Y-You really think so?"

        "She gives me a hopeful smile"

        a "Of course I do!"

        "She starts leaning towards me as she continues to draw."

        hide ganhappysad
        show ganfocustears

        "After an hour or so, she's fully taken up my space and hers as she adds details, working at the paper from every possible angle."

        g "Almost..."

        "She begins to shade in some areas of the drawing and go back over some of her lines to thicken them as she finishes up."

        g "Done!"

        hide ganfocustears
        show ganhopetears

        "She picks her drawing up, holding it in front of me with a cautious smile."

        play sound "audio/paper.mp3" volume 0.9

        window hide

        show ganart1 with moveinbottom

        pause

        window show

        "It's an anime style girl that strongly resembles Pomni in a cheerleading uniform, holding up a pair of pom-poms." 
        "Around the drawing are the words “Pomni wants you to get pumped!”"

        hide ganhopetears
        with None
        show ganhopetears at myright
        with moveinbottom

        g "What do you think?"

        menu:
            "That's really good, Gangle!":
                $ ganpoint += 2

                play sound "audio/paper.mp3" volume 0.9
                hide ganart1 with moveoutbottom

                show ganhopetears at center
                with move
                hide ganhopetears
                show ganhappysad

                "Gangle smiles at me."

                g "Thanks [avatar], you promise you’re not just saying that?"

                a "I’m serious."

                hide ganhappysad
                show ganshytears

                "Gangle blushes, looking away from me as she continues."

                g "I'm really excited to work with you to make the culture festival a success!"

                stop music fadeout 1.0

                play sound "audio/schoolbell.mp3" volume 0.9

                "Just as I finish cheering up Gangle, the bell to dismiss class rings."

                hide ganshytears
                show gansurprisetears

                g "Oh no, I kept you here and you missed all your afternoon classes."

                a "It's okay, Gangle. I wanted to be here."

                hide gansurprisetears
                show ganshytears

                g "heheh..."

                g "Well we should probably grab our things..."

                jump walkhomedecision


            "That sure is…something":
                $ ganpoint -= 1

                stop music fadeout 1.5
                    
                play sound "audio/paper.mp3" volume 0.9
                hide ganart1 with moveoutbottom

                play music "audio/Tense.mp3" volume 0.5 fadein 1.0
 
                show ganhopetears at center
                with move
                hide ganhopetears
                show gansadtears

                "Gangle frowns again, I should've just lied and said I liked it."

                g "I know..."

                "She does?"

                hide gansadtears
                show ganunsuretears

                g "Nothing I draw is ever as good as I want it to be."

                hide ganunsuretears
                show ganverge

                "Her body begins to shake as she starts to cry, tears soaking into the drawing she was so lovingly working on a few moments ago."

                "I feel terrible about what I just did."

                "Gangle really needed my support, especially after her falling out with Zooble, and all I could do was make her feel worse."

                play sound "audio/schoolbell.mp3" volume 0.5

                "The last bell rings, signaling the end of the day."

                "I slink away with a guilty expression as Gangle is crying. I can't stand how awkward I made things."

                jump walkhomedecision

    label zoolunchD1:

        play music "audio/Afternoon.mp3" volume 0.5 fadein 1.5
              
        hide zoobapology
        show zoobcurious at myleft

        hide ganbigcry
        show gansniffle at myright

        z "Thank you, [avatar]."

        "Zooble sighs, exhausted, but clearly regretting that they upset Gangle."

        hide zoobcurious
        show zoobapology at myleft

        z "Seriously, Gangle, I promise I wasn't trying to hurt your feelings."

        "Gangle manages to choke back enough tears to respond."

        g "I know that."

        hide gansniffle
        show ganapprehensivetears at myright

        g "I just wanted us all to have fun today, and during the culture festival."

        "Zooble leans over, putting a hand on Gangle’s arm ribbon."

        hide zoobapology
        show zoobhesitant at myleft

        z "I know, and I'm sorry about being so rude about the culture fair."

        hide zoobhesitant
        show zoobneutral at myleft

        z "If you want to take this seriously, then I’ll take it seriously too."

        hide zoobneutral
        show zoobsquint2 at myleft

        z "Besides, I think [avatar] is really excited about the culture festival. Right?"

        "They shoot me a look that tells me it's time to speak up."

        a "Th-that's right!"

        "I stumble over my words, injecting as much enthusiasm into them as I can muster."

        a "I care a lot about the culture festival, and I'm really excited to work with both of you on preparations for it!"

        hide zoobsquint2
        show zoobneutral at myleft

        hide ganapprehensivetears
        show ganhopetears at myright

        "Zooble gives me an appreciative nod as Gangle regains her composure." 
        "Her comedy mask is still broken for now, but she offers us both a delicate smile."

        hide ganhopetears
        show gantimidtears at myright

        g "Thanks, you guys."

        hide gantimidtears
        show ganhappysad at myright

        g "Can we spend the rest of the day in the art studio working on posters?"

        a "Actually, I have some afternoon class-"

        "Zooble wraps their pincir-like hand around my forearm."

        hide zoobneutral
        show zoobglare at myleft

        z "You're coming with us."

        "I sure am."

        scene art room bg with flash
        show afternoon at top_left

        "I let Zooble lead me to the art studio as Gangle starts to smile again, giddy at the prospect of spending a whole afternoon doing art for the culture festival."

        "Gangle pulls open a closet in the back of the art studio, pulling out stacks of paper before handing several pieces to me and Zooble, along with some boxes of colored pencils."

        show ganbasictears at myright
        with moveinright
                
        show zoobbasic at myleft
        with moveinleft

        g "Since we're all doing art for the culture festival, let's all draw some posters, then we can vote which ones will make the cut!"

        "I glance down and start to sweat."

        "I haven't drawn anything more complex than a stick figure since the third grade."

        "I glance over to Zooble's paper." 
                
        "They’ve already started drawing a bunch of unique designs, contrasting different colors against one another to produce something that looks like it belongs in a high end art gallery."

        hide ganbasictears
        show ganfocustears at myright

        "I crane my neck to peer at Gangle's art. There's something familiar about the excited anime figure she's drawing, but I still can't put my finger on what it is."

        "Zooble sees me peering over at Gangle's work."

        hide zoobbasic
        show zoobeyebrow at myleft

        z "Why don't you start working on your own poster?"

        "Gulp."

        a "S-sure thing!"

        hide zoobeyebrow
        hide ganfocustears
        with moveoutbottom

        "I try to scribble something resembling an excited student for my poster, but the proportions are all wrong."

        "When I try to draw the school, all I can do is draw a rectangle with smaller rectangles for the windows."

        "When I add a little sun in the top left corner and try to draw the courtyard, the picture is complete."

        "This definitely looks like what a toddler would bring home to his parents, something that would end up under a magnet on the fridge for years."

        "Zooble leans over and gives a bemused chuckle."

        show zooblaugh with moveinbottom

        z "Seriously dude?"

        menu:
            "Yeah, I suck.":
                hide zooblaugh
                show zoobneutral

                z "I didn’t say that."

                hide zoobneutral
                show zoobshrug

                z "Look, you may not be the best, but we all start somewhere."

                hide zoobshrug
                show zoobexplain

                z "If you just pity yourself and call your art terrible, you'll never improve."

                "Zooble's pretty wise." 
                "I go back to my art piece and try to add more to it, watching what Zooble and Gangle do and trying to mimic their techniques."

            "It’s not like your art is any better.":
                $ zoopoint -= 1

                hide zooblaugh
                show zoobirritated

                "Zooble glares at me."

                z "Wow, just wow."

                "They shake their head. There’s a moment of quiet before Zooble turns back to me."

                hide zoobirritated
                show zoobthreaten 

                z "You better not say that about Gangle’s art. If you do, don’t bother coming back here tomorrow."

                "I shrug, I guess they can dish it out but they can’t take it."

            "Pretty sad, huh? But its my best work":
                $ zoopoint += 1

                hide zooblaugh
                show zoobneutral 

                "Zooble seems to respect me for admitting it."

                hide zoobneutral
                show zoobshrug

                z "Well, I don’t think you’re winning any art contests any time soon, but you can always ask me or Gangle for help."

                hide zoobshrug
                show zoobthink2

                "Zooble reaches over to my paper and adds a few perspective lines and a bit of shading."

                "It's like they see something in the picture that I don’t," 
                        
                "and from the few details they add, it transforms from a child’s drawing to something that actually looks like a high school student put effort into."

        scene art room bg with flash
        show afternoon at top_left 
        with None
                
        show ganhappysad at myright 
        with moveinright

        show zoobbasic at myleft
        with moveinleft

        g "Time’s up, let's see everyone’s art!"

        "we set all three of our pieces on the table in the center of the art room."

        "We all take a moment to look at one another’s art."

        "Gangle has drawn an anime style mascot waving two flags with the school crest on them, jumping up and down, saying “Please visit the school culture fair!”"

        "Zooble has drawn a series of geometric figures and tessellations in different colors, but when you look at it at the right angle, it spells out “Culture Fair.”"

        "I have drawn a few stick figures enthusiastically pointing at a box shaped school, with a few perspective and shading lines added making it half respectable."

        "It takes a moment for me to realize Gangle and Zooble are looking at me."

        "Oh crap, they expect me to pick my favorite."

        menu:
            "I like Gangle’s art the most":
                $ ganpoint += 1

                hide ganhappysad
                show ganembarrassedtears at myright

                "Gangle is an awkward blushing bundle of ribbons as she tries to brush off my compliment."

                g "Uh, I mean, it's not that good, you know"

                "She’s not good at playing it cool, but it’s really cute to see her like this"

                hide ganembarrassedtears
                show ganshytears at myright

                g " I think Zooble’s is good too and yours is..."

                hide ganshytears
                show ganohtears at myright

                "Gangle is at a loss for words as she looks at mine."

                hide ganohtears
                show ganhesitanttears at myright

                g "Unique."

                "I grimmace."

                a "That bad?"

                hide ganhesitanttears
                show ganhappysad at myright

                "Gangle giggles."

                g "Maybe we can put you in charge of something else, like putting up the posters!"

                hide zoobbasic
                show zooblaugh at myleft

                z "That sounds good to me."

                "We pass time laughing and talking about art until the bell rings to dismiss us for the day."

                stop music fadeout 1.0

                play sound "audio/schoolbell.mp3" volume 0.5

                "Guess I should grab my things."

                jump walkhomedecision
                    
            "Zooble came up with the coolest design.":
                $ zoopoint += 1

                hide zoobbasic
                show zoobblush at myleft

                "Zooble blushes a bit, rubbing their arm before looking away."

                z "Well, I think we all did a good job."

                "They pause."

                hide zoobblush
                show zoobbasic at myleft

                z "Except for [avatar]."

                "Gangle giggles as Zooble points out my lackluster drawing."

                hide ganhappysad
                show ganhesitanttears at myright

                g "I don’t know, it's kind of cute!"

                hide zoobbasic
                show zoobeyesclosed2 at myleft

                z "Cute because it looks like a five year old drew it."

                a "I swallow my pride and laugh with them, we laugh until the bell rings to dismiss afternoon classes."

                stop music fadeout 1.0

                play sound "audio/schoolbell.mp3" volume 0.5

                hide zoobeyesclosed2 
                show zoobbasic at myleft

                z "Well, I hated today a lot less than I thought I would."

                "They look at me, gratitude in their eyes."

                "Thanks for hanging out with us, [avatar]."

                "They say before heading out. I should probably go grab my things too."

                jump walkhomedecision

            "I knocked this one out of the park.":
                hide zoobbasic
                show zoobeyebrow at myleft

                hide ganhappysad
                show ganconcerntears at myright
                    
                "Gangle and Zooble look at me, then at my art."

                hide ganconcerntears
                show ganfocustears at myright

                "Gangle keeps craning her neck trying to look at it from different angles."

                hide zoobeyebrow
                show zoobthink at myleft

                "Zooble squints at it, as if there’s something they aren't seeing."

                hide ganfocustears
                show ganohtears at myright

                g "I don’t get it."

                "There’s a pause."

                hide zoobthink
                show zoobconcern at myleft

                z "I don’t think there's anything to get about it."

                "They both look at their own pieces, then back at mine."

                hide ganohtears
                show ganunsuretears at myright

                g "It’s not very good."

                hide zoobconcern
                show zoobeyesclosed3 at myleft

                z "No, it isn’t."

                stop music fadeout 1.0

                play sound "audio/schoolbell.mp3" volume 0.5

                "The bell rings as an awkward silence hangs in the air."

                hide zoobeyesclosed3
                show zoobexplain at myleft

                z "Well its been real."

                hide zoobexplain with moveoutleft

                hide ganunsuretears
                show ganhopetears

                g "Y-yeah, thanks for joining us today [avatar]."

                hide ganhopetears with moveoutleft

                "There was no real enthusiasm in either of their voices."

                "As I leave, I try not to imagine the things Zooble and Gangle might be saying about my “art” once I leave the room."

                jump walkhomedecision
                    
            
    label tourlunch:

        if not ragtour:
            "I find Ragatha in the cafeteria and approach her."

            show ragsmile with moveinbottom

            a "Hey Ragatha?"

            hide ragsmile
            show ragcurious

            r "Hey [avatar]! Is everything okay?"

            a "I heard you usually give a school tour to new students..."

            "I awkwardly trail off."

            "She immediately perks up."

            hide ragcurious
            show ragnervousexcite

            r "Oh! Yeah! Yes. I do."

            hide ragnervousexcite
            show ragexcite

            r "Did you want me to take you for a tour?"

            "I nod."
        
        if ragtour:

            "I grab a sandwich from the lunchline and look around for Ragatha." 
            "She did want to give me a tour, right?"

            show ragnervousexcite with moveinbottom

            r "Oh! [avatar]! Sorry for keeping you waiting. Didja want to start our tour today?"

            a "Sure thing!"

            hide ragnervousexcite
            show ragexcite

            r "That’s what I like to hear!"

        hide ragexcite
        show ragconfident

        r "Let’s get started then."

        scene stairwell bg with flash
        show afternoon at top_left

        "She starts by leading me to the stairs in the middle of the school."

        show ragsmile with moveinbottom

        r "This is the main stairwell. Our homeroom is upstairs, so you need to know where this is to get to class."

        "She gives me a friendly smile before realization strikes her."

        hide ragsmile
        show ragnervouslaugh

        r "But you probably already knew that, cause our class is on the third floor, and you would have had to take the stairs to get there."

        "She sighs, but regains her composure quickly, putting on a slightly less cheery smile as she takes my hand."

        hide ragnervouslaugh with moveoutleft

        scene lunchroom bg with flash
        show afternoon at top_left
        with None

        show ragunsure with moveinright

        "She walks to the left, taking us back to the lunchroom."

        r "This is the lunchroom, where you can grab a bite to-"

        hide ragunsure
        show ragstiff

        "She cuts herself off, eyeing the sandwich that I’m still eating."

        hide ragstiff
        show ragindignant

        "Wait a second."

        "She puts her palm to her face"

        hide ragindignant
        show ragsigh

        r "You just met me in the lunchroom."

        "Ragatha sighs."

        hide ragsigh
        show ragnervoussmile

        r "So uh, you’ve already been here too, huh?"

        "She giggles nervously, putting on an even weaker, faker smile."

        hide ragnervoussmile
        show ragpunch

        "She grabs my wrist with gusto, pulling me along with so much zeal that I feel like she’s going to tug it out of the socket."

        "I wince as she pulls me towards the next location."

        hide ragpunch with moveoutleft

        scene stairwell bg with flash
        show afternoon at top_left
        with None

        show ragpunch with moveinright

        r "Well I can at least show you to our homeroom..."

        "We head back outside the lunchroom, and are halfway up the stairwell, when Ragatha realizes that I was in the same class as her this morning, so I’ve already seen this too."

        hide ragpunch
        show ragfrustrated

        r "Ugh! I’m sorry [avatar]..."

        "She pulls at her red, strangely licorice-like hair."

        r " I just wasted your entire lunch period taking you around places you already saw at the school."

        "I offer an apologetic, shy smile."

        a "Well, kinda, I guess."

        hide ragfrustrated
        show ragsigh

        "She sighs again, slumping forward."

        hide ragsigh
        show ragdisappoint

        r "You must be pretty annoyed with me, huh?"

        hide ragdisappoint
        show raguncomfy

        "She says, not looking me in the eye."

        menu:
            "Yeah, I didn’t even get to rest on my lunch break.":

                hide raguncomfy
                show ragsigh

                "Ragatha is completely deflated, but it seems like she’s more disappointed with herself than with my reaction."

                r "Yeah."

                "She rubs the back of her neck, looking down at me."

                hide ragsigh
                show raguncomfysmile

                r "Hey, I’ll write you a pass so you can have a second lunch before going to your afternoon classes, you can do whatever you want, would that make things better?"

                "She offers an apologetic smile."

                "I guess as far as apologies go, this works for me."

                a "Uh, sure, thanks."

                hide raguncomfysmile
                show ragdisappoint

                r "And sorry again."

                "She says, rushing the words out as she writes a slip allowing me to take a second lunch break."

                hide ragdisappoint
                show ragunsure

                r "I’ll see you later, [avatar]?"

                "She offers me a polite smile and waves at me before heading to her own afternoon classes."

                hide ragunsure with moveoutleft

                "Well, I can probably forgive her for wasting my time, maybe I should give her another chance to make a better impression."

                jump walkhomedecision
                    
            "The whole tour was just a stupid waste of time.":
                $ ragpoint -= 1

                hide raguncomfy
                show ragdisappoint

                "Ragatha completely deflates at my response."

                r "Yeah, I know, I’m a pretty disappointing class rep, huh?"

                hide ragdisappoint
                show raguncomfysmile

                "She gives me a sad smile."

                r "Well, uh, sorry for wasting your time, I’m gonna go do class rep things."

                "All of the excitement has gone out of her tone as she walks away."

                hide raguncomfysmile with moveoutleft

                "I wish I had just been able to enjoy lunch, but I guess I’m heading to afternoon classes."

                jump walkhomedecision
                    
            "It’s okay, I know you meant well.":
                $ ragpoint += 1

                "She clearly meant well, I don’t see any reason to put her down."

                hide raguncomfy
                show ragnervousexcite

                "Ragatha perks right back up, as if all of her mistakes are undone by my forgiveness."

                r "Oh, uh, well if you’re having a good time, maybe I can continue the tour and excuse you from afternoon classes?"

                scene caine office bg with flash
                show afternoon at top_left

                "We stop by the principal’s office."

                show cainpipe at myleft

                "Caine is leaning against the door, bubbles coming out of his pipe."

                "Wait, isn’t it a violation of the code of conduct to smoke a pipe on school grounds?"

                c "Ragatha, [avatar], what do I owe the pleasure to?"

                show raghappy at myright
                with moveinright

                r "Hey Caine, I was giving [avatar] a tour of the school, but I wasn’t able to give them a full tour during lunch."

                hide raghappy
                show ragnervouslaugh at myright

                r "Can they be excused from afternoon classes so I can show them other places in the school?"

                "Caine stops a moment, then nods."

                hide cainpipe
                show cainexcited at myleft

                c "I don’t see why not, now go along my scrumptious little scholars, and take in the glorious work that is my academy!"

                "Ragatha turns to me, taking my hand in hers."

                hide ragnervouslaugh
                show ragconfident at myright

                r "Let’s not waste any time, [avatar]!"

                r "Next stop, the library."

                scene library bg with flash
                show afternoon at top_left
                with None

                show ragconfident at right 
                with moveinright

                "We visit the library, row upon row of bookshelves crowds this room."

                "Pomni is sorting through a massive pile of books."

                show pommurmur at myleft
                with moveinbottom

                hide ragconfident
                show ragnosmile at right

                p "Dry Multure, Migration habits of vultures…"

                "Guess she’s still trying to find a book on culture festivals."

                "We leave her to it."

                scene art room bg with flash
                show afternoon at top_left
                with None

                show ragconfident at right
                with moveinright

                r "We also have an art classroom."

                show ganfocus at center

                show zoobbasic at left
                with moveinbottom

                "As we walk into the art room, Zooble and Gangle are working away, designing posters for the school."

                "I peek over Gangle’s shoulder."

                "She’s drawing Pomni with..."

                "Generous proportions."

                "Gangle sees me and throws herself over her art."

                hide ganfocus
                show ganfrustrated

                g "Don’t look [avatar]!!!"

                "Zooble turns to me and glares."

                hide zoobbasic
                show zoobirritated at left

                z "She’s not done with it yet, don’t you know how impolite it is to look at art before it’s done?"

                "I was just curious."

                hide ragconfident
                show ragnervouslaugh at right

                "Ragatha takes my wrist and begins to usher me out."

                r "Sorry guys!"

                hide ragnervouslaugh with moveoutright

                scene stairwell bg with flash
                show afternoon at top_left
                with None

                show ragnervouslaugh 
                with moveinright

                "She closes the door behind her and catches her breath."

                hide ragnervouslaugh
                show raghappy 

                r "Alright, time to show you my favorite spot on campus."

                "We walk for several minutes, she leads me down the staircase all the way outside."

                scene softball bg with flash
                show afternoon at top_left
                        
                "I see a large patch of dirt in the shape of a diamond, surrounded by a chain link fence."

                "Is that a-"

                show ragcheerconfident

                r "This is the softball field!"

                a "Do you play?"

                "That was apparently the right question to ask."

                "Ragatha’s smile widens."

                hide ragcheerconfident
                show ragconfident

                r "Yep! Sometimes I can get the other guys out here. But Caine actually has a pitching machine, so sometimes I just go out here to let out stress."

                r " If you ever wanna join me, let me know!"

                "I file the information away for later."

                stop music fadeout 1.0

                play sound "audio/schoolchime.mp3" volume 0.1

                "In the distance, the bell to dismiss evening class rings."

                hide ragconfident
                show ragcheer

                r "And now I’ll walk us back to the lockers so you can pack up and head out for today!"

                "Well I guess that’s the end of our tour for today. Time to head out."

                $ ragtourcomplete = True

                jump walkhomedecision

    label classroomD1:

        stop music fadeout 1.5
        scene homeroom dark bg with fade
        show afternoon at top_left

        "I walk back to my classroom." 
        "I’m going to spend the rest of my day here, and at least I won’t have to struggle against all the other kids trying to head back after lunch."

        show kingidle

        "When I walk back in, I see Mr. Kinger, he’s sitting down, pulling out a sandwich from a picnic basket."
        "The classroom lights have been turned out, and the curtains drawn. It's as dark as night in here."

        hide kingidle
        show kingcuriousnhsr

        k "[avatar]?"

        hide kingcuriousnhsr
        show kingcheerynh

        k "Good to see you again! It seems like we run into each other quite a bit these days!"

        "Doesn’t he realize that I’m one of his students?"

        hide kingcheerynh
        show kingidle

        "We pass lunch in silence for a few moments."

        hide kingidle
        show kingapologysr

        k "Hey [avatar], wouldn’t you rather sit with one of your classmates?"

        a "Well, I mean it just makes sense for me to sit here."

        "Mr. Kinger pauses a moment."

        hide kingapologysr
        show kingsorrynh

        k "I see."

        "He takes a break from his sandwiches."

        hide kingsorrynh
        show kingidle

        k "Well, [avatar], if you want to live a solitary life, I don’t think anyone here is going to stop you."

        hide kingidle
        show kingexplain

        k "Honestly, there’s nothing wrong with being alone, especially if that’s what you want."

        hide kingexplain
        show kingexcitedsr

        k "But, if you don’t want to be alone, I think we have a really good class of students, and I feel you could have a really good school experience if you nurture your bonds with any of them."

        hide kingexcitedsr
        show kingdown

        "Mr. Kinger looks a little sad."

        k "In this world, one of the worst feelings is being alone when the only thing you want is the company of others."

        "Maybe I should ask him about someone."

        menu:
            "Ragatha seems cool.":
                $ ragpoint += 1

                hide kingdown
                show kingcheerysr

                k "Ragatha is honestly a very sweet girl."

                hide kingcheerysr
                show kingsorrynh 
                
                k "I think she struggles to find her own voice, and she sometimes puts herself out just to make others happy." 
                
                hide kingsorrynh
                show kingcuriousnhsr

                k "I think Ragatha could really use someone to help her find her own voice and just be there for her."

                hide kingcuriousnhsr
                show kingexcitednh

                k "And I know she likes to give school tours to the new students, so that's a good excuse to hang out with her."
            
            "I like Gangle.":
                $ ganpoint += 1

                hide kingdown
                show kingexcitedsr

                k "Gangle is a very nice girl, and she’s so talented when she really applies herself." 

                hide kingexcitedsr
                show kingexcited

                k "I think if she had someone to boost her confidence and confide in, she could achieve almost anything."

            "I want to understand Zooble better.":
                $ zoopoint += 1

                hide kingdown
                show kingneutral

                k "Zooble may look like they don’t care about anything, but I think that people with the experiences Zooble has had in life do that to protect themselves."
                
                hide kingneutral
                show kingexplain

                k "I don’t think there’s anything wrong with having thick skin, but Zooble could probably use a friend or partner to open up to once in a while."

            "Tell me about Pomni.":
                $ pompoint += 1

                hide kingdown
                show kingexcited

                k "Pomni is the newest member of our class, aside from you of course, but I’m always surprised with how resilient she is."

                hide kingexcited
                show kingapologysr

                k "The problem is that it always seems that when she gets close to somebody, that somebody ends up moving away or pushing Pomni away."
                
                hide kingapologysr
                show kingcheerynh
                
                k "I think if someone offered her a consistent and positive friendship, it would mean a lot to her."

            "I want to bond with Jax more":
                $ jaxpoint += 1

                hide kingdown
                show kingsquint

                k "Jax is a tough nut to crack. I don’t know him as well as I know the others."

                hide kingsquint
                show kingthoughtsr

                k "I do know he lost someone who was really important to him, and he took it very hard."

                hide kingthoughtsr
                show kingneutral

                k "I think a good friend would challenge Jax sometimes, because I do think there’s somebody worth saving buried underneath that tough exterior."

            "How about you, Mr. Kinger?":
                $ kingpoint += 1

                hide kingdown
                show kingcurioussr

                k "Me? Well what is there to talk about?" 

                hide kingcurioussr
                show kingexplain

                k "I went to school for seven years for Computer Science, and somehow I ended up as an English teacher for some school in the Japanese countryside."

                "Kinger chuckles"

                hide kingexplain
                show kingthoughtsr

                k "I used to have a wife as well, before"

                hide kingthoughtsr
                show kingdown

                "He trails off before looking over at picture frame on his desk."

                hide kingdown
                show kingapologysr

                k "Anyways, you can just call me Kinger, no need for that mister or missus stuff." 

                hide kingapologysr
                show kingcheerynh
                
                k "I’ll always be in this classroom if you need someone to talk to!"

                play sound "audio/schoolbell.mp3" volume 0.5

                hide kingcheerynh
                show kingsorrynh

                "Kinger looks at me for a moment, as if he wants to say more, but he walks over to the light switch, letting out a regretful sigh as he flicks the lights back on."

                play sound "audio/switch.mp3" volume 0.5
                scene homeroom bg with flash
                show afternoon at top_left

                show kingcurious

                "When he sees me again, he seems visibly surprised."

                k "[avatar], what are you doing here? Shouldn’t you be eating lunch?"

                "I sigh and shake my head, that’s more like the teacher I spent the morning with."

                hide kingcurious
                show kingneutral

                k "Well you should probably head to your afternoon classes."

                "Kinger ushers me out and I continue on to my afternoon classes. They're pretty uneventful." 
                
                "Before soon enough the last bell rings and it's time to head home."

                jump walkhomedecision
                
            "Stay silent":

                hide kingdown
                show kingidle

                k "Or we could just eat lunch, nothing wrong with that."

                "Even Mr. Kinger seems weirded out by the awkward silence. Oh well, I just came in here to get a break from all the noise."

                hide kingidle

                "I eat the rest of my lunch in silence, Mr. Kinger respecting my choice to not have conversation. After lunch concludes, I head to my afternoon classes."

                "They're pretty uneventful and before long the bell for the end of the day rings."

                play sound "audio/schoolbell.mp3" volume 0.5

                jump walkhomedecision
    

        "I’m momentarily stunned by his insights, it's like I’m talking to a different person than the teacher I met this morning."

        a "Uh…"

        hide kingneutral
        hide kingcheerynh
        hide kingexcited
        hide kingexplain
        hide kingexcitednh

        show kingexplain2

        k "Sorry, I know that’s a lot to take in."

        hide kingexplain2
        show kingcheerynh

        "He chuckles jovially."

        k "But I have a lot of respect for my class, and I really do think any of them would make an excellent friend."

        "He leans forward until he’s almost right next to me."

        hide kingcheerynh
        show kingwinksr

        k "Or more, if you know what I mean."

        "He offers me a playful wink."

        hide kingwinksr
        show kingcheerynh

        k "But again, no pressure, do what makes you feel best!"

        hide kingcheerynh
        show kingcuriousnhsr

        k "Anyway, [avatar], it's been really nice chatting but I have a lesson plan to finish."

        hide kingcuriousnhsr
        show kingexcited
        
        k  "You should get back out there."

        "He seems to smile at me before lightly ushering me out."

        play music "audio/Afternoon.mp3" volume 0.5 fadein 1.0

        jump lunchdecision

    label lonerlunch:

        stop music fadeout 1.5

        scene lunchroom bg
        show afternoon at top_left

        play music "audio/Tense.mp3" volume 0.5 fadein 1.0

        "I found a seat at an empty table and set my food down there."

        "Apparently today was pork cutlet day, but by the time I got to the front of the line, all of the pork cutlets had already been taken by other students."
        "I ended up just getting a slice of stale pizza and a chocolate milk."

        "I sigh."

        "This is just like my old school."

        "I sit alone."

        "Just like my old school."

        stop music fadeout 1.5

        play sound "audio/schoolbell.mp3" volume 0.5

        "When the lunch bell finally rings, I step out of the lunch room and head to afternoon classes."

        "They're uneventful."

        "Finally the last bell rings and it is time to go home. What a boring day."

        jump walkhomedecision

    label walkhomedecision:

    scene lockers bg with flash
    show afternoon at top_left

    $ highestScore = max(jaxpoint, ragpoint, ganpoint, pompoint, zoopoint, kingpoint)

    "I walked to my locker, entering the combination as I put my books away and get ready to head out for the day." 
    "My mind drifts to the day's events, I wonder if someone will ask me to walk back with them..."

    if highestScore >= 3:

        if ganpoint == highestScore:
            $ ganwalk = True
            "As I gather my things, a familiar masked girl walks up to me."

            show ganshy with moveinbottom

            g "Hey [avatar], wanna walk back with me? I can show you some other art I’ve done, and you can tell me what you think of it?"

            "She gives me a hopeful look."

            a "Sure thing, Gangle, I’d like that!"

            hide ganshy
            show ganbigblush

            "Gangle almost melts into shy giggles as she takes my hand and leads me out."

            jump ganwalkD1


        if zoopoint == highestScore:
            $ zoowalk = True
            "As I gather my things, a familiar figure walks up to me."

            show zoobbasic with moveinbottom

            z "Oh, hey [avatar]. You still here?"

            "I nod, clutching my books."

            hide zoobbasic
            show zoobshy

            z "Well, since you're still here, wanna walk back with me?"

            a "Yeah Zooble, that sounds nice."

            hide zoobshy
            show zoobembarrassed

            z "Cool."

            "Their voice is completely non-plussed, but I can tell they’re happy I said yes."

            jump zoowalkD1


        if ragpoint == highestScore:
            $ ragwalk = True
            "As I gather my things, a familiar doll walks up to me."

            show ragawkwardblush with moveinbottom

            r "Hey [avatar]! You getting ready to head back for the day?"

            a "Yep!"

            hide ragawkwardblush
            show ragshy2

            "Ragatha looks around a bit seemingly working up the courage to ask something."

            r "You know, if you want to, I could walk you back today, how does that sound?"

            a "Sure thing!"

            hide ragshy2
            show ragnervousexcite

            r "Oh! Awesome!"

            "She beams."

            jump ragwalkD1

        if pompoint == highestScore:
            $ pomwalk = True
            "As I gather my things, a familiar jester walks up to me."

            show pomheadtiltsmile with moveinbottom

            p "Hey [avatar]! About to head back?"

            a "That's right."

            hide pomheadtiltsmile
            show pomcautioussmile

            p "If you want somebody to walk back with, I’m free."

            "She offers me a shy smile."

            a "Sure, sounds good."

            hide pomcautioussmile
            show pomlaugh

            p " Great!"

            "She pauses to redo her response."

            hide pomlaugh
            show pomtuck

            p "I mean, uh, that’s cool, I guess."

            "She’s trying to hide it, but I think she had more fun than she expected. I did too, so I’m happy for her company on the way back."

            jump pomwalkD1

        if jaxpoint == highestScore:
            $ jaxwalk = True
            "As I gather my things, a familiar figure swaggers up to me."

            show jaxwink with moveinbottom

            j "Heeey new kid. You're still hanging around?"

            a "Yep! Just getting ready to head out."

            hide jaxwink
            show jaxsidesmirk2

            j "Whaddya say, how about I walk with you after school today?"

            "Surprised at Jax asking to walk me home, I run out of words and just nod."

            j "Cool, let’s go."

            jump jaxwalkD1

    if kingpoint >= 2:
        "I gather my things and wait a little bit, but alas. No one approaches me."

        "I wonder if Kinger would mind walking back with me?"

        play music "audio/Evening.mp3" volume 0.5 fadein 1.5

        scene homeroom bg with flash
        show afternoon at top_left

        "I decided to head back to the classroom."

        "I’ve never asked a teacher to walk with me after school, but I feel closer to Kinger than any of my classmates right now."

        "As the last of the students filter out of his room, Mr. Kinger draws the blinds and turns the light off."

        play sound "audio/switch.mp3" volume 0.5
        scene homeroom dark bg with fade
        show afternoon at top_left

        show kingneutral

        k "[avatar], what are you doing here?"

        hide kingneutral
        show kingcurioussr

        k "Didn’t you go on Ragatha’s tour of the school, or spend time in the library with Pomni?"

        "I shake my head."

        a "I only had time for lunch before I went to my afternoon classes."

        k "Kinger furrows his brow, concerned."

        hide kingcurioussr
        show kingsquint

        k "That’s no good, [avatar], I really think you’re missing out on some good experiences by spending all your time in my class."

        "Damn, he didn’t have to do me like that."

        "I clear my throat."

        a "You may be right, but I don’t want to head back alone today, and I was going to ask if you were free after school today."

        hide kingsquint
        show kingcheerysr

        "Kinger chuckles as he opens a desk."

        "He begins to assemble a pillow fort from various pillows hidden in the drawers of his desk."

        hide kingcheerysr
        show kingexcitednh

        k "Sorry [avatar], but I live here."

        "A chill runs down my spine."

        "I always heard teachers didn’t have lives outside of school, but I never suspected this."

        "Kinger looks at me before sliding the last pillow into place."

        hide kingexcitednh
        show kingcuriousnhsr

        k "Good night, [avatar]."

        hide kingcuriousnhsr with moveoutbottom

        "I decide to walk back alone, thoroughly unnerved."

        jump lonerwalk

    else:
        "I gather my things and wait a little bit, but alas. No one approaches me."

        "Guess I didn't make a substantial enough impression on anyone today."

        "Just like my old school."

        "Well, there's always tomorrow."

        "I head out of the school front doors and brave the chill of the evening on my own."

        jump lonerwalk

    label lonerwalk:

        stop music fadeout 1.5
        play music "audio/Tense.mp3" volume 0.5 fadein 1.0

        scene dark with fade

        "I sit on the curb, waiting for my parents to come pick me up."

        "I wait."

        "And wait."

        "And wait."

        scene extschooln bg with fade
        show night at top_left

        "It’s starting to get dark..."

        "and cold."

        play sound "audio/wind.mp3" volume 0.9

        "A cool breeze rushes by chilling me to the bone and filling my nose with the scent of stale cherry blossoms."

        "And…"

        "I could swear it smells like an old abandoned office?"

        "Must be my sinuses acting up or something."

        "The moon is high in the sky as I get up from my perch and begin to walk."

        "As I make my way further from the school entrance, I see a silhouette of someone in the trees."

        "Looks like someone {i} was {/i} waiting for me."

        "They’re too short to be Ragatha, Gangle, Zooble, or Jax."

        "And I don’t remember Pomni wearing a suit like that..."

        show cainsil with dissolve

        q "Ahoy there, [avatar]!"

        "As I reach the treeline, their appearance becomes more clear."
        
        show cainneutral with dissolve

        a "{i}Principal Caine?{/i}"

        hide cainsil
        hide cainneutral
        show cainshowoff

        c "Hey there Old Sport!"

        "He extends a hand."

        "I hesitantly take it."

        a "H-hey Principal Caine."

        "I can’t suppress a shiver."

        a "Pretty cold out here, huh?"

        hide cainshowoff
        show cainthink

        c "Is it? I hadn’t noticed!"

        "He shrugs, as if the weather is of no consequence."

        hide cainthink
        show caindisappoint

        c "Looks like you had a rough first day, [avatar]..."

        hide caindisappoint
        show cainshrug

        c "It's a shame too!"
        
        c "When we talked earlier in the intro, I really thought you seemed excited to mingle!"

        "I give him a confused look."

        "Talked earlier? Intro? What is he talking about?"

        hide cainshrug
        show cainthink2

        c "Hmmm."

        "He looks away from me and taps his chin."

        hide cainthink2
        show cainright

        c "Well no matter!"

        hide cainright
        show caingettem

        c "I guess we’ll need to restart from square one, eh?"

        "He whips back around to face me, his expression bright."

        "Square one?"

        a "Wha-?"

        window hide

        show D1gameover with fade

        "Principal Caine reaches out and taps me with his cane."

        "I feel my memories begin to unravel."

        "It’s a weirdly uncomfortable feeling."

        "First my memories become fuzzy, like I’m watching them on TV, but the TV has really bad reception."

        "Then my entire body starts tingling, like when you sleep on your arm weird and when you wake up" 
        
        "it feels fuzzy and you can’t move it, no matter how hard you try."

        "All shades of color fade to a dull grey."

        "Even my sense of smell fades as I feel myself pulled into Principal Caine’s cane."

        c "Maybe next time, flex those socializing muscles a bit! Eh, [avatar]?"

        "I’m barely able to hear him, it feels like I’m underwater."

        c "Here’s a hint, focus on spending time with at least one person."

        c "And maybe say things that they’d like to hear?"

        c "Just some advice, best of luck next go round!"

        "With a shake of his cane, the last of my consciousness dissolves."

        scene dark with fade

        show game over with dissolve

        pause

        jump DEMO_END




    label ganwalkD1:

        stop music fadeout 1.5
        play music "audio/Evening.mp3" volume 0.5 fadein 1.5

        scene extschoole bg with flash
        show night at top_left
        
        "As we get to walking, Gangle and I start talking about her art again. I’m as full of compliments as ever."

        show ganbasic with moveinbottom

        a "Seriously, Gangle, you should show more people your art."

        a "I bet you could even successfully publish a manga-inspired webcomic or something like that!"

        hide ganbasic
        show gansad

        g "O-oh"

        "Did I say something wrong? Her face falls instantly"

        hide gansad
        show gannervous

        g "Sorry, what you said just reminded me of something"

        hide gannervous
        show ganapprehensive

        g "Something about my past I don’t like to remember."

        hide ganapprehensive
        show gansad

        "She looks away from me."

        "I didn’t mean to hurt her feelings."

        "I decide to leave the topic alone for now."

        "Desperate to change the topic as we leave school for the day, I decide to ask her a question."

        a "So Gangle, do you drive yourself to school or take the bus?"

        hide gansad
        show ganoh

        g "Huh?"

        "She tilts her mask as she stares at me, confused."

        a "You know, how do you get from here to your house?"

        hide ganoh
        show ganconcern

        g "[avatar]..."

        "She trails off"

        hide ganconcern
        show ganapprehensive

        g "Do you not know?"

        a "Not know what?"

        "Gangle presses her ribbon-hands together, seeming to give her next words a great deal of thought."

        hide ganapprehensive
        show ganexplain2

        g "Uh, [avatar], we live on campus."

        a "Whaaaat?"

        "I must have misheard her."

        "Also, who’s we?"

        "I’m certain I was dropped off by my parents today."

        "Even if I can’t remember what car I was dropped off in."

        "Or what my parents look like."

        "Or what my house looks like."

        hide ganexplain2
        show gannervous

        g "Yeah, Caine made us some housing on campus after Kinger started cluttering our homeroom with his pillow fort." 
        
        g "Before we complained, we all just had to sleep at our desks."

        a "Oh, that’s cool for you guys, but who’s we?"

        "Gangle pauses before gesturing to the school, herself, and even me."

        hide gannervous
        show ganhesitant

        g "Zooble, Pomni, Jax, Me, Ragatha, and now I guess you do too."

        "I start to breathe in and out rapidly, sweat rolling down my face as the weight of her words strike me."

        a "No way, but I mean my parents dropped me off this morning, didn’t they? I mean I can’t remember anything about them, but I’m sure I was dropped off..."

        a "Maybe."

        a "Probably."

        "Gangle gives me a concerned look"

        hide ganhesitant
        show ganunsure

        g "[avatar],"

        g "You’re scaring me..."

        "I can hear the threat of panic and despair in her voice."

        "I take a deep breath."

        "I have to be strong for Gangle"

        a "Uh o-okay, okay."

        a "Can you lead me to my dorm?"

        hide ganunsure
        show gannervous

        "Gangle still looks a little concerned, but the threat of all-encompassing despair has left her voice, and she’s able to give me a gentle smile as she offers one of her ribbon hands for me to take."

        g "Sure thing!"

        "As we walk, I start asking her about the dorms."

        "What kind of things I can expect, like does each dorm have a bathroom, is a bed already set up for me, how much privacy do we have in our dorms."

        hide gannervous
        show ganthink

        g "Well I don’t really know about your dorm, because each of ours are customized to ourselves."

        "Customized?"

        hide ganthink
        show ganhesitant

        g "But every room at least has a bed and a desk!"

        "She’s trying to make the best of this strange situation, but I keep my more skeptical comments to myself."

        a "Well that’s nice."

        scene dorms e bg with flash
        show night at top_left

        "Gangle leads me to a nearby building. We start walking past all of the rooms."

        "Even the doors seem customized."

        "Pomni’s door is half red and half blue, like her outfit in class."

        "Ragatha’s door looks like the door to a ranch-style house, almost as out of place in the plain dorm hallway as Pomni’s room."

        "Jax’s door is criss-crossed with black-and-yellow striped tape"

        scene avatar door with flash
        show night at top_left

        "We finally come to my room, a plain oak door. Embossed on a brass nameplate, is my name."

        show ganbasic at myright
        with moveinbottom

        g "I guess this is your room."

        "She gives me a shy smile."

        hide ganbasic
        show ganoh at myright

        "As I push the door open, I can see Gangle shifting in the periphery of my vision, trying to peek inside to see what my room says about me."

        scene avatar dorm bg with flash
        show night at top_left
        
        "She’s probably just as disappointed as I am as we peer into my room."

        "The walls are plain."

        "A boring grey mattress sits on a wooden bedframe, with a folded duvet on top emblazoned with the school emblem, as well as a pair of white pillows."

        "A disused PC that looks like it's from the 80s is sitting on a desk in the far corner of the room. There’s also a stack of paper and an assortment of office-style pens and pencils."
        
        show ganapprehensive with moveinbottom

        g "Oh, it’s nice..."

        "She’s trying to inject as much false enthusiasm as she can muster, but neither Gangle nor I are particularly impressed with this room."

        a "Sorry if it's not as impressive as everyone else’s room."

        "I blurt out."

        hide ganapprehensive
        show ganhesitant

        g "No, no, it's fine! I think it's cool that it's plain like this, it gives you a lot of room to customize it yourself!"

        hide ganhesitant
        show ganidle

        "We both look at each other, every once in a while, one of us tries to start a conversation, but neither of us can keep one alive for long."

        hide ganidle
        show ganexplain2

        g "W-well I’ll leave you to your new room."

        a "Yeah..."

        "A part of me wants her to stay so I don’t have to confront my bland and depressing room alone, but I also know it would just make things more awkward."

        a "Thanks for showing me to my room, Gangle"

        hide ganexplain2
        show gancasual

        g "No problem..."

        g "I’ll see you tomorrow in class?"

        "She’s asking me if I’m going to bother showing up tomorrow."

        "The thought of trying to run or just hiding in my room is appealing, but I couldn’t abandon Gangle like that."

        a "Yeah, I promise."

        hide gancasual with moveoutbottom

        "Gangle offers me a shy smile as she heads out of my room."

        "I just stand there for a while, trying to adjust to my new home."

        "I stand there so long, I almost don’t notice as a piece of paper slips under my door."

        "I turn around to pick it up."

        "It’s a drawing by Gangle!"

        play sound "audio/paper.mp3" volume 0.9

        window hide

        show ganart2 with moveinbottom

        pause

        window show

        "She drew herself in her sailor uniform, smiling."

        "Underneath, she has written the caption “Welcome to our School!"

        "She’s so adorable."

        play sound "audio/paper.mp3" volume 0.9

        hide ganart2 with moveoutbottom

        "I find a container of thumbtacks, and push one into the wall above my bed, decorating my room with Gangle’s art."

        "It’s a small piece in a mostly blank room, but it's something, and I’m so grateful to Gangle for trying to make me feel comfortable here."

        "Maybe things won’t be so awful."

        stop music fadeout 1.5

        scene dark with fade

        "I lay down on my bed, defeated by the day. It doesn't take long for me to drift to sleep..."

        jump wackywatch


    label zoowalkD1:

        stop music fadeout 0.5
        play music "audio/Evening.mp3" volume 0.5 fadein 1.0

        scene extschoole bg with flash
        show night at top_left

        "Zooble and I make our way out the front doors of school."

        "I walk to the curb, trying to find a comfortable seat on the sidewalk as I wait for my parents to pick me up."

        show zoobconcern with moveinbottom

        z "Uh, what are you doing?"

        "They give me a weird look."

        a "Waiting for my parents to pick me up, why?"

        "Zooble seems only more confused by my answer."

        hide zoobconcern
        show zoobannoyed2

        z "[avatar], how old are you?"

        "I laugh."

        a "That’s a weird question to ask."

        "I begin to count on my fingers, only to realize I somehow forgot how old I am."

        "How did I forget how old I am?"

        a "Uh, it’s not important, how old are you?"

        hide zoobannoyed2
        show zoobeyebrow

        "Zooble raises an eye at my response, but lets it slide."

        hide zoobeyebrow
        show zoobbasic

        z "I’m 22."

        "I’m completely bamboozled by Zooble’s respoozle."

        "Bamzoobled?"

        "I shake my head."

        a "Well, I’m probably an appropriate age to be picked up by my parents."

        "Zooble sighs, pinching where the bridge of their nose would be with their claw hand."

        hide zoobbasic
        show zoobcurious

        z "[avatar], I don’t know how you didn’t notice this, but there literally is no outside world."

        z "Just the school and the dorms."

        a "Dorms?"

        hide zoobcurious
        show zoobbasic

        z "Yeah. I mean I still don’t like Caine, but at least he gave us all individualized rooms just a little off campus, and that was..."

        hide zoobbasic
        show zoobthink

        "Zooble pauses to make sure their next words aren’t too complimentary towards Caine."

        hide zoobthink
        show zoobshrug

        z "decent, of him."

        "They seem satisfied with their word choice."

        a "But my parents, I was dropped off by them this morning, it feels as real as my name, and my last school."

        hide zoobshrug
        show zoobapology

        z "[avatar],"

        "They give me a look of pity."

        z "Seriously, try to remember any concrete details about your life outside of this school."

        "I try and I try, but all I get is a splitting headache, the harder I try, the worse the pain."

        a "I got nothing."

        hide zoobapology
        show zoobexplain

        z "Yeah, something happens to our memory when we come to this school." 

        hide zoobexplain
        show zoobneutral

        z "Come on, let's get you to your room before it gets much colder out."

        "Zooble takes my wrist in their hand and leads me to the dorms."

        scene dorms e bg with flash
        show night at top_left
        with None

        show zoobthink with moveinbottom

        z "Alright, which room is yours."

        "Each door has so much personality, I can instantly tell who is probably staying in each."

        "The red and blue door is probably Pomni’s, the door criss-crossed with caution tape could belong to Jax, and the ranch door reminds me of Ragatha for some reason."

        "We also pass a dark sleek door with bright geometric shapes on it."

        a "Your room?"

        hide zoobthink
        show zoobbasic

        z "Yup."

        "They’re quick with their response but not curt, clearly Zooble is more interested in finding my room than making small talk right now."

        scene avatar door with flash
        show night at top_left
        
        "Unlike all of the other fancy doors, mine turns out to be a plain oak door. We know it's mine thanks to a brass nameplate with my name on it."

        show zoobneutral2 at myleft

        z "Well, you wanna check it out?"

        a "Yeah, let's see what Caine cooked up for me."

        "I pop open the door, looking inside expectantly."

        scene avatar dorm bg with flash
        show night at top_left

        "If I had to describe this room in one word, it would be inoffensive."

        "or boring."

        "All the walls are painted a plain shade of white. My mattress is grey, with a thick duvet embroidered with the school emblem folded on top. Two pillows also sit on my bed."

        "At the desk sits a pile of paper, a set of blue and black pens, a handful of sharpened pencils, and a computer that looks like it was plucked out of an office in the 80s."

        show zoobthink with moveinbottom
        
        z "It’s..."

        "Zooble pauses to find appropriate words."

        hide zoobthink
        show zoobconcern

        z "Roomy?"

        "I turn to them for a moment, before bursting into laughter."

        a "You can say that again."

        "I can’t hide my grin at Zooble actually trying to be nice."

        a "It’s the emptiest room I’ve ever seen in my life."

        "It’s literally so boring it’s funny."

        hide zoobconcern
        show zooblaugh

        "Zooble starts chuckling too."

        z "Yeah, I don’t know what you did to p{image=censor_bar} off Caine, but he must have decided to give you the most boring room he could think up."

        "We laugh at the sheer hilarity of my unfortunate room for a few minutes."

        hide zooblaugh
        show zoobeyebrow

        z "Well, the room sucks, but if you give me a few minutes, I’ll whip something up to make it less plain."

        a "Sounds like a plan, I guess I’ll unpack my backpack and see if I can rearrange things to give the room some more personality."

        hide zoobeyebrow
        show zoobshrug

        z "Good luck."

        "Zooble snorts as they leave my room."

        hide zoobshrug with moveoutbottom

        "I close the door. There isn’t much to work with, but I manage to arrange the pens in a neat little pyramid, and start trying to sketch something to put on the wall."

        "A few minutes later, someone slides a paper under my door."

        "I pick it up."

        play sound "audio/paper.mp3" volume 0.5

        window hide

        show zoobart1 with moveinbottom

        pause

        window show

        "Zooble has done a self-portrait in a neo-cubist style, incorporating various geometric shapes to make an interesting background to their self-portrait."

        play sound "audio/paper.mp3" volume 0.5
        
        hide zoobart1 with moveoutbottom
        
        "I search around in my desk and manage to find a thumbtack."

        "I pin Zooble’s drawing to my wall, and remind myself to thank them for the art next time we talk."

        "Spending the day with Zooble was actually really nice, despite our rocky start."

        "I hope I can spend more time with them in the future."

        stop music fadeout 1.0

        scene dark with fade

        "I lay down on my bed, defeated by the day. It doesn't take long for me to drift to sleep..."

        jump wackywatch


    label ragwalkD1:

        stop music fadeout 0.5
        play music "audio/Evening.mp3" volume 0.5 fadein 1.0

        scene extschoole bg with flash
        show night at top_left
        
        "Ragatha and I make our way to the front doors of the school."

        show ragnosmile

        r "Hey, [avatar],"

        "She looks at me, as if she just remembered something very important."

        hide ragnosmile
        show ragcurious

        r "This is your first night here, right?"

        a "Uh, sure?"

        "I mean it's technically my first day here, the sun has barely begun to set, so I don’t know why she’s saying ‘first night.’"

        hide ragcurious
        show ragsmile

        r "I’ll show you to the dorms then."

        "She gives me a polite smile."

        "I hate to let her down, but..."

        a "Actually, Ragatha, my parents are picking me up today."

        "Ragatha gives me a confused look"

        hide ragsmile
        show ragnervouslaugh

        r "Are you sure about that, [avatar]?"

        a "I think I am?"

        "I’m not sure why she’s questioning that."

        "But as she asks me the question, I try to remember what my parents said about picking me up today."

        "I begin to discover worrying gaps in my memories."

        "Did my mom or my dad drop me off?"

        "Was it someone else?"

        "What does the car that I was dropped off in look like?"

        "What do my parents look like?"

        "I begin to hyperventilate as I realize, if it weren’t for seeing my own reflection in a mirror when I was washing my face in the bathroom this morning, I wouldn’t even remember what I look like."

        "What’s happening to me?"

        "In the corner of my eyes, abstract patterns begin to fade in and out of existence"

        hide ragnervouslaugh
        show ragunsure

        r "It’s okay [avatar], everyone goes through this the first day they’re here."

        "My breath begins to steady."

        "The abstract patterns fade, things start to feel"

        "Well, normal definitely isn’t the word, but at least a little more okay."

        a "Th-they do?"

        hide ragunsure
        show raguncomfysmile

        r "Yeah, it's this weird thing. Nobody really knows how it works. Most of us can't even remember our own names."

        "Well, at least I managed to remember my name..."

        "Unless somebody else made that up for me?"

        "No, that’s ridiculous."

        hide raguncomfysmile
        show ragdisappoint

        r "Honestly, I haven’t seen anyone ever leave campus."

        a "So we, what, just go inside and sleep on the floor of our homeroom?"

        hide ragdisappoint
        show raglaugh

        "Ragatha laughs."

        hide raglaugh
        show raghappy

        r "No, Caine actually built us a set of dorms to stay in."

        "She says, offering a hand."

        r "Something to give us a break from the ol’ rigamarole of going from class to class."

        "I take her hand."

        hide raghappy
        show ragcheer

        r "I'll lead you there, don't worry."

        "Ragatha smiles gently as she leads me by my hand to a building nearby."

        scene dorms e bg with flash
        show night at top_left

        "Just by glancing at the doors, I can tell who stays where."

        "The vibrant red-and-blue door has to be Pomni’s room."

        "Another door is sleek with bright geometric shapes all over it, that has to be where Zooble stays"

        "I could pick Jax’s door out of a crowd, it's darker than the others and criss-crossed with black-and-yellow striped caution tape."

        scene ragatha door with flash
        show night at top_left

        "Ragatha stops at a ranch-style door before proceeding."

        show ragcheer at myright

        r "This is my room, [avatar]."

        hide ragcheer
        show ragsmile at myright

        "She smiles."

        r "I’m the class rep and the Resident Assistant here, so if you have any trouble with any of your dorm-mates, or need anything for your room, I’m your gal!"

        "She gives a jovial swing of her arm, sliding her door open."

        show dark with fade

        "The inside is adorned with doilies, a thick blue duvet covers her bed, and I think I even see a tea-set on her white dresser."

        hide dark with fade

        hide ragsmile
        show ragconfident at myright

        r "My door’s always open!"

        "As we stand there, Jax walks by. He gives Ragatha a wicked grin."

        show jaxsidesmirk at left 
        with moveinleft

        hide ragconfident
        show ragindignant at myright

        r "Or it would be, if I could trust Jax not to put a centipede in my room."

        "Jax gives her an offended look."

        show jaxsidesmirk at center
        with move

        hide jaxsidesmirk
        show jaxshrug 

        hide ragindignant
        show ragpout at myright

        j "Come on Ragatha, pranking the RA? I can’t believe you think so little of me."

        show jaxshrug at right
        with move

        hide jaxshrug
        show jaxeyeshut at right

        "He says, barely hiding a sadistic grin."

        hide jaxeyeshut with moveoutright

        r "Ignore him."

        "She pauses a moment."

        hide ragpout
        show ragnervoussmile at myright

        r "And if you don’t want to wake up to a centipede in your room, don’t let Jax in."

        "Jax lets out a dark chuckle as he overhears her, unlocking his door before stepping inside."

        "She waits a few moments to make sure he’s out of earshot before lowering her voice."

        hide ragnervoussmile
        show ragnervouslaugh at myright

        r "But seriously, as long as you’re not Jax, you’re welcome to come visit me, if you need to relax, or talk to somebody, or just want to say hi."

        hide ragnervouslaugh
        show ragcheerconfident at myright

        r "Now let’s go find your room, new stuff!"

        "We walk side by side until we find a new door that doesn’t apparently belong to anyone else here."

        scene avatar door with flash
        show night at top_left

        "This door is"

        "Substantially less impressive than the doors to all the other rooms."

        "A plain oak door with my name on a brass nameplate."

        "I couldn’t come up with a more boring door if I tried to imagine one."

        "Ragatha turns towards me, noticing my disappointment."

        show ragnervousexcite at myright

        r "Hey, looks can be deceiving, maybe it's really nice inside!"

        "I twist the handle and pull the door open."

        scene avatar dorm bg with flash
        show night at top_left

        "The room looks..."

        "Empty."

        "Really empty."

        "The walls are plain and unadorned."

        "A grey mattress sits on a cheap-looking wooden bedframe."

        "A duvet decorated with the school’s logo has been set atop the mattress, as well as a pair of plain white pillows."

        "In the back corner, an aging wooden desk has been set up, with a few sheets of paper, a set of number 2 pencils, and some ball-point pens in blue and black."

        "Not even any pens in my favorite colors."

        show ragnervoussmile with moveinbottom

        r "Well..."

        hide ragnervoussmile
        show ragnervousexcite

        r "There’s a lot of room to customize!"

        "She walks around in the vast emptiness of my room, the plain walls making it seem even bigger and emptier than it is."

        a "Haha, yeah."

        "I rub a hand across the back of my neck."

        a "Can we go back and hang out in your room for a bit?"

        "I really don’t want to be alone here."

        hide ragnervousexcite
        show ragsurprise

        r "O-oh!"

        hide ragsurprise
        show ragshy

        r "I’m really sorry [avatar], but Caine doesn’t want us in each other’s rooms after the sun is down."

        "She offers an apologetic smile"

        hide ragshy
        show ragunsure

        r "I know, it's a silly rule, but he says that since this is supposed to be a “family friendly” environment, he doesn’t want us in each other’s rooms at night."

        "She backs out of my room, crossing her arms across her chest with a nervous giggle."

        hide ragunsure
        show raguncomfysmile

        r "I technically shouldn’t even be in your room right now."

        "The rest of our conversation continues with her standing in the hallway and me in my dorm."

        a "So that’s it for today?"

        hide raguncomfysmile
        show ragthink

        r "Yeah, I mean, you know where school is, right? And you remember all the places I showed you?"

        "I nod."

        "It’s a lot to take in, but I think I’m good."

        a "Uh, yeah, I think I got it from here, I guess."

        hide ragthink
        show ragunsure

        "Ragatha nods with a weak smile"

        r "Uhm, good, that’s good!"

        hide ragunsure
        show raguncomfy

        "We stand there."

        "The conversation has definitely dried up, neither of us knows what to say next."

        a "Uh, I’ll see you in class tomorrow?"

        hide raguncomfy
        show ragnervousexcite

        r "Well, I can walk with you to class tomorrow, if you’d like?"

        "I nod, that’s something at least."

        a "Y-yeah, you know, if you aren’t too busy being class rep and resident assistant?"

        "She smiles."

        hide ragnervousexcite
        show ragcheerconfident

        r "Well as class rep, I’m supposed to help new students get acclimated to our academy..."

        r "So I can definitely make time for you tomorrow."

        hide ragcheerconfident with moveoutbottom

        "I smile back at her as we exchange goodbyes and I close my door."

        "Maybe things will be alright."

        stop music fadeout 1.0

        scene dark with fade

        "I lay down on my bed, defeated by the day. It doesn't take long for me to drift to sleep..."

        jump wackywatch


    label pomwalkD1:

        stop music fadeout 0.5
        play music "audio/Evening.mp3" volume 0.5 fadein 1.0

        scene extschoole bg with flash
        show night at top_left
        with None

        show pomheadtiltsmile with moveinbottom

        p "So, [avatar], how was your first day at school?"

        a "It was pretty crazy, you know, as far as first days go. Time to get home and get some shut eye."

        hide pomheadtiltsmile
        show pomconfused

        "Pomni gives me a confused look."

        p "Home?"

        a "Yeah, you know home? With my parents? To relax?"

        hide pomconfused
        show pomerm

        p "Uh, right..."

        "She gives me a concerned look."

        a "What, is there something wrong with going home?"

        hide pomerm
        show pomsweatsmile2

        p "[avatar], I don’t know how to tell you this..."

        hide pomsweatsmile2
        show pommurmur

        p "So, uh, I,"

        "She begins to fidget with her hands."

        "Is she about to confess to me?"

        hide pommurmur
        show pomexplain

        p "Let me ask you this, where do you think you live?"

        a "What kind of question is that? I live in-"

        "I trail off, my mouth going dry, my thoughts racing."

        "Where do I live?"

        "What’s happening?"

        "Am I going insane?"

        "My mind reels as it tries to process information, and can only fill in blanks. The faces and names of my parents, what my house looks like, how I got to school."

        "I feel a trickle of blood running down my nose as I strain my mind for something, anything, that defines my life outside of this school."

        "Then I look over at the girl I’ve spent the day with."

        "Pomni is looking up at me, a kind expression on her face."

        hide pomexplain
        show pomsoft

        p "I thought so."

        hide pomsoft
        show pomcautioussmile

        p "When people come to this school,"

        p "They forget everything about the outside world."

        hide pomcautioussmile
        show pomtalk

        p "I even forgot my name before I came here."

        hide pomtalk
        show pomsoft

        "She offers me a comforting smile."

        "The warmth of her smile anchors me in the moment, pulling me back from my fractured thoughts as my thoughts return to the current moment."

        a "So, what do we do? Do we just go back inside and sleep at our desks?"

        hide pomsoft
        show pomchuckle

        "Pomni chuckles."

        hide pomchuckle
        show pomreassure

        p "Sorry, I wasn’t laughing at you, you just sounded so shocked when you asked me."

        hide pomreassure
        show pomheadtiltsmile

        p "Caine actually provided us some dorms to stay at during the night."

        a "Dorms?"

        "Pomni rubs the back of her neck as she gives me an apologetic smile."

        hide pomheadtiltsmile
        show pomsweatsmile2

        p "Yeah, I know."

        hide pomsweatsmile2
        show pomnervoussmile

        p "But it was nice of Caine to set up a place for us to stay in."

        "I nod, still processing everything."

        "Pomni starts walking ahead towards a building nearby."

        hide pomnervoussmile
        show pomcautioussmile

        p "Come on, let's go find your room."

        scene dorms e bg with flash
        show night at top_left

        "The dorm building is completely unremarkable, but maybe that’s a good thing."

        "We stride past door after door until we come to one at the end of the second floor."

        "Each door is decorated according to the personality of the person staying inside."

        "For instance, Gangle’s door looks like a traditional japanese style door."

        "Pomni’s door is half red and half blue, mimicking the vibrant shades she normally wears around school and the color of her eyes."

        scene avatar door with flash
        show night at top_left

        "My door is a plain oak door, with the name [avatar] embossed on a brass nameplate."

        show pomcautioussmile at myleft
        with moveinbottom

        p "Guess this is your room."

        "She smiles nervously."

        "I nod."

        hide pomcautioussmile
        show pomtalk at myleft

        p "Are you going to be okay?"

        "I hesitate a moment before nodding again."

        "I open the door, which is unlocked."

        scene avatar dorm bg with flash
        show night at top_left

        "My room is pretty generic. A grey mattress sits on a wood bed frame, a duvet with the school’s emblem is on top of the mattress, as well as a pair of plain white pillows."

        "A desk with a set of pens and pencils has also been placed in the room, along with an old desk chair and a desktop that looks like it belongs in the 80s."

        "Pomni steps in with me."

        a "This is a lot to take in..."

        show pomsweatsmile2 with moveinbottom

        p "Yeah..."

        "She rubs the back of her neck."

        hide pomsweatsmile2
        show pomreassure

        p "Well, I’m just down on the first floor if you need me."

        p "Look for the blue and red door."

        "She offers a nervous giggle."

        a "Okay, I’m sorry if I’m spacing out."

        a "It’s just-"

        hide pomreassure
        show pomsweatsmile

        p "A lot to take in, I know."

        "She offers me a sympathetic smile."

        hide pomsweatsmile
        show pomcautioussmile

        p "But honestly, once you get used to it, it can be sort of nice."

        hide pomcautioussmile
        show pomreassure

        p "And you don’t have to worry about being late for school."

        "I can’t blame her for trying to find the optimism in a situation like this."

        "Especially when it feels like we don’t have any way to resist the will of Principal Caine."

        hide pomreassure with moveoutbottom

        "As Pomni quietly leaves me to my thoughts, my mind begins to wander again."

        "Who is Caine?"

        "What is Caine?"

        "And why can’t anyone remember their lives before they came to this school."

        "I collapse on my bed, the world spins as I stare up at the fluorescent light that illuminates my room."

        "I hope to get the answers to my questions some time soon."

        "My thoughts also drift to Pomni."

        "The time we spent together today."

        "Her walking me to the dorms and explaining everything to me."

        "I’m lucky to have someone like Pomni around."

        "That is the one thing I’m sure of."

        stop music fadeout 1.0

        scene dark with fade

        "It doesn't take long for me to drift to sleep..."

        jump wackywatch

    label jaxwalkD1:

        stop music fadeout 0.5
        play music "audio/Evening.mp3" volume 0.5 fadein 1.0

        scene extschoole bg with flash
        show night at top_left

        "The front doors open for us, and I stand outside, waiting at the curb. My parents dropped me off this morning, and I’m sure they’ll be here any moment to pick me up."

        "Jax stands next to me for a few moments."

        "He gives me a confused look."

        show jaxeyebrow with moveinbottom

        j "What are you waiting for, kid?"

        a "Uh, my parents. Are you waiting to get picked up too?"

        hide jaxeyebrow
        show jaxirony

        j "I’m 22 years old, I haven’t been picked up by my parents for like six years."

        hide jaxirony
        show jaxbored

        j "I’m going to the dorms."

        "What?"

        a "What?"

        j "The dorms."

        hide jaxbored
        show jaxeyebrow

        "He looks at me like I’m an idiot."

        hide jaxeyebrow
        show jaxeyeroll

        j "The on-campus housing Caine designed for our class, where we stay when classes end."

        a "Oh, that sounds nice, I wish I was staying on campus."

        hide jaxeyeroll
        show jaxsurprise

        "His annoyed expression changes."

        hide jaxsurprise
        show jaxeyeshut

        j "Oh you poor little lamb."

        "His voice drips with sarcasm."

        hide jaxeyeshut
        show jaxcringe

        j "Caine really didn't tell you anything, did he?"

        hide jaxcringe
        show jaxshrug

        j "Look, [avatar], I’d love to watch you stand out here until the sun goes down and you start shivering in your little school uniform."

        hide jaxshrug
        show jaxsly

        "Jax smirks."

        j "Honestly, just imagining it is pretty funny."

        "The smile drops from his face."

        hide jaxsly
        show jaxannoyed2

        j "Your parents aren’t coming for you."

        "He says to me in a deadpan, before continuing."

        hide jaxannoyed2
        show jaxeyeroll

        j "Come on, we need to get to the dorms before it gets too cold out."

        j "Caine only gave us summer uniforms."

        "A chill travels through the air, and I shiver in place."

        "Jax shivers too."

        hide jaxeyeroll
        show jaximpatient

        j "I’m losing my patience."

        "He glares at me."

        a "Jax, I’m telling you, I don’t have any housing on campus, my parents are picking me up."

        hide jaximpatient
        show jaxshrug

        "Jax just sighs."

        j "You just don't know when to give up."

        "He glowers before walking away from me."

        hide jaxshrug
        show jaxnonchalant

        j "Suit yourself, new kid."

        "He walks off to the dorms."

        hide jaxnonchalant with moveoutbottom

        stop music fadeout 2.0

        "I’ll show him."

        "My parents will be here soon."

        "An hour passes, the sun begins to sink below the horizon."

        scene extschooln bg with fade
        show night at top_left

        play sound "audio/wind.mp3" volume 0.9

        "Another hour passes, the moon is visible and the sky is darkening."

        "It’s getting really cold out here."

        "Like really, really cold."

        "I look the way Jax walked when he left me standing here."

        "A nice warm room sounds really good right now."

        a "Where are they?"

        "I stick it out another half hour before sighing, frustrated."

        "Did they forget about me?"

        "I walk towards the dorms, seeking shelter in the plain building."

        scene dorms n bg with flash
        show night at top_left

        play music "audio/Evening.mp3" volume 0.5 fadein 1.0

        "As I do, I run into Jax."

        "Why was he heading out?"

        show jaxtired with moveinbottom

        j "Finally come to your senses, new kid?"

        "He asks, sounding tired."

        a "No, I just stepped inside cause my parents forgot to pick me up, I bet they’ll be here any moment."

        "Jax's eyes narrow in annoyance and he drags a yellow-gloved hand across his face in exasperation."

        hide jaxtired
        show jaximpatient

        a "Listen, new kid, get it through your head."

        hide jaximpatient
        show jaxexasperated

        j "There is no outside world."

        a "There’s the school,"

        "He points to the large brick building across from where we are."

        j "The dorms,"

        "He points to the building we’re standing in."

        j "And that’s it!"

        hide jaxexasperated
        show jaxmurmurtired

        "He mutters something under his breath."

        a "O-okay then..."

        a "But if these are the only two places, why were you going outside?"

        hide jaxmurmurtired
        show jaxironytired

        j "I, uh, that is-"

        "His face flushes and he turns away from me."

        hide jaxironytired
        show jaxtiredblush

        j "I just wanted some fresh air."

        "It’s pretty cold outside though."

        a "Okay, well if everyone stays here, then I should have a room here."

        a "Show me my room, if I'm supposed to stay here."

        "I grin, comfortable in my undefeatable logic."

        hide jaxtiredblush
        show jaxwut

        j "Huh, yeah, you’re probably right. Let's go find your room so I can stop babysitting you."

        "What?"

        "Jax grabs my hand in his as he hauls me through the hallways, but I'm not complaining."

        "Just another way for us to hang out together!"

        "As we walk through the hallways, a thousand questions rush through my head."

        "We pass a traditional japanese style door."

        hide jaxwut
        show jaxbored2

        j "Gangle."

        "We pass a door that’s half blue and half red."

        hide jaxbored2
        show jaxshrug

        j "Pomni."

        "We pass a dark door with black-and-yellow caution tape criss-crossing it."

        hide jaxshrug
        show jaxsly

        j "Me."

        "We pass a door that looks like it belongs in a ranch-style home."

        hide jaxsly
        show jaxeyeroll

        j "Ragatha."

        "We pass a sleek door with bright geometric shapes all over it."

        hide jaxeyeroll
        show jaxnonchalant

        j "Zooble."

        "We come to the end of the hallway, finding a plain wood door with a brass nameplate, listing my name."

        scene avatar door night with flash
        show night at top_left
        with None

        show jaxbored at myleft 
        with moveinbottom

        j "And this must be you."

        "I stand there in stunned disappointment."

        hide jaxbored
        show jaxconfused at myleft

        j "Are you going in or…?"

        "He looks sort of annoyed I haven’t opened the room yet."

        "I twist the handle and open my bland door into"

        scene avatar dorm bg with flash
        show night at top_left

        "An equally bland room."

        "A grey mattress sits atop a wooden bed frame with plain white pillows. A dark green comforter with the school emblem on it has been neatly folded."
        "In the back right corner, a beaten up metal desk sits, with a computer that looks almost as old as the desk."
        "A neat stack of papers and a set of black pens and pencils have also been provided."

        show jaxbored2 with moveinbottom

        j "Wow, pretty boring."

        "I try to look around the room for anything to dispute these words, but come up empty."

        "He walks to the center of the room and looks around at the plain interior."

        hide jaxbored2
        show jaxnope

        j "Not beating the NPC allegations with this one."

        a "Huh?"

        "NPC?"

        hide jaxnope
        show jaxdisbelief

        j "You think Caine would have put a movie poster or something up."

        hide jaxdisbelief
        show jaxsidesmirk2

        j "Guess he thinks you’re boring, huh, [avatar]?"

        a "No, no, I’m sure my parents just-"

        hide jaxsidesmirk2
        show jaxeyeroll

        "Jax has stopped listening by this point and is striding out of my room."

        j "What a waste of time."

        hide jaxeyeroll with moveoutbottom

        a "W-wait Jax, aren’t you going to say good-"

        play sound "audio/doorslam.mp3" volume 0.9

        "Jax slams the door in the middle of my sentence."

        a "-night?"

        "I give up on any expectations I have for Jax being polite."

        "Even if he skipped out on saying goodbye for the day, I feel like I might be making a connection with Jax."

        "Maybe."

        stop music fadeout 1.5

        scene dark with fade

        "I lay down on my bed, defeated by the day. It doesn't take long for me to drift to sleep..."

        jump wackywatch

    label wackywatch:

        window hide

        pause 2.0

        scene avatar dorm nolights bg with fade
        show night at top_left

        "It doesn't feel like I was sleeping long when the lights in my room flash on, as if overridden by some remote console."

        scene avatar dorm bg
        show night at top_left

        play music "audio/Caine-theme.mp3" volume 0.4 fadein 1.0

        "The room to my dorm flies open as confetti sprays from the fire sprinkler."

        "Doesn’t that violate some sort of building safety code?"

        c "Hello my darling toybox characters!"

        "Principal Caine announces from what sounds like the hallway."

        "Ah well, time to investigate."

        show CG_wackywatch1 with flash

        z "Caine, what the f{image=censor_bar} are you trying to pull this late at night."

        c "Hahaha Zooble,"

        "His laugh is fast, forced, and manic, as if he’s used to this treatment but none too pleased by it."

        c "You’re lucky I even let you GET sleep."

        "This he blurts out in a harsh monotone before recovering his cheery demeanor."

        c "I’m here because, even with the Culture Fair pulling in new viewers, we’re still not hitting the numbers that the academy needs us to."

        c "Which is why I’ve secured us a sponsorship!"

        "He stretches out the last word, using some sort of effect to apply an ethereal reverb to his words."

        c "Without further ado, I introduce you all to"

        play sound "audio/drumroll.mp3" volume 0.5

        "A drumroll plays from somewhere in the background. Ragatha looks a little more awake, but the rest of us are still trying to shake off sleep to understand what exactly principal Caine is talking about."

        show CG_wackywatch2 with flash

        c "The Wacky Watch!"

        c "You see, the vendors for Wacky Watch have been having trouble finding a good audience for their product."

        c "But now, we have the perfect setting! Teen drama!"

        g "B-but we’re adults, I’m actually-" 

        c "Now now Gangle, I know this is a lot to take in, which is why I’ve already taken the liberty of affixing a wacky watch to each of your wrists!"

        "Each of us glance down. To my shock, the watch is already on my wrist! How did it get there?"

        p "What in the-"

        hide CG_wackywatch2 with fade

        c "And don’t try removing them either!"

        c "They’ve been affixed to your wrists with a very special adhesive."

        c "And if you do try to remove them, lets just say they’ll be taking a little piece of you with them."

        "I can hear Gangle beginning to whine as panic sets in." 
        "Pomni tugs at her wacky watch, but no matter how hard she tugs, the wrist watch stays affixed, her gloves stretching like a rubber band as she pulls at the watch." 
        "Ragatha just looks down with a resigned sigh."

        z "Caine, I can’t remove the arm with the wacky watch, what the f{image=censor_bar}!"

        "Principal Caine ignores our complaints as he continues his monologue."

        c "You see my turtle doves, in order to secure the funding we need to make it to day 5 and the culture fair, I need you wearing the wacky watches at ALL TIMES."

        c "Luckily I secured a deal where I won’t need all of you to do ad reads, but it is of paramount importance that none of you insult or try to disable your wacky watches."

        c "Good luck with school life, can’t wait to see what you do with the culture fair, byeeeeee..."

        stop music fadeout 1.0

        "He stretches out the last syllable as his body folds in on itself an infinite number of times, disappearing from sight."

        scene dorms n bg with fade
        show night at top_left
        with None

        show ragunsure at right
        with moveinbottom

        r "Well, I know it isn’t ideal, but at least we can all talk to each other now! Should make communicating about the culture fair easier."

        "With the sound of breaking glass, Gangle’s comedy mask shatters and falls from her face. Tears well up in her eyes."

        show gansadtears
        with moveinbottom

        g "I don’t want a wacky watch."

        "Seeing the situation unfolding before her, Pomni pipes up."

        show pomexplain at left
        with moveinbottom

        p "Well, I think it could be useful, and look Gangle, there’s even a picture chat function where you can send people things you draw."

        show pomexplain at myleft
        with move

        hide pomexplain
        show pomsweatsmile2 at myleft

        "Pomni goes over to Gangle, lifting her wrist and pointing out the picture chat feature."

        hide gansadtears
        show ganapprehensivetears

        g "T-that is kind of nice..."

        "Gangle sniffles."

        hide ragunsure 
        show ragcheerconfident at right

        r "Yeah, that’s the right spirit, Pomni, now let's all get some sleep before we start classes again tomorrow."

        scene dorms n bg 
        show night at top_left

        play sound "audio/doorslam.mp3" volume 0.5

        "Everyone’s door closes."

        #squiggly lines from jax's door maybe

        "I hear a muffled shout from Jax’s door."

        j "What the heck, why is there a watch stuck to my arm?"

        "I decide to hide in my room before Jax looks for someone to take out his frustration on."

        scene avatar dorm nolights bg with fade
        show night at top_left

        "I flick my dorm light off as I close my door."

        "I check my wacky watch."

        if pomwalk: 
            "I got a text from…XDDCC?"

            x_nvl "Hey [avatar], I just wanted to send this text cause I know you’re new here." 
            x_nvl "I’m sorry about Caine, he’s really weird."
            x_nvl "everything here is really weird."

            "Before she fires off the next text, she fixes her name in the texting app."
            
            p_nvl "Oops, guess Caine forgot to update my name here too"
            p_nvl "{image=emoji/shock.png}"
            p_nvl " Anyways, I wanted to thank you for sticking with me today, and for helping me out in the library."
            p_nvl "I know this place is weird, but maybe if us new kids stick together, we can still have a good time."
            p_nvl "{image=emoji/happy.png}"
            a_nvl "Yeah, honestly sometimes I feel like you’re the only one who gets me"
            a_nvl "Maybe cause we’re both the new kids, but I really appreciate you hanging out with me today"
            a_nvl "I’m still getting used to things though"
            p_nvl "{image=emoji/blush.png}"
            p_nvl "Well, I’m not going anywhere any time soon"
            p_nvl "So if we keep sticking together, maybe you can feel like a member of the class too"
            a_nvl "Yeah, I’d like that too"
            p_nvl "Good night, study partner {image=emoji/happy.png}"
            a_nvl "Good night, Pomni"

            scene dark with fade

            "My room may be empty, but I don’t feel as alone anymore thanks to Pomni’s texts."

            "I’m really lucky to have a friend like Pomni."

            "Even if we didn’t make any headway on finding out what a culture fair is, I’m excited to spend tomorrow at the library with her."

            "My excitement for tomorrow keeps me warm, and helps me drift off into a peaceful slumber as my mind wanders to what tomorrow might hold."

            window hide

            pause 1.0

            show DAY1 with fade

            pause 1.0

            show DAY1 complete with dissolve

            pause

            hide DAY1 complete with fade

            pause 1.0

            jump DEMO_END

        if ganwalk:
            "I got a picture chat from Gangle, it looks like she may have used a filter for her profile picture..."

            g_nvl "{image=images/wwgangle1.png}"
            a_nvl "{image=images/wwavatar1.png}"
            g_nvl "{image=images/wwgangle2.png}"
            g_nvl " I really appreciate the time you spent with me today [avatar]." 
            g_nvl "From sitting next to me in class today to being nice about my art." 
            g_nvl "I know this place isn’t very fun, but I hope we can keep spending time together."
            a_nvl "You’re pretty cool Gangle, I really liked drawing posters with you today, even if my art skills need work"
            g_nvl "I really think everyone can do art if they try, and I can help you with some pointers if you want"
            a_nvl "That sounds perfect, Gangle"
            g_nvl "{image=images/wwgangle3.png}"
            a_nvl "Your art on the picture chat app is so cool, btw"
            g_nvl "Thanks [avatar], I hope you keep choosing to spend time with the art club"
            a_nvl "As long as you don’t make fun of my art too much"
            g_nvl "{image=emoji/laughcry.png}"
            a_nvl "Sleep well, Gangle, we got a lot of art to work on tomorrow"
            g_nvl "You too, looking forward to it"
            a_nvl "{image=emoji/happy.png}"

            scene dark with fade

            "I eventually get to sleep, but I can’t stop thinking of Gangle and how cute her smile is."

            "I want to be the best friend I can be to her."

            "But I leave those thoughts for another day as sleep overtakes me."

            window hide

            pause 1.0

            show DAY1 with fade

            pause 1.0

            show DAY1 complete with dissolve

            pause

            hide DAY1 complete with fade

            pause 1.0

            jump DEMO_END

        if zoowalk: 
            "I got a text from Zooble. Looks like they haven't updated their profile picture."

            z_nvl "I hate this thing."
            a_nvl "I know, I hate it too, but at least we can talk without being in the same room."
            z_nvl "yeah"
            z_nvl "that is nice"
            z_nvl "i guess"
            a_nvl "Still though, it's pretty late, wanna text more tomorrow?"
            z_nvl "Yeah"

            if zoobfriend:

                "I almost pull my covers up, but my wacky watch lights up with a few more texts."


                z_nvl "and thanks. For everything today." 
                z_nvl "For sitting with me and humoring me, and for helping me smooth things over with Gangle" 
                z_nvl "and for being cool when we made fun of your art."
                z_nvl "You seem like a really cool person, and I hope you keep spending time with the art club"
                z_nvl "even if you can’t draw for s{image=censor_bar}"

                "It appears that whatever censor Caine has applied to the school also works on our wacky watches."

                "Ah well."

                "I send Zooble a laughing crying emoji before pulling up the covers and getting to sleep."

            scene dark with fade

            "As I get to sleep in my bland and empty room, my thoughts drift to Zooble."

            "Our relationship was off to a rocky start, but I’m glad I stuck with them. I really hope we can spend more time together tomorrow."

            window hide

            pause 1.0

            show DAY1 with fade

            pause 1.0

            show DAY1 complete with dissolve

            pause

            hide DAY1 complete with fade

            pause 1.0

            jump DEMO_END



        if ragwalk:
            "I got a text from Ragatha, her portrait is outlined in gold to indicate that she’s an RA."

            r_nvl "Hey [avatar]"
            r_nvl "I just wanted to check in on you after the whole wacky watch thing."
            a_nvl "I guess I’m doing pretty okay, Ragatha"
            a_nvl "Just getting used to how things work here"
            r_nvl "I get that"
            r_nvl "Showing up to this school, losing your memories, and now the wacky watch"
            r_nvl "It's a lot for anyone to take in"
            a_nvl "You’re telling me"

            "There’s a few moments before Ragatha responds"

            r_nvl "Well, if you ever need to talk to anyone, I’m here"
            a_nvl "Thanks, I’ll have to take you up on that"
            r_nvl "Oh really?"
            a_nvl "Yeah, it's nice to talk with you"
            r_nvl "That's kind of you to say, [avatar]"
            r_nvl "Maybe I can make you tea sometime this week, between all the culture fair stuff"
            a_nvl "That sounds nice"
            r_nvl "Cool B)"

            "Did she just send a smiling sunglasses emoji?"

            "Well, Ragatha can be kind of old-fashioned, but it seems like she genuinely wants to help me fit in here"

            scene dark with fade

            "At least I have one friend at this school..."

            window hide

            pause 1.0

            show DAY1 with fade

            pause 1.0

            show DAY1 complete with dissolve

            pause

            hide DAY1 complete with fade

            pause 1.0

            jump DEMO_END

        if jaxwalk:
            "I got a text from Jax. He has set his avatar to a picture of himself flipping off the camera."

            j_nvl "What the heck is up with this stupid watch?" 
            j_nvl "Why can’t I take it off?"
            j_nvl "I did NOT consent to this"
            
            "I laugh, that sounds like the Jax I know."

            a_nvl "You didn’t miss much"
            a_nvl "Apparently principal Caine took a sponsorship from wacky watch to keep the school open or something"
            a_nvl "And now they’re physically stuck on us"
            j_nvl "They really are"
            j_nvl "This sucks"
            j_nvl "The fact that I could be subjected to Ragatha or Gangle’s opinion at any time has to violate some sort of convention"
            a_nvl "Yeah, but at least we can text each other whenever, right?"
            j_nvl "I guess"
            j_nvl "{image=emoji/eyeroll.png}"
            a_nvl "I hope you sleep well tonight, even though Caine stuck these wacky watches on us"

            "I wait several minutes for a response, but nothing."
            "I begin to pull the sheets over my head when the wacky watch buzzes with another text from Jax."

            j_nvl "whatever, nighty night new kid"
            j_nvl "don’t let the centipedes bite."

            scene dark with fade

            "As I get to sleep, I cherish the bond that Jax and I have built today." 
            
            "I can’t wait to find out what sort of trouble we can get into tomorrow."

            window hide

            pause 1.0

            show DAY1 with fade

            pause 1.0

            show DAY1 complete with dissolve

            pause

            hide DAY1 complete with fade

            pause 1.0

            jump DEMO_END

label DEMO_END:
    show demo page with fade
    pause
    return

   



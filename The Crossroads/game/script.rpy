# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default _game_menu_screen = "save"
define y = Character("You", image="apple")
image side apple = LayeredImageProxy("apple")

define n = Character('') #narration
define u = Character('???') #unknown 
define c = Character('Cheshire', image="cheshire")
define r = Character('Ramsey', image='ramsey')
define m = Character('The Master', image="bee")
define d = Character('The Dame', image="dame")
define b = Character('Little Boy', image="boy")
define p = Character('Bo Peep', image="bopeep")

transform double_size:
    align(0.5, 0.5)
    zoom 2

transform evening:
    matrixcolor TintMatrix("#7FA5F2")
    
image finaldoor = "images/finaldoor.webp"
image dooranimation:
    "door_open_1.webp"
    pause 0.5
    "door_open_2.webp"
    pause 0.5
    "door_open_3.webp"
    pause 0.5
    "door_open_4.webp"
    pause 0.5
    "door_open_5.webp"
    pause 0.5

default bee_bad_end = None
default bee_delivered = False
default dame_delivered = False
default boy_delivered = False
default p_inspected = False
default b_inspected = False
default keys = 0
default selectedDoor = 0

init python:
    def check_keys (narr, you, door, inspected):
        if inspected == False:
            renpy.say(n,narr)
            renpy.say(y,you)
            renpy.jump(door)
        else:
            y("No, I've already gone through this door.")
            renpy.call_screen("doorScene")

screen doorScene():
    imagemap:
        ground "images/bg hallway.webp"
    
    imagebutton auto "images/door1_%s.webp":
        focus_mask True
        
        action [SetVariable("selectedDoor", 1), ToggleScreen("doorScene"), Jump("doors")]

    imagebutton auto "images/door2_%s.webp":
        focus_mask True
        action [SetVariable("selectedDoor", 2), ToggleScreen("doorScene"), Jump("doors")]

    imagebutton auto "images/finaldoor_%s.webp":
        focus_mask True
        action [SetVariable("selectedDoor", 0), ToggleScreen("doorScene"), Jump("doors")]

# The game starts here.

label start:
    scene bg black with fade
    play music "spooky-bells-ambiance.wav" volume 0.7
    "Tomorrow is the day. Countless hours at the studio, blood, sweat, and tears have led up to this."
    "Ever since you were a child, you’ve loved to dance. After starting middle school, you finally got your parents to sign you up for dance classes."
    "You were never that great at it, but tomorrow will be your chance to prove yourself at your first dance competition."
    "You’re sure you’re ready, but more practice wouldn’t hurt, would it?"

    show bg tenniscourt

    "After wandering the woods behind your house, you come across an abandoned tennis court. Its net is riddled with large holes, and the lines around the court have significantly faded."
    "It may be a little rough, but it’s still a large and flat area — a perfect stage."
    "Near the edge of the court is an old well. Its pulley is nowhere to be seen, most likely rotted away with age."
    "Looking down into the well, all you see is pitch black. You drop a few pebbles down it, mimicking one of your favourite stories, but never hear a splash."

    menu:
        ". . ."
        "Find somewhere else":
            jump boring_end
        "Stay and practice":
            jump stay_and_practice

label boring_end:
    "Thinking back to your favourite story, you warily back away from the well."
    y bmad mshout"No way, I've played these games before!!"
    "This is not the time for adventure. There is too much at stake tomorrow, and you can’t risk any accidents."
    "You turn back to look for a better place to practice."
    "In the distance, a pair of yellow eyes narrow to slits as they stare after you, its sharp smile turning into a frown."
    play sound "eerie-resonant-tone.mp3"
    call screen boring_end
    return

label stay_and_practice:
    y braised eside mmumble "Interesting..."
    "You’ll investigate the well on your break. But first, dance. You move back to the court and begin your routine. As you dance, you begin to feel dizzy and lose your balance."
    "Not realizing how close you are to the well, you fall right in!"
    show bg black with fade
    play sound "eerie-wind.mp3" loop volume 0.7
    "Darkness surrounds you as you tumble through the air, spinning round and round. The fall seems to go on forever."
    y "{cps=30}How deep does this hole go...{/cps}"
    "You try to keep track of how much time has passed, but keep losing count."
    y bneutral eneutral mneutral "{cps=30}One Mississippi, two Mississippi...{/cps}"
    "Though it was bright and sunny today, you look up to see a star—filled sky. Looking down, a faint light is beginning to grow."
    "It's getting"
    "{cps=20}bigger{/cps}"
    "{cps=15}bigger...{/cps}"
    "{cps=10}BIGGER...{/cps}"
    stop sound
    with fade
    with vpunch
    play sound "walk-on-dirt.mp3" volume 2.0

    "You scrunch your eyes shut in anticipation, only to bounce off something and land on soft dirt."
    y bsad eclosed mfrown "Oof..."

    show bg cave with fade

    "Feeling along what must be dirt walls, your eyes are drawn to a soft light in the otherwise dark cave."
    "Under the opening of the hole you dropped out of is a large mushroom surrounded by a fairy ring. Its gently pulsing light is entrancing..."
    "The scuttle of limbs behind you breaks you out of your trance. Whirling around, you make out the faint outline of a door further down the cave."
    "It is nondescript, unassuming. A simple wooden door, perhaps made of birch."
    "The doorknob feels smooth and cold in your hand as you twist it. The door swings open instantly."

    show bg hallway

    "As you step forward, a long and narrow hallway stretches out before you, with plain beige walls and a dark red carpet full of dirt."
    "The door slams shut behind you and vanishes."
    play sound "door-slam.wav" volume 1.0
    with hpunch
    
    u "{w}Welcome."
    "You spin around wildly, trying to locate the source of the voice, except it comes from everywhere and nowhere, echoing through the hall. You become dizzy and fall to the ground."
    "A sharp smile (or was it two?) spins before your eyes as you try to regain your bearings. The smile sits high above the doorframe at the end of the hall."
    "Slowly, a yellow pair of eyes appears, followed by a set of pointed ears, massive paws, and finally a tail. A large blue cat marked with swirling patterns grins at you as it flicks its tail in amusement."

    show cheshire eneutral noears nomouth at truecenter with dissolve 
    show cheshire body eaneutral mgrin with dissolve

    y bneutral eneutral mopen "I know you. You're the Cheshire cat, right? The one from Wonderland?"

    c eamad emad mfrown "Not {i}the{/i} Cheshire cat, but {i}a{/i} Cheshire cat. How could you mistake us? We’re not even the same colour."
    y braised eclosed "Sorry, you’re right. Your fur is a much nicer colour. What's your name?"

    c eaneutral enarrow "Cats don't have names."
    y eneutral "No?"
    c "No."
    y bsad "Okaaay, well I'm Apple. What is this place?"

    c eneutral mgrin "This is The Crossroads. A place that is neither here nor there."
    c enarrow "Many have come seeking something: to make deals, an escape, an adventure. The doors are never the same, all except for this one."

    # call screen finaldoor_closeup
    show finaldoor with dissolve
    y mmumble "Is that the exit? I really need to go home and practice. "
    extend mshout "I have a dance competition tomorrow!"
    hide finaldoor with dissolve
    c eamad mfrown "It is said that those who unlock this door can walk into a reality of their choosing."
    c eaneutral mgrin "It grants wishes, in a way."
    y braised mmumble "And where would I be able to find the keys?"
    c enarrow "Take a look around and you might just find them... If you survive long enough."
    
    show cheshire -body noears nomouth with dissolve 
    hide cheshire with dissolve

    y bmad eside mfrown "Well that was helpful."

label hall:
    scene bg hallway
    if keys == 0:
        "You go to inspect the doors."
    elif keys >= 1:
        "You find yourself back in the hallway."
        if keys == 2:
            jump true_ending
    call screen doorScene

label doors:
    if selectedDoor == 1:
        $ desc = ["The door on the left is white, dotted with pink polka-dots. White lace curtains hang from the doorframe, parted in the middle and tied with pink silk bows. Painted in the center of the door is a baby-blue shepherd’s crook.","Very cute, very demure."]
        $ check_keys(desc[0], desc[1], "little_bo_peep", globals()['p_inspected'])
    elif selectedDoor == 2:
        $desc = ["The door on the right is a flawless steel, the colour of obsidian black that gleams in the light. In the centre of it is a silver knocker in the shape of a sheep's head. As you approach the door, your reflection in the silver pull bar warps.", "Sick knocker. But why does my reflection look fluffy..."]
        $check_keys(desc[0], desc[1], "black_sheep", globals()['b_inspected'])
    else:
        y "Locked... Gotta find all the keys."
        call screen doorScene
    
label little_bo_peep:
    scene bg black with fade
    play music "spooky-bells-ambiance.wav" volume 0.7 loop
    "{cps=20}{i} Little Bo-Peep has lost her sheep {/i} 
    \n{i} and she doesn't know where to find them. {/i}{/cps}"
    "{cps=20}{i} Leave them alone, {/i}
    \n{i} and they'll come home {/i}{/cps}"
    "{cps=20}{i} wagging their tails behind them. {/cps}{/i}"
    show bg grass_field with fade
    play sound "grass-rustling.mp3" loop volume 0.7
    "A gentle breeze caresses your cheek as you open the door. Your eyes are greeted with the sight of lush green fields dotted with wild flowers."
    y "This is a great place to dance."
    "You begin to dance through the fields until you come upon a dirt path worn with hooves. From there, the path diverges."
    "On the left, a humble wooden house comes into view."
    "On the right, the faint sound of weeping can be heard amid the whispers of the breeze."

    menu:
        "Check out the house":
            $ check_house = True
            show bg cabin
            "The house is more like a log cabin, made of deep red wood with a blue painted roof. There is a small set of stairs that leads up to a porch overlooking the fields."
            "In the corner of the porch is a rocking chair covered in knitted quilts. You take a seat only to find that the chair is bolted to the porch, making it completely immobile."
            y bsad mfrown "What kind of psychopath does that...?"
            "You get up and peek through the window. Inside is an unlit fireplace, collecting dust."
            "Lying before it in the center of the room is a sheepskin rug, head and all. Above the fireplace is an assortment of stuffed sheep heads."
            "Some look peaceful, while others are frozen mid-bleat, as if crying out. One in particular seems to be staring straight at you through the window."
           
            play sound "eerie-resonant-tone.mp3" volume 0.2
            show sheephead_board at truecenter

            y eshocked "Okay, now {i}that's{/i} psychopathic."
            hide sheephead_board
            "The sheep's piercing gaze is unsettling. Tearing your eyes away, you decide to turn back."

        "Follow the sound":
            $ check_house = False
            "Following the sound, you come across a small cottage."

    show bg barn
    
    if check_house:
        "Unlike the depressing log cabin, the cottage looks bright and cheerful. Its walls are a pale pink, with minimal grime."
    else:
        "The cottage looks bright and cheerful. Its walls are a pale pink, with minimal grime."
    "Pink polka-dotted curtains with white lace trim frame the windows. Beneath the windowsills are flowerbeds with red spider lilies in full bloom."
    "Looming behind the cottage is a large red barn. The weeping noise gets louder as you approach the barn. The doors were flung wide open, the hinges of their lock smashed."
    "Crouched in front of the barn is a ball of pink and white fabric."
    u "My sheep... my sheep..."
    y bneutral eside mmumble "That must be the source of the weeping."
    "Cautiously approaching the ball, you call out."
    y bsad eneutral mopen "Are you okay?"

    show bopeep bsad esquint msad

    "The ball of fabric uncurls to reveal the face of a young girl. Her hazel eyes glisten with tears as she peers out from underneath her bonnet."
    show bopeep mshout
    u "I've lost my sheep and don't know where to find them!"
    u "They're gone!" 
    show bopeep esad
    u "Gone!"
    show bopeep bmad esquint mshout
    u "The Huntsman must have let them out."

    menu:
        "They'll be okay.":
            pass
        "The Huntsman?":
            jump bp_bad_end
    show bopeep msad
    y eclosed mneutral "Don't worry, they can't have gone too far. Let's wait a bit; I'm sure they'll come back."
    y bhappy eneutral mopen "How about I teach you my favourite dance in the meantime? Let's go over here."
    
    show bg grass_field with fade
    
    "You herd the girl under the shade of some apple trees, trying to keep her spirits up."
    y eclosed "Your pretty dress might make it harder to move, so I’ll go easy on you."
    y mgrin "What’s your name? My friends call me Apple, like the fruit!"
    
    play sound "scary-scream.wav" fadeout 0.5 volume 0.5
    with hpunch
    
    "You jump up and grab an apple from a low-hanging branch. Just then, the tree makes an ear-piercing screech." 
    y bsad eshocked mshout "!!"
    
    show bopeep bsad eclosed mneutral
    
    u "They don't like that. Would {i}you{/i} like it if someone ripped off one of your limbs?"
    y eclosed mneutral "..."
    p bneutral eneutral mneutral "I'm Bo Peep."
    "You drop the apple and roll it to the base of the tree."
    y mopen "...Sorry, I was a little hungry."
    p bsad esquint msad "Oh, my poor sheep. They must be getting hungry, too! I was supposed to take care of them—"
    p esad mshout "where have they gone!"
    y eneutral mmumble"Don't you ever take time for yourself? Who takes care of you?"
    p msad "The sheep always come first."
    y bmad mfrown "That won’t do! You’ve got to relax a bit first, then I’ll help you look for your sheep."
    y mneutral "Follow my lead."
    "You take Bo Peep's hand and twirl her a few times, her dress fanning out around her."
    p bhappy eclosed msmile "Hehe!"    
    y bhappy eclosed mwidesmile "Now that we’ve loosened up a bit, let’s get started. First, you do this…"
    "Striking a pose, you look at Bo Peep to follow. After teaching her the steps, you begin to count."
    y eneutral mopen "One, two, three, four..."
    p eneutral "How are we supposed to dance without music?"
    y bneutral eside mfrown "Hmmm..."
    y bhappy eshocked mwidesmile "!"
    y eclosed mneutral "Hmm hm..."
    "Bo Peep picks up your tune, and the two of you twirl and dance until the sun sets."
    
    show bg grass_field at evening
    with fade

    p bhappy eclosed msmile "That was the most fun I've had in a while!"
    p bneutral eneutral mneutral "Thank you."
    "Just then, round shapes appear on the horizon. As the blobs get closer, you realize it is a herd of sheep."
    p bhappy eclosed msmile "They're back!!!"
    p mneutral "I guess you guys have found something else to eat, huh? "
    play sound "eerie-resonant-tone.mp3" volume 0.2
    extend esquint "{cps=25}I almost had a yummy treat for you.{/cps}"
    extend eclosed msmile " This is my new friend Apple! Let’s get you guys back home."
    hide bopeep
    show bg barn with fade
    "Bo Peep herds her sheep back to the barn."
    show bopeep
    p "Can you please watch over them while I find a new padlock?"
    y mopen "Sure."
    hide bopeep
    "There’s something peculiar about these sheep, but you can’t put your finger on it."
    "The one closest to you seems to be chewing on something."
    y "What are you eating, bud?"
    
    show sheephead_base
   
    "The sheep spits something out, and a colourful feather floats out alongside some small white objects."
    hide sheephead_base
    play sound "sheep-baa.mp3"
    "The sheep lets out a loud bleat and yawns, revealing a row of razor-sharp teeth before walking away. Upon closer inspection, you realize it is a pile of bones."
    "One of them has been chewed into the shape of a key."
    call screen bone_key with Dissolve(.5)
    $ keys += 1
    $ p_inspected = True
    p "Apple, could you give me a hand in here?"
    "Feeling apprehensive, you hesistate before finally stepping inside."
    if keys >= 1:
        jump hall

label bp_bad_end:
    play sound "grass-rustling.mp3" loop volume 0.5
    y braised eside mfrown "The Huntsman?"

    show bopeep bmad esquint msad
    u "He lives down the road and likes to hunt my sheep for sport."
    
    show bopeep mshout
    u "His cabin is filled with his trophies!"
    u "I have to find him before he does!" 

    p bsad eneutral "Will you help me? What's your name? I'm Bo Peep."
    y bhappy eclosed mgrin "Of course! My friends call me Apple."

    p bhappy eclosed msmile "Thanks, Apple. Oh, let's check near those apple trees first!"

    show bg grass_field

    y bneutral eneutral mneutral "These apples look delicious. The sheep must love eating them."
 
    p bneutral eneutral mneutral "Yes, it's always a treat for them. But ever since the Huntsman, they've developed a taste for humans."
    
    play sound "eerie-resonant-tone.mp3" volume 0.2
    p esquint "{cps=20}He deserved it anyway.{/cps}"
    y bhappy eshocked mmumble "...What?"
    n "Bo Peep lets out a sharp whistle, and a herd of sheep rushes out of the underbrush to surround you."
 
    p bsad eclosed mneutral "Sorry!"
    play sound "sheep-herd.mp3"
    "The sheep begin bleating loudly, overwhelming your senses."
    "As they close in on you, the last thing you see are rows of razor-sharp teeth."
    
    with vpunch
    call screen bad_end_bopeep
    return

label black_sheep:
    scene bg black with fade 

    "{cps=20}{i}Baa, baa black sheep{/i} 
    \n{i}Have you any wool?{/i}{/cps}"
    "{cps=20}{i}Yes sir, yes sir. Three bags full.{/i}"
    "{cps=20}{i}One for the master{/i}{/cps}"
    "{cps=20}{i}and one for the dame.{/i}{/cps}"
    "{cps=20}{i}And one for the little boy
    \nwho lives down the lane.{/cps}{/i}"
    play music "industrial_machine_tone.mp3" fadein 1.0
    "Stepping through the door, you run into something soft."
    show bg woolmill
    show ramsey silhouette with vpunch
    show ramsey side with dissolve
    u "Goodness! Late {i}and{/i} clumsy! We’ve got a busy day ahead of us, special delivery orders and a new batch of wool just came in for processing."
    y braised eshocked mmumble "Wha—"
    "The ram shoves three bags full of wool into your arms before ushering you towards the door."
    show ramsey sideclosed
    u "Now, there’s The Master, The Dame, and The Little Boy who lives down the lane."
    show ramsey sideopen 
    u "Don’t forget to make them sign for the delivery. We’ve been getting complaints lately about customers not receiving their orders."
    y bsad eneutral "But I—"
    u "Shush!"
    stop music
    show ramsey front frontopen
    
    u "{cps=5}...{/cps}{cps=20}Something looks off.{/cps}"
    y "That's what I've been trying to tell you—"
    u "Ah! Why aren't you in uniform?"

    "In one swift motion, the ram slides a fluffy hood over your head." with vpunch

    y noeffect hat bruh "..."
    play music "industrial_machine_tone.mp3" fadein 1.0
    show ramsey frontclosed
    u "There we go! We're on a tight schedule, so hurry back."
    "And with that, the ram hands you his clipboard and shoves you through the door into the main entrance, shutting it behind you and leaving you bewildered."
    hide ramsey
    "You pound on the door to no avail."
    
    with hpunch
    
    y hat bmad eneutral mshout normal"Hey! You've got the wrong person!"
    "You give in and sigh. Luckily, the clipboard contains all the information you need."

    menu:
        y eside mfrown "Let's just get this over with... Who should I deliver to first?"
        "The Master":
            jump the_master
        "The Dame":
            jump the_dame
        "The Little Boy":
            jump little_boy

label the_master:
    scene bg garden
    play music "spooky-bells-ambiance.wav" volume 0.7
    "You walk out the door and into a garden."
    y hat braised mmumble "Huh?"
    "Swivelling around, you look back at the door you came out of and see a small shed."
    y "Uhh, okay..."
    "The garden is filled with drooping flowers. Upon closer inspection, you realize the flowers are lifelike wax sculptures partially melted by the sun."
    "Connected to the garden is a large mansion, its full height diminished by melted rooftops. The walls are streaked with dried globs of wax."
    #show bg gates
    "Circling around to the front of the mansion, you spot a plaque in the melted remains of what looks like a mailbox."
    centered "The Master"
    y eside mfrown "Master of what?"
    "There's a flicker of movement in the corner of your eye. At the entrance, a very large bee is trying to smooth out the globs of wax."
    
    show bee silhouette
    
    y eneutral mopen "...Delivery for The Master?"
    show bee wings base greet aalert with dissolve
    m  "Ah, yes! That's me, master of wax. This way, please."
    "Opening the gates, the Master flits inside, gesturing for you to follow. The mansion seems to be made entirely out of beeswax and is excellently crafted."
    
    show bg bparlour
    
    "The Master leads you to a parlour."
    m aweird "Sorry for the mess; the weather has been swinging between hot and cold these days."
    m adroop "All these repairs have been keeping me from my art. You can leave the wool by the table."
    m aalert "Sit, sit! Let me make you some tea."
    y bsad eclosed "Oh no, that's okay—"
    m "Nonsense! It's the least I can do. I'll be right back!"
    hide bee
    "And with that, The Master flits off again, leaving you alone."
    "The parlour is quite humble, with few furnishings."
    "As you are inspecting one of the bookshelves, a chilling sensation brushes against your right side, emanating from a room in the corner. The door is partially open."
    "You strain your ears for any sound of movement, but only hear the ticking of a clock."

    menu:
        "Check it out":
            # show bg workroom
            show bg black
            play music "creepy-basement.mp3"
            "You push the door open to find a small workroom, containing partially melted wax statues of three small children."
            "Their expressions are an assortment of shock and fear. The tops of their heads are slightly melted, and you notice strands of hair sticking out from each of them."
            "A chill runs down your spine, and it’s not because of the AC."
            y eshocked mmumble ""
            "The Master’s buzzing voice grows louder as they approach the parlour room, talking aloud. You hurry back to your seat."
            stop music fadeout 0.5
            "The Master returns with a tray of tea and honeycombs."
        "Stay":
            "After a few minutes, The Master returns with a tray of tea and honeycombs."
    show bg bparlour
    show bee
    play sound "eerie-resonant-tone.mp3" volume 0.2
    m wings armback aneutral tray holdtray "Sorry for the wait! Have some tea."

    menu:
        y bneutral eneutral mneutral "Oh..."
        "Drink the tea":
            $ bee_bad_end = True
        "Decline the tea":
            pass

    m aalert "While you're here, let me show you my latest project! It's actually about humans."

    # show bg workroom with fade
    show bg black with fade
    play music "creepy-basement.mp3" fadein 1.0
    y eshocked mfrown "These are... very expressive. And realistic. You really are a master of your craft."
    m aweird "Well, I'm still working on my human sculpting skills. It helps to have good models."
    show bee:
        ease 0.5 zoom 1.1 ypos 1.2
    m "...You would make an excellent subject. Are you interested in modelling?"     

    if bee_bad_end:
        y braised eclosed mneutral "Not really..."
        "You try to back up but feel dizzy. Your legs give out, and the last thing you see before darkness closes over you is The Master's serene smile."
        show bee aneutral:
            ease 0.5 zoom 1.0 ypos 1.2 
        with fade
       
        y bsad eneutral mmumble "What the... Is this wax?"
        
        with hpunch
        
        y bmad mfrown "I can't move..."
        m aalert "Ah, you're awake! So sorry, but you really are too good of a model to pass up."
        play sound "eerie-resonant-tone.mp3" volume 0.2
        m aweird "{cps=15}But don't worry, this won't hurt.{/cps} {cps=8}Soon you won't feel anything...{/cps}"
        "The Master adds one last piece of wax over your face, sealing your fate."
        
        stop music
        call screen bad_end_bee
        return
    else:
        "You back up slowly." #zoom out screen
        show bee:
            ease 0.5 zoom 1.0 ypos 1.2
        y braised eclosed mneutral "Maybe another time, I still have deliveries to make. The Ram is waiting for me. Please sign here."
        m aneutral "The Ram? Oh, you must mean Mr Ramsey."
        m adroop "That's a shame..."
        "After taking the clipboard back, you decide to show yourself out."
        $ bee_delivered = True

        if boy_delivered == False or dame_delivered == False:
            menu:
                y bneutral eside mmumble "Who should I deliver to next?"
                "The Little Boy" if boy_delivered == False:
                    jump little_boy
                "The Dame" if dame_delivered == False:
                    jump the_dame
        else:
            jump wool_mill  
    
label the_dame:
    scene bg dparlour
    $ tarts = False
    play music "spooky-bells-ambiance.wav" volume 0.7
    "You walk out the front door and into a parlour. It's decorated red and black, with a checkered floor and velvet chairs."
    "Sunlight streams in through the heavy black curtains parted in two, illuminating the room. Decorating the walls are framed paintings of a regal-looking woman, most likely the lady of the house."
    "On the coffee table is a tray of tarts."

    menu:
        y hat "Ooh..."
        "Eat the tarts":
            y eside "Maybe just a little bite..."
            $ tarts = True

            y hat noeffect bruh "{i}(This tastes like dirt...){/i}"
        "Don't eat the tarts":
            pass
    
    play sound "radio-static.wav" fadein 0.8
    "A voice crackles to life and echoes throughout the room."
    u "Announcing the arrival of The Dame!"

    show dame with moveinright #neutral #slide in from right
    d "..."
    d bshocked eshocked"!"
    d mopen "Who are you? What are you doing in my house!"
    d bmad "{b}GUARDS!{/b}"

    menu:
        "It was an accident!":

            y hat normal bhappy eshocked mshout "This is a misunderstanding. I don't even know how I got here!"
            if tarts:
                d "Liar! You ate my tarts. You must be a thief in disguise!"
            else:
                play sound "eerie-resonant-tone.mp3" volume 0.2
                d braised enarrow msmirk flat "What, are you telling me you just teleported in here?"

            menu:
                "Tell the truth":
                    if tarts:
                        y hat eneutral mmumble "Wait, let me explain..."
                    else:
                        y hat braised eneutral mopen "Kinda? It's been a weird day."
                        d bmad eneutral mfrown curl "Absolutely ridiculous."
                        y bsad mshout "It's true! Let me explain..."

                    with fade

                    d bneutral enarrow mneutral "Hmm... What an interesting concept. Let's test it."
                    "With a snap of her fingers, two armoured guards appear and grab you by the arms. They shove you through the parlour doors, and you turn around to see nothing has changed."

                    y noeffect bruh ". . ."
                    d msmirk "I knew it. Guards, take her to the guillotine."

                    y normal bsad eshocked mshout "WHAT? Wait—"
                    "You are once again seized. Despite your struggles, you are dragged away to your doom..."
                    
                    call screen bad_end_dame(tarts)
                    return
                "Lie":
                    y hat braised eside mopen "Well, no. The front door was unlocked and I somehow ended up here while looking for you."
                    "You shake the bag of wool in your hand and pass her your clipboard."
                    y hat msad eclosed "If you could just sign beside your name, I'll get out of your hair at once."
                    d mfrown "...Fine. Begone." #check expression
                    y bsad eside mneutral "{i}(Don't have to tell me twice!){/i}"
                    "She hands you the clipboard, and you hurry to the door."
        "I'm just making a delivery!":
            y normal bhappy eshocked mshout "{cps=40}Waitwaitwait!{/cps} I'm just here to make a delivery!"
            if tarts:
                d "Liar! You ate my tarts. You must be a thief in disguise!"
            else:
                d flat braised enarrow "Prove it then!"

            y bsad eneutral "I've got your wool right here! "
            extend  mmumble "And I'm definitely not wearing this hat for fun."
            d curl bneutral eneutral mfrown "Hmm, that {i}is{/i} Mr Ramsey’s uniform. " 
            extend mneutral "I think it’s quite cute. I apologize for the accusation. "
            if tarts == False:
                extend "Please help yourself to some tarts."
                y bhappy eclosed mneutral "Sure, thanks."

                y noeffect bruh "{i}(This tastes like dirt...){/i}"
                d braised enarrow "Is it not to your liking?" 

                y normal bsad eclosed mgrin "Oh no! No, it's great!"
            
            d flat eneutral mopen "How did you get in here?"

            menu:
                "Tell the truth":
                    y hat braised eside mmumble "It's been a weird day. I don't even know where to start..."
                    
                    with fade

                    d curl bneutral enarrow mneutral "Hmm... What an interesting concept. Let's test it."
                    "With a snap of her fingers, two armoured guards appear and grab you by the arms. They shove you through the parlour doors, and you turn around to see nothing has changed."

                    y noeffect bruh ". . ."
                    d flat msmirk "I knew it. Guards, take her to the guillotine."

                    y normal bsad eshocked mshout "WHAT? Wait—"
                    "You are once again seized. Despite your struggles, you are dragged away to your doom..."
                
                    call screen bad_end_dame(tarts)
                    return
                "Lie":
                    y hat bsad eside mopen "Well, the front door was unlocked. I somehow ended up here while looking for you."
                    d curl bmad enarrow mfrown "Looks like somebody isn't doing their job. Unacceptable. I'll have to look into it later."
                    "You shake the bag of wool in your hand and pass her your clipboard."
                    y eneutral "Riiight. Before you do that, if you could just sign beside your name, I'll get out of your hair at once."
                    d bneutral "...Alright."
                    "She hands you the clipboard, and you hurry to the door."
    $ dame_delivered = True
    if bee_delivered == False or boy_delivered == False:
        menu:
            y hat bneutral eside mmumble "Who should I deliver to next?"
            "The Master" if bee_delivered == False:
                jump the_master
            "The Little Boy" if boy_delivered == False:
                jump little_boy
    else:
        jump wool_mill      

label little_boy:
    scene bg treehouse
    play music "spooky-bells-ambiance.wav" volume 0.7
    play sound "grass-rustling.mp3" volume 0.3
    "You step out the door and onto the balcony of a treehouse. From there, you can see the wool factory a hop, skip, and twirl away down the lane."
    show boy
    "Under the shade of leaves sits a little boy at a picnic table. An assortment of finger foods is spread out before him."
    "The table is set for three other guests, each with their own teacup and saucer."
    y hat "Wool delivery!"
    "You set the bag of wool down by the table and hand the boy your clipboard. He wordlessly signs before asking:"
    play sound "eerie-resonant-tone.mp3" volume 0.2
    b eclosed mopen "Would you like to stay for some tea? I'm afraid it's a little cold, though."
    b bsad esad mfrown "We were supposed to have a tea party today, but it seems my guests are running late."
    # Flicker boy sprite
    "You look at the carefully arranged food, completely untouched, and the empty seats. You should be getting back to your task, but the boy’s hopeful expression makes you feel a twinge of pity."
    "Glancing at the fancy teapot, you see a wisp of steam curl out of the spout."

    menu:
        "Join the tea party":
            play sound "pouring-into-a-cup.wav"
            "You take a seat across from the boy and fill your plate with snacks, then pick up a teacup. He grins at you as you silently hold it out for him to fill."
            y eside mmumble "{i}(This tea is still hot...){/i}"
            y eneutral mopen "What's your name?"
            
            b "I... can't remember. I woke up one day, and I was here. All I knew was that I was waiting for someone to join me..."
            play sound "eerie-resonant-tone.mp3" volume 0.2
            b bangry eneutral mneutral "{cps=15}Someone like you.{/cps}"
            y braised "And how long have you been waiting here?"
            b esad mfrown "Weeks... months... years. I lost track a long time ago."
            stop music
            b eneutral "{cps=30}But now that you're here," 
            extend mneutral " it doesn't matter anymore.{/cps}"
            
            y mmumble "What? What about your other guests?"
            b "Anyone would do, as long as I could find someone to replace me."
            
            b eclosed "Thank you."
            "The boy stands up from the table. You try to follow, but are stuck to your seat."
            
            with hpunch
            
            y bmad eshocked mshout "What is this? Let me go!"
            b "Sorry for tricking you, and thank you for setting me free." 
            hide boy with dissolve
            "As the cold realization sets in that you are trapped here until someone else can replace you, the table turns pristine once again."
            "Waiting."
            call screen bad_end_boy
            return
        "Head back":
            pass 
        
    y eside mfrown "{i}(If the tea is cold like he says it is, there shouldn't be any steam. Something feels off...){/i}"
    y bsad eclosed mopen "As much as I'd like to, I really should be heading back now."
    
    # show boy #sad
    
    b eneutral "Just for a little bit? No one else has shown up."
    y "I'm really sorry, but I need to go."
    "You begin to turn away from the table, but whip back when you hear the boy screech behind you—"
    play sound "monster_growl.wav" loop
    b crazy ecrazy mshout bsad "PLEASE! I'VE BEEN HERE FOR {i}SO LONG!{/i} {cps=18}{size=+10}{b}I JUST NEED SOMEONE TO TAKE MY PLACE.{/b}{/size}{/cps}"  with hpunch
    #flicker sprite
    y "Yeahh... Time to get out of here."
    "You hurry to the balcony door while the boy continues to cry and screech."
    b bangry "COME BACK! {size=+10}{b}{cps=15}COME... BACK...{/cps}{/b}{/size}"
    $ boy_delivered = True
    # TODO: optimize delivery choice structure
    if bee_delivered == False or dame_delivered == False:
        menu:
            y "Who should I deliver to next?"
            "The Master" if bee_delivered == False:
                stop sound
                jump the_master
            "The Dame" if dame_delivered == False:
                stop sound
                jump the_dame
    else:
        stop sound
        jump wool_mill            

label wool_mill:
    scene bg woolmill with fade
    play music "industrial_machine_tone.mp3" fadein 1.0
    "You find yourself back at the wool mill, ready to report back. Mr Ramsey looks up from his station and calls out to you."
    
    show ramsey #neutral
    
    r "Good work. Grab me a new pair of shears from the back, would you?"
    
    call screen ram_key with Dissolve(.5)
    
    "At the back of the mill is a door labelled “Supply Closet”. You unlock the door and yank your hood off before stepping inside."
    $ keys += 1
    $ b_inspected = True
    stop music
    jump hall

label true_ending:
    play music "spooky-bells-ambiance.wav" volume 0.7
    play sound "key-jangle.wav" volume 1.0
    "Digging into your pockets, you feel two keys clink together and pull them out. With the bone key and Mr Ramsey’s key in hand, you approach the final door."
    show cheshire eneutral noears nomouth at truecenter with dissolve
    show cheshire body eaneutral mgrin at truecenter with dissolve
    c "Congratulations. Are you ready to unlock it?"
    menu:
        "Ready.":
            pass
    
    "You steel yourself before sliding the bone key into the first lock. It feels fragile in your hand, and you turn it with care."
    play sound "door-lock.wav" volume 0.8
    "{cps=40}{i}Click.{/i}{/cps}"
    "The ball of wool on the black sheep’s key tickles your hand as you insert it into the second lock and turn. "
    play sound "door-lock.wav" volume 0.8
    "{cps=40}{i}Click.{/i}{/cps}" #(animate door opening). 
    show dooranimation
    play sound "old-creaking-wooden-door.mp3"
    "You grasp the handle and pull with all your strength."
    "Only darkness lies beyond the door, silent and still."
    c "What reality will you wish for?"
    y bmad "One where I’m the best dancer to ever live. I {i}will{/i} win that competition, and I’m gonna blow everyone’s socks off."
    y bneutral eclosed "…And a reality where there’s a little bit of magic all around."
    "Taking a deep breath, you plunge into the darkness."

    scene bg tenniscourt at evening
    with fade 

    "You wake up sprawled on your back. The sun has begun to set, casting an orange glow across the sky. Sitting up, you realize you are back on the tennis court."
    y bmad eside mmumble "Was it all a dream?"
    "You head home, thinking about that strange dream."
    "Later that night, as you drift off to sleep, the crescent moon transforms into a sharp smile, and a pair of yellow eyes wink at you."
    # centered "{b}THE END{/b}"
    call screen true_end
    # This ends the game.
    return

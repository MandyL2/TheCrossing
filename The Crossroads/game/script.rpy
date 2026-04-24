# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You", image="apple")
image side apple = LayeredImageProxy("apple")

define n = Character('') #narration
define u = Character('???') #unknown 
define c = Character('Cheshire', image="cheshire")
# image cheshire_cat = "cheshire" 
define r = Character('Ramsey')
# image ramsey = "images/ram/ram.png"
define m = Character('The Master')
# image bee = "images/master/master.png"
define d = Character('The Dame')
# image dame = "images/dame/dame.png"
define b = Character('Little Boy')
# image boy = "images/boy/boy.png"
define p = Character('Bo Peep', image="bopeep")
# image bopeep = "bopeep"

transform double_size:
    # ypos 2.0
    xalign 0.5
    zoom 1.5

default bee_bad_end = None
default bee_delivered = False
default dame_delivered = False
default boy_delivered = False
default p_inspected = False
default b_inspected = False
default keys = 0
# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flash_then_shake = MultipleTransition(flash, 0.25, vpunch, 1.0)

init python:
    def check_keys (narr, you, door, inspected):
        if inspected == False:
            renpy.say(n,narr)
            renpy.say(y,you)
            renpy.jump(door)
        else:
            n("No, I've already gone through this door.")
            renpy.jump("doors")

# The game starts here.

label start:
    scene bg room with fade

    n "Tomorrow is the day. Countless hours at the studio, blood, sweat, and tears have led up to this."
    n "Ever since you were a child, you’ve loved to dance. After starting middle school, you finally got your parents to sign you up for dance classes."
    n "You were never that great at it, but tomorrow will be your chance to prove yourself at your first dance competition."
    n "You’re sure you’re ready, but more practice wouldn’t hurt, would it?"

    show bg tennis court

    n "After wandering the woods behind your house, you come across an abandoned tennis court. Its net is riddled with large holes, and the lines around the court have significantly faded."
    n "It may be a little rough, but it’s still a large and flat area — a perfect stage."
    n "Near the edge of the court is an old well. Its pulley is nowhere to be seen, most likely rotted away with age."
    n "Looking down into the well, all you see is pitch black. You drop a few pebbles down it, mimicking one of your favourite stories, but never hear a splash."

    menu:
        ". . ."
        "Find somewhere else":
            jump boring_end
        "Stay and practice":
            jump stay_and_practice

label boring_end:
    n "Thinking back to your favourite story, you warily back away from the well."
    y bmad mshout"No way, I've played these games before!!"
    n "This is not the time for adventure. There is too much at stake tomorrow, and you can’t risk any accidents."
    n "You turn back to look for a better place to practice."
    n "In the distance, a pair of yellow eyes narrow to slits as they stare after you, its sharp smile turning into a frown."
    centered "{b} {i} BORING END {/i} {/b}"
    return

label stay_and_practice:
    y braised eside mmumble "Interesting..."
    n "You’ll investigate the well on your break. But first, dance. You move back to the court and begin your routine. As you dance, you begin to feel dizzy and lose your balance."
    n "Not realizing how close you are to the well, you fall right in!"
    n "Darkness surrounds you as you tumble through the air, spinning round and round. The fall seems to go on forever."
    y "{cps=30}How deep does this hole go...{/cps}"
    n "You try to keep track of how much time has passed, but keep losing count."
    y bneutral eneutral mneutral "{cps=30}One Mississippi, two Mississippi...{/cps}"
    n "Though it was bright and sunny today, you look up to see a star—filled sky. Looking down, a faint light is beginning to grow."
    n "It's getting"
    n "{cps=20}bigger{/cps}"
    n "{cps=15}bigger...{/cps}"
    n "{cps=10}BIGGER...{/cps}"

    with fade
    with vpunch

    n "You scrunch your eyes shut in anticipation, only to bounce off something and land on soft dirt."
    y bsad eclosed mfrown "Oof..."

    show bg mushrooms with fade

    n "Feeling along what must be dirt walls, your eyes are drawn to a soft light in the otherwise dark cave."
    n "Under the opening of the hole you dropped out of is a large mushroom surrounded by a fairy ring. Its gently pulsing light is entrancing..."
    n "The scuttle of limbs behind you breaks you out of your trance. Whirling around, you make out the faint outline of a door further down the cave."
    n "It is nondescript, unassuming. A simple wooden door, perhaps made of birch."
    n "The doorknob feels smooth and cold in your hand as you twist it. The door swings open instantly."

    show bg hallway

    n "As you step forward, a long and narrow hallway stretches out before you, with plain beige walls and a dark red carpet full of dirt."
    n "The door slams shut behind you and vanishes."

    with hpunch
    
    u "{w}Welcome."
    n "You spin around wildly, trying to locate the source of the voice, except it comes from everywhere and nowhere, echoing through the hall. You become dizzy and fall to the ground."
    n "A sharp smile (or was it two?) spins before your eyes as you try to regain your bearings. The smile sits high above the doorframe at the end of the hall."
    n "Slowly, a yellow pair of eyes appears, followed by a set of pointed ears, massive paws, and finally a tail. A large blue cat marked with swirling patterns grins at you as it flicks its tail in amusement."

    show cheshire at truecenter 

    y bneutral eneutral mopen "I know you. You're the Cheshire cat, right? The one from Wonderland?"

    show cheshire eamad emad mfrown

    c "Not {i}the{/i} Cheshire cat, but {i}a{/i} Cheshire cat. How could you mistake us? We’re not even the same colour."
    y braised eclosed "Sorry, you’re right. Your fur is a much nicer colour. What's your name?"

    show cheshire eaneutral enarrow
    c "Cats don't have names."
    y eneutral "No?"
    c "No."
    y bsad "Okaaay, well I'm Apple. What is this place?"

    show cheshire eneutral mgrin
    c "This is The Crossroads. A place that is neither here nor there."
    show cheshire enarrow
    c "Many have come seeking something: to make deals, an escape, an adventure. The doors are never the same, all except for this one."

    # show final door

    y mmumble "Is that the exit? I really need to go home and practice."
    extend mshout "I have a dance competition tomorrow!"
    show cheshire eamad mfrown
    c "It is said that those who unlock this door can walk into a reality of their choosing."
    show cheshire eaneutral mgrin
    c "It grants wishes, in a way."
    y braised mmumble "And where would I be able to find the keys?"
    show cheshire enarrow
    c "Take a look around and you might just find them... If you survive long enough."
    
    hide cheshire #smile #fade out 

    y bmad eside mfrown "Well that was helpful."

label hall:
    scene bg hallway
    if keys == 0:
        n "You go to inspect the doors."
    elif keys >= 1:
        n "You find yourself back in the hallway."
        if keys == 2:
            jump true_ending
    jump doors

label doors:
    menu:
        "Door 1":
            $desc = ["The door on the left is white, dotted with pink polka-dots. White lace curtains hang from the doorframe, parted in the middle and tied with pink silk bows. Painted in the center of the door is a baby-blue shepherd’s crook.","Very cute, very demure."]
            $check_keys(desc[0], desc[1], "little_bo_peep", globals()['p_inspected'])

        "Door 2": 
            $desc = ["The door on the right is a flawless steel, the colour of obsidian black that gleams in the light. In the centre of it is a silver knocker in the shape of a sheep's head. As you approach the door, your reflection in the silver pull bar warps.", "Sick knocker. But why does my reflection look fluffy..."]
            $check_keys(desc[0], desc[1], "black_sheep", globals()['b_inspected'])
    

label little_bo_peep:
    with fade
    "{cps=20}{i} Little Bo-Peep has lost her sheep {/i} 
    \n{i} and she doesn't know where to find them. {/i}{/cps}"
    "{cps=20}{i} Leave them alone, {/i}
    \n{i} and they'll come home {/i}{/cps}"
    "{cps=20}{i} wagging their tails behind them. {/cps}{/i}"
    scene bg grass field

    n "A gentle breeze caresses your cheek as you open the door. Your eyes are greeted with the sight of lush green fields dotted with wild flowers."
    y "This is a great place to dance."
    n "You begin to dance through the fields until you come upon a dirt path worn with hooves. From there, the path diverges."
    n "On the left, a humble wooden house comes into view."
    n "On the right, the faint sound of weeping can be heard amid the whispers of the breeze."

    menu:
        "Check out the house":
            $ check_house = True
            show bg house
            n "The house is more like a log cabin, made of deep red wood with a blue painted roof. There is a small set of stairs that leads up to a porch overlooking the fields."
            n "In the corner of the porch is a rocking chair covered in knitted quilts. You take a seat only to find that the chair is bolted to the porch, making it completely immobile."
            y bsad mfrown "What kind of psychopath does that...?"
            n "You get up and peek through the window. Inside is an unlit fireplace, still smouldering from being put out. "
            n "Lying before it in the center of the room is a sheepskin rug, head and all. Above the fireplace is an assortment of stuffed sheep heads."
            n "Some look peaceful, while others are frozen mid-bleat, as if crying out. One in particular seems to be staring straight at you through the window."
           
            show sheep head
            hide sheep head 

            y eshocked "Okay, now {i}that's{/i} psychopathic."
            n "The sheep's piercing gaze is unsettling. Tearing your eyes away, you decide to turn back."

        "Follow the sound":
            $ check_house = False
            n "Following the sound, you come across a small cottage."

    show bg barn
    
    if check_house:
        n "Unlike the depressing log cabin, the cottage looks bright and cheerful. Its walls are a pale pink, with minimal grime."
    else:
        n "The cottage looks bright and cheerful. Its walls are a pale pink, with minimal grime."
    n "Pink polka-dotted curtains with white lace trim frame the windows. Beneath the windowsills are flowerbeds with red spider lilies in full bloom."
    n "Looming behind the cottage is a large red barn. The weeping noise gets louder as you approach the barn. The doors were flung wide open, the hinges of their lock smashed."
    n "Crouched in front of the barn is a ball of pink and white fabric."
    u "My sheep... my sheep..."
    y bneutral eside mmumble "That must be the source of the weeping."
    n "Cautiously approaching the ball, you call out."
    y bsad eneutral mopen "Are you okay?"

    show bopeep bsad esquint msad

    n "The ball of fabric uncurls to reveal the face of a young girl. Her hazel eyes glisten with tears as she peers out from underneath her pink bonnet."
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
    n "You herd the girl under the shade of some apple trees, trying to keep her spirits up."
    y eclosed "Your pretty dress might make it harder to move, so I’ll go easy on you."
    y mgrin "What’s your name? My friends call me Apple, like the fruit!"
    n "You jump up and grab an apple from a low-hanging branch. Just then, the tree makes an ear-piercing screech."
    y bsad eshocked mshout "!!"
    show bopeep bsad eclosed mneutral
    u "They don't like that. Would {i}you{/i} like it if someone ripped off one of your limbs?"
    y eclosed mneutral "..."

    show bopeep bneutral eneutral mneutral
    p "I'm Bo Peep."
    n "You drop the apple and roll it to the base of the tree."
    y mopen "...Sorry, I was a little hungry."

    show bopeep bsad esquint msad
    p "Oh, my poor sheep. They must be getting hungry, too! I was supposed to take care of them—"
    show bopeep esad mshout
    p "where have they gone!"
    y eneutral mmumble"Don't you ever take time for yourself? Who takes care of you?"
    show bopeep msad
    p "The sheep always come first."

    y bmad mfrown "That won’t do! You’ve got to relax a bit first, then I’ll help you look for your sheep."
    y mneutral "Follow my lead."
    n "You take Bo Peep's hand and twirl her a few times, her dress fanning out around her."
    
    show bopeep bhappy eclosed msmile
    p "Hehe!"    
    y bhappy eclosed mwidesmile "Now that we’ve loosened up a bit, let’s get started. First, you do this…"
    n "Striking a pose, you look at Bo Peep to follow. After teaching her the steps, you begin to count."
    y eneutral mopen "One, two, three, four..."

    show bopeep eneutral
    p "How are we supposed to dance without music?"
    y bneutral eside mfrown "Hmmm..."
    y bhappy eshocked mwidesmile "!"
    y eclosed mneutral "Hmm hm..."
    n "Bo Peep picks up your tune, and the two of you twirl and dance until the sun sets."
    
    with fade
    show bopeep bhappy eclosed msmile
    p "That was the most fun I've had in a while!"
   
    show bopeep bneutral eneutral mneutral
    p "Thank you."
    n "Just then, round shapes appear on the horizon. As the blobs get closer, you realize it is a herd of sheep."
    
    show bopeep bhappy eclosed msmile
    p "They're back!!!"
    show bopeep mneutral
    p "I guess you guys have found something else to eat, huh? "
    extend show bopeep esquint "{cps=25}I almost had a yummy treat for you.{/cps}"
    extend show bopeep eclosed msmile " This is my new friend Apple! Let’s get you guys back home."
    hide bopeep
    n "Bo Peep herds her sheep back to the barn."
    show bopeep
    p "Can you please watch over them while I find a new padlock?"
    y mopen "Sure."
    hide bopeep
    n "There’s something peculiar about these sheep, but you can’t put your finger on it."
    n "The one closest to you seems to be chewing on something."
    y "What are you eating, bud?"
    
    show sheep stare
   
    n "The sheep spits something out, and a colourful feather floats out alongside some small white objects."
    hide sheep stare
    n "The sheep lets out a loud bleat and yawns, revealing a row of razor-sharp teeth before walking away. Upon closer inspection, you realize it is a pile of bones."
    n "One of them has been chewed into the shape of a key."
    call screen bone_key with Dissolve(.5)
    $ keys += 1
    $ p_inspected = True
    p "Apple, could you give me a hand in here?"
    n "Feeling apprehensive, you hesistate before finally stepping inside."
    if keys >= 1:
        jump hall

label bp_bad_end:
    y braised eside mfrown "The Huntsman?"

    show bopeep bmad esquint msad
    u "He lives down the road and likes to hunt my sheep for sport."
    
    show bopeep mshout
    u "His cabin is filled with his trophies!"
    u "I have to find him before he does!" 

    show bopeep bsad eneutral
    p "Will you help me? What's your name? I'm Bo Peep."
    y bhappy eclosed mgrin "Of course! My friends call me Apple."

    show bopeep bhappy eclosed msmile
    p "Thanks, Apple. Oh, let's check near those apple trees first!"
    y bneutral eneutral mneutral "These apples look delicious. The sheep must love eating them."
    
    show bopeep bneutral eneutral mneutral
    p "Yes, it's always a treat for them. But ever since the Huntsman, they've developed a taste for humans."
    
    show bopeep esquint
    p "{cps=20}He deserved it anyway.{/cps}"
    y bhappy eshocked mmumble "...What?"
    n "Bo Peep lets out a sharp whistle, and a herd of sheep rushes out of the underbrush to surround you."
    
    show bopeep bsad eclosed mneutral
    p "Sorry!"
    n "The sheep begin bleating loudly, overwhelming your senses."
    n "As they close in on you, the last thing you see are rows of razor-sharp teeth."
    
    with vpunch
    
    "{i} *CRUNCH* {/i}"
    centered "{b}{i} BAD END {/i}{/b}"
    return

label black_sheep:
    scene bg wool mill 
    with fade 

    n "{cps=20}{i}Baa, baa black sheep{/i} 
    \n{i}Have you any wool?{/i}{/cps}"
    "{cps=20}{i}Yes sir, yes sir. Three bags full.{/i}"
    "{cps=20}{i}One for the master{/i}{/cps}"
    "{cps=20}{i}and one for the dame.{/i}{/cps}"
    "{cps=20}{i}And one for the little boy
    \nwho lives down the lane.{/cps}{/i}"

    n "Stepping through the door, you run into something soft."

    show ramsey with vpunch

    u "Goodness! Late {i}and{/i} clumsy! We’ve got a busy day ahead of us, special delivery orders and a new batch of wool just came in for processing."
    y "Wha—"
    n "The ram shoves a clipboard and three bags full of wool into your arms before ushering you towards the door."
    u "Now, there’s The Master, The Dame, and The Little Boy who lives down the lane."
    u "Don’t forget to make them sign for the delivery. We’ve been getting complaints lately about customers not receiving their orders."
    y "But I—"
    u "Shush!"
    
    show ramsey #stare
    
    u "{cps=5}...{/cps}{cps=20}Something looks off.{/cps}"
    y "That's what I've been trying to tell you—"
    u "Ah! Why aren't you in uniform?"
    
    show apple # uniform with vpunch

    n "In one swift motion, the ram slides a fluffy hood with sheep ears over your head"

    show apple # bruh

    y "..."
    u "There we go! We're on a tight schedule, so hurry back."
    n "And with that, the ram shoves you through the door into the main entrance, shutting it behind you and leaving you bewildered."
    n "You pound on the door to no avail."
    
    with hpunch
    
    y "Hey! You've got the wrong person!"
    n "You give in and sigh. Luckily, the clipboard contains all the information you need."

    menu:
        y "Let's just get this over with... Who should I deliver to first?"
        "The Master":
            jump the_master
        "The Dame":
            jump the_dame
        "The Little Boy":
            jump little_boy

label the_master:
    scene bg masters house
    
    n "You walk out the door and into a garden."
    y "Huh?"
    n "Swivelling around, you look back at the door you came out of and see a small shed."
    y "Uhh, okay..."
    n "The garden is filled with drooping flowers. Upon closer inspection, you realize the flowers are lifelike wax sculptures partially melted by the sun."
    n "Connected to the garden is a large mansion, its full height diminished by melted rooftops. The walls are streaked with dried globs of wax."
    n "Circling around to the front of the mansion, you spot a plaque in the melted remains of what looks like a mailbox."
    centered "The Master"
    y "Master of what?"
    n "There's a flicker of movement in the corner of your eye. At the entrance, a very large bee is trying to smooth out the globs of wax."
    
    show bee #silhouette
    
    y "...Delivery for The Master?"
    
    show bee #happy
    
    m "Ah, yes! That's me, master of wax. This way, please."
    n "Opening the gates, the Master flits inside, gesturing for you to follow. The mansion seems to be made entirely out of beeswax and is excellently crafted."
    n "The Master leads you to a parlour."
    m "Sorry for the mess; the weather has been swinging between hot and cold these days."
    
    show bee #sigh
    
    m "All these repairs have been keeping me from my art. You can leave the wool by the table."
    m "Sit, sit! Let me make you some tea."
    y "Oh no, that's okay—"
    m "Nonsense! It's the least I can do. I'll be right back!"
    n "And with that, The Master flits off again, leaving you alone."
    n "The parlour is quite humble, with few furnishings."
    n "As you are inspecting one of the bookshelves, a chilling sensation brushes against your right side, emanating from a room in the corner. The door is partially open."
    n "You strain your ears for any sound of movement, but only hear the ticking of a clock."

    menu:
        "Check it out":
            show bg workroom
            "You push the door open to find a small workroom, containing partially melted wax statues of three small children."
            "Their expressions are an assortment of shock and fear. The tops of their heads are slightly melted, and you notice strands of hair sticking out from each of them."
            "A chill runs down your spine, and it’s not because of the AC."
            "The Master’s buzzing voice grows louder as they approach the parlour room, talking aloud. You hurry back to your seat."
            "The Master returns with a tray of tea and honeycombs."
        "Stay":
            "After a few minutes, The Master returns with a tray of tea and honeycombs."

    m "Sorry for the wait! Have some tea."

    menu:
        y "Oh..."
        "Drink the tea":
            $ bee_bad_end = True
        "Decline the tea":
            pass

    m "While you're here, let me show you my latest project! It's actually about humans."

    show bg workroom

    y "These are... very expressive. And realistic. You really are a master of your craft."
    m "Well, I'm still working on my human sculpting skills. It helps to have good models."
    m "...You would make an excellent subject. Are you interested in modelling?"

    if bee_bad_end:
        y "Not really..."
        n "You try to back up but feel dizzy. Your legs give out, and the last thing you see before darkness closes over you is The Master's serene smile."
        
        with fade
       
        y "What the... Is this wax?"
        
        with hpunch
        
        y "I can't move..."
        m "Ah, you're awake! So sorry, but you really are too good of a model to pass up."
        m "{cps=15}But don't worry, this won't hurt.{/cps} {cps=8}Soon you won't feel anything...{/cps}"
        n "The Master adds one last piece of wax over your face, sealing your fate."
        centered "{b}{i}BAD END{/i}{/b}"
        return
    else:
        "You back up slowly." #zoom out screen
        y "Maybe another time, I still have deliveries to make. The Ram is waiting for me. Please sign here."
        m "The Ram? Oh, you must mean Mr Ramsey."
        m "That's a shame..."
        n "After taking the clipboard back, you decide to show yourself out."
        $ bee_delivered = True

        if boy_delivered == False or dame_delivered == False:
            menu:
                y "Who should I deliver to next?"
                "The Little Boy" if boy_delivered == False:
                    jump little_boy
                "The Dame" if dame_delivered == False:
                    jump the_dame
        else:
            jump wool_mill  
    
label the_dame:
    scene bg parlour
    $ tarts = False
    
    n "You walk out the front door and into a parlour. It's decorated red and black, with a checkered floor and velvet chairs."
    n "Sunlight streams in through the heavy black curtains parted in two, illuminating the room. Decorating the walls are framed paintings of a regal-looking woman, most likely the lady of the house."
    n "On the coffee table is a tray of tarts."

    menu:
        y "Ooh..."
        "Eat the tarts":
            y "Maybe just a little bite..."
            $ tarts = True
            
            show apple # bruh

            y "{i}(This tastes like dirt...){/i}"
        "Don't eat the tarts":
            pass

    n "A voice crackles to life and echoes throughout the room."
    u "Announcing the arrival of The Dame!"

    show dame #neutral #slide in from right
    show dame #shocked
    d "Who are you? What are you doing in my house! {b}GUARDS!{/b}"

    menu:
        "It was an accident!":
            show apple # shocked

            y "This is a misunderstanding. I don't even know how I got here!"
            if tarts:
                d "Liar! You ate my tarts. You must be a thief in disguise!"
            else:
                d "What, are you telling me you just teleported in here?"

            menu:
                "Tell the truth":
                    y "Kinda? It's been a weird day."
                    d "Absolutely ridiculous."
                    y "It's true! Let me explain..."

                    with fade

                    d "Hmm... What an interesting concept. Let's test it."
                    n "With a snap of her fingers, two armoured guards appear and grab you by the arms. They shove you through the parlour doors, and you turn around to see nothing has changed."

                    show apple # bruh

                    y ". . ."
                    d "I knew it. Guards, take her to the guillotine."

                    show apple # shocked

                    y "WHAT? Wait—"
                    n "You are once again seized. Despite your struggles, you are dragged away to your doom..."
                    centered "{b}{i}BAD END{/i}{/b}"
                    return
                "Lie":
                    y "Well, no. The front door was unlocked and I somehow ended up here while looking for you."
                    n "You shake the bag of wool in your hand and pass her your clipboard."
                    y "If you could just sign beside your name, I'll get out of your hair at once."
                    d "...Fine. Begone."
                    y "{i}(Don't have to tell me twice!){/i}"
                    n "She hands you the clipboard, and you hurry to the door."
        "I'm just making a delivery!":
            show apple # shocked

            y "{cps=40}Waitwaitwait!{/cps} I'm just here to make a delivery!"
            if tarts:
                d "Liar! You ate my tarts. You must be a thief in disguise!"
            else:
                d "Prove it then!"

            y "I've got your wool right here! And I'm definitely not wearing this hat for fun."
            d "Hmm, that {i}is{/i} Mr Ramsey’s uniform. I think it’s quite cute. I apologize for the accusation. "
            if tarts == False:
                extend "Please help yourself to some tarts."
                y "Sure, thanks."

                show apple # bruh

                y "{i}(This tastes like dirt...){/i}"
                d "Is it not to your liking?" 

                show apple # smile

                y "Oh no! No, it's great!"
            
            d "How did you get in here?"

            menu:
                "Tell the truth":
                    show apple # neutral

                    y "It's been a weird day. I don't even know where to start..."
                    
                    with fade

                    d "Hmm... What an interesting concept. Let's test it."
                    n "With a snap of her fingers, two armoured guards appear and grab you by the arms. They shove you through the parlour doors, and you turn around to see nothing has changed."

                    show apple # bruh

                    y ". . ."
                    d "I knew it. Guards, take her to the guillotine."

                    show apple # shocked

                    y "WHAT? Wait—"
                    n "You are once again seized. Despite your struggles, you are dragged away to your doom..."
                    centered "{b}{i}BAD END{/i}{/b}"
                    return
                "Lie":
                    y "Well, the front door was unlocked. I somehow ended up here while looking for you."

                    show dame #frown

                    d "Looks like somebody isn't doing their job. Unacceptable. I'll have to look into it later."
                    n "You shake the bag of wool in your hand and pass her your clipboard."
                    y "Riiight. Before you do that, if you could just sign beside your name, I'll get out of your hair at once."
                    d "...Alright."
                    n "She hands you the clipboard, and you hurry to the door."
    $ dame_delivered = True
    if bee_delivered == False or boy_delivered == False:
        menu:
            y "Who should I deliver to next?"
            "The Master" if bee_delivered == False:
                jump the_master
            "The Little Boy" if boy_delivered == False:
                jump little_boy
    else:
        jump wool_mill      

label little_boy:
    scene bg treehouse

    n "You step out the door and onto the balcony of a treehouse. From there, you can see the wool factory a hop, skip, and twirl away down the lane."
    show boy
    n "Under the shade of leaves sits a little boy at a picnic table. An assortment of finger foods is spread out before him."
    n "The table is set for three other guests, each with their own teacup and saucer."
    y "Wool delivery!"
    n "You set the bag of wool down by the table and hand the boy your clipboard. He wordlessly signs before asking:"
    b "Would you like to stay for some tea? I'm afraid it's a little cold, though."
    b "We were supposed to have a tea party today, but it seems my guests are running late."
    # Flicker boy sprite
    n "You look at the carefully arranged food, completely untouched, and the empty seats. You should be getting back to your task, but the boy’s hopeful expression makes you feel a twinge of pity."
    n "Glancing at the fancy teapot, you see a wisp of steam curl out of the spout."

    menu:
        "Join the tea party":
            n "You take a seat across from the boy and fill your plate with snacks, then pick up a teacup. He grins at you as you silently hold it out for him to fill."
            #water pouring sfx
            y "{i}(This tea is still hot...){/i}"
            y "What's your name?"
            
            show boy #sad
            
            b "I... can't remember. I woke up one day, and I was here. All I knew was that I was waiting for someone to join me..."
            b "{cps=15}Someone like you.{/cps}"
            y "And how long have you been waiting here?"
            b "Weeks... months... years. I lost track a long time ago."
            b "{cps=30}But now that you're here, {w=1.0} it doesn't matter anymore.{/cps}"
            
            show apple # shocked
            
            y "What? What about your other guests?"
            b "Anyone would do, as long as I could find someone to replace me."
            
            show boy #happy
            
            b "Thank you."
            n "The boy stands up from the table. You try to follow, but are stuck to your seat."
            
            with hpunch
            show apple # angry
            
            y "What is this? Let me go!"
            b "Sorry for tricking you, and thank you for setting me free." #fade out
            n "As the cold realization sets in that you are trapped here until someone else can replace you, the table turns pristine once again."
            n "Waiting."
            centered "{b}{i}BAD END{/i}{/b}"
            return
        "Head back":
            pass 
        
    y "{i}(If the tea is cold like he says it is, there shouldn't be any steam. Something feels off...){/i}"
    y "As much as I'd like to, I really should be heading back now."
    
    show boy #sad
    
    b "Just for a little bit? No one else has shown up."
    y "I'm really sorry, but I need to go."
    n "You begin to turn away from the table, but whip back when you hear the boy screech behind you—"
    b "PLEASE! I'VE BEEN HERE FOR {i}SO LONG!{/i} {cps=18}{size=+10}{b}I JUST NEED SOMEONE TO TAKE MY PLACE.{/b}{/size}{/cps}"  with hpunch
    #flicker sprite
    y "Yeahh... Time to get out of here."
    n "You hurry to the balcony door while the boy continues to cry and screech."
    b "COME BACK! {size=+10}{b}{cps=15}COME... BACK...{/cps}{/b}{/size}"
    $ boy_delivered = True
    # TODO: optimize delivery choice structure
    if bee_delivered == False or dame_delivered == False:
        menu:
            y "Who should I deliver to next?"
            "The Master" if bee_delivered == False:
                jump the_master
            "The Dame" if dame_delivered == False:
                jump the_dame
    else:
        jump wool_mill            

label wool_mill:
    scene bg wool mill
    
    n "You find yourself back at the wool mill, ready to report back. Mr Ramsey looks up from his station and calls out to you."
    
    show ramsey #neutral
    
    r "Good work. Grab me a new pair of shears from the back, would you?"
    
    centered "obtained key"
    
    n "At the back of the mill is a door labelled “Supply Closet”. You unlock the door and step inside."
    $ keys += 1
    $ b_inspected = True
    jump hall

label true_ending:
    n "Digging into your pockets, you feel two keys clink together and pull them out. With the bone key and Mr Ramsey’s key in hand, you approach the final door."
    show cheshire smile
    c "Congratulations. Are you ready to unlock it?"
    menu:
        "Ready.":
            pass
    
    n "You steel yourself before sliding the bone key into the first lock. It feels fragile in your hand, and you turn it with care."
    n "{cps=40}{i}Click.{/i}{/cps}"
    n "The ball of wool on the black sheep’s key tickles your hand as you insert it into the second lock and turn. "
    n "{cps=40}{i}Click.{/i}{/cps}" #(animate door opening). 
    n "Only darkness lies beyond the door, silent and still."
    c "What reality will you wish for?"
    show apple # determined
    y "One where I’m the best dancer to ever live. I {i}will{/i} win that competition, and I’m gonna blow everyone’s socks off."
    y "…And a reality where there’s a little bit of magic all around."

    show bg tennis court with fade

    n "You wake up sprawled on your back. The sun has begun to set, casting an orange glow across the sky. Sitting up, you realize you are back on the tennis court."
    y "Was it all a dream?"
    n "You head home, thinking about that strange dream."
    n "Later that night, as you drift off to sleep, the crescent moon transforms into a sharp smile, and a pair of yellow eyes wink at you."
    centered "{b}THE END{/b}"
    # This ends the game.
    return

screen bone_key():
    modal True
    on "show" action [Function(renpy.music.set_volume, 1.0, channel="sound"), Play(channel="sound", file="key-get.wav")] #increase volume
    imagebutton:
            background "#746e60a8"
            idle "obtained_bp_key.webp"
            xalign 0.5
            yalign 0.0
            # zoom 0.8
            action Hide("popup_letter", Dissolve(.5)), Return(False)

screen ram_key():
    modal True
    on "show" action [Function(renpy.music.set_volume, 1.0, channel="sound"), Play(channel="sound", file="key-get.wav")]
    transform:
        zoom 0.8
    imagebutton:
        background "#746e60a8"
        idle "obtained_r_key.webp" 
        xalign 0.5
        yalign 0.0
        action Hide("popup_letter", Dissolve(.5)), Return(False)

screen finaldoor_closeup():
    modal True
    vbox:
        add "images/finaldoor_hover.webp" at double_size
        align (0.5, 0.5)
        # zoom 2.0

screen boring_end():
    modal True
    on "show" action Play(channel="sound", file="eerie-resonant-tone.mp3")
    imagebutton:
        idle "boring_end.webp"
        action Return()

screen bad_end_bee():
    modal True
    on "show" action Play(channel="sound", file="beehive-asmr.mp3")
    imagebutton:
        idle "bad_end_bee.webp"
        action Return()

screen bad_end_dame(tarts):
    modal True
    on "show" action Play(channel="sound", file="chop.mp3")
    imagebutton:
        if tarts:
            idle "bad_end_dame2.webp"
        else:
            idle "bad_end_dame1.webp"
        action Return()

screen bad_end_boy():
    modal True
    on "show" action Play(channel="sound", file="creepy-basement.mp3")
    imagebutton:
        idle "bad_end_boy.webp"
        action Return()

screen bad_end_bopeep():
    modal True
    on "show" action Play(channel="sound", file="crunch.wav")
    imagebutton:
        idle "bad_end_bopeep.webp"
        action Return()

screen true_end():
    modal True
    on "show" action Play(channel="sound", file="key-get.wav")
    imagebutton:
        idle "true_end.webp"
        action Return()
screen bone_key():
    modal True
    imagebutton:
            background "#746e60a8"
            idle "obtained_bp_key.webp"
            xalign 0.5
            yalign 0.0
            action Hide("popup_letter", Dissolve(.5)), Return(False)

screen ram_key():
    modal True
    
    imagebutton:
        background "#746e60a8"
        idle "obtained_r_key.webp" 
        xalign 0.5
        yalign 0.0
        action Hide("popup_letter", Dissolve(.5)), Return(False)
screen bone_key():
    modal True
    imagebutton:
            idle "obtained_bp_key.webp"
            xalign 0.5
            yalign 0.0
            action Hide("popup_letter", Dissolve(.5)), Return(False)
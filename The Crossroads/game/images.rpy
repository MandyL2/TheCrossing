layeredimage apple:
    
    #base
    always "apple_base"

    #face
    group eyes auto:
        attribute eneutral default

    group nose:
        attribute normal default

    group mouth auto:
        attribute mneutral default

    group brows auto:
        attribute bneutral default

    #outfit
    group outfit:
        attribute hat:
            "apple_outfit_hat"

layeredimage cheshire:
    zoom 0.7
    #base
    always "cheshire_base"

    #face
    group eyes auto:
        attribute eneutral default
    
    group mouth auto:
        attribute mgrin default

    group ears auto:
        attribute eaneutral default

layeredimage bopeep:
    # base
    always "bopeep_base"

    #face 
    group brows auto:
        attribute bneutral default

    group eyes auto:
        attribute eneutral default

    group mouth auto:
        attribute mneutral default
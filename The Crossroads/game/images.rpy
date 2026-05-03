layeredimage apple:
    
    #base
    always "apple_base"

    #face
    group eyes auto:
        attribute eneutral default
        attribute noeffect null

    group nose auto:
        attribute normal default

    group mouth auto:
        attribute mneutral default
        attribute noeffect null

    group brows auto:
        attribute bneutral default
        attribute noeffect null

    #outfit
    group outfit:
        attribute hat:
            "apple_outfit_hat"

layeredimage cheshire:
    zoom 0.7
    #base
    attribute body:
        "cheshire_base"

    #face
    group eyes auto:
        attribute eneutral default
        attribute noeyes:
            null
    
    group mouth auto:
        attribute mgrin default
        attribute nomouth:
            null

    group ears auto:
        attribute eaneutral default
        attribute noears:
            null

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

layeredimage ramsey:
    zoom 0.9
    #base
    group pose auto:
        attribute side default

    group eyes auto:
        attribute sideopen default

layeredimage bee:
    ypos 1.2
    zoom 0.75

    
    attribute wings:
        "bee_wings"

    attribute armback:
        "bee_armback"
    #base
    group pose auto:
        attribute base default

    group ant auto:
        attribute aneutral default

    group arms auto:
        attribute noarms default:
            null

    attribute tray:
        "bee_tray"
        
    attribute holdtray:
        "bee_holdtray"

layeredimage dame:
    group hand auto:
        attribute curl default
    #base
    always "dame_base"

    group brows auto:
        attribute bneutral default

    group eyes auto:
        attribute eneutral default

    group mouth auto:
        attribute mneutral default

    

layeredimage boy:
    #base
    always "boy_base"

    #hair
    group hair auto:
        attribute normal default

    #face
    group eyes auto:
        attribute eneutral default

    group mouth auto:
        attribute mneutral default

    group brows auto:
        attribute bneutral default


# Copyright 2026 CuteShadow
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# 
#
# Ren'Py Auto Positioner: 1.0
#
# https://cuteshadow.itch.io/lazy-positioner-in-renpy


#################################################
## SETTINGS
#################################################

## Character sprites that will be auto position'd.
## Put your sprites here, the image name.
define AUTO_SPRITES = ["bopeep", "ramsey",  "dame", "boy"]

## You can make the spacing between them more or less.
define AUTO_XTRASPACING = 0

# You can move all your sprites horizontally in pixels.
define AUTO_XOFFSET = 0

# You can move all your sprites vertically in pixels.
define AUTO_YOFFSET = 600

# You can change the zoom of all your sprite.
# Where 1.0 is the original and 2.0 is twice the size.
define AUTO_ZOOM = 0.9


#################################################
## CODE
#################################################


## Auto place sprites as they appear on the screen.
transform auto(sprite):
    function auto_partial(auto_f, sprite=sprite)


## A convenient position override.
transform x(x=0.5):
    xcenter x
    yalign 1.0
    yoffset AUTO_YOFFSET
    zoom AUTO_ZOOM


init python:

    ## So I can reuse the auto function.
    from functools import partial as auto_partial

    ## Find nice places to space out the sprites.
    def auto_positions(n):
        MIDDLE = 0.5

        # Spacing.
        # gap -- sprite -- gap -- sprite -- gap -- etc.
        gaps = n + 1
        space = 1 / (gaps)
        
        # Positions.
        positions = [(i + 1) * space for i in range(n)]

        # Convert pixels into fractions.
        auto_xtraspacing = AUTO_XTRASPACING
        if isinstance(auto_xtraspacing, int):
            auto_xtraspacing = auto_xtraspacing / config.screen_width
        auto_xtraspacing *= 10  # bigger impact

        # Adjust spacing.
        offset_positions = [
            MIDDLE + (pos - MIDDLE) * (1 + auto_xtraspacing)
            for pos in positions
        ]
        
        # Tada!
        return offset_positions


    ## The auto position function.
    def auto_f(trans, st, at, sprite):
        # Yalign to bottom.
        trans.yalign = 1.0

        # Offset.
        trans.yoffset = AUTO_YOFFSET
        trans.xoffset = AUTO_XOFFSET

        # Zoom.
        trans.zoom = AUTO_ZOOM

        # Check who's on the screen.
        visible = [c for c in AUTO_SPRITES if renpy.showing(c)]
        count = len(visible)

        # Slot the sprite into the correct position.
        if count >= 1 and sprite in visible:
            i = visible.index(sprite)
            trans.xcenter = auto_positions(count)[i]

        # This is fast enough to update instantly.
        return 0.01


    ## Apply the auto position transform to each sprite automatically.
    for sprite in AUTO_SPRITES:
        config.tag_transform[sprite] = [auto(sprite)]

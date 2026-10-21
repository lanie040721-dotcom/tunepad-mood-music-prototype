# CHINESE-STYLE HAPPY DREAMY PAD
# Bright pentatonic harmony layer
#
# Goal:
# Add a brighter and happier supporting harmony behind the main Happy melody.
#
# The Pad should not become another main melody.
# Instead, it works as a soft background layer that supports the energetic Happy track.
# Finalise the notes 

# To improve this:
# - three-note harmonies are used instead of single notes
# - the harmony uses bright pentatonic-style pitch material
# - each chord is sustained for a long duration
# - velocity remains low so the Pad stays in the background
# - low-pass filtering softens the sound

# The pitch material is based on:
# C - D - E - G - A

# MIDI notes:
# 60 - 62 - 64 - 67 - 69
# These notes are combined into open,
# consonant three-note harmonies
# to create a brighter and more positive sound.


# Happy Pad Variations


# "pad_variations" stores three different harmonic versions of the Happy Pad.
#
# Each variation contains four chords.
# Each chord is written as a list of three MIDI notes.
# For example:
# [60, 64, 67] means that notes 60, 64 and 67 are played at the same time.
#
# This creates a three-note harmony instead of a single melodic note.
#
# TunePad can play a list of notes together when that list is passed into playNote().
#
# The three variations use the same pentatonic-style pitch material, but the order of the harmonies changes.
#
# This creates different harmonic outcomes while keeping the same Happy character.
# "pad_variations" is a nested list.
# The outer list stores three variations.
# Each variation contains four chord lists,
# and each chord list contains three integer MIDI notes.

pad_variations = [

    # Variation 1 - Bright and Open
    #
    # The first chord:
    # [60, 64, 67]
    # creates a stable and bright opening.
    #
    # The second harmony:
    # [62, 67, 69]
    # introduces D, G and A,
    # creating a more open pentatonic colour.
    #
    # The third harmony:
    # [64, 67, 72]
    # moves the harmony upward
    # and increases the feeling of brightness.
    #
    # The final chord returns to:
    # [60, 64, 67]
    # creating a stable ending.

    [
        [60, 64, 67],
        [62, 67, 69],
        [64, 67, 72],
        [60, 64, 67]
    ],


    # Variation 2 - Playful Harmony
    #
    # This version changes the order of the same harmonic material.
    #
    # The harmony rises earlier to create a slightly more energetic result.
    #
    # It then moves to: [62, 67, 69] before returning to the stable ending chord.
    #
    # This works well with the "Bouncy" Happy melody variation.

    [
        [60, 64, 67],
        [64, 67, 72],
        [62, 67, 69],
        [60, 64, 67]
    ],


    # Variation 3 - Gentle Movement
    # This variation begins with:
    # [62, 67, 69]
    #
    # It then moves through a brighter higher harmony before returning downward.
    #
    # The harmonic movement is more gradual and slightly less direct than Variation 2.

    [
        [62, 67, 69],
        [60, 64, 67],
        [64, 67, 72],
        [60, 64, 67]
    ]
]


# Control Variable


# "variation" selects which harmonic pattern will be used from pad_variations.
#
# Python list positions start from 0.
# Therefore:
# variation = 0
# selects Variation 1 - Bright and Open
#
# variation = 1
# selects Variation 2 - Playful Harmony
#
# variation = 2
# selects Variation 3 - Gentle Movement
#
# Changing only this number allows the Pad to produce a different harmonic result without rewriting the code.
# "variation" is an integer variable.
# Its value is used as a list index.
#

variation = 2



# This line uses the value of "variation" to select one complete chord progression.
#


pad_chords = pad_variations[variation]


# Rhythm

# Each harmony lasts for 4 beats.
#
# There are four chords in total:
# 4 beats x 4 chords = 16 beats
# This matches the total length of the main Happy track.
#
# The main Happy melody uses many short notes, while the Pad uses very long chords.
#
# This contrast is intentional:

# Main Happy melody
# = active, fast and energetic
#
# Happy Pad
# = smooth, sustained and supportive
#
# Because the Pad changes only every 4 beats, it does not compete with the main melody.

# "pad_duration" is a list of four integer values.
# Each value controls the duration
# of the chord at the same list index.
pad_duration = [
    4, 4, 4, 4
]


# Dynamics / Velocity


# The velocity values are intentionally very low.
#
# The main Happy melody uses much stronger velocity values around 78-94.
#
# The Pad uses values around 16-19.
#
# This large difference in velocity keeps the Pad behind the main melody.
#
# Small changes between each chord prevent the background layer from sounding completely static.

# "pad_velocity" is a list of integer values.
# Each value controls the velocity
# of the chord at the same list index.
pad_velocity = [
    16, 19, 18, 17
]


# Generate Happy Pad


# A low-pass filter is applied to reduce some of the high-frequency brightness.
#
# This is important because the Happy melody is already bright and energetic.
#
# The Pad should sound warm and supportive, rather than sharp or dominant.
#
# A frequency of 1050 keeps some brightness while still softening the Pad.

# "with lowpass(...)" creates an effect block.
# Every chord played inside this indented block
# receives the low-pass effect.
#
# 1050 is an integer value representing
# the filter cutoff frequency.
with lowpass(frequency = 1050):


    # The for loop moves through all four chords in pad_chords.
    #
    # "i" represents the current chord position.
    #
    # pad_chords[i]
    # selects the current three-note harmony.
    #
    # pad_duration[i]
    # selects how long the chord lasts.
    #
    # pad_velocity[i]
    # controls how strongly the chord is played.

# len(pad_chords) returns the number of chords in the list.
# In this case, len(pad_chords) = 4.
#
# range(0, 4) creates the index values:
# 0, 1, 2, 3.
#
# During each loop, "i" is an integer
# representing the current list position.
#
# The same index is used to match:
# pad_chords[i], pad_duration[i] and pad_velocity[i].
    for i in range(0, len(pad_chords)):


        # playNote() receives a LIST of notes:
        #
        # for example:
        # [60, 64, 67]
        #
        # Because a list is used,
        # TunePad plays all three notes together.
        #
        # This produces a chord-like harmony instead of a single note.
        #
        # "sustain = 0.4" allows the chord to ring slightly longer, making the Pad smoother and helping the harmonies connect.

        playNote(
            pad_chords[i],
            beats = pad_duration[i],
            velocity = pad_velocity[i],
            sustain = 0.4
        )
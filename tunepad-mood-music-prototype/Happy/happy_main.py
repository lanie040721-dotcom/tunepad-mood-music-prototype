# HAPPY MOOD 
# Controlled Variation
#
# Goal:
# Create different musical outcomes while keeping the same overall Happy emotion.
# Finalise the notes 

# The Happy mood is created through several musical rules:
# - A brighter and relatively high pitch range
# - Short note durations for a faster rhythm
# - Higher velocity for stronger and more energetic sound
# - Repeated melodic patterns
# - Swing to make the rhythm feel more playful

# By changing only the value of "variation", the program selects a different melody while keeping the same Happy musical rules.



# Happy Melodic Variations

# "happy_variations" is a list containing three different melodic patterns.
# Each pattern is itself another list of MIDI note numbers.
# For example:
# 60 = C
# 64 = E
# 67 = G
# 69 = A
# 72 = high C

# These notes are mainly in a bright middle-to-high register,
# which helps maintain the Happy character.
#
# The three variations use similar pitch material, but change the order and direction of the melody.
# "happy_variations" is a nested list, or a list of lists.
# Each inner list contains 12 integer MIDI pitch values.
# This allows several melodies to be stored
# in one variable and selected by index.

happy_variations = [

    # Variation 1 - Rising and Bright
    #
    # This melody frequently moves upward
    # from lower notes toward higher notes.
    #
    # Rising pitch movement helps create
    # a more uplifting and open feeling.

    [60, 64, 67, 72,
     69, 67, 64, 67,
     64, 67, 69, 72],


    # Variation 2 - Bouncy
    #
    # This pattern moves repeatedly between
    # middle and higher notes.
    #
    # The frequent changes in direction
    # create a more playful and bouncing effect.

    [64, 67, 72, 69,
     67, 64, 69, 72,
     67, 69, 64, 67],


    # Variation 3 - Up and Down
    #
    # This version changes pitch direction
    # more frequently than Variation 1.
    #
    # The alternating high and low notes
    # create a more lively and active melodic shape.

    [60, 67, 64, 72,
     67, 69, 64, 67,
     72, 69, 67, 64]
]




# Rhythm Rules


# "happy_duration" controls how long each note is played.
#
# Most notes last only 0.5 beats. These shorter notes make the melody move quickly, supporting the energetic Happy mood.
#
# Some notes last for 1 beat.
# These longer notes create small pauses in the movement and stop the rhythm from sounding too mechanical.
#
# The total duration of one phrase is 8 beats.
# "happy_duration" is a list containing
# integer and floating-point values.
#
# Each value controls the duration
# of the note at the same list index.

happy_duration = [

    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 1, 1,
    0.5, 0.5, 1, 1
]



# Dynamics / Velocity


# "velocity" controls how strongly each note is played.
#
# Higher values produce a stronger and louder sound.
#
# The Happy melody uses relatively high velocity values between 78 and 94.
#
# This gives the music more energy than the Calm mood.
#
# The values are not all identical.
# Small changes in velocity make the phrase sound more expressive and less robotic.
# "happy_velocity" is a list of integer values.
# Each value controls the velocity
# of the note at the same list index.

happy_velocity = [

    78, 82, 86, 90,
    86, 82, 88, 92,
    82, 86, 90, 94
]



# Control Variables


# "variation" controls which melodic pattern will be selected from happy_variations.
#
# Python lists start counting from 0.
#
# Therefore:
# variation = 0 selects the FIRST melody
#
# variation = 1 selects the SECOND melody
#
# variation = 2 selects the THIRD melody
#

# "variation" is an integer variable.
# Its value is used as a list index.
variation = 2



# Repetition


# "repeat_times" controls how many times
# the selected phrase is repeated.
#
# One Happy phrase lasts 8 beats.
#
# repeat_times = 2
# therefore creates:
#
# 8 beats x 2 = 16 beats
#
# Repetition helps create a longer
# and more complete musical structure.

# "repeat_times" is an integer variable.
# It controls how many times the selected lists are repeated.
repeat_times = 2



# Swing


# "swing_amount" controls the swing effect.
# Swing slightly changes the timing of the rhythmic pattern.
#
# This reduces the feeling of strict,mechanical computer timing and creates a more playful and lively groove.
#
# A value of 0.2 creates a relatively light swing, so the effect supports the Happy mood without changing the rhythm too strongly.

# "swing_amount" is a floating-point variable.
# Its value is passed into the swing effect.
swing_amount = 0.2



# Select the Variation


# This line connects the control variable to the melodic variation list.


happy_notes = happy_variations[variation]



# Build the 16-beat Phrase


# Multiplying a Python list repeats its contents.
#
# For example:
# happy_notes * 2 repeats the selected 8-beat melodic structure twice.
#
# The same process is used for:
# - pitch
# - duration
# - velocity
#
# This keeps all three musical parameters aligned.

notes = happy_notes * repeat_times

durations = happy_duration * repeat_times

velocities = happy_velocity * repeat_times


# Generate Happy Music

# The swing effect is applied around the complete playback section.
#
# This means all notes played inside this block receive the swing timing effect.

# "with swing(...)" creates an effect block.
# Every note played inside this indented block
# receives the swing timing effect.
with swing(swing_amount):


    # The for loop moves through every note in the repeated melody.
    # "i" represents the current position in the lists.
    #
    # For example:
    # notes[i]
    # selects the current pitch
    #
    # durations[i]
    # selects its corresponding duration
    #
    # velocities[i]
    # selects its corresponding velocity
    #
    # This allows three separate lists
    # to work together as one musical phrase.

    # len(notes) returns the number of items in the list.
# In this version, len(notes) = 24.
#
# range(0, 24) creates the index values
# from 0 to 23.
#
# During each loop, "i" is an integer
# representing the current list position.
#
# The same index is used to match:
# notes[i], durations[i] and velocities[i].
    for i in range(0, len(notes)):


        # playNote() generates each note.
        #
        # Pitch comes from the selected variation.
        # Duration comes from happy_duration.
        # Velocity comes from happy_velocity.
        #
        # The loop repeats this process
        # until every note in the 16-beat phrase
        # has been played.

        playNote(
            notes[i],
            beats = durations[i],
            velocity = velocities[i]
        )
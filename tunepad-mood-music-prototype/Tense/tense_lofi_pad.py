# TENSE MOOD 
# Controlled Variation
#
# Goal:
# Make the Tense mood sound more continuous,darker and more intense.
# Finalise the notes 



# Tense Melodic Variations


# "tense_variations" stores three different melodic versions of the Tense mood.
#
# Each variation contains 8 MIDI note values.
#
# The notes stay in a relatively low register,
# mainly around:
# 46 - 49
#
# A lower register helps create
# a darker and heavier musical character.
#
# Most of the pitch movement is chromatic.
#
# This means many notes move by only one semitone,
# for example:
#
# 48 -> 49
# 48 -> 47
# 47 -> 48
#
# Small chromatic movement creates tension because the notes are very close together and do not create a relaxed melodic shape.
#
# The three variations use similar pitch material, but change the order and direction of movement.
# "pad_variations" is a nested list, or a list of lists.
# Each inner list contains four integer MIDI pitch values.
# This allows several pitch patterns to be stored
# in one variable and selected by index.

# This allows different musical outcomes while keeping the same Tense emotional rules.
# "tense_variations" is a nested list, or a list of lists.
# Each inner list contains 8 integer MIDI pitch values.
# This allows several melodies to be stored
# in one variable and selected by index.

tense_variations = [

    # Variation 1 - Repetitive Chromatic Pressure
    
    # This pattern repeatedly moves between neighbouring chromatic notes.
    
    # For example:
    # 48 -> 49 -> 48 -> 49
    
    # The repetition creates a sense of pressure and makes the music feel trapped around a very small pitch area.
   
    # The second half also moves between 47 and 48, continuing the same unstable chromatic feeling.

    [48, 49, 48, 49,
     47, 48, 47, 48],


    # Variation 2 - Dark Chromatic Descent

    # This variation has more downward movement.

    # Notes such as:
    # 48 -> 47 -> 46 create a darker descending direction.

    # The melody later rises slightly again,preventing it from becoming completely predictable.
    # This creates a dark but still unstable result.

    [48, 47, 48, 46,
     47, 48, 49, 48],


    # Variation 3 - Unstable but Connected
    # This version changes direction frequently:
    # 47 -> 48 -> 49 -> 48
    # 47 -> 46 -> 48 -> 47
    # The melody moves up and down, but the pitch intervals stay small.
    # This keeps the music connected while still sounding uncertain and unstable.

    [47, 48, 49, 48,
     47, 46, 48, 47]
]


# Rhythm Variations


# "duration_variations" controls how long each note is played.
#
# Instead of using large rests, rhythmic instability is now created mainly through different note lengths.
#
# This makes the music more continuous while still avoiding a predictable rhythm.
#
# Short values such as:
# 0.5 beats create quick movement.
#
# Longer values such as: 1.5 or 2 beats create moments where tension is held for longer.
#
# The mixture of short and long durations prevents the rhythm from feeling regular.
#
# Each variation totals 8 beats.
#
# Because the phrase is repeated twice:
#
# 8 beats x 2 = 16 beats.

# "duration_variations" is also a nested list.
# It contains integer and floating-point values,
# such as 1 and 0.75.
#
# Each duration value corresponds to
# the pitch at the same list index.

duration_variations = [

    # Variation 1
    #
    # Alternates between medium and longer notes.
    #
    # This creates repeated pressure, with longer notes near the end holding the tension for more time.

    [0.75, 0.75, 1, 0.5,
     1, 1, 1.5, 1.5],


    # Variation 2
    # Uses several short and uneven durations.
    # The changing lengths make the phrase feel less predictable.

    [1, 0.5, 1, 0.5,
     1.5, 1, 1, 1.5],


    # Variation 3
    # Begins with shorter notes and finishes with longer sustained values.
    # This can make the phrase feel as if tension is gradually building and being held.

    [0.5, 1, 0.5, 1,
     0.75, 0.75, 1.5, 2]
]


# Dynamics / Velocity


# "tense_velocity" controls how strongly each note is played.
#
# The values range approximately from 72 to 96.
#
# These values are stronger than the Calm track.
#
# The velocity also changes from note to note, instead of remaining constant.
#
# This creates dynamic contrast.
#
# Stronger notes can feel more sudden and aggressive, while weaker notes create contrast before the next strong note arrives.
#
# The later notes become stronger, helping create a sense of increasing pressure.

# "tense_velocity" is a list of integer values.
# Each value controls the velocity
# of the note at the same list index.

tense_velocity = [
    72, 78, 82, 88,
    84, 92, 96, 88
]



# Control Variables


# "variation" selects which Tense melody and rhythmic pattern will be used.
# Python lists start counting from 0.
# Therefore:
# variation = 0
# selects Chromatic Pressure

# variation = 1
# selects Dark Descent

# variation = 2
# selects Connected Instability

# By changing only this value, I can create a different Tense outcome without rewriting the whole program.
# "variation" is an integer variable
# and its value is used as a list index.

variation = 2


# "repeat_times" controls how many times
# the selected 8-beat phrase is repeated.
# repeat_times = 2
# means:
# 8 beats x 2 = 16 beats.

repeat_times = 2
# "repeat_times" is an integer variable.
# It controls how many times the selected lists are repeated.

# "filter_frequency" controls the low-pass filter cutoff.

# A lower filter frequency reduces some high-frequency brightness and makes the sound darker.

# This supports the Tense mood by preventing the sound from becoming too bright.

# "filter_frequency" is an integer variable.
# Its value is passed into the low-pass effect
# as the cutoff frequency.
filter_frequency = 1200



# Select the Variation


# These two lines connect the selected variation number to the correspondingpitch and duration lists.



tense_notes = tense_variations[variation]

tense_duration = duration_variations[variation]


# Build the 16-beat Phrase

# Multiplying each list by repeat_times repeats the selected pattern.
# In Python, multiplying a list by an integer repeats its contents.
# Because repeat_times = 2,
# each 8-item list becomes a 16-item list.

# Pitch, duration and velocity are all repeated in the same way, so they remain aligned.
# Each 8-beat phrase is repeated twice, creating a total 16-beat structure.

notes = tense_notes * repeat_times
durations = tense_duration * repeat_times
velocities = tense_velocity * repeat_times


# Generate Tense Music


# The low-pass filter is applied around the entire musical phrase.
# This reduces high-frequency brightness and makes the overall sound darker.

# "with lowpass(...)" creates an effect block.
# Every note played inside this indented block
# receives the low-pass effect
with lowpass(frequency = filter_frequency):


    # A pitch bend effect is also applied across the complete 16-beat phrase.
    # The bend values are:
    # 0, 40, -30, 60, 0 cents
    # These are intentionally smaller than the Week 10 version.

    # The purpose is not to create an obvious "bending" sound.
    # Instead, it adds subtle pitch instability across the phrase.
    # This helps the music feel slightly unsettled.

# "with bend(...)" creates another effect block
# inside the low-pass block.

# Therefore, the notes inside it receive
# both low-pass filtering and pitch bend.
    with bend(
        cents = [0, 40, -30, 60, 0],
        beats = 16
    ):


        # The for loop moves through every note in the 16-beat phrase.
        #
        # "i" represents the current position in the lists.
        
        # notes[i]
        # selects the current pitch.
        
        # durations[i]
        # selects the matching note length.
        
        # velocities[i]
        # selects the matching dynamic level.

        # len(notes) returns the number of items in the list.

        
 # In this version, len(notes) = 16.

# range(0, 16) creates the index values from 0 to 15.
# During each loop, "i" is an integer
# representing the current list position.
#
# The same index is used to match:
# notes[i], durations[i] and velocities[i].
        for i in range(0, len(notes)):


            # playNote() combines
            # the pitch, duration and velocity into one musical event.
            #
            # The loop repeats this process until all notes are played.
            #
            # There are no regular rests between the notes in this version.
            #
            # This helps the melody stay continuous and creates more sustained pressure.

            playNote(
                notes[i],
                beats = durations[i],
                velocity = velocities[i]
            )
# CALM MOOD 
# Controlled Variation

# Goal:
# Create a richer Calm melody while keeping the movement slow, smooth and gentle.
# Finalise the notes 

# Calm Variations


# "calm_variations" stores three different melodic versions of the Calm mood.
# Each variation contains 8 MIDI note values.
# The notes stay within a relatively limited range, mainly between MIDI 57 and 64.
# Keeping the pitch range limited helps avoid dramatic jumps or sudden melodic movement.
# Each variation changes the direction of the melody, but all three follow the same Calm design rules.
# This allows the program to create different musical outcomes without changing the overall emotion.
# "calm_variations" is a nested list, or a list of lists.
# The outer list stores three different melodic variations.
# Each inner list stores 8 integer values.
# These integer values represent MIDI pitches.

# For example:
# calm_variations[0]
# selects the first complete melody.

# calm_variations[0][0]
# selects the first MIDI note of the first melody.
#
# Using a nested list allows several melodies
# to be stored inside one variable and selected by index.
calm_variations = [

    # Variation 1 - Gentle Wave
    
    # Notes:
    # 57 -> 60 -> 62 -> 60
    # 57 -> 60 -> 62 -> 60
    
    # The melody gradually rises and falls within
    # a small pitch range.
    # This repeated wave-like shape creates
    # a stable and predictable feeling.
    # Because there are no large jumps, 
    # the melody remains gentle rather than dramatic.

    [57, 60, 62, 60,
     57, 60, 62, 60],


    # Variation 2 - Soft Descent

    # Notes:
    # 64 -> 62 -> 60 -> 57
    # 60 -> 59 -> 57 -> 60

    # This variation starts slightly higher and gradually moves downward.

    # The descending movement creates a settling and relaxing feeling.
    
    # The second half introduces smaller movement before gently returning upward at the end.
    
    # This keeps the melody expressive without becoming too active.

    [64, 62, 60, 57,
     60, 59, 57, 60],


    # Variation 3 - Floating
    # Notes:
    # 57 -> 60 -> 62 -> 60
    # 64 -> 62 -> 60 -> 57

    # This variation changes direction more often.
    # It rises, returns, rises again, and then gradually moves downward.
    # The direction feels slightly less predictable, which creates a floating musical quality.
    # The movement still stays within a limited pitch range, so the result remains calm and controlled.

    [57, 60, 62, 60,
     64, 62, 60, 57]
]


# Rhythm Variations


# "duration_variations" controls how long each note is played.

# Each melodic variation has its own matching rhythm pattern.
# Most note durations are between: 1.5 and 2.5 beats.

# These relatively long durations reduce musical activity and make the melody feel slower.
#
# The durations are not all identical.
# Slight changes in note length create a more natural and expressive phrase instead of a completely mechanical rhythm.

# Each complete duration variation totals 16 beats.

# Therefore, the Calm phrase already lasts 16 beats and does not need to be repeated.
# "duration_variations" is also a nested list.
#
# Each inner list contains 8 numerical values.
# These values are integers or floating-point numbers,
# such as 2 and 2.5.
#
# Each value corresponds to the note
# at the same index in calm_variations.
#
# For example:
# calm_notes[0] uses calm_duration[0]
# calm_notes[1] uses calm_duration[1]
#
# This keeps the pitch and duration data aligned.
duration_variations = [

    # Variation 1 - Gentle Wave
    #
    # The 2.5-beat notes create
    # longer moments of stability.
    #
    # The shorter 1.5-beat notes
    # allow the melody to continue moving
    # without becoming too slow.
    #
    # Total duration = 16 beats.

    [2.5, 1.5, 2, 2,
     2.5, 1.5, 2, 2],


    # Variation 2 - Soft Descent
    # This rhythm uses a combination of 2, 1.5 and 2.5 beat durations.
    # The longer 2.5-beat notes help hold important parts of the descending phrase.
    # Total duration = 16 beats.

    [2, 2, 1.5, 2.5,
     2, 2, 1.5, 2.5],


    # Variation 3 - Floating

    # This rhythm changes between 1.5, 2 and 2.5 beat durations.
    
    # The changing note lengths make the phrase feel more fluid, while the overall rhythm remains slow.

    # Total duration = 16 beats.

    [2.5, 2, 1.5, 2,
     2.5, 1.5, 2, 2]
]


# Dynamics / Velocity


# "calm_velocity" controls how strongly each note is played.
# The velocity values are very low: approximately 24 - 32.
# Low velocity helps the melody sound:
# softer
# gentler
# less aggressive
# less energetic

# This is important because the Calm mood should feel quieter than the Happy and Tense moods.

# The velocity values are not completely identical.
# Small dynamic changes help the melody feel expressive without making it sound dramatic or energetic.
# "calm_velocity" is a list of integer values.
#
# Each integer controls the velocity
# of the note at the same list position.
#
# For example:
# calm_velocity[0] = 26
# controls the first note,
#
# while calm_velocity[7] = 24
# controls the eighth note.
#
# This list has the same number of items
# as calm_notes and calm_duration,
# so pitch, duration and velocity can be matched by index.
calm_velocity = [
    26, 30, 32, 28,
    26, 31, 29, 24
]


# Control Variables


# "variation" selects which melodic and rhythm variation will be used.

# Python lists begin counting from 0.
# Therefore:
# variation = 0
# selects Gentle Wave

# variation = 1
# selects Soft Descent

# variation = 2
# selects Floating

# "variation" is an integer variable.
#
# Its integer value is used as a list index.
#
# Because Python list indexing starts from 0:
# 0 means the first item,
# 1 means the second item,
# 2 means the third item.
#
# Therefore, variation = 1
# tells the program to select
# the second melody and rhythm variation.

variation = 1


# "filter_frequency" controls the cutoff frequency of the low-pass filter.

# A low-pass filter reduces some high-frequency brightness.

# Using a frequency of 1000 makes the sound softer and warmer, which supports the Calm character.

filter_frequency = 1000


# Select the Chosen Variation


# These lines connect the control variable with the corresponding melody and rhythm lists.
#


# calm_variations[1]
# = Soft Descent melody

# and:

# duration_variations[1]
# = Soft Descent rhythm.

# This ensures that the selected melody and its matching duration pattern are used together.

calm_notes = calm_variations[variation]

calm_duration = duration_variations[variation]


# Generate Calm Music


# The selected phrase already lasts 16 beats.

# Unlike some earlier versions, there are no regular rest() commands between each note.

# Removing these rests helps avoid a stop-start feeling.

# Instead of:
# note -> silence -> note -> silence

# the notes move directly from one to the next.



# The low-pass filter is applied to the complete Calm phrase.
#
# This reduces some high-frequency brightness and creates a softer overall timbre.

with lowpass(frequency = filter_frequency):


    # The for loop moves through every note in the selected Calm variation.

    # "i" represents the current position
    # in the lists.

    # For each value of i:
    # calm_notes[i]
    # selects the current pitch.

    # calm_duration[i]
    # selects the matching duration.
    
    # calm_velocity[i]
    # selects the matching velocity.
    
    # This allows pitch, rhythm and dynamics to work together as one musical phrase.
# len(calm_notes) returns the number of items
# stored in the calm_notes list.
#
# In this version:
# len(calm_notes) = 8.
#
# range(0, len(calm_notes))
# therefore creates the index values:
#
# 0, 1, 2, 3, 4, 5, 6, 7.
#
# During each loop, "i" is an integer
# representing one list position.
#
# The same value of "i" is used
# to read pitch, duration and velocity.
#
# For example, when i = 2:
#
# calm_notes[2]
# selects the third pitch,
#
# calm_duration[2]
# selects the third duration,
#
# calm_velocity[2]
# selects the third velocity.
#
# This keeps all three musical parameters synchronised.
    for i in range(0, len(calm_notes)):


# playNote() plays the current note using the selected pitch, duration and velocity.
        
# sustain = 0.4 allows the note to ring slightly longer.
# The playNote() function receives several parameters:

# calm_notes[i]
# is an integer MIDI pitch.

# beats = calm_duration[i]
# receives an integer or floating-point duration value.

# velocity = calm_velocity[i]
# receives an integer velocity value.

# sustain = 0.4
# uses a floating-point value.

# These different data values are combined
# by playNote() to control how each musical note sounds.

        playNote(
            calm_notes[i],
            beats = calm_duration[i],
            velocity = calm_velocity[i],
            sustain = 0.4
        )
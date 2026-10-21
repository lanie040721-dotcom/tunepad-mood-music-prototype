# CHINESE-STYLE CALM DREAMY PAD 
# Chinese-inspired atmospheric supporting layer

# Goal:
# Create a soft, smooth and spacious background that supports the main Calm melody.
# Finalise the notes

# Dreamy Pad was selected because it creates a softer and more atmospheric texture, which is more suitable for the Calm mood.

# The Pad is not designed to act as another main melody.
#
# Instead, it works as a slow background layer that adds depth and Chinese-inspired colour.
#
# The main musical design rules are:

# pentatonic-style pitch material
# limited pitch movement
# long sustained notes
# very low velocity
# no regular rests
#soft low-pass filtering
#
# These features help the Pad remain gentle, continuous and unobtrusive.



# Chinese-inspired Pitch Material


# The Pad uses pentatonic-style pitch material:

# G - A - C - D - E

# MIDI notes:
# 55 - 57 - 60 - 62 - 64
#
# This limited set of notes is used to create a Chinese-inspired musical colour.
#
# The pitch range is also relatively limited, which helps avoid large melodic jumps.
#
# This is important for the Calm mood, because large or sudden pitch changes could make the music feel too active.


# Chinese-inspired Variations


# "pad_variations" stores three different pitch patterns for the Calm Pad.

# "pad_variations" is a nested list, or a list of lists.
# Each inner list contains four integer MIDI pitch values.
# This allows several pitch patterns to be stored
# inside one variable and selected by index.

# Each variation contains only four notes.

# This is intentional.

# The main Calm melody already contains more melodic movement and detail.
#
# The Pad therefore uses fewer notes and much longer durations.
#
# This allows it to remain in the background instead of competing with the main melody.
#
# The three variations change pitch direction, while keeping the same slow and gentle character.

pad_variations = [

    # Variation 1 - Gentle Rise
    
    # Notes:
    # 55 -> 57 -> 60 -> 62
    
    # This variation gradually moves upward.
    
    # The movement is slow and controlled, creating a gentle lifting feeling  without becoming energetic.
    
    # Because each note is sustained for a long time, the rising movement still feels calm.

    [55, 57, 60, 62],


    # Variation 2 - Soft Descent
    
    # Notes:
    # 62 -> 60 -> 57 -> 55
    
    # This variation gradually moves downward.
    
    # Descending pitch movement can create a sense of settling and relaxation.
    #
    # This variation works particularly well with the main Calm "Soft Descent" variation.

    [62, 60, 57, 55],


    # Variation 3 - Floating
    
    # Notes:
    # 57 -> 60 -> 55 -> 57
   
    # This pattern changes direction gentlyinstead of only rising or falling.
    #
    # The less direct movement creates a floating and atmospheric feeling.
    #
    # The long note durations prevent the changing direction from sounding too active.

    [57, 60, 55, 57]
]


# Control Variable


# "variation" selects which Pad pattern will be used.

# Python lists begin counting from 0.

# Therefore:
# variation = 0
# selects Gentle Rise

# variation = 1
# selects Soft Descent

# variation = 2
# selects Floating

# "variation" is an integer variable.
# Its value is used as a list index.



# "variation" is an integer variable.
# Its value is used as a list index.



variation = 1


# This line uses the value of "variation" to select one complete Pad pattern.

pad_notes = pad_variations[variation]



# Rhythm


# Each Pad note lasts for 4 beats.
# There are four notes in total:
# 4 beats x 4 notes = 16 beats

# This matches the total length of the main Calm Week 11 track.

# The long duration of each Pad note creates a slow and sustained texture.
# There are no regular rests between notes.


# One Pad note moves directly into the next note
# "pad_duration" is a list containing four integer values.
#
# Each value corresponds to one note
# at the same position in pad_notes.
#
# For example:
# pad_notes[0] uses pad_duration[0] = 4 beats.
#
# Therefore:
# 4 + 4 + 4 + 4 = 16 beats.

pad_duration = [
    4, 4, 4, 4
]


# Dynamics / Velocity


# "pad_velocity" controls how strongly each Pad note is played.

# The values are intentionally very low: approximately 16 - 22.
#
# The main Calm melody uses stronger velocity values than this.
#
# This difference ensures that:
# Main Calm melody
# = foreground

# Dreamy Pad
# = background

# The Pad should be audible, but it should not attract more attention than the main melody.
#
# Small changes in velocity prevent the sustained notes from sounding completely static.

# "pad_velocity" is a list of integer values.
# Each value controls the velocity
# of the Pad note at the same list index.
#
# pad_notes, pad_duration and pad_velocity
# all contain four items, so they can be matched by index.

pad_velocity = [
    18, 22, 20, 16
]


# Generate Pad Layer


# A low-pass filter is applied around the complete Pad layer.

# Low-pass filtering reduces some high-frequency brightness.



# A frequency of 900 is used to keep the Dreamy Pad gentle and suitable for the Calm mood.

with lowpass(frequency = 900):
# "with lowpass(...)" creates an effect block.
# Every note played inside this indented block
# receives the low-pass effect.

# The integer value 900 is the filter cutoff frequency.

    # The for loop moves through all four Pad notes.
    
    # "i" represents the current position in the lists.
    
    # pad_notes[i]
    # selects the current pitch.
    
    # pad_duration[i]
    # selects how long the note lasts.
    
    # pad_velocity[i]
    # selects how strongly the note is played.

# len(pad_notes) returns the number of items in the list.
# In this case, len(pad_notes) = 4.
#
# range(0, 4) creates the index values:
# 0, 1, 2, 3.
#
# During each loop, "i" is an integer
# representing the current list position.
#
# The same index is used to select
# the matching pitch, duration and velocity.

    for i in range(0, len(pad_notes)):


        # playNote() generates each Pad note.

        # Each note is:
        # long
        # soft
        # sustained

        # sustain = 0.8
        # allows each note to ring longer.

    
        playNote(
            pad_notes[i],
            beats = pad_duration[i],
            velocity = pad_velocity[i],
            sustain = 0.8
        )
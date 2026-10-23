# CHINESE-STYLE TENSE LOFI PAD 
# Chinese-inspired atmospheric supporting layer

# Goal:
# Create a soft, dark and continuous background that supports the Tense mood without competing with the main melody.
# Finalise the notes 

# The Lofi Pad is used as an atmospheric layer rather than a second melody.
#
# The main design rules are:
# pentatonic-style pitch material
# relatively low register
# very long note durations
# no regular rests
# very low velocity
# dark low-pass filtering
# gentle sustain

# The main Tense melody is responsible for chromatic instability, irregular rhythm and pressure.

# The Pad is responsible for atmosphere, depth and Chinese-inspired colour.


# Chinese-inspired Pitch Material


# The Pad uses a pentatonic-style pitch set:
# G - A - C - D - E
# MIDI notes:
# 55 - 57 - 60 - 62 - 64
# This pitch material is different from the main Tense melody.

# The main Tense melody mainly uses:
# 46 - 49

# while the Pad stays slightly higher:
# 55 - 64

# This separation helps the two layers avoid competing in exactly the same pitch range.

# The Pad remains lower than the previous Strings layer, helping reduce brightness and harshness.


# Chinese-inspired Variations


# "pad_variations" stores three different
# atmospheric pitch patterns.

# Each variation contains only four notes.

# This is intentional.

# The main Tense melody is already active and contains more rhythmic movement.

# The Pad therefore uses fewer notes so that it stays slow and supportive.

# The three variations change pitch direction, but all keep the same dark and spacious character.

pad_variations = [

    # Variation 1 - Dark Suspended
    
    # Notes:
    # 55 -> 57 -> 60 -> 57
    
    # This pattern rises slowly and then returns downward.
    
    # The movement is gentle and limited, creating a suspended feeling rather than a clear melodic destination.
   
    # This helps maintain uncertainty without adding too much activity.

    [55, 57, 60, 57],


    # Variation 2 - Slow Falling
    
    # Notes:
    # 62 -> 60 -> 57 -> 55
    
    # This version gradually moves downward.
    
    # Descending pitch movement helps create a darker and heavier atmosphere.
    # It works well with the Tense mood because the phrase feels as if it is slowly sinking.

    [62, 60, 57, 55],


    # Variation 3 - Floating
    
    # Notes:
    # 57 -> 60 -> 55 -> 57
    
    # The direction changes gently instead of moving only upward or downward.
    
    # This creates a floating and slightly uncertain atmosphere.
    
    # Because the notes are still held for a long time, the pattern remains smooth rather than busy.

    [57, 60, 55, 57]
]



# Control Variable


# "variation" selects which Pad pattern will be used.

# Python lists begin counting from 0.

# Therefore:

# variation = 0
# selects Dark Suspended

# variation = 1
# selects Slow Falling

# variation = 2
# selects Floating

# Changing this number produces a different atmospheric result  without rewriting the whole code.
# "variation" is an integer variable.
# Its value is used as a list index.
#


variation = 2


# This line uses the selected variation number to choose one complete Pad pattern.


pad_notes = pad_variations[variation]



# Rhythm


# Each Pad note lasts for 4 beats.
# There are four notes in total:
# 4 beats x 4 notes = 16 beats
# This matches the total length of the main Tense Week 11 track.

# The long durations help the Pad sound smooth and continuous.

# There are no regular rests between notes.

# This was an important Week 11 refinement, because the previous version sounded too stop-start and disconnected.
#
# The Pad now behaves more like a sustained background texture.

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
#
# The values are intentionally very low:
# 18 - 24
#
# The main Tense melody uses much stronger velocity values around 72 - 96.
#
# This large difference is intentional.
# It ensures that:
# Main Tense melody
# = foreground

# Lofi Pad
# = background atmosphere

# The Pad should be noticeable, but it should not become the main focus.
#
# Small changes between the velocity values help the layer avoid sounding completely static.
# "pad_velocity" is a list of integer values.
# Each value controls the velocity
# of the Pad note at the same list index.

pad_velocity = [
    20, 24, 22, 18
]


# Generate Pad Layer


# A low-pass filter is applied to the entire Pad layer.
#
# Low-pass filtering reduces high-frequency brightness.
#
# This helps the Lofi Pad sound:
# darker
# softer
# less sharp
# less prominent

# A frequency of 850 is intentionally low because the Tense supporting layer should feel darker than the Happy or Calm background layers.

# "with lowpass(...)" creates an effect block.
# Every note played inside this indented block
# receives the low-pass effect.
#
# 850 is an integer value representing
# the filter cutoff frequency.
with lowpass(frequency = 850):


    # The for loop moves through all four Pad notes.
    
    # "i" represents the current position in the lists.
    
    # pad_notes[i]
    # selects the current pitch.
    
    # pad_duration[i]
    # selects how long the note lasts.
    
    # pad_velocity[i]
    # controls the dynamic level.

    # len(pad_notes) returns the number of items in the list.
# In this case, len(pad_notes) = 4.
#
# range(0, 4) creates the index values:
# 0, 1, 2, 3.
#
# During each loop, "i" is an integer
# representing the current list position.
#
# The same index is used to match:
# pad_notes[i], pad_duration[i] and pad_velocity[i].

    for i in range(0, len(pad_notes)):


        # playNote() generates each Pad note.
        
        # The notes are long and quiet, so they form a background texture rather than a separate melody.
        
        # sustain = 0.5
        # allows each note to ring slightly longer than its written duration.
        #
        # This helps connect the notes and creates a smoother transition between each Pad sound.

        playNote(
            pad_notes[i],
            beats = pad_duration[i],
            velocity = pad_velocity[i],
            sustain = 0.5
        )

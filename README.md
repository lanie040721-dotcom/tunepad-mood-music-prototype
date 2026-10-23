# TunePad Mood Music Prototype

## Overview

This project is an emotion-based music prototype based on TunePad and Python. It mainly explores how to express different musical emotions through structures such as pitch, duration, intensity, loops, indices, nested lists, and sound effects in the code.

The project includes three emotions: calm, happy, and tense. Each emotion has a main melody and a supporting layer. It creates corresponding auditory effects using different musical rules.

- `Calm/calm_main.py`: Main melody code for calm, which mainly uses longer durations, lower intensity, and gentle musical variations.
- `Calm/calm_dreamy_pad.py`: Dreamy Pad supporting layer for Calm section.
- `Happy/happy_main.py`: Main melody code for Happy, which mainly uses brighter pitches, shorter durations and swing.
- `Happy/happy_dreamy_pad.py`: Dreamy Pad and chord background layer for Happy section.
- `Tense/tense_main.py`: Main melody code for Tense, which mainly uses lower pitch ranges, semitone movements, and bends.
- `Tense/tense_lofi_pad.py`: Tense’s Lofi Pad supporting layer.

## Main Function

The project uses lists to store pitch, duration and velocity and connects the data using the same index. Then, a for loop is used to play the whole music automatically. Both the main melody and the supporting layer have different controlled variations. Users can choose different versions by changing variation to 0, 1, or 2, while keeping the same emotional rules.

## Environment

This project was developed and tested in TunePad’s Python-based coding environment. The code uses TunePad functions such as `playNote()`, `lowpass()`, `swing()`, `bend()` and so on. Thus, it is suggested to run it in the TunePad environment instead of using the standard Python interpreter directly.

## Audio Previews

This project provides the exported music files under Calm, Happy, and Tense emotions, respectively, when variation = 2, so it is convenient for the audience to test the final music effect.

- `Audio/Tense.mp3`: Tense music, with Lofi Pad as the background, so it creates a dark and unstable atmosphere.
- `Audio/Calm.mp3`: Calm music integrating with the Dreamy Pad background, so it creates a peaceful and gentle atmosphere.
- `Audio/Happy.mp3`: Happy music with the Dreamy Pad background, so it can create a good and positive musical effect.

All three audio files use variation = 2. Thus, it can demonstrate the combination effect of the main melody and supporting material using the same emotional rule.

These audio files are used to display the actual sound output only. Please refer to the Python code file to check the completed music logic, variations, lists, loops and variation settings.

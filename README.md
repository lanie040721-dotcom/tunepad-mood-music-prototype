# TunePad Mood Music Prototype

## Overview

This project is an emotion-based music prototype developed using TunePad and Python. It explores how musical emotions can be expressed through coding structures such as pitch, duration, velocity, variables, lists, loops, indexing, nested lists, and sound effects.

The project focuses on three emotional moods: **Calm, Happy, and Tense**. Each mood contains a main melody and a supporting musical layer. Different musical rules are used to create distinct auditory experiences while maintaining the intended emotional character.

## Project Structure

```text
tunepad-mood-music-prototype/
├── README.md
├── Calm/
│   ├── calm_main.py
│   └── calm_dreamy_pad.py
├── Happy/
│   ├── happy_main.py
│   └── happy_dreamy_pad.py
└── Tense/
    ├── tense_main.py
    └── tense_lofi_pad.py
```

### 1. Calm

- `Calm/calm_main.py`: Contains the main Calm melody. It uses longer note durations, lower velocity, gentle pitch movement, and soft filtering to create a peaceful atmosphere.
- `Calm/calm_dreamy_pad.py`: Provides a soft Dreamy Pad supporting layer with sustained notes and gentle musical movement.

### 2. Happy

- `Happy/happy_main.py`: Contains the main Happy melody. It uses brighter pitches, shorter note durations, stronger velocity, repetition, and swing to create a lively and positive mood.
- `Happy/happy_dreamy_pad.py`: Provides a Dreamy Pad chord layer that adds bright harmony while remaining softer than the main melody.

### 3. Tense

- `Tense/tense_main.py`: Contains the main Tense melody. It uses a lower pitch range, chromatic movement, dynamic contrast, and pitch-bending effects to create tension and instability.
- `Tense/tense_lofi_pad.py`: Provides a dark and sustained Lofi Pad supporting layer that adds atmosphere without competing with the main melody.

## Main Features

### Structured Musical Data

Lists store pitch, duration, and velocity values. The same index connects the corresponding values, allowing them to control individual musical events together.

### Loops and Repetition

`for` loops process musical data automatically, reducing repeated code and making the musical structure easier to maintain.

### Controlled Variation

Nested lists store different melodic or harmonic patterns. The integer variable `variation` selects a version using an index from `0` to `2`. This allows different musical outcomes while preserving the basic rules of each mood.

### Effects and Supporting Layers

TunePad effects, including `lowpass()`, `swing()`, and `bend()`, help shape the musical character. Supporting layers add harmonic depth and atmosphere to the main melodies.

## Environment and Execution

This project was developed and tested in TunePad's Python-based coding environment. It uses TunePad-specific functions such as `playNote()`, `lowpass()`, `swing()`, and `bend()`.

The code is intended to run in TunePad rather than directly in a standard Python interpreter. To hear the musical results, open the corresponding TunePad project and play the relevant cells.

## Project Goal

The goal of this project is to explore how code can organise musical data, establish creative rules, generate controlled variations, and produce different emotional outcomes through iterative testing and refinement.

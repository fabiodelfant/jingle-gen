# Jingle-Gen

## What it does

Creates a cool jingle in your favorite (limited) modes and keys!

## Motivation

Music theory is kind of diffiult. Ear training is even moreso. This aims to provide a tool to help students identify a variety of modes.

## Obstacles I encountered

Although a front end was written for this project, I ran into issues when attempting to bind script execution to front end button events. 

## Future Development

Beyond the scope of a hackathon, I'd like to properly write a front end UI. Additionally, I'd like to expand on this to generate songs 
with chords and logical progressions, potentially implemented with a probabilistic markov model based on frequencies of chord progressions
in actual music.

## How to use it 

Clone the repository and navigate to the directory. Then, run
```bash
python soundgen.py [key] [mode]
```
Where [key] and [mode] are chosen from:
`keys = ["a", "b", "c", "d", "e", "f", "g"]`
`modes = ["ionian", "dorian", "mixolydian", "locrian"]`

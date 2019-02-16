import numpy as np
import random
import simpleaudio as sa

# calculate note frequencies
from numpy.core._multiarray_umath import ndarray

A_freq = 440
Ash_freq = A_freq * 2 ** (1 / 12)
B_freq = A_freq * 2 ** (2 / 12)
C_freq = A_freq * 2 ** (3 / 12)
Csh_freq = A_freq * 2 ** (4 / 12)
D_freq = A_freq * 2 ** (5 / 12)
Dsh_freq = A_freq * 2 ** (6 / 12)
E_freq = A_freq * 2 ** (7 / 12)
F_freq = A_freq * 2 ** (8 / 12)
Fsh_freq = A_freq * 2 ** (9 / 12)
G_freq = A_freq * 2 ** (10 / 12)
Gsh_freq = A_freq * 2 ** (11 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.25
t = np.linspace(0, T, T * sample_rate, False)

# generate sine wave notes
A_note = np.sin(A_freq * t * np.pi)
Ash_note = np.sin(Ash_freq * t * np.pi)
B_note = np.sin(B_freq * t * np.pi)
C_note = np.sin(C_freq * t * np.pi)
Csh_note = np.sin(Csh_freq * t * np.pi)
D_note = np.sin(D_freq * t * np.pi)
Dsh_note = np.sin(Dsh_freq * t * np.pi)
E_note = np.sin(E_freq * t * np.pi)
F_note = np.sin(F_freq * t * np.pi)
Fsh_note = np.sin(Fsh_freq * t * np.pi)
G_note = np.sin(G_freq * t * np.pi)
Gsh_note = np.sin(Gsh_freq * t * np.pi)

AO_note = np.sin(A_freq * t * 2 * np.pi)
AshO_note = np.sin(Ash_freq * t * 2 * np.pi)
BO_note = np.sin(B_freq * t * 2 * np.pi)
CO_note = np.sin(C_freq * t * 2 * np.pi)
CshO_note = np.sin(Csh_freq * t * 2 * np.pi)
DO_note = np.sin(D_freq * t * 2 * np.pi)
DshO_note = np.sin(Dsh_freq * t * 2 * np.pi)
EO_note = np.sin(E_freq * t * 2 * np.pi)
FO_note = np.sin(F_freq * t * 2 * np.pi)
FshO_note = np.sin(Fsh_freq * t * 2 * np.pi)
GO_note = np.sin(G_freq * t * 2 * np.pi)
GshO_note = np.sin(Gsh_freq * t * 2 * np.pi)


def get_ionian_l(input_key):
    key = {"c": np.array((C_note, E_note, G_note, BO_note, CO_note)),
           "d": np.array((D_note, Fsh_note, AO_note, CO_note, D_note)),
           "e": np.array((E_note, Gsh_note, BO_note, DO_note, EO_note)),
           "f": np.array((F_note, AO_note, CO_note, DshO_note, FO_note)),
           "g": np.array((G_note, BO_note, DO_note, FO_note, GO_note)),
           "a": np.array((A_note, Csh_note, E_note, GO_note, AO_note)),
           "b": np.array((B_note, Dsh_note, Fsh_note, AO_note, BO_note))}
    return key[input_key]


def get_dorian_pa(input_key):
    key = {"c": np.array((C_note, E_note, G_note, AshO_note, CO_note)),
           "d": np.array((D_note, Fsh_note, AO_note, BO_note, D_note)),
           "e": np.array((E_note, Gsh_note, BO_note, CshO_note, EO_note)),
           "f": np.array((F_note, AO_note, CO_note, DO_note, FO_note)),
           "g": np.array((G_note, BO_note, DO_note, EO_note, GO_note)),
           "a": np.array((A_note, Csh_note, E_note, FshO_note, AO_note)),
           "b": np.array((B_note, Dsh_note, Fsh_note, GshO_note, BO_note))}
    return key[input_key]


def get_mixolydian(input_key):
    key = {"c": np.array((C_note, E_note, G_note, AshO_note, CO_note)),
           "d": np.array((D_note, Fsh_note, AO_note, BO_note, DO_note)),
           "e": np.array((E_note, Gsh_note, BO_note, CshO_note, EO_note)),
           "f": np.array((F_note, AO_note, CO_note, DO_note, FO_note)),
           "g": np.array((G_note, BO_note, DO_note, EO_note, GO_note)),
           "a": np.array((A_note, Csh_note, E_note, Fsh_note, AO_note)),
           "b": np.array((B_note, Dsh_note, Fsh_note, Gsh_note, BO_note))}
    return key[input_key]


def get_locrian(input_key):
    key = {"c": np.array((C_note, Dsh_note, Fsh_note, AshO_note, CO_note)),
           "d": np.array((D_note, F_note, Gsh_note, BO_note, DO_note)),
           "e": np.array((E_note, G_note, AshO_note, CshO_note, EO_note)),
           "f": np.array((F_note, Gsh_note, BO_note, DO_note, FO_note)),
           "g": np.array((G_note, AshO_note, CshO_note, EO_note, GO_note)),
           "a": np.array((A_note, C_note, Dsh_note, FshO_note, AO_note)),
           "b": np.array((B_note, D_note, E_note, GshO_note, BO_note))}
    return key[input_key]


# concatenate notes
def make(key, mode):
    x = {"ionian": get_ionian_l(key),
         "dorian": get_dorian_pa(key),
         "mixolydian": get_mixolydian(key),
         "locrian": get_locrian(key)}
    c = x[mode]
    a = np.array((c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)],
                  c[random.randint(0, len(c))]))
    b = np.array((c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)],
                  c[random.randint(0, len(c))]))
    d = np.array((c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)], c[random.randint(0, len(c) - 1)],
                  c[random.randint(0, len(c))]))
    return np.vstack((a, b, a, d))


audio = make("c", "mixolydian")

# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)
wave_obj = sa.WaveObject(audio, 1, 2, sample_rate)
# start playback
play_obj = wave_obj.play()
# wait for playback to finish before exiting
play_obj.wait_done()

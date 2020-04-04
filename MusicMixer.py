# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:29:54 2020

@author: jkc11
"""

import numpy as np
import wave
import struct

class Song:
    adc_max = 16000

    def __init__(self,frame_rate=48000.0,n_channels=2,sampwidth=2,comptype="NONE",compname="not compressed"):
        self.frame_rate = frame_rate
        self.frames = np.array([])
        self.n_channels = n_channels
        self.sampwidth = sampwidth
        self.comptype = comptype
        self.compname = compname

    def getnframes(self):
        return len(self.frames)
        
    def load_song(self,name):
        with wave.open(name, 'r') as wave_file:
            data = wave_file.readframes(wave_file.getnframes())
            self.frames = struct.unpack("{0}h".format(wave_file.getnframes()),data)
            self.frame_rate = wave_file.getframerate()
            self.n_channels = wave_file.getnchannels()
            self.sampwidth = wave_file.getsampwidth()
            self.comptype = wave_file.getcomptype()
            self.compname = wave_file.getcompname()
            
    def save_song(self,name):
        with wave.open(name, 'w') as wave_file:
            wave_file.setparams((self.n_channels, self.sampwidth, int(self.frame_rate), self.getnframes(), self.comptype, self.compname))
            frames = [int(frame*Song.adc_max) for frame in self.frames]
            data = struct.pack("{0}h".format(self.getnframes()),*frames)
            wave_file.writeframes(data)

    def add_tone(self, frequency, t1, t2, amplitude=1, transition=None, transition_length=0.25):
        start_frame = int(t1*self.frame_rate)
        end_frame = int(t2*self.frame_rate)
        if self.getnframes() < end_frame:
            self.frames = np.append(self.frames,np.zeros(end_frame-self.getnframes()))
        tone = np.array([amplitude*np.sin(2*np.pi*frequency*x/self.frame_rate) for x in range(end_frame-start_frame)])
        trans_frame_length = int(transition_length*self.frame_rate)
        if transition == 'Linear':
            tone[:trans_frame_length] *= np.linspace(0,1,trans_frame_length)
            tone[-trans_frame_length:] *= np.linspace(1,0,trans_frame_length)
        self.frames[start_frame:end_frame] += tone

    def add_note(self, note, t, amplitude=1):
        notes = {'E2':82.41,'A2':110.00,'D3':146.83,'G3':196.00,'B3':246.94,'E4':329.63}
        self.add_tone(notes[note],t,t+2,amplitude=amplitude,transition='Linear')

    def add_chord(self, chord, t):
        chords = {'C':['A2','D3','B3'],'F':['E2','A2','D3','G3','B3','E4'],'A':['D3','G3','B3'],'D':['G3','B3','E4'],'G':['E2','A2','E4'],'E':['A2','D3','G3']}
        for note in chords[chord]:
            self.add_note(note,t,amplitude=1/len(chords[chord]))
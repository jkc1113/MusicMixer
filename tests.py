from MusicMixer import Song

if __name__ == "__main__":
    test_song = Song()
    test_song.add_tone(500,0,2)
    test_song.save_song("test1.wav")
    test_song.add_tone(300,2,3)
    test_song.add_tone(700,3,4)
    test_song.save_song("test2.wav")
    test_song.add_tone(300,4,7,amplitude=1/3)
    test_song.add_tone(500,5,7,amplitude=1/3)
    test_song.add_tone(700,6,7,amplitude=1/3)
    test_song.save_song("test3.wav")
    test_song = Song()
    test_song.add_tone(500,0,2,transition='Linear')
    test_song.add_tone(300,2,3,transition='Linear')
    test_song.add_tone(700,3,4,transition='Linear')
    test_song.add_tone(300,4,7,amplitude=1/3,transition='Linear')
    test_song.add_tone(500,5,7,amplitude=1/3,transition='Linear')
    test_song.add_tone(700,6,7,amplitude=1/3,transition='Linear')
    test_song.save_song("test4.wav")
    test_song = Song()
    test_song.add_note('E2',0)
    test_song.add_note('A2',2)
    test_song.add_note('D3',4)
    test_song.add_note('G3',6)
    test_song.add_note('B3',8)
    test_song.add_note('E4',10)
    test_song.save_song("notes.wav")
    test_song = Song()
    test_song.add_chord('C',0)
    test_song.add_chord('F',2)
    test_song.add_chord('A',4)
    test_song.add_chord('D',6)
    test_song.add_chord('G',8)
    test_song.add_chord('E',10)
    test_song.save_song("chords.wav")

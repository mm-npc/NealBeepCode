from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(5))

tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

#song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]

# 88 Freq
# 8 Categories
# 11 freq per category

# Categories:
cat1 = [ 'B0',  'C1',  'CS1', 'D1',  'DS1', 'E1',  'F1',  'FS1', 'G1',  'GS1', 'A1' ]
cat2 = [ 'AS1', 'B1',  'C2',  'CS2', 'D2',  'DS2', 'E2',  'F2',  'FS2', 'G2',  'GS2']
cat3 = [ 'A2',  'AS2', 'B2',  'C3',  'CS3', 'D3',  'DS3', 'E3',  'F3',  'FS3', 'G3' ]
cat4 = [ 'GS3', 'A3',  'AS3', 'B3',  'C4',  'CS4', 'D4',  'DS4', 'E4',  'F4',  'FS4']
cat5 = [ 'G4',  'GS4', 'A4',  'AS4', 'B4',  'C5',  'CS5', 'D5',  'DS5', 'E5',  'F5' ]
cat6 = [ 'FS5', 'G5',  'GS5', 'A5',  'AS5', 'B5',  'C6',  'CS6', 'D6',  'DS6', 'E6' ]
cat7 = [ 'F6',  'FS6', 'G6',  'GS6', 'A6',  'AS6', 'B6',  'C7',  'CS7', 'D7',  'DS7']
cat8 = [ 'E7',  'F7',  'FS7', 'G7',  'GS7', 'A7',  'AS7', 'B7',  'C8',  'CS8', 'D8' ]

# :
rfSong =  [ "B0",  "E1",  "A1"  ]
lfSong =  [ "AS1", "DS2", "GS2" ]
mfSong =  [ "A2",  "D3",  "G3"  ]
hfSong =  [ "GS3", "CS4", "FS4" ]
vhfSong = [ "G4",  "C5",  "F5"  ]
uhfSong = [ "FS5", "B5",  "E6"  ]
shfSong = [ "F6",  "AS6", "DS7" ]
ehfSong = [ "E7",  "A7",  "D8"  ]


def playtone(frequency):
    buzzer.duty_u16(32768)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
            print(tones[mysong[i]])
        sleep(0.3)
    bequiet()
# playsong(song)

# def playsong():
#     for i in range(len(tones)):
#     #for i in range(3):
#         #tuple(tones.items())[i][1]
#         playtone(tuple(tones.items())[i][1])
#         print(str(tuple(tones.items())[i][0]) + ": " + str(tuple(tones.items())[i][1]))
#         #sleep(0.03)
#         sleep(3)
#     bequiet()
# #playsong()
    
# playtone(48)
# sleep(0.03)
# playtone(98)
# sleep(0.13)
# playtone(148)
# sleep(0.03)
# bequiet()
# 
# sleep(5)
# 
# playtone(200)
# sleep(0.03)
# playtone(300)
# sleep(0.13)
# playtone(400)
# sleep(0.03)
# bequiet()
# 
# sleep(5)
# 
# playtone(800)
# sleep(0.03)
# playtone(900)
# sleep(0.13)
# playtone(1000)
# sleep(0.03)
# bequiet()

# sleep(5)


# Level 1:
print("Level 1:")
playtone(208)
sleep(0.03)
playtone(277)
sleep(0.23)
playtone(370)
sleep(0.03)
bequiet()

sleep(5)
#


# Level 2:
print("Level 2:")
playtone(740)
sleep(0.03)
playtone(988)
sleep(0.23)
playtone(1319)
sleep(0.03)
bequiet()

sleep(5)
#


# Level 3:
print("Level 3:")
playtone(1397)
sleep(0.03)
playtone(1865)
sleep(0.23)
playtone(2489)
sleep(0.03)
bequiet()

sleep(5)
#



playsong(rfSong)
sleep(5)
playsong(mfSong)
sleep(5)
playsong(lfSong)
sleep(5)
playsong(hfSong)
sleep(5)
playsong(vhfSong)
sleep(5)
playsong(uhfSong)
sleep(5)
playsong(shfSong)
sleep(5)
playsong(ehfSong)
sleep(5)
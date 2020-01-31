#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    lyric = """NESHA BY ARMAN ALIF LYRICS
Tomar Neshay Poira
Ami Hoilam Dewana,
Tomar Jonno Haray Gelo
Amar Thikana...
Tomar Moto Thakla Tumi
Khobor Nila na,
Tomar Kajol Ronge Rangao
Tumi Kar Angina... ? - [ 2 ]

Aj Amar Vetor Jurei Jurei
Sudhu Neshar Bosobas..
Nesha Hasay - Neshai Kaday
Nai Ami Amar...
Roj Bikaler Moto
Tomay Ar To Dekhi na,
Ami Amar Motoi Thakbo Valo,
Khobor Nio na..

Thakte Hobe Tomay
Chhara Kotha Chhilo na,
Aj Vetor Ghore Dhoya Thake,
Tumi Thako na..
Amar Laal Ronga Hridpindo
Hoiteche Kalo,
Kolijata Jak Pure
Tobu Tumi Thako Valo.. - [ 2 ]

Aj Amar Vetor Jurei Jurei
Sudhu Neshar Bosobas..
Nesha Hasay - Neshai Kaday
Nai Ami Amar...
Roj Bikaler Moto
Tomay Ar To Dekhi na,
Ami Amar Motoi Thakbo Valo,
Khobor Nio na..

Ami Jeno Konodino
Cigarette na chhui,
Bolta Tumi Korta Shashon,
Lagto Re Valoi..
Aj Nicotine e Hoiche Kalo
Vetor Ghorer Sob,
Ekhon Shashon Kora Mayaboti
Koi gelo koi?.. - [ 2 ] 

Aj Amar Vetor Jurei Jurei
Sudhu Neshar Bosobas..
Nesha Hasay - Neshai Kaday
Nai Ami Amar...
Roj Bikaler Moto
Tomay Ar To Dekhi na,
Ami Amar Motoi Thakbo Valo,
Khobor Nio na.. - [ 2 ]"""

    speak(lyric)

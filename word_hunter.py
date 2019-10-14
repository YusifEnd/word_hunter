#!/usr/bin/env

import sys
import time
import sqlite3
import random


start = """
 -------    -----    ------
| START |  | NEW |  | EXIT |
 -------    -----    ------
"""

in_playing = """
  ------    -------    --------
 | EXIT |  | SCORE |  | TOP 10 |
  ------    -------    --------
"""


def loading():
    print('Loading')
    for i in range(10):
        print('>', end=' ')
        time.sleep(0.3)



nameless = ['pass', 'exit', 'sys', 'start']  # don't use for username :)
via = sqlite3.connect('oyun.db')
curs = via.cursor()

via_gamer = sqlite3.connect('gamer.db')
curs_gamer = via_gamer.cursor()

print('\t\t<:- SOZ OVCUSU -:>')
print(start)
time.sleep(0.5)


def add_table_gamer():
    curs_gamer.execute('CREATE TABLE IF NOT EXISTS gamer (user_name TEXT, sifre TEXT, point INT)')
    via_gamer.commit()


add_table_gamer()


def add_user(user_name, sifre,  point):
    curs_gamer.execute('INSERT INTO gamer VALUES(?, ?, ?)', (user_name, sifre, point))
    via_gamer.commit()


class Oyun(object):
    listx = []
    curs.execute("SELECT * FROM finds")
    for i in curs.fetchall():
        listx.append(*i)
    show = list(random.choice(listx))
    random.shuffle(show)

    def __init__(self):
        self.name = user
        self.password = parol
        self.player_point = 0
        self.tapdi = list()

    def main(self):
        print("\n", '*' * 30)
        print('\t\t', *self.show)
        while True:
            found = list() # soz_bazasi.baza_a
            curs.execute('SELECT * FROM words')
            for w in curs.fetchall():
                found.append(*w)
            answer = input('_>:')
            fltr = [True if hrf in self.show else False for hrf in answer]
            if answer in found:
                if answer in self.tapdi:
                    print('Bu söz artıq tapılıb ;-)')
                else:
                    self.tapdi.append(answer)
                    self.player_point += 1
                    print('DOĞRU CAVAB ...')
            elif answer not in found:
                if answer == 'exit':
                    print('Oyun sonlanir ...')
                    print('Bu oyunda siz {} xal qazandiniz ;)'.format(self.player_point))
                    curs_gamer.execute('SELECT point FROM gamer WHERE user_name=?', [self.name])
                    for i in curs_gamer.fetchone():
                        if i > self.player_point:
                            pass
                        elif i < self.player_point:
                            curs_gamer.execute('SELECT * FROM gamer')
                            curs_gamer.execute('UPDATE gamer SET point=? WHERE user_name=?', [self.player_point, self.name])
                            via_gamer.commit()
                    time.sleep(3)
                    sys.exit()
                elif answer == 'score':
                    curs_gamer.execute('SELECT * FROM gamer')
                    curs_gamer.execute('SELECT point FROM gamer WHERE user_name=?', [self.name])
                    for bal in curs_gamer.fetchone():
                        print('Topladiginiz en yuksek bal: ', bal)
                elif answer == 'top 10':
                    curs_gamer.execute('SELECT * FROM gamer ORDER BY point DESC LIMIT 10')
                    for i in curs_gamer.fetchall():
                        print(i[0], ':', i[2])
                elif not all(fltr):
                    print('Yazdiginiz sozde sertden kenar herf(ler) var !')
                else:
                    print('duz tapmadiniz')


while True:
    alo = input('\nSecdiyiniz bolmenin adini bura yazin_>:')
    if alo == 'exit':
        sys.exit()
    elif alo == 'start':
        while True:
            user = input('Oyuncu adinizi daxil edin: ').upper()
            parol = input('Oyuncu sifrenizi daxil edin: ')
            curs_gamer.execute('SELECT * FROM gamer WHERE user_name=? and sifre=?', (user, parol))
            datas = curs_gamer.fetchone()
            if datas:
                loading()
                print(in_playing)
                gamer = Oyun()
                gamer.main()
            else:
                print('Oyuncu adi ve ya sifresi sehvdir !')
    elif alo == "new":
        while True:
            user = input('Oyuncu adinizi teyin edin: ').upper()
            data = curs_gamer.execute('SELECT * FROM gamer WHERE user_name=?', [user])
            if len(user) == 0:
                print('Oyuncu adinizi qeyd etmediniz')
            elif user.lower() in nameless:
                print('Bu oyuncu adi ile qeydiyyat qadagandir !!!')
            elif bool(*data) is True:
                print('Bu oyuncu adi artiq istifade olunub. Xahis olunur basqa ad secin')
            else:
                while True:
                    parol = input('Oyuncu sifrenizi teyin edin: ')
                    if len(parol) < 6:
                        print('Sifrede en az 6 simvol olmalidir')
                    else:
                        loading()
                        print(in_playing)
                        add_user(user, parol, 0)
                        gamer = Oyun()
                        gamer.main()
    else:
        print('Xahis olunur acar sozu duzgun daxil edesiniz !')


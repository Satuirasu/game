import random


def perv():
    print('Вы просыпаетесь в лесу, так же вы слышите чей то голос, так же вы видите оленячто будете делать?')
    print('1: Пойти в глуш леса', '\n', '2: Остаться на месте', '\n', '3:Пойти на голос', '\n', ' 4: Пойти за оленем',
          '\n')


def glush():
    print('Вы пошли в глуш леса и видете дом в лесу ваши действия')
    print('1:Пойти в дом', '\n', '2:Пройти мимо', '\n')


def dom():
    print('Вы пошли в дом ')
    print('Дом кажется заброшенным ')
    print('1:Остаться в доме ', '\n', '2:Выйти из дома и продолжить путь', '\n')


def mimo():
    print('Идя по лесу вы замечаете речку')
    print('1:Пойти вниз по реке ', '\n', '2:Пойти вверх по реке', '\n')


def in_dom():
    print('Вы остались дома, однако через некоторое время хозяин дома возращяется домой с ружьем')
    print('Вы погибли')


def viyti():
    mimo()


def reka_verx():
    print('Вы пошли вверх по реке')
    print('Вам повезло вы вышли к поселению')
    print('Поздравляю вы успешно завершили квест')


def reka_vniz():
    print('Вы пошли вниз по реке,однако этот путь привел вас в болото ')
    print('Вы не смогли самостоятельно выбраться из болота')
    print('Вы погибли')


def ostalsa():
    print('Вы остались на месте,однако наступает ночь что будете делать')
    print('1:лечь спать ', '\n', '2:Не спать всю ночь', '\n')


def lesh():
    print('Вы легли спать, однако пока вы спали к вам пришла стая волков ')
    print('Вы погибли')


def ne_spal_nich():
    print('Вы не спали всю ночь, вы чувствуете усталость, а так же вы чувствуете сильный голод, вы видете куст незнакомых ягод ')
    print('1:Съесть незнакомые ягоды  ', '\n', '2: Потерпеть', '\n')


def cel():
    print('Вы съели незнакомые ягоды')
    print('Они оказались ядовитыми ')
    print('Вы погибли')


def ne_cel():
    print('Вы не стали есть ягоды')
    print('Из-за истощения вы погибли')


def poshel_na_golos():
    print('Вы  пошли на голос ')
    print('Это оказались разбойники, удача не на вашей стороне они вас заметили ')
    print('вы услышали их тайну')
    print('Вас убили')


def olen():
    print('Вы отправились за оленем, кажется олень настроен недружелюбно')
    print('1:Напасть на оленя', '\n', '2: Сбежать от оленя', '\n', '3: Оглядется по сторонам', '\n', '4: Попытаться напугать ', '\n')


def napal():
    print('Олень оказался сильнее вы мертвы')


def sbejat():
    print('Олень с легкостью вас догнал вы мертвы')


def ogladetsa():
    print('Вы оглядываетесь по сторонам')


def napugal():
    print('Вы решили попробовать напугать оленя')


def domitusha():
    print('Вы вошли в дом, в нем сидел лесник и чистил свое ружье')
    print('1:Отдать тушу леснику', '\n', '2:Вы не решаете отдать тушу леснику ', '\n')
def poslelesnika():
    print('После вы пошли по лесу и услышали чьи-то голоса')
    print('Вы спрятались в кусты ')
    print('1:Отступить', '\n', '2:Попытаться напасть', '\n')

while True:
    perv()
    try:
        otvet = int(input())
    except TypeError:
        print('Вы ввели не число')
        otvet = 0
    except ValueError:
        print('Вы ввели не число')
        otvet = 0
    except NameError:
        print('Вы ввели не число')
        otvet = 0
    if otvet == 1:
        glush()
        otvet = 0
        try:
            otvet = int(input())
        except TypeError:
            print('Вы ввели не число')
            otvet = 0
        except ValueError:
            print('Вы ввели не число')
            otvet = 0
        except NameError:
            print('Вы ввели не число')
            otvet = 0
        if otvet == 1:
            dom()
            otvet = 0
            try:
                otvet = int(input())
            except TypeError:
                print('Вы ввели не число')
                otvet = 0
            except ValueError:
                print('Вы ввели не число')
                otvet = 0
            except NameError:
                print('Вы ввели не число')
                otvet = 0
            if otvet == 1:
                in_dom()
                break
            elif otvet == 2:
                viyti()
                otvet = 0
                try:
                    otvet = int(input())
                except TypeError:
                    print('Вы ввели не число')
                    otvet = 0
                except ValueError:
                    print('Вы ввели не число')
                    otvet = 0
                except NameError:
                    print('Вы ввели не число')
                    otvet = 0
                if otvet == 2:
                    reka_verx()
                    break
                elif otvet == 1:
                    reka_vniz()
                    break
        elif otvet == 2:
            mimo()
            otvet = 0
            try:
                otvet = int(input())
            except TypeError:
                print('Вы ввели не число')
                otvet = 0
            except ValueError:
                print('Вы ввели не число')
                otvet = 0
            except NameError:
                print('Вы ввели не число')
                otvet = 0
            if otvet == 2:
                reka_verx()
                break
            elif otvet == 1:
                reka_vniz()
                break
    elif otvet == 2:
        ostalsa()
        otvet = 0
        try:
            otvet = int(input())
        except TypeError:
            print('Вы ввели не число')
            otvet = 0
        except ValueError:
            print('Вы ввели не число')
            otvet = 0
        except NameError:
            print('Вы ввели не число')
            otvet = 0
        if otvet == 1:
            lesh()
            break
        elif otvet == 2:
            ne_spal_nich()
            otvet = 0
            try:
                otvet = int(input())
            except TypeError:
                print('Вы ввели не число')
                otvet = 0
            except ValueError:
                print('Вы ввели не число')
                otvet = 0
            except NameError:
                print('Вы ввели не число')
                otvet = 0
            if otvet == 1:
                cel()
                break
            elif otvet == 2:
                ne_cel()
                break
    elif otvet == 3:
        poshel_na_golos()
        break
    elif otvet == 4:
        olen()
        otvet = 0
        try:
            otvet = int(input())
        except TypeError:
            print('Вы ввели не число')
            otvet = 0
        except ValueError:
            print('Вы ввели не число')
            otvet = 0
        except NameError:
            print('Вы ввели не число')
            otvet = 0
        if otvet == 1:
            napal()
            break
        elif otvet == 2:
            sbejat()
            break
        elif otvet == 3:
            ogladetsa()
            i = random.randrange(1, 100)
            if i <= 20:
                print('Вы нашли палку')
                print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n', '3: Махать палкой', '\n')
                otvet = 0
                try:
                    otvet = int(input())
                except TypeError:
                    print('Вы ввели не число')
                    otvet = 0
                except ValueError:
                    print('Вы ввели не число')
                    otvet = 0
                except NameError:
                    print('Вы ввели не число')
                    otvet = 0
                if otvet == 1:
                    print('Вы напали на оленя')
                    i = 0
                    i = random.randrange(1, 100)
                    if i <= 10:
                        print('Вам удалось победить оленя ')
                        print('1:Взять тушу с собой', '\n', '2: Оставить на месте', '\n')
                        otvet = 0
                        try:
                            otvet = int(input())
                        except TypeError:
                            print('Вы ввели не число')
                            otvet = 0
                        except ValueError:
                            print('Вы ввели не число')
                            otvet = 0
                        except NameError:
                            print('Вы ввели не число')
                            otvet = 0
                        if otvet == 1:
                            print('Вы забрали тушу и отправились в лес')
                            glush()
                            otvet = 0
                            try:
                                otvet = int(input())
                            except TypeError:
                                print('Вы ввели не число')
                                otvet = 0
                            except ValueError:
                                print('Вы ввели не число')
                                otvet = 0
                            except NameError:
                                print('Вы ввели не число')
                                otvet = 0
                            if otvet == 1:
                                domitusha()
                                otvet = 0
                                try:
                                    otvet = int(input())
                                except TypeError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except ValueError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except NameError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                if otvet == 1:
                                    print('Вы отдаете тушу леснику')
                                    print('Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                    poslelesnika()
                                    otvet = 0
                                    try:
                                        otvet = int(input())
                                    except TypeError:
                                            print('Вы ввели не число')
                                            otvet = 0
                                    except ValueError:
                                            print('Вы ввели не число')
                                            otvet = 0
                                    except NameError:
                                            print('Вы ввели не число')
                                            otvet = 0
                                    if otvet==1:
                                            print('Вы решили отступить')
                                            print('Однако вы не посмотрели под ноги и наступили на палку')
                                            print('Треск был услышан разбойниками ')
                                            print('Вас поймали ')
                                            print('Вы мертвы')
                                            break
                                    elif otvet==2:
                                            print('Вы попытались напасть на разбойников')
                                            i = 0
                                            i = random.randrange(1, 100)
                                            if i <=35:
                                                print('Вам удалось победить разбойников')
                                                print('Сокровища разбойиков достаются вам')
                                                print('С сокровищами вы отправляетесь дальше в лес')
                                                mimo()
                                                otvet = 0
                                                try:
                                                    otvet = int(input())
                                                except TypeError:
                                                    print('Вы ввели не число')
                                                    otvet = 0
                                                except ValueError:
                                                    print('Вы ввели не число')
                                                    otvet = 0
                                                except NameError:
                                                    print('Вы ввели не число')
                                                    otvet = 0
                                                if otvet == 2:
                                                    print('Вы пошли вверх по реке')
                                                    print('Вам повезло вы вышли к поселению')
                                                    print('Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                    break
                                                elif otvet == 1:
                                                    reka_vniz()
                                                    break
                                            else:
                                                print('Вам не удалось победить разбойников')
                                                print('Вы мертвы')
                                                break
                                    elif otvet == 2:
                                        print('Вы решили не отдавать тушу леснику ')
                                        print('Вы огорчили лесника')
                                        print('Он выгнал вас из дома')
                                        print('Идя с тушей по лесу на вас напала стая волков ')
                                        print('Вы мертвы')
                                        break
                        elif otvet == 2:
                            print('Вы не стали брать тушу оленя ')
                            glush()
                            otvet = 0
                            try:
                                otvet = int(input())
                            except TypeError:
                                print('Вы ввели не число')
                                otvet = 0
                            except ValueError:
                                print('Вы ввели не число')
                                otvet = 0
                            except NameError:
                                print('Вы ввели не число')
                                otvet = 0
                            if otvet == 1:
                                dom()
                                otvet = 0
                                try:
                                    otvet = int(input())
                                except TypeError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except ValueError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except NameError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                if otvet == 1:
                                    in_dom()
                                    break
                                elif otvet == 2:
                                    viyti()
                                    otvet = 0
                                    try:
                                        otvet = int(input())
                                    except TypeError:
                                        print('Вы ввели не число')
                                        otvet = 0
                                    except ValueError:
                                        print('Вы ввели не число')
                                        otvet = 0
                                    except NameError:
                                        print('Вы ввели не число')
                                        otvet = 0
                                    if otvet == 2:
                                        reka_verx()
                                        break
                                    elif otvet == 1:
                                        reka_vniz()
                                        break
                            elif otvet == 2:
                                mimo()
                                otvet = 0
                                try:
                                    otvet = int(input())
                                except TypeError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except ValueError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                except NameError:
                                    print('Вы ввели не число')
                                    otvet = 0
                                if otvet == 2:
                                    reka_verx()
                                    break
                                elif otvet == 1:
                                    reka_vniz()
                                    break
                    else:
                        print('Палки не хватило чтобы победить оленя ')
                        print('Вы мертвы')
                        break
            if 20 < i <= 40:
                print('Оглядевшись вы нашли лакомство')
                print('1:Попытаться приручить оленя', '\n', '2: Съесть самому', '\n')
                otvet = 0
                try:
                    otvet = int(input())
                except TypeError:
                    print('Вы ввели не число')
                    otvet = 0
                except ValueError:
                    print('Вы ввели не число')
                    otvet = 0
                except NameError:
                    print('Вы ввели не число')
                    otvet = 0
                if otvet == 1:
                    i = 0
                    i = random.randrange(1, 100)
                    if i < 50:
                        print('Вы приручили оленя ')
                        print('Олень вывел вас из леса')
                        print('Вам повезло вы вышли из леса и обрели верного друга')
                        break
                    else:
                        print('Олень поел и убежал')
                        print('Вы пошли по лесу ')
                        print('Вы начали испытывать беспокойство ')
                        print('Через неекоторое время ваш труп уже клевали птицы')
                        break
                elif otvet==2:
                    print('Олень рассержен')
                    print('Вы стали обедом для оленя')
                    break
            else:
                print('Вы ничего не нашли ')
                print('Пока вы осматривались олень приблизился к вам')
                print('Вы мертвы')
                break
        elif otvet == 4:
            napugal()
            i = 0
            i = random.randrange(1, 100)
            if i>=80:
                print('Вам повезло вам удалось напугать оленя он убежал')
                print('Однако вы ранены')
                print('Вам повезло напугать оленя однако вы не смогли выжить и умерли от голода')
                break
            else:
                print('Олень непоколебим ')
                print('Олень разорвал вас рогами')
                break
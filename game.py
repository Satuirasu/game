import random

def invent():
    print(inventory)
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
    print(
        'Вы не спали всю ночь, вы чувствуете усталость, а так же вы чувствуете сильный голод, вы видете куст незнакомых ягод ')
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
    print('1:Напасть на оленя', '\n', '2: Сбежать от оленя', '\n', '3: Оглядется по сторонам', '\n',
          '4: Попытаться напугать ', '\n')


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
score=0
inventory = [None,None,None,None,None,None]

while True:
    perv()
    print('Так же вы можете открыть инвентарь 8')
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
        score=+1
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
                print('вы набрали ',score,'очков')
                break
            elif otvet == 2:
                viyti()
                score=+1
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
                    score=+2
                    print('вы набрали ', score, 'очков')
                    break
                elif otvet == 1:
                    reka_vniz()
                    score=+1
                    print('вы набрали ', score, 'очков')
                    break
            elif otvet == 8:
                invent()
                print('Напишите 1 для выхода из инвенторя')
                exit = int(input())
                if exit == 1:
                    dom()
                else:
                    exit = int(input())
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
                score=+2
                print('вы набрали ', score, 'очков')
                break
            elif otvet == 1:
                reka_vniz()
                score=+1
                print('вы набрали ',score,'очков')
                break
        elif otvet == 8:
            invent()
            print('Напишите 1 для выхода из инвенторя')
            exit = int(input())
            if exit == 1:
                mimo()
            else:
                exit = int(input())
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
            print('вы набрали ', score, 'очков')
            break
        elif otvet == 2:
            ne_spal_nich()
            score=+1
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
                print('вы набрали ', score, 'очков')
                break
            elif otvet == 2:
                ne_cel()
                print('вы набрали ', score, 'очков')
                break
        elif otvet == 8:
            invent()
            print('Напишите 1 для выхода из инвенторя')
            exit = int(input())
            if exit == 1:
                ostalsa()

            else:
                exit = int(input())
    elif otvet == 3:
        poshel_na_golos()
        print('вы набрали ', score, 'очков')
        break
    elif otvet == 4:
        olen()
        score=+2
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
            print('вы набрали ', score, 'очков')
            break
        elif otvet == 2:
            sbejat()
            print('вы набрали ', score, 'очков')
            break
        elif otvet == 3:
            ogladetsa()
            score=+1
            i = random.randrange(1, 100)
            if i <= 20:
                print('Вы нашли палку')
                score=+1
                inventory[0]='палка'
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
                    inventory[0]=None
                    i = 0
                    i = random.randrange(1, 100)
                    if i <= 10:
                        print('Вам удалось победить оленя ')
                        score=+2
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
                            inventory[1]='туша'
                            glush()
                            score=+1
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
                                score=+1
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
                                    inventory[1]=None
                                    print('Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                    inventory[2]='ружье'
                                    poslelesnika()
                                    score=+1
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
                                        print('Вы решили отступить')
                                        print('Однако вы не посмотрели под ноги и наступили на палку')
                                        print('Треск был услышан разбойниками ')
                                        print('Вас поймали ')
                                        print('Вы мертвы')
                                        print('вы набрали ', score, 'очков')
                                        break
                                    elif otvet == 2:
                                        print('Вы попытались напасть на разбойников')
                                        score=+2
                                        i = 0
                                        i = random.randrange(1, 100)
                                        if i <= 35:
                                            print('Вам удалось победить разбойников')
                                            print('Сокровища разбойиков достаются вам')
                                            print('С сокровищами вы отправляетесь дальше в лес')
                                            score=+3
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
                                                score=+1
                                                print('Вам повезло вы вышли к поселению')
                                                print('Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                print('вы набрали ', score, 'очков')
                                                break
                                            elif otvet == 1:
                                                reka_vniz()
                                                print('вы набрали ', score, 'очков')
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
                                        print('вы набрали ', score, 'очков')
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
                                    print('вы набрали ', score, 'очков')
                                    break
                                elif otvet == 2:
                                    viyti()
                                    score=+1
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
                                        score=+1
                                        print('вы набрали ', score, 'очков')
                                        break
                                    elif otvet == 1:
                                        reka_vniz()
                                        print('вы набрали ', score, 'очков')
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
                                    score=+1
                                    print('вы набрали ', score, 'очков')
                                    break
                                elif otvet == 1:
                                    reka_vniz()
                                    print('вы набрали ', score, 'очков')
                                    break
                    else:
                        print('Палки не хватило чтобы победить оленя ')
                        print('Вы мертвы')
                        print('вы набрали ', score, 'очков')
                        break
                elif otvet==2:
                    print('Вы кинули палку, олень не отвлекся','\n','Вы мертвы', '\n')
                    print('вы набрали ', score, 'очков')
                    break
                elif otvet==3:
                    print('Вы махнули палкой, олень разозлился','\n','Вы мертвы','\n')
                    print('вы набрали ', score, 'очков')
                    break
                elif otvet==8:
                    invent()
                    print('Напишите 1 для выхода из инвенторя')
                    exit = int(input())
                    if exit == 1:
                        print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n', '3: Махать палкой','\n')
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
                            score=+1
                            inventory[0] = None
                            i = 0
                            i = random.randrange(1, 100)
                            if i <= 10:
                                print('Вам удалось победить оленя ')
                                score=+2
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
                                    inventory[1] = 'туша'
                                    score=+1
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
                                        score=+1
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
                                            inventory[1] = None
                                            score=+1
                                            print('Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                            inventory[2] = 'ружье'
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
                                            if otvet == 1:
                                                print('Вы решили отступить')
                                                print('Однако вы не посмотрели под ноги и наступили на палку')
                                                print('Треск был услышан разбойниками ')
                                                print('Вас поймали ')
                                                print('Вы мертвы')
                                                print('вы набрали ', score, 'очков')
                                                break
                                            elif otvet == 2:
                                                print('Вы попытались напасть на разбойников')
                                                score=+2
                                                i = 0
                                                i = random.randrange(1, 100)
                                                if i <= 35:
                                                    print('Вам удалось победить разбойников')
                                                    print('Сокровища разбойиков достаются вам')
                                                    print('С сокровищами вы отправляетесь дальше в лес')
                                                    score=+3
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
                                                        score=+1
                                                        print('Вам повезло вы вышли к поселению')
                                                        print('Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                    elif otvet == 1:
                                                        reka_vniz()
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                else:
                                                    print('Вам не удалось победить разбойников')
                                                    print('Вы мертвы')
                                                    print('вы набрали ', score, 'очков')
                                                    break
                                            elif otvet == 2:
                                                print('Вы решили не отдавать тушу леснику ')
                                                print('Вы огорчили лесника')
                                                print('Он выгнал вас из дома')
                                                print('Идя с тушей по лесу на вас напала стая волков ')
                                                print('Вы мертвы')
                                                print('вы набрали ', score, 'очков')
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
                                        score=+1
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
                                            print('вы набрали ', score, 'очков')
                                            break
                                        elif otvet == 2:
                                            viyti()
                                            score=+1
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
                                                score=+1
                                                print('вы набрали ', score, 'очков')
                                                break
                                            elif otvet == 1:
                                                reka_vniz()
                                                print('вы набрали ', score, 'очков')
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
                                            score=+1
                                            print('вы набрали ', score, 'очков')
                                            break
                                        elif otvet == 1:
                                            reka_vniz()
                                            print('вы набрали ',score,'очков')
                                            break
                                        elif otvet == 8:
                                            invent()
                                            print('Напишите 1 для выхода из инвенторя')
                                            exit = int(input())
                                            if exit == 1:
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
                                                    inventory[1] = None
                                                    print(
                                                        'Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                                    inventory[2] = 'ружье'
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
                                                    if otvet == 1:
                                                        print('Вы решили отступить')
                                                        print('Однако вы не посмотрели под ноги и наступили на палку')
                                                        print('Треск был услышан разбойниками ')
                                                        print('Вас поймали ')
                                                        print('Вы мертвы')
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                    elif otvet == 2:
                                                        print('Вы попытались напасть на разбойников')
                                                        score=+2
                                                        i = 0
                                                        i = random.randrange(1, 100)
                                                        if i <= 35:
                                                            print('Вам удалось победить разбойников')
                                                            score=+2
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
                                                                score=+1
                                                                print('Вам повезло вы вышли к поселению')
                                                                print('Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                                print('вы набрали ', score, 'очков')
                                                                break
                                                            elif otvet == 1:
                                                                reka_vniz()
                                                                print('вы набрали ', score, 'очков')
                                                                break
                                                        else:
                                                            print('Вам не удалось победить разбойников')
                                                            print('Вы мертвы')
                                                            print('вы набрали ', score, 'очков')
                                                            break
                                                    elif otvet == 2:
                                                        print('Вы решили не отдавать тушу леснику ')
                                                        print('Вы огорчили лесника')
                                                        print('Он выгнал вас из дома')
                                                        print('Идя с тушей по лесу на вас напала стая волков ')
                                                        print('Вы мертвы')
                                                        print('вы набрали ', score, 'очков')
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
                                                    score=+1
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
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                    elif otvet == 2:
                                                        viyti()
                                                        score=+1
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
                                                            score=+1
                                                            print('вы набрали ', score, 'очков')
                                                            break
                                                        elif otvet == 1:
                                                            reka_vniz()
                                                            print('вы набрали ', score, 'очков')
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
                                                        score=+1
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                    elif otvet == 1:
                                                        reka_vniz()
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                            else:
                                                exit = int(input())
                            else:
                                print('Палки не хватило чтобы победить оленя ')
                                print('Вы мертвы')
                                print('вы набрали ', score, 'очков')
                                break
                        elif otvet == 2:
                            print('Вы кинули палку, олень не отвлекся', '\n', 'Вы мертвы', '\n')
                            print('вы набрали ', score, 'очков')
                            break
                        elif otvet == 3:
                            print('Вы махнули палкой, олень разозлился', '\n', 'Вы мертвы', '\n')
                            print('вы набрали ', score, 'очков')
                            break
                    else:
                        exit = int(input())

            if 20 < i <= 40:
                print('Оглядевшись вы нашли лакомство')
                score=+1
                print('1:Попытаться приручить оленя', '\n', '2: Съесть самому', '\n')
                inventory[3]='лакомство'
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
                        score=+3
                        print('Олень вывел вас из леса')
                        print('Вам повезло вы вышли из леса и обрели верного друга')
                        print('вы набрали ', score, 'очков')
                        break
                    else:
                        print('Олень поел и убежал')
                        print('Вы пошли по лесу ')
                        print('Вы начали испытывать беспокойство ')
                        print('Через некоторое время ваш труп уже клевали птицы')
                        print('вы набрали ', score, 'очков')
                        break
                elif otvet == 2:
                    print('Олень рассержен')
                    print('Вы стали обедом для оленя')
                    print('вы набрали ', score, 'очков')
                    break
                elif otvet == 8:
                    invent()
                    print('Напишите 1 для выхода из инвенторя')
                    exit = int(input())
                    if exit == 1:
                        print('Оглядевшись вы нашли лакомство')
                        score=+1
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
                                score=+3
                                print('Олень вывел вас из леса')
                                print('Вам повезло вы вышли из леса и обрели верного друга')
                                print('вы набрали ', score, 'очков')
                                break
                            else:
                                print('Олень поел и убежал')
                                print('Вы пошли по лесу ')
                                print('Вы начали испытывать беспокойство ')
                                print('Через некоторое время ваш труп уже клевали птицы')
                                print('вы набрали ', score, 'очков')
                                break
                        elif otvet == 2:
                            print('Олень рассержен')
                            print('Вы стали обедом для оленя')
                            print('вы набрали ', score, 'очков')
                            break
                    else:
                        exit = int(input())
            else:
                print('Вы ничего не нашли ')
                print('Пока вы осматривались олень приблизился к вам')
                print('Вы мертвы')
                print('вы набрали ', score, 'очков')
                break
        elif otvet == 4:
            napugal()
            i = 0
            i = random.randrange(1, 100)
            if i >= 80:
                print('Вам повезло вам удалось напугать оленя он убежал')
                score=+1
                print('Однако вы ранены')
                print('Вам повезло напугать оленя однако вы не смогли выжить и умерли от голода')
                print('вы набрали ', score, 'очков')
                break
            else:
                print('Вы мертвы')
                print('вы набрали ', score, 'очков')
                break
        elif otvet == 8:
                invent()
                print('Напишите 1 для выхода из инвенторя')
                exit = int(input())
                if exit == 1:
                    olen()
                    score=+1
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
                        print('вы набрали ', score, 'очков')
                        break
                    elif otvet == 2:
                        sbejat()
                        print('вы набрали ', score, 'очков')
                        break
                    elif otvet == 3:
                        ogladetsa()
                        i = random.randrange(1, 100)
                        if i <= 20:
                            print('Вы нашли палку')
                            score=+1
                            inventory[0] = 'палка'
                            print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n',
                                  '3: Махать палкой', '\n')
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
                                score=+1
                                inventory[0] = None
                                i = 0
                                i = random.randrange(1, 100)
                                if i <= 10:
                                    print('Вам удалось победить оленя ')
                                    score=+2
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
                                        score=+1
                                        inventory[1] = 'туша'
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
                                                inventory[1] = None
                                                print(
                                                    'Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                                inventory[2] = 'ружье'
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
                                                if otvet == 1:
                                                    print('Вы решили отступить')
                                                    print('Однако вы не посмотрели под ноги и наступили на палку')
                                                    print('Треск был услышан разбойниками ')
                                                    print('Вас поймали ')
                                                    print('Вы мертвы')
                                                    print('вы набрали ', score, 'очков')
                                                    break
                                                elif otvet == 2:
                                                    print('Вы попытались напасть на разбойников')
                                                    i = 0
                                                    i = random.randrange(1, 100)
                                                    if i <= 35:
                                                        print('Вам удалось победить разбойников')
                                                        score=+1
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
                                                            score=+2
                                                            print('Вам повезло вы вышли к поселению')
                                                            print(
                                                                'Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                            print('вы набрали ', score, 'очков')
                                                            break
                                                        elif otvet == 1:
                                                            reka_vniz()
                                                            print('вы набрали ', score, 'очков')
                                                            break
                                                    else:
                                                        print('Вам не удалось победить разбойников')
                                                        print('Вы мертвы')
                                                        print('вы набрали ', score, 'очков')
                                                        break
                                                elif otvet == 2:
                                                    print('Вы решили не отдавать тушу леснику ')
                                                    print('Вы огорчили лесника')
                                                    print('Он выгнал вас из дома')
                                                    print('Идя с тушей по лесу на вас напала стая волков ')
                                                    print('Вы мертвы')
                                                    print('вы набрали ', score, 'очков')
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
                                                print('вы набрали ', score, 'очков')
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
                                                    score=+1
                                                    print('вы набрали ', score, 'очков')
                                                    break
                                                elif otvet == 1:
                                                    reka_vniz()
                                                    print('вы набрали ', score, 'очков')
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
                                                score=+1
                                                print('вы набрали ', score, 'очков')
                                                break
                                            elif otvet == 1:
                                                reka_vniz()
                                                print('вы набрали ', score, 'очков')
                                                break
                                else:
                                    print('Палки не хватило чтобы победить оленя ')
                                    print('Вы мертвы')
                                    print('вы набрали ', score, 'очков')

                                    break
                            elif otvet == 2:
                                print('Вы кинули палку, олень не отвлекся', '\n', 'Вы мертвы', '\n')
                                print('вы набрали ', score, 'очков')
                                break
                            elif otvet == 3:
                                print('Вы махнули палкой, олень разозлился', '\n', 'Вы мертвы', '\n')
                                print('вы набрали ', score, 'очков')
                                break
                            elif otvet == 8:
                                invent()
                                print('Напишите 1 для выхода из инвенторя')
                                exit = int(input())
                                if exit == 1:
                                    print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n',
                                          '3: Махать палкой',
                                          '\n')
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
                                        inventory[0] = None
                                        i = 0
                                        i = random.randrange(1, 100)
                                        if i <= 10:
                                            print('Вам удалось победить оленя ')
                                            score=+2
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
                                                inventory[1] = 'туша'
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
                                                        inventory[1] = None
                                                        print(
                                                            'Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                                        inventory[2] = 'ружье'
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
                                                        if otvet == 1:
                                                            print('Вы решили отступить')
                                                            print(
                                                                'Однако вы не посмотрели под ноги и наступили на палку')
                                                            print('Треск был услышан разбойниками ')
                                                            print('Вас поймали ')
                                                            print('Вы мертвы')
                                                            print('вы набрали ', score, 'очков')
                                                            break
                                                        elif otvet == 2:
                                                            print('Вы попытались напасть на разбойников')
                                                            score=+1
                                                            i = 0
                                                            i = random.randrange(1, 100)
                                                            if i <= 35:
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
                                                                    print(
                                                                        'Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                                    score=+3
                                                                    print('вы набрали ', score, 'очков')
                                                                    break
                                                                elif otvet == 1:
                                                                    reka_vniz()
                                                                    print('вы набрали ', score, 'очков')

                                                                    break
                                                            else:
                                                                print('Вам не удалось победить разбойников')
                                                                print('Вы мертвы')
                                                                print('вы набрали ', score, 'очков')

                                                                break
                                                        elif otvet == 2:
                                                            print('Вы решили не отдавать тушу леснику ')
                                                            print('Вы огорчили лесника')
                                                            print('Он выгнал вас из дома')
                                                            print('Идя с тушей по лесу на вас напала стая волков ')
                                                            print('Вы мертвы')
                                                            print('вы набрали ', score, 'очков')

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
                                                    score=+1
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
                                                        print('вы набрали ', score, 'очков')

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
                                                            score=+1
                                                            print('вы набрали ', score, 'очков')

                                                            break
                                                        elif otvet == 1:
                                                            reka_vniz()
                                                            print('вы набрали ', score, 'очков')

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
                                                        score=+1
                                                        print('вы набрали ', score, 'очков')

                                                        break
                                                    elif otvet == 1:
                                                        reka_vniz()
                                                        print('вы набрали ', score, 'очков')

                                                        break
                                        else:
                                            print('Палки не хватило чтобы победить оленя ')
                                            print('Вы мертвы')
                                            print('вы набрали ', score, 'очков')

                                            break
                                    elif otvet == 2:
                                        print('Вы кинули палку, олень не отвлекся', '\n', 'Вы мертвы', '\n')
                                        print('вы набрали ', score, 'очков')

                                        break
                                    elif otvet == 3:
                                        print('Вы махнули палкой, олень разозлился', '\n', 'Вы мертвы', '\n')
                                        print('вы набрали ', score, 'очков')

                                        break
                                else:
                                    exit = int(input())

                        if 20 < i <= 40:
                            print('Оглядевшись вы нашли лакомство')
                            score=+1
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
                                    score=+3
                                    print('Олень вывел вас из леса')
                                    print('Вам повезло вы вышли из леса и обрели верного друга')
                                    print('вы набрали ', score, 'очков')

                                    break
                                else:
                                    print('Олень поел и убежал')
                                    print('Вы пошли по лесу ')
                                    print('Вы начали испытывать беспокойство ')
                                    print('Через некоторое время ваш труп уже клевали птицы')
                                    print('вы набрали ', score, 'очков')

                                    break
                            elif otvet == 2:
                                print('Олень рассержен')
                                print('Вы стали обедом для оленя')
                                print('вы набрали ', score, 'очков')

                                break
                        else:
                            print('Вы ничего не нашли ')
                            print('Пока вы осматривались олень приблизился к вам')
                            print('Вы мертвы')
                            print('вы набрали ', score, 'очков')

                            break
                    elif otvet == 4:
                        napugal()
                        i = 0
                        i = random.randrange(1, 100)
                        if i >= 80:
                            print('Вам повезло вам удалось напугать оленя он убежал')
                            print('Однако вы ранены')
                            print('Вам повезло напугать оленя однако вы не смогли выжить и умерли от голода')
                            print('вы набрали ', score, 'очков')

                            break

                        else:
                            print('Олень непоколебим ')
                            print('Олень разорвал вас рогами')
                            print('вы набрали ', score, 'очков')

                            break
                    elif otvet == 8:
                        invent()
                        print('Напишите 1 для выхода из инвенторя')
                        exit = int(input())
                        if exit == 1:
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
                                    score=+1
                                    inventory[0] = 'палка'
                                    print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n',
                                          '3: Махать палкой', '\n')
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
                                        inventory[0] = None
                                        i = 0
                                        i = random.randrange(1, 100)
                                        if i <= 10:
                                            print('Вам удалось победить оленя ')
                                            score=+2
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
                                                inventory[1] = 'туша'
                                                glush()
                                                score=+1
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
                                                        score=+2
                                                        inventory[1] = None
                                                        print(
                                                            'Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                                        inventory[2] = 'ружье'
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
                                                        if otvet == 1:
                                                            print('Вы решили отступить')
                                                            print(
                                                                'Однако вы не посмотрели под ноги и наступили на палку')
                                                            print('Треск был услышан разбойниками ')
                                                            print('Вас поймали ')
                                                            print('Вы мертвы')
                                                            print('вы набрали ', score, 'очков')

                                                            break
                                                        elif otvet == 2:
                                                            print('Вы попытались напасть на разбойников')
                                                            score=+2
                                                            i = 0
                                                            i = random.randrange(1, 100)
                                                            if i <= 35:
                                                                print('Вам удалось победить разбойников')
                                                                score=+3
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
                                                                    score=+1
                                                                    print('Вам повезло вы вышли к поселению')
                                                                    print(
                                                                        'Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                                    print('вы набрали ', score, 'очков')

                                                                    break
                                                                elif otvet == 1:
                                                                    reka_vniz()
                                                                    print('вы набрали ', score, 'очков')

                                                                    break
                                                            else:
                                                                print('Вам не удалось победить разбойников')
                                                                print('Вы мертвы')
                                                                print('вы набрали ', score, 'очков')

                                                                break
                                                        elif otvet == 2:
                                                            print('Вы решили не отдавать тушу леснику ')
                                                            print('Вы огорчили лесника')
                                                            print('Он выгнал вас из дома')
                                                            print('Идя с тушей по лесу на вас напала стая волков ')
                                                            print('Вы мертвы')
                                                            print('вы набрали ', score, 'очков')

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
                                                        print('вы набрали ', score, 'очков')

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
                                                            score=+1
                                                            print('вы набрали ', score, 'очков')

                                                            break
                                                        elif otvet == 1:
                                                            reka_vniz()
                                                            print('вы набрали ', score, 'очков')

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
                                                        score=+1
                                                        print('вы набрали ', score, 'очков')

                                                        break
                                                    elif otvet == 1:
                                                        reka_vniz()
                                                        print('вы набрали ', score, 'очков')

                                                        break
                                        else:
                                            print('Палки не хватило чтобы победить оленя ')
                                            print('Вы мертвы')
                                            print('вы набрали ', score, 'очков')

                                            break
                                    elif otvet == 2:
                                        print('Вы кинули палку, олень не отвлекся', '\n', 'Вы мертвы', '\n')
                                        print('вы набрали ', score, 'очков')

                                        break
                                    elif otvet == 3:
                                        print('Вы махнули палкой, олень разозлился', '\n', 'Вы мертвы', '\n')
                                        print('вы набрали ', score, 'очков')

                                        break
                                    elif otvet == 8:
                                        invent()
                                        print('Напишите 1 для выхода из инвенторя')
                                        exit = int(input())
                                        if exit == 1:
                                            print('1:Напасть на оленя, используя палку', '\n', '2: Кинуть палку', '\n',
                                                  '3: Махать палкой',
                                                  '\n')
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
                                                score=+2
                                                inventory[0] = None
                                                i = 0
                                                i = random.randrange(1, 100)
                                                if i <= 10:
                                                    print('Вам удалось победить оленя ')
                                                    score=+3
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
                                                        inventory[1] = 'туша'
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
                                                                inventory[1] = None
                                                                print(
                                                                    'Лесник накормил вас и отдал свое старое ружье вы дальше отправились в путь')
                                                                inventory[2] = 'ружье'
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
                                                                if otvet == 1:
                                                                    print('Вы решили отступить')
                                                                    print(
                                                                        'Однако вы не посмотрели под ноги и наступили на палку')
                                                                    print('Треск был услышан разбойниками ')
                                                                    print('Вас поймали ')
                                                                    print('Вы мертвы')
                                                                    print('вы набрали ', score, 'очков')

                                                                    break
                                                                elif otvet == 2:
                                                                    print('Вы попытались напасть на разбойников')
                                                                    i = 0
                                                                    i = random.randrange(1, 100)
                                                                    if i <= 35:
                                                                        print('Вам удалось победить разбойников')
                                                                        print('Сокровища разбойиков достаются вам')
                                                                        print(
                                                                            'С сокровищами вы отправляетесь дальше в лес')
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
                                                                            print(
                                                                                'Поздравляем вы вышли из леса, а так же вы стали давольно богатым')
                                                                            score=+1
                                                                            print('вы набрали ', score, 'очков')

                                                                            break
                                                                        elif otvet == 1:
                                                                            reka_vniz()
                                                                            print('вы набрали ', score, 'очков')

                                                                            break
                                                                    else:
                                                                        print('Вам не удалось победить разбойников')
                                                                        print('Вы мертвы')
                                                                        print('вы набрали ', score, 'очков')

                                                                        break
                                                                elif otvet == 2:
                                                                    print('Вы решили не отдавать тушу леснику ')
                                                                    print('Вы огорчили лесника')
                                                                    print('Он выгнал вас из дома')
                                                                    print(
                                                                        'Идя с тушей по лесу на вас напала стая волков ')
                                                                    print('Вы мертвы')
                                                                    print('вы набрали ', score, 'очков')

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
                                                                print('вы набрали ', score, 'очков')

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
                                                                    score=+1
                                                                    print('вы набрали ', score, 'очков')

                                                                    break
                                                                elif otvet == 1:
                                                                    reka_vniz()
                                                                    print('вы набрали ', score, 'очков')

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
                                                                score=+1
                                                                print('вы набрали ', score, 'очков')

                                                                break
                                                            elif otvet == 1:
                                                                reka_vniz()
                                                                print('вы набрали ', score, 'очков')

                                                                break
                                                else:
                                                    print('Палки не хватило чтобы победить оленя ')
                                                    print('Вы мертвы')
                                                    print('вы набрали ', score, 'очков')

                                                    break
                                            elif otvet == 2:
                                                print('Вы кинули палку, олень не отвлекся', '\n', 'Вы мертвы', '\n')
                                                print('вы набрали ', score, 'очков')

                                                break
                                            elif otvet == 3:
                                                print('Вы махнули палкой, олень разозлился', '\n', 'Вы мертвы', '\n')
                                                print('вы набрали ', score, 'очков')

                                                break
                                        else:
                                            exit = int(input())

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
                                            score=+3
                                            print('Олень вывел вас из леса')
                                            print('Вам повезло вы вышли из леса и обрели верного друга')
                                            print('вы набрали ', score, 'очков')

                                            break
                                        else:
                                            print('Олень поел и убежал')
                                            print('Вы пошли по лесу ')
                                            print('Вы начали испытывать беспокойство ')
                                            print('Через некоторое время ваш труп уже клевали птицы')
                                            print('вы набрали ', score, 'очков')

                                            break
                                    elif otvet == 2:
                                        print('Олень рассержен')
                                        print('Вы стали обедом для оленя')
                                        print('вы набрали ', score, 'очков')

                                        break
                                else:
                                    print('Вы ничего не нашли ')
                                    print('Пока вы осматривались олень приблизился к вам')
                                    print('Вы мертвы')
                                    print('вы набрали ', score, 'очков')

                                    break
                            elif otvet == 4:
                                napugal()
                                i = 0
                                i = random.randrange(1, 100)
                                if i >= 80:
                                    print('Вам повезло вам удалось напугать оленя он убежал')
                                    print('Однако вы ранены')
                                    print('Вам повезло напугать оленя однако вы не смогли выжить и умерли от голода')
                                    print('вы набрали ', score, 'очков')

                                    break

                                else:
                                    print('Олень непоколебим ')
                                    print('Олень разорвал вас рогами')
                                    print('вы набрали ', score, 'очков')

                                    break
                        else:
                            exit = int(input())
    elif otvet==8:
        invent()
        print('Напишите 1 для выхода из инвенторя')
        exit=int(input())
        if exit ==1:
            perv()
        else:
            exit = int(input())

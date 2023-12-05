from IPython.utils.sysinfo import pprint
#@title RPGの戦闘みたいなsomething V.1.4.1
#latest セキュリティの面と音声消したとか
import binascii
import random
import time
import IPython

#関数の作成
def hoge():
    hoge_hoge = 0

def zokuseidamage(zokuseiplus,selectedenemy,inputdamage):
    if (int(selectedenemy) == 1 ) and (int(enemytypeA) == (zokuseiplus)):
        print('属性ダメージが入った！')
        return (int(inputdamage)+ 4+ (atp*2))
    elif (int(selectedenemy) == 2 ) and (int(enemytypeB) == (zokuseiplus)):
        print('属性ダメージが入った！')
        return (int(inputdamage)+ 4+ (atp*2))
    elif  (int(selectedenemy) == 3 ) and (int(enemytypeC) == (zokuseiplus)):
        print('属性ダメージが入った！')
        return (int(inputdamage)+ 4+ (atp*2))
    else :
        return inputdamage

def damage_calculation(cold,enemylevel,dep,level,defpow):
    damage = (random.randrange(4+(enemylevel*3),10+(enemylevel*4)))
    if cold > 0 :
        damage = ( damage - (enemylevel * 2) )
    damage = (damage -(int(dep)*int(level)/3))
    damage = (damage * defpow)
    damage = round(damage) #小数点以下四捨五入
    damage = str(damage)
    print(damage + "のダメージを受けた！")
    damage = int(damage)
    return damage

replay = 1

dataload = input("データコードで引き継ぎますか？ 0= no 1= yes!")
if int(dataload) == 1 :
    dataload = input('保存コードを入れてください。※カッコは外してね')
    data = dataload.split(',')  # 入力文字列をカンマで分割してリストにする
    indata = [int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value for value in data]
    name = binascii.unhexlify(name_utf).decode("utf-16")
    XP = int(indata[1])
    nextlevel = int(indata[2])
    enemylevel = int(indata[3])
    money = int(indata[4])
    HPplus = int(indata[5])
    MPplus = int(indata[6])
    atp = int(indata[7])
    dep =  float(indata[8])
    healpow = int(indata[9])
    healMPpow =int(indata[10])
    HPpotionzansu = int(indata[11])
    MPpotionzansu = int(indata[12])

if int(XP) == 0:
    if (name) == (''):
        name =input('名前を入力してください!')

while replay == 1 :
    print("----------------------")
    if replay == 1 :
        buyUI = 0
        buyUI = input('''買い物する？
        する→1　しない→0
        ''')
        if int(buyUI) == 1 :   #買い物
            buyselect = 1
            print(buyselect)
            while not (int(buyselect) == 0):
                print("----------------------")
                print('所持金は '+ str(money) + '円')
                buywant = input('''買いたい物を選んでね！
                0.退出
                1.HP回復ポーション (¥50)  所持：''' + str(HPpotionzansu) +'''
                2.MP回復ポーション (¥50)  所持：''' + str(MPpotionzansu) +'''
                ''')
                buywant = int(buywant)
                if buywant == 0 :
                    buyselect = 0
                elif buywant == 1 :
                    if money >= 50 :
                        HPpotionzansu = int(HPpotionzansu + 1)
                        print('HP回復ポーションを一つ購入した！')
                        money = (int(money) - 50 )
                elif buywant == 2 :
                    if money >= 50 :
                        MPpotionzansu = int(MPpotionzansu + 1)
                        print('HP回復ポーションを一つ購入した！')
                        money = (int(money) - 50 )
        else:
            hoge()
    print("----------------------")
    nige = 0
    poisonA = (0)
    fireturnA = (0)
    dreinA = (0)
    poisonB = (0)
    fireturnB = (0)
    dreinB = (0)
    poisonC = (0)
    fireturnC = (0)
    dreinC = (0)
    ifturnend = 0
    stguptime = 0
    cold = (0)
    MP = (100 + int(MPplus))
    MPwake = (int(MP) / 10)
    rare = 1
    rare = (random.randrange(1 , 101)) #2% de rare
    if rare == 10 :
        rareplus = 20
    else :
        rareplus = 0
    enemylevel = int(enemylevel)    #HPsetting
    enemyHPA =(random.randrange(80 +(enemylevel*20)+ (rareplus*2),100 +(enemylevel*30)+(rareplus*2)))
    eneHPAwake = (enemyHPA / 10)
    enemyHPB =(random.randrange(70 +(enemylevel*10),80 +(enemylevel*10)))
    eneHPBwake = (enemyHPB / 10)
    enemyHPC =(random.randrange(50 +(enemylevel*10),80 +(enemylevel*10)))
    eneHPCwake = (enemyHPC / 10)
    enemytypeA = (random.randrange(0,8))
    enemytypeB = (random.randrange(0,8))
    enemytypeC = (random.randrange(0,8))
    enemylevel = str(enemylevel)
    print( name+'   Lv.' + str(level))
    print('敵が現れた！')
    print('敵のレベルは'+ enemylevel)
    if rare == 10 :
        print("レアな敵がいる！")
    enemylevel = int(enemylevel)
    enemycount = (random.randrange(1,4))
    if level == 1 :
        enemycount = 1
        enemytypeA = 0
    if level == 2 :
        enemycount = 2
        enemytypeA = 0
        enemytypeB = 4
    if level == 3 :
        enemycount = 2
    if enemycount == 1 :
        enemyHPB = 0
        enemyHPC = 0
    elif enemycount == 2 :
        enemyHPC = 0
    HP = (100 + HPplus)
    HPwake = (HP * 0.1)

    while ifturnend == 0 :#ここから戦闘選択開始
        print("----------------------")
        fireturnA = (int(fireturnA) - 1)
        poisonA = (int(poisonA) - 1 )
        fireturnB = (int(fireturnB) - 1)
        poisonB = (int(poisonB) - 1 )
        fireturnC = (int(fireturnC) - 1)
        poisonC = (int(poisonC) - 1 )
        stguptime = (int(stguptime) - 1)
        if stguptime <= 0 :
            stgup = 0
        defpow = 1
        miss = 0
        enemyHPA = int(enemyHPA)
        MP = (int(MP) + 5 + int(healMPpow))
        if MP > int(int(MPwake) * 10) :
            MP = (int((int(MPwake) * 10)))
        kaisu = 10
        while kaisu > 0 :  #敵AのHP
            if enemytypeA == 1 :
                textcolor = ('\033[38;2;255;0;0m')
            elif enemytypeA == 2 :
                textcolor = ('\033[35m')
            elif enemytypeA == 3 :
                textcolor = ("\033[38;2;255;255;0m")
            elif enemytypeA == 4 :
                textcolor = ('\033[32m')
            elif enemytypeA == 5 :
                textcolor = ("\033[38;2;201;108;2m")
            elif enemytypeA == 6 :
                textcolor = ("\033[38;2;172;3;252m")
            elif enemytypeA == 7 :
                textcolor = ("\033[38;2;255;255;242m")
            else :
                textcolor = ('\033[39m')
            kaisu = (kaisu - 1)
            if enemyHPA >= ((eneHPAwake) * (kaisu)):
                enemyHPA = str(enemyHPA)
                print(str(textcolor) +"残り敵AのHP : "+ (enemyHPA) + '\033[33m'+(("■")*(kaisu+1))+'\033[31m'+(("□")*(9-kaisu))+'\033[39m')
                kaisu = 0
                enemyHPA = int(enemyHPA)
        kaisu = 10
        if enemycount >= 2 :  #敵BのHP
            while kaisu > 0 :
                if enemytype == 1 :
                    textcolor = ('\033[38;2;255;0;0m')
                elif enemytypeB == 2 :
                    textcolor = ('\033[35m')
                elif enemytypeB == 3 :
                   textcolor = ("\033[38;2;255;255;0m")
                elif enemytypeB == 4 :
                   textcolor = ('\033[32m')
                elif enemytypeB == 5 :
                   textcolor = ("\033[38;2;201;108;2m")
                elif enemytypeB == 6 :
                   textcolor = ("\033[38;2;172;3;252m")
                elif enemytypeB == 7 :
                   textcolor = ("\033[38;2;255;255;242m")
                else :
                   textcolor = ('\033[39m')
                kaisu = (kaisu - 1)
                if enemyHPB >= ((eneHPBwake) * (kaisu)):
                    enemyHPB = str(enemyHPB)
                    print(str(textcolor) +"残り敵BのHP : "+  (enemyHPB)+'\033[33m'+ (("■")*(kaisu+1))+'\033[31m' +(("□")*(9-kaisu))+'\033[39m')
                    kaisu = 0
                    enemyHPB = int(enemyHPB)
        kaisu = 10
        if enemycount == 3 :  #敵CのHP
            while kaisu > 0 :
               if enemytypeC == 1 :
                   textcolor = ('\033[38;2;255;0;0m')
               elif enemytypeC == 2 :
                   textcolor = ('\033[35m')
               elif enemytypeC == 3 :
                  textcolor = ("\033[38;2;255;255;0m")
               elif enemytypeC == 4 :
                  textcolor = ('\033[32m')
               elif enemytypeC == 5 :
                  textcolor = ("\033[38;2;201;108;2m")
               elif enemytypeC == 6 :
                  textcolor = ("\033[38;2;172;3;252m")
               elif enemytypeC == 7 :
                  textcolor = ("\033[38;2;255;255;242m")
               else :
                  textcolor = ('\033[39m')
               kaisu = (kaisu - 1)
               if enemyHPC >= ((eneHPCwake) * (kaisu)):
                  enemyHPC = str(enemyHPC)
                  print(str(textcolor) +"残り敵CのHP : "+ (enemyHPC) +'\033[33m'+ (("■")*(kaisu+1))+'\033[31m' +(("□")*(9-kaisu))+'\033[39m')
                  kaisu = 0
                  enemyHPC = int(enemyHPC)
        kaisu = 10
        while kaisu > 0 : #自分のHP
            kaisu = (kaisu - 1)
            if HP >= ((HPwake) * (kaisu)):
                HP = str(HP)
                print("残り自分HP : "+"\033[38;2;245;20;125m"+ (HP) + (("■")*(kaisu+1))+(("□")*(9-kaisu)+"\033[0m"))
                kaisu = 0
                HP = int(HP)
        kaisu = 10
        while kaisu > 0 : #自分のMP
            kaisu = (kaisu - 1)
            if MP >= ((MPwake) * (kaisu)):
                MP = str(MP)
                print("残り自分MP : "+"\033[38;2;53;246;252m"+ (MP) + (("■")*(kaisu+1))+(("□")*(9-kaisu)+"\033[0m"))
                kaisu = 0
                MP = int(MP)

        select =input("""あなたのターン！
        1.攻撃　2.防御
        3.回復   4.逃げる
        """)
        select = int(select)

        if select == 1 : #攻撃
            if level >= 3 :
                print('''攻撃手段を選べ！
                1.斬撃(MP 0)　  　        '''+"\033[38;2;255;0;0m2.フレア(MP 10 )\033[0m"+'''
                '''+"\033[38;2;0;221;252m3.フローズン(MP 15 )\033[0m"+'''    '''+"\033[38;2;172;3;252m4.ディーティリオ(MP 20 )\033[0m"+'''
                '''+"\033[38;2;0;253;85m5.エアブレード(MP 15)\033[0m")
                atselect = input()
            elif level >= 5:
                print('''攻撃手段を選べ！
                1.斬撃(MP 0)　  　        '''+"\033[38;2;255;0;0m2.フレア(MP 10 )\033[0m"+'''
                '''+"\033[38;2;0;221;252m3.フローズン(MP 15 )"+'   '+ "\033[38;2;172;3;252m4.ディーティリオ(MP 20 )\033[0m"+'''
                '''+"\033[38;2;0;253;85m5.エアブレード(MP 15)\033[0m"+'''6.ストレングアップ(MP 20 )''')
                atselect = input()
            elif level >= 7:
                print('''攻撃手段を選べ！
                1.斬撃(MP 0)　  　        '''+"\033[38;2;255;0;0m2.フレア(MP 10 )\033[0m"+'''
                '''+"\033[38;2;0;221;252m3.フローズン(MP 15 )"+'   '+ "\033[38;2;172;3;252m4.ディーティリオ(MP 20 )\033[0m"+'''
                '''+"\033[38;2;0;253;85m5.エアブレード(MP 15)\033[0m"+'''6.ストレングアップ(MP 20 )
                '''+"\033[38;2;240;245;184m7.ドレイン(MP 30)\033[0m")
                atselect = input()
            else :
                print('''攻撃手段を選べ！
                1.斬撃(MP 0)　 　      '''+"\033[38;2;255;0;0m2.フレア(MP 10 )\033[0m"+'''
                '''+"\033[38;2;0;221;252m3.フローズン(MP 15 )"+''' '''+"\033[38;2;172;3;252m4.ディーティリオ(MP 20 )\033[0m")
                atselect = input()
            damage = 0
            if enemyHPA < 1 and enemyHPB < 1 :
                selectenemy = 3
            elif enemyHPC < 1 and enemyHPB < 1 :
                selectenemy = 1
            elif enemyHPA < 1 and enemyHPC < 1 :
                selectenemy = 2
            elif enemycount == 2 or enemycount == 3 :  #敵選ぶ
                selectenemy = input('1~' + str(enemycount) + 'の敵をえらべ！')
                selectenemy = int(selectenemy)
            else :
                selectenemy = 1
            print("----------------------")
            if int(atselect) == 1 : #斬撃の攻撃判定
                print("あなたは切りかかった！")
                critical = (random.randrange(1,6))
                damage = (random.randrange(15 + atp + stgup ,35 + atp + stgup ))
                if critical == 3 :
                    damage = (damage * 2)
                    print("会心の一撃！！")

            elif int(atselect) == 2 : #フレアの攻撃判定
                if MP >= 10 :
                    print("あなたは"+"\033[38;2;255;0;0m フレア \033[0m"+"で攻撃した！")
                    print("敵は燃えた！")
                    damage = (random.randrange(10 + atp + stgup , 20 + atp + stgup))
                    damage = (zokuseidamage(4,selectenemy,damage))
                    if selectenemy == 1 :
                        fireturnA = 2
                    if selectenemy == 2 :
                        fireturnB = 2
                    if selectenemy == 3 :
                        firetunrC = 2
                    MP = (MP - 10)
                else :
                    print('しかしMPが足りなかった！')

            elif int(atselect) == 3 : #フローズンの攻撃判定
                if MP >= 15 :
                    print("あなたは"+"\033[38;2;0;221;252m フローズン \033[0m"+"を唱えた！")
                    print("敵の動きが鈍ったようだ！")
                    damage = (random.randrange(5 + atp + stgup , 25 + atp + stgup))
                    zokuseidamage(1,selectenemy,damage)
                    cold = 3
                    MP = (MP - 15)
                else :
                    print('しかしMPが足りなかった！')

            elif int(atselect) == 4 : #ディーティリオ毒の攻撃判定
                if MP >= 20 :
                    print('あなたは'+ "\033[38;2;172;3;252m ディーティリオ \033[0m"+'を唱えた！')
                    print('敵は毒になった！')
                    damage = (random.randrange(10 + atp+ stgup , 26 + atp + stgup ))
                    zokuseidamage(7,selectenemy,damage)
                    if selectenemy == 1 :
                        poisonA = 5
                    if selectenemy == 2 :
                        poisonB = 5
                    if selectenemy == 3 :
                        poisonC = 5
                    MP = (MP - 20)
                else :
                    print('しかしMPが足りなかった！')

            elif int(atselect) == 5 and (level >= 3) : #エアブレードの攻撃判定
                if MP >= 15 :
                    print('あなたは'+"\033[38;2;0;253;85m エアブレード \033[0m"+'を唱えた！')
                    damage = (random.randrange(7 + atp + stgup , 40 + atp + stgup))
                    zokuseidamage(5,selectenemy,damage)
                    MP = (MP - 15)
                else :
                    print('しかしMPが足りなかった！')

            elif int(atselect) == 6 and (level >= 6 ) : #ストレングアップの判定
                if MP >= 20 :
                    print('攻撃力が上がった！')
                    stgup = (random.randrange(5+int(level),9+int(level)))
                    stguptime = 4
                    MP = (MP - 20)
                else :
                    print('しかしMPが足りなかった！')

            elif int(atselect) == 7 and (level >= 8 ) : #ドレインの判定
                if MP >= 30 :
                    print('ドレイン を唱えた！')
                    if selectenemy == 1 :
                        dreinA = 3
                    if selectenemy == 2 :
                        dreinB = 3
                    if selectenemy == 3 :
                        dreinC = 3
                    MP = (MP - 20)
                else :
                    print('しかしMPが足りなかった！')

            if selectenemy == 1 :       #基本ダメージ
                enemyHPA = ( int(enemyHPA) - int(damage) )
            if selectenemy == 2 :
                enemyHPB = ( int(enemyHPB) - int(damage) )
            if selectenemy == 3 :
                enemyHPC = ( int(enemyHPC) - int(damage) )
            print("敵に"+str(damage)+("のダメージ！"))
            if int(fireturnA) > 0 :          #デバフダメージ
                damage = (random.randrange(6,13))
                enemyHPA =  (int(enemyHPA) - int(damage))
                print('敵Aに ' + str(damage) + 'の'+"\033[38;2;255;0;0m炎\033[0m"+'ダメージ！')
            if int(poisonA) > 0 :
                damage = (random.randrange(4,9))
                enemyHPA = (int(enemyHPA) - int(damage))
                print('敵Aに ' +str(damage) + 'の'+ "\033[38;2;172;3;252m毒\033[0m"+'ダメージ！')
            if int(fireturnB) > 0 :
                damage = (random.randrange(6,13))
                enemyHPB =  (int(enemyHPB) - int(damage))
                print('敵Bに ' + str(damage) + 'の'+"\033[38;2;255;0;0m炎\033[0m"+'ダメージ！')
            if int(poisonB) > 0 :
                damage = (random.randrange(4,9))
                enemyHPB = (int(enemyHPB) - int(damage))
                print('敵Bに ' +str(damage) + 'の'+ "\033[38;2;172;3;252m毒\033[0m"+'ダメージ！')
            if int(fireturnC) > 0 :
                damage = (random.randrange(6,13))
                enemyHPC =  (int(enemyHPC) - int(damage))
                print('敵Cに ' + str(damage) + 'の'+"\033[38;2;255;0;0m炎\033[0m"+'ダメージ！')
            if int(poisonC) > 0 :
                damage = (random.randrange(4,9))
                enemyHPC = (int(enemyHPC) - int(damage))
                print('敵Cに ' +str(damage) + 'の'+ "\033[38;2;172;3;252m毒\033[0m"+'ダメージ！')
            if int(dreinA) > 0 :
                damage = (random.randrange(8+int(atp),13+int(atp)))
                heal = (damage)
                print('体力が'+str(heal)+"回復した!")
                HP = (int(HP)+int(heal))
            if int(dreinB) > 0 :
                damage = (random.randrange(8+int(atp),13+int(atp)))
                heal = (damage)
                print('体力が'+str(heal)+"回復した!")
                HP = (int(HP)+int(heal))
            if int(dreinC) > 0 :
                damage = (random.randrange(8+int(atp),13+int(atp)))
                heal = (damage)
                print('体力が'+str(heal)+"回復した!")
                HP = (int(HP)+int(heal))

            if int(enemyHPA) >= 0 :
                print('敵は生き残っている')
            else :
                print("----------------------")
                print("敵を倒した！")
                win = 1

        elif select == 2 : #防御
            defpow = int(random.randrange(5,9))
            defpow = (defpow * 0.1)
            print("防御力があがった！")

        elif select == 3 : #行動
            actselect = input('''
            回復方法を選べ！
            1.HP回復魔法(MP 10 )        2.HP回復ポーション : '''+ str(HPpotionzansu)+ '''
            3.MP回復ポーション : '''+ str(MPpotionzansu))
            if int(actselect) == 1 :
                if MP >= 10 :
                    heal =(random.randrange(13 + healpow ,37 + healpow ))
                    print("体力が " + str(heal) +"回復した！")
                    HP = (int(HP) + heal)
                    if HP >  ( int(HPwake) * 10 ) :
                        HP =  ( int(HPwake) * 10 )
                    MP = ( int(MP) - 10 )
                else :
                    print('しかしMPが足りなかった！')
            elif int(actselect) == 2 :
                if HPpotionzansu > 0 :
                    if HP > ( int(HPwake) * 10 ) :
                        HP = ( HPwake * 10 )
                else :
                    print('ポーションの数が足りないぞ！')
            elif int(actselect) == 3 :
                if MPpotionzansu > 0 :
                    MP = (MP + 20 + healMPpow)
                    print('体力が' + str(20 + int(healMPpow)) + '回復した！')
                    if MP > ( int(MPwake) * 10 ) :
                        MP = ( MPwake * 10 )
                else :
                    print('ポーションの数が足りないぞ！')

        elif select == 4 : #逃げ
            death = (random.randrange(3))
            death = int(death)
            if death == 1 :
                print("あなたは逃げた...")
                time.sleep(2)
                print("逃げることに成功した！！！")
                enemyHPA = -10
                enemyHPB = -10
                enemyHPC = -10
                nige = 1
            else :
                print("あなたは逃げた...")
                time.sleep(3)
                print("逃げるのに失敗した！"+(30-(level*7)-(enemylevel*3))+"のダメージ！！")
                HP = (HP - 30-(level*7)-(enemylevel*3))
                miss = 1

        elif select == 20221222 :
            enemyHPA = 0
            enemyHPB = 0
            enemyHPC = 0

        if ( enemyHPA <= 0 ) and (enemyHPB <= 0 ) and (enemyHPC <= 0 ):
            ifturnend = 1
        if enemyHPA > 0 : #敵のターン1
            tekiselect = (random.randrange(1,3))
            if tekiselect == 1 :
                if miss == 1 :
                    print("----------------------")
                    print("攻撃は続く...")
                else :
                    print("----------------------")
                    if int(sound) == 1 :
                        display(IPython.display.Audio("MY damege.wav", autoplay=True))
                        print(('''
                        ''')*20)
                    print("敵のターン！")
                    damage = damage_calculation(cold,enemylevel,dep,level,defpow)
                    HP = ( HP - damage)
            elif tekiselect == 2 :
                print("----------------------")
                heal = (random.randrange(8+enemylevel , 12 + enemylevel))
                print('敵が'+str(heal)+'回復した！')
                enemyHPA = (enemyHPA + int(heal))
                if (enemyHPA) > int(eneHPAwake)*10 :
                    enemyHPA = (int(eneHPAwake)*10)

        if enemyHPB > 0 : #敵のターン2
            tekiselect = (random.randrange(1,3))
            if tekiselect == 1 :
                if miss == 1 :
                    print("----------------------")
                    print("攻撃は続く...")
                else :
                    print("----------------------")
                    if int(sound) == 1 :
                        display(IPython.display.Audio("MY damege.wav", autoplay=True))
                        print(('''
                        ''')*20)
                    print("敵Bのターン！")
                    damage = damage_calculation(cold,enemylevel,dep,level,defpow)
                    HP = ( HP - damage)
            elif tekiselect == 2 :
                print("----------------------")
                heal = (random.randrange(8+enemylevel , 12 + enemylevel))
                print('敵Bが'+str(heal)+'回復した！')
                enemyHPB = (enemyHPB + int(heal))
                if (enemyHPB) > int(eneHPBwake)*10 :
                    enemyHPB = (int(eneHPBwake)*10)

        if enemyHPC > 0 : #敵のターン3
            tekiselect = (random.randrange(1,3))
            if tekiselect == 1 :
                if miss == 1 :
                    print("----------------------")
                    print("攻撃は続く...")
                else :
                    print("----------------------")
                    if int(sound) == 1 :
                        display(IPython.display.Audio("MY damege.wav", autoplay=True))
                        print(('''
                        ''')*20)
                    print("敵のターン！")
                    damage = damage_calculation(cold,enemylevel,dep,level,defpow)
                    HP = ( HP - damage)
            elif tekiselect == 2 :
                print("----------------------")
                heal = (random.randrange(8+enemylevel , 12 + enemylevel))
                print('敵Cが'+str(heal)+'回復した！')
                enemyHPC = (enemyHPC + int(heal))
                if (enemyHPA) > int(eneHPCwake)*10 :
                    enemyHPC = (int(eneHPCwake)*10)
        if HP <= 0 :
            print("死んでしまった！")
            enemyHPA = -1
            break

    #戦闘終了
    enemylevel = (enemylevel + 1)
    if nige == 1 :
        plusXP = (random.randrange((1+enemylevel),(3+enemylevel)))
    else  :
        plusXP = (random.randrange((10+enemylevel),(18+enemylevel)))
        plusXP = (plusXP * enemycount)
    nextlevel = (((level * level ) * 5)+5)
    XP = (XP+(plusXP))
    plusXP = str(plusXP)
    print("XPを"+ plusXP + "獲得した！")
    plusXP = int(plusXP)
    moneyplus = (random.randrange((int(enemylevel)*5)+45,(int(enemylevel)*5)+70))
    money = (money + int(moneyplus))
    print('moneyを'+str(moneyplus)+'獲得した！')
    if XP >= nextlevel :   #level up
        level = (level + 1)
        print("レベルが1上がった")
        HPplus = (HPplus + 15)
        MPplus = (MPplus + 20)
        atp = (atp + 4)
        dep = (dep - 0.1)
        healpow = (healpow + 3)
        healMPpow = (healMPpow + 2)
        if level == 3 :
            print('エアブレードを覚えた！')
        elif level == 5 :
            print('ストレングアップを覚えた！')
        elif level == 7 :
            print('ドレインを覚えた！')
    plusXP = (plusXP * enemycount)
    nextlevel = (((level * level ) * 5)+5)
    print("次のレベルまで"+str(int(nextlevel)-int(XP)))
    win = (0)

    print("----------------------")
    replay = input('''もう一度戦う?
    やる→1　やらない→0''')
    replay = int(replay)
    print("----------------------")
    print('保存コードを表示しますか はい→1  いいえ→0')
    saveselect = input()
    if int(saveselect) == 1 :
        name_utf = str(binascii.hexlify(name.encode("utf-16")))
        savecode = (name_utf,XP,nextlevel,enemylevel,money,HPplus,MPplus,atp,dep,healpow,healMPpow,HPpotionzansu,MPpotionzansu)
        print(*savecode)
        print("こぴぺして保存してね！")
#コードの終わり

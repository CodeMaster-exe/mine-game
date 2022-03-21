print('''                                        MINER FRENZY
                          ██████████████████████████████████████                        
                        ██▒▒██    ░░██  ██    ░░██▒▒██    ░░██▓▓██                      
                      ██▒▒  ░░██░░██    ░░██░░██▒▒  ░░██░░██▓▓  ▓▓██                    
                    ██▒▒  ░░  ░░██    ░░  ░░██▒▒  ░░  ░░██▓▓  ▓▓  ▓▓██                  
                    ██████████████████████████████████████████████████                  
                    ██▒▒▒▒▒▒▒▒░░██        ░░██▒▒▒▒▒▒▒▒░░██▓▓▓▓▓▓▓▓▓▓██                  
                      ██▒▒  ░░░░██      ░░░░██▒▒    ░░░░██▓▓  ▓▓▓▓██                    
                        ██▒▒  ░░░░██    ░░░░██▒▒  ░░░░██▓▓  ▓▓▓▓██                      
                          ██▒▒  ░░██    ░░░░██▒▒  ░░░░██▓▓  ▓▓██                        
                            ██▒▒  ░░██  ░░░░██▒▒  ░░██▓▓  ▓▓██                          
                              ██▒▒░░██  ░░░░██▒▒  ░░██▓▓▓▓██                            
        ░░      ░░              ██▒▒░░██  ░░██▒▒░░██▓▓▓▓██                ░░      ░░    
                                  ██▒▒██  ░░██▒▒░░██▓▓██  ░░                            
                                    ██▒▒██░░██▒▒██▓▓██                                  
                                      ████░░██▒▒████                                    
                                    ░░  ██░░██▒▒██        ░░                            
                                          ██████                                      
''')
NUM = 0
num = 0
gem = 0
coin = 0
coin_g_10 = False
coin_g_15 = False
coin_g_100 = False
coin_g_50 = False
dev_pass = '76g51!!@ff47'
dev_PASS = input('Are you dev? If yes please enter pass: ')
while NUM < 1:
    if dev_PASS == dev_pass:
        coin = 999999999
        print(f'Coin = {coin}')
        break
    else:
        print('Wrong pass.')
        break
print('Type start for commands and more.')
while num < 1:
    cmd = input('>>> ')
    cmd = cmd.lower()
    if cmd == 'mine':
        gem = gem + 1
        print(f'+ 1 gem You have {gem} gems.')
    elif cmd == 'start':
        print(f'''Welcome please red the following
        Your progress will NOT be saved
        If you go negative gems GAME OVER
        Possible commands:
        Mine, +1 gem
        Quit, quit the game
        dp mine, + 2 gems
        drill, +5 gems
        tnt, +9 gems and +1 coin
        shop, gives you possible shop items to buy
        beg, +1 coin
        inv, +5 coins -15 gems
        item, shows what you have
        ''')
    elif cmd == 'item':
        print(f'''Your Items:
        Gems: {gem}
        Coins: {coin}     
        ''')
    elif cmd == 'quit':
        print('Gems Reset...')
        break
    elif cmd == 'dp mine':
        gem = gem + 2
        print(f'+ 2 gems You have {gem} gems.')
    elif cmd == 'drill':
        gem = gem + 5
        print(f'+ 5 gems You have {gem} Gems.')
    elif cmd == 'tnt':
        gem = gem + 10 - 1
        coin = coin + 1
        print(f'+ 10 gems + 1 coin You have {gem} gems and {coin} coins. You lost 1 gem')
    elif cmd == 'shop':
        print('''You can Buy the following
        100 gems - cost 10 coins - cmd = bhg
        Mdrill - cost 15 coins - cmd = Mdrill:
        Mdrill gives you ???? of gems
        Nuke - cost 100 coins - cmd = bnuke;
        Gives you ????? gems
        ''')
    elif cmd == 'beg':
        coin = coin + 1
        print(f'+ 1 coin, you have {coin} coins.')
    elif cmd == 'inv':
        coin = coin + 5
        gem = gem - 15
        print(f'+ 5 coins, you have {coin} coins. You lost 15 gems in investing, you have {gem} gems.')

        # SHOP STUFF


    elif coin >= 10:
        coin_g_10 = True
    elif not coin >= 10:
        coin_g_10 = False
    if cmd == 'bhg':
        if coin_g_10:
            gem = gem + 100
            coin = coin - 10
            print(f'+ 100 gems Your balance: {coin} coins, You have {gem} gems.')
        else:
            print(f'Not enough coins your balance: {coin} coins.')


    elif coin >= 15:
        coin_g_15 = True
    elif not coin >= 15:
        coin_g_15 = False
    if cmd == 'mdrill':
        if coin_g_15:
            gem = gem + 792
            coin = coin - 15
            print(f'+ 792 gems Your balance: {coin} coins, You have {gem} gems.')
        else:
            print(f'Not enough coins your balance: {coin} coins.')



    elif coin >= 100:
        coin_g_100 = True
    elif not coin >= 15:
        coin_g_100 = False
    if cmd == 'bnuke':
        if coin_g_100:
            gem = gem + 678391
            coin = coin - 100
            print(f'+ 678391 gems Your balance: {coin} coins, You have {gem} gems.')
        else:
            print(f'Not enough coins your balance: {coin} coins.')


    elif coin >= 50:
        coin_g_50 = True
    elif not coin >= 50:
        coin_g_50 = False
    if gem < 0:
        print("GAME OVER")
        break

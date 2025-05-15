mood=input('Enter your mood(1-happy, 2-sad)off - exit:')
while mood!= 'off':
    if mood=='2':
        print('Do you want a joke?')
        X=input('(1-yes, 2- no)')
        if X=='1':
            print('Why don’t pirates take a shower before they walk the plank?They just wash up on shore.')
        if X=='2':
            print('you can watch a comedy film like(Airplane! (1980))')
    if mood=='1' or '2':    
        talk=input('Do you want to chat?(1-yes, 2-no)')
        if talk =='1':
            y=input('what music do you like?')
            if y=='rock':
                print("'Purple Haze' by Jimi Hendrix")
            if y=='jazz':
                print("Round Midnight")
        if talk=='2':
            print('go to sleep')
            break
    break

                

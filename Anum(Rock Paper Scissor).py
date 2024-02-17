import random
print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
print('  %   *   R O C K   *  P A P E R  *   S C I S S O R   *     % ')
print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
print('            ...!!   LETS START THE GAME   !!...')
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print('#######################################')
        print('Total match:',ma)
        print('Human Score:',hs)
        print('AI Score:',cs)
        if(hs>cs):
            print('congrats you have own')
        elif(cs>hs):
            print('AI Won.... Better luck next time')
        else:
            print('Match Draw')
        print('#######################################')
        break
    c=input('choose  Rock->   Paper->  Scissor->  Stop->stop: ')
    if(c=='p'):
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print('Human :paper','AI:Rock')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Human :win','AI:lost')
                print('---------------------')
            case 12:
                ma=ma+1
                cs=cs+1
                print('Human :paper','AI:Scissor')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Human :lost','AI:won')
                print('---------------------')
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print('Human :paper','AI:Paper')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Match Draw')
                print('--------------------')
    elif(c=='r'):
          point=20+random.randint(1,3)
          match point:
              case 21:
                 ma=ma+1
                 hs=hs+1
                 print('Human :paper','AI:Rock')
                 print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                 print('Human :win','AI:lost')
                 print('---------------------')
              case 22:
                 ma=ma+1
                 cs=cs+1
                 print('Human :paper','AI:Scissor')
                 print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                 print('Human :lost','AI:won')
                 print('---------------------')
              case 23:
                 ma=ma+1
                 hs=hs+1
                 cs=cs+1
                 print('Human :paper','AI:Paper')
                 print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                 print('Match Draw')
                 print('--------------------') 
                   
    elif(c=='s'):
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs=hs+1
                print('Human :paper','AI:Rock')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Human :win','AI:lost')
                print('---------------------')
            case 32:
                ma=ma+1
                cs=cs+1
                print('Human :paper','AI:Scissor')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Human :lost','AI:won')
                print('---------------------')
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print('Human :paper','AI:Paper')
                print('Match:',ma,'Human Score:',hs,'AI Score:',cs)
                print('Match Draw')
                print('--------------------') 
        
    elif(c=='stop'):
         break
print('             *  GAME OVER  *         ')
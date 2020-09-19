
while(1):
    f = open('help.txt')
    anstext=f.read()
    w = open('qwerty.txt', 'w',encoding="cp1251",errors='ignore')
    w.write(anstext)
    f.close()
    w.close()


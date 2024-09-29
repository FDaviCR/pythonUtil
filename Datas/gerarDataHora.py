def cont():
    fim = int(input("Digite o último número a imprimir: "))
    x = 1

    while(x <= fim):
        print(x)
        x = x + 1

def data():
    import time
    agr = time.localtime()
    
    print("%d:" % agr.tm_hour,"%d:" % agr.tm_min,"%d" % agr.tm_sec)
    print("%d/" % agr.tm_mday,"%d/" % agr.tm_mon,"%d" %agr.tm_year)
    print("Dia da semana: %d" % agr.tm_wday)
    print("Dia do ano: %d" % agr.tm_yday)
    print("Horário de verão: %d" % agr.tm_isdst)

#    print(agr.tm_min)
#    print(agr.tm_hour)
#    print(agr.tm_sec)
#    print(agr.tm_mday)
#    print(agr.tm_mon)
#    print(agr.tm_year)
#    print(agr.tm_wday)
#    print(agr.tm_yday)
#    print(agr.tm_isdst)

data()

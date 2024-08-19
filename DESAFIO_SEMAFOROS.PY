import time

# TEMPO SEMÁFOROS

# VERDE_NORTE   =  25
# VERDE_SUL     =  25
# VERDE_LESTE   =  15
# VERDE_OESTE   =  15

# AMARELO_NORTE =  5
# AMARELO_SUL   =  5
# AMARELO_LESTE =  5
# AMARELO_OESTE =  5

# VERMELHO_NORTE=  40
# VERMELHO_SUL  =  40
# VERMELHO_LESTE=  50 
# VERMELHO_OESTE=  50

#sinais

# SINAL_NORTE = ["VERDE", "AMARELO", "VERMELHO"]
# SINAL_SUL   = ["VERDE", "AMARELO", "VERMELHO"]
# SINAL_LESTE = ["VERDE", "AMARELO", "VERMELHO"]
# SINAL_OESTE = ["VERDE", "AMARELO", "VERMELHO"]

# Cores dos semáforos

VERDE =  "\033[0;32;40m VERDE \033[m"
AMARELO = "\033[0;33;40m AMARELO \033[m"
VERMELHO = "\033[0;31;40m VERMELHO \033[m"



#PROGRAMA RODANDO

while True:
    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}   Sinal leste : {}\n".format(VERDE, VERDE, VERMELHO, VERMELHO))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERMELHO, VERMELHO, VERDE, VERDE))
    for cont in range(25, -1, -1):
        print (cont)
        time.sleep(1)


    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}   Sinal leste : {} ".format(AMARELO, AMARELO, VERMELHO, VERMELHO))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERMELHO, VERMELHO, VERDE, VERDE))
    for cont in range(5, -1, -1):
        print (cont)
        time.sleep(1)
    

    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}   Sinal leste : {} ".format(VERMELHO, VERMELHO, VERDE, VERMELHO))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERDE, VERDE, VERMELHO, VERDE))
    for cont in range(15, -1, -1):
        print (cont)
        time.sleep(1)
    

    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}  Sinal leste : {} ".format(VERMELHO, VERMELHO, AMARELO, VERMELHO))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERDE, VERDE, VERMELHO, VERDE))
    for cont in range(5, -1, -1):
        print (cont)
        time.sleep(1)
    

    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}   Sinal leste : {} ".format(VERMELHO, VERMELHO, VERMELHO, VERDE))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERDE, VERDE, VERDE, VERMELHO))
    for cont in range(15, -1, -1):
        print (cont)
        time.sleep(1)
    
    
    print (" Sinal norte : {}   Sinal sul : {}   Sinal oeste : {}   Sinal leste : {} ".format(VERMELHO, VERMELHO, VERMELHO, AMARELO))
    print(" Semaforo pedestre norte : {} semaforo pedestre sul: {} semaforo pedestre oeste: {} semaforo pedestre leste: {}".format(VERDE, VERDE, VERDE, VERMELHO))
    for cont in range(5, -1, -1):
        print (cont)
        time.sleep(1)
    
    
    
   
        




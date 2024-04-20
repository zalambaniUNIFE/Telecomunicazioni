import codaMM1Rit, time, os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


if __name__ == '__main__':
    a=[]
    tm=[]
    try:
        i = open("input.txt", "r")
        Tempo = int(i.readline())
        
        while True:
            Alfa = i.readline()
            TassoMorti = i.readline()
            if not Alfa or not TassoMorti:
                break
            a.append(int(Alfa))
            tm.append(int(TassoMorti))

    except Exception as error:
        print(error, "\n")
        print("errore apertura file di input, inserimento da tastiera")
        Ripetizioni = int(input("Inserire quante volte vuoi ripeterlo: "))
        Tempo = int(input("Inserire il tempo di testing: "))
        Alfa = int(input("Inserire il valore alfa: "))
        TassoMorti = int(input("Inserire il valore mu: "))
        for Nk in range(Ripetizioni):
            a.append(Alfa)
            tm.append(TassoMorti)

    d = open('data.tmp', "w")
    Ripetizioni = len(a)
    
    
    for k in range(len(a)):
        Alfa = a[k]
        TassoMorti = tm[k]
        
        codaMM1Rit.reset()
        stop_threads = False
        
        os.system('cls')
        
        print("Test numero ", k+1, " di ", len(a), "    Fine stimata: ", (timedelta(seconds=Tempo*(Ripetizioni-k)*codaMM1Rit.modi())+datetime.now()).strftime("%H:%M:%S"), " (", timedelta(seconds=Tempo*codaMM1Rit.modi()*(Ripetizioni-k)), ")")
        print("\n    Ora di inizio: ", (datetime.now()).strftime("%H:%M:%S"))
        print("\n    Tempo di esecuzione richiesto: ", timedelta(seconds=Tempo*codaMM1Rit.modi()))
        print("\n    Ora prevista di fine: ", (timedelta(seconds=Tempo*codaMM1Rit.modi())+datetime.now()).strftime("%H:%M:%S"))
        
        threadGen = codaMM1Rit.generaPKG("Generatore", Alfa)
        threadSer = codaMM1Rit.servitore("Servitore", TassoMorti)
        threadCod = codaMM1Rit.coda("coda")
        threadTkinter = codaMM1Rit.grafica("grafica", Alfa, TassoMorti)
        
        threadGen.start()
        threadSer.start()
        threadCod.start()
        threadTkinter.start()

        codaMM1Rit.attendi(Tempo)
        stop_threads = True

        threadGen.kill()
        threadSer.kill()
        threadCod.kill()
        threadTkinter.kill()
            
        threadGen.join()
        threadSer.join()
        threadCod.join()
        threadTkinter.join()
        
        print('\n')
        wS=0.0
        wQ=0.0
        x=[]
        y1=[]
        y2=[]
        for i in range(len(codaMM1Rit.tempoFine())):
            wQ = (wQ + (codaMM1Rit.tempoServizio()[i] - codaMM1Rit.tempoInizio()[i])/codaMM1Rit.modi())
            wS = (wS + (codaMM1Rit.tempoFine()[i] - codaMM1Rit.tempoInizio()[i])/codaMM1Rit.modi())
            x.append(i+1)
            y1.append(wS/(i+1))
            y2.append(wQ/(i+1))
        print('Tempo medio in coda (wQ): ' + str(wQ/len(codaMM1Rit.tempoFine())))
        print('Tempo medio nel sistema (wS): ' + str(wS/len(codaMM1Rit.tempoFine())))
        print('Pacchetti medi in coda (lQ): ' + str((sum(codaMM1Rit.mediaCoda())-codaMM1Rit.mediaCoda()[0])/codaMM1Rit.mediaCoda()[0]))
        print('Pacchetti medi nel sistema (lS): ' + str((sum(codaMM1Rit.mediaSistema())-codaMM1Rit.mediaSistema()[0])/codaMM1Rit.mediaSistema()[0]))

        
        plt.plot(x, y1, label='wS')
        plt.plot(x, y2, label='wQ')
        plt.title("Grafico della media - esecuzione "+str(k))
        plt.xlabel("Pacchetti inviati")
        plt.ylabel("Tempo trascorso")
        plt.legend()
        #plt.show()
        plt.savefig("Esecuzione"+str(k)+".png")
        plt.close()
        
        f = open("Esecuzione"+str(k)+".txt", "w")
        f.write('Valore di alfa: ' + str(Alfa))
        f.write('\nValore di mu: ' + str(TassoMorti))
        f.write('\nTempo medio in coda (wQ): ' + str(wQ/len(codaMM1Rit.tempoFine())))
        f.write('\nTempo medio nel sistema (wS): ' + str(wS/len(codaMM1Rit.tempoFine())))
        f.write('\nPacchetti medi in coda (lQ): ' + str((sum(codaMM1Rit.mediaCoda())-codaMM1Rit.mediaCoda()[0])/codaMM1Rit.mediaCoda()[0]))
        f.write('\nPacchetti medi nel sistema (lS): ' + str((sum(codaMM1Rit.mediaSistema())-codaMM1Rit.mediaSistema()[0])/codaMM1Rit.mediaSistema()[0]))
        f.write('\nPacchetti Inviati: ' + str(len(codaMM1Rit.tempoInizio())))
        f.write('\nPacchetti Serviti: ' + str(len(codaMM1Rit.tempoFine())))
        f.write('\nProbabilità di stato: ')
        tmp = list(set(codaMM1Rit.mediaC[1:]))
        fre = []
        for i in range(len(tmp)):
            fre.append(0)
            
        for i in codaMM1Rit.mediaC[1:]:
            fre[tmp.index(i)] += 1
            
        for i in range(len(tmp)):
            f.write('P('+str(tmp[i])+') = '+str(fre[i]/(len(codaMM1Rit.mediaC)-1))+'\n')
            
        f.close()
        time.sleep(2)

        d.write(str(Alfa)+'\n'
                +str(TassoMorti)+'\n'
                +str(wQ/len(codaMM1Rit.tempoFine()))
                +'\n'+str(wS/len(codaMM1Rit.tempoFine()))
                +'\n'+str((sum(codaMM1Rit.mediaCoda())-codaMM1Rit.mediaCoda()[0])/codaMM1Rit.mediaCoda()[0])
                +'\n'+str((sum(codaMM1Rit.mediaSistema())-codaMM1Rit.mediaSistema()[0])/codaMM1Rit.mediaSistema()[0])
                +'\n')
    d.close()
    os.system('python Grafico.py')

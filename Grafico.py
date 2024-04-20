#GRAFICO

import matplotlib.pyplot as plt
import math, os

def colori(alpha, val):
    try:
        color =['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta','brown', 'pink', 'violet', 'teal', 'gray', 'lime', 'olive', 'indigo','maroon', 'gold', 'silver', 'black']
        tmp = list(set(alpha))
        return color[tmp.index(val)]
    except:
        print("array di alfa troppo grande")
        return 'red'

def graficowQ(alpha, wq, mu):

    for i in range(len(alpha)):
        x=1-math.exp(-(alpha[i]/mu[i]))
        y=wq[i]*mu[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(alpha,alpha[i]))
    
    asseX=[]
    for i in range(1, 1000):
        asseX.append(float(i)/1000)

    tmp = list(set(alpha))
    assiY=[[]]
    i=0
    for alf in tmp:
        assiY.append([])
        for ro in asseX:
            assiY[i].append((alf)/ro)
        plt.plot(asseX, assiY[i], label='alpha='+str(alf)+'pkt/s', color=colori(alpha,alf))

        i += 1

    plt.title("Grafico teorico di wQ al variare di ro fissato alpha")
    plt.ylabel("wQ*mu^2+mu")
    plt.xlabel("ro")
    plt.legend()
    plt.savefig('log/Grafico teorico di wQ al variare di ro fissato alpha.png')
    plt.show()
    plt.close()

def graficowQa(alpha, wq, mu):

    for i in range(len(alpha)):
        x=alpha[i]
        y=wq[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(mu,mu[i]))
    
    asseX=[]
    for i in range(1, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(mu))
    assiY=[[]]
    i=0
    for mo in tmp:
        assiY.append([])
        for alf in asseX:
            ro=1-math.exp(-(alf/mo))
            assiY[i].append((alf-ro*mo)/(mo**2*ro))
        plt.plot(asseX, assiY[i], label='mu='+str(mo)+'pkt/s', color=colori(mu,mo))

        i += 1

    plt.title("Grafico teorico di wQ al variare di alpha")
    plt.ylabel("wQ")
    plt.xlabel("alpha")
    plt.legend()
    plt.savefig('log/Grafico teorico di wQ al variare di alpha.png')
    plt.show()
    plt.close()

def graficowQm(alpha, wq, mu):

    for i in range(len(mu)):
        x=mu[i]
        y=wq[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(alpha,alpha[i]))
    
    asseX=[]
    for i in range(1000, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(alpha))
    assiY=[[]]
    i=0
    for alf in tmp:
        assiY.append([])
        for mo in asseX:
            ro=1-math.exp(-(alf/mo))
            assiY[i].append((alf-ro*mo)/(mo**2*ro))
        plt.plot(asseX, assiY[i], label='alpha='+str(alf)+'pkt/s', color=colori(alpha,alf))

        i += 1

    plt.title("Grafico teorico di wQ al variare di mu")
    plt.ylabel("wQ")
    plt.xlabel("mu")
    plt.legend()
    plt.savefig('log/Grafico teorico di wQ al variare di mu.png')
    plt.show()
    plt.close()

def graficowS(alpha, ws, mu):

    for i in range(len(alpha)):
        x=1-math.exp(-(alpha[i]/mu[i]))
        y=ws[i]*(mu[i]**2)
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(alpha,alpha[i]))
    
    asseX=[]
    for i in range(1, 1000):
        asseX.append(float(i)/1000)

    tmp = list(set(alpha))
    assiY=[[]]
    i=0
    for alf in tmp:
        assiY.append([])
        for ro in asseX:
            assiY[i].append((alf)/ro)
        plt.plot(asseX, assiY[i], label='alpha='+str(alf)+'pkt/s', color=colori(alpha,alf))

        i += 1

    plt.title("Grafico teorico di wS al variare di ro fissato alpha")
    plt.ylabel("wS*mu^2")
    plt.xlabel("ro")
    plt.legend()
    plt.savefig('log/Grafico teorico di wS al variare di ro fissato alpha.png')
    plt.show()
    plt.close()
    
def graficowSa(alpha, ws, mu):

    for i in range(len(alpha)):
        x=alpha[i]
        y=ws[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(mu,mu[i]))
    
    asseX=[]
    for i in range(1, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(mu))
    assiY=[[]]
    i=0
    for mo in tmp:
        assiY.append([])
        for alf in asseX:
            ro=1-math.exp(-(alf/mo))
            assiY[i].append((alf)/((mo**2)*ro))
        plt.plot(asseX, assiY[i], label='mu='+str(mo)+'pkt/s', color=colori(mu,mo))

        i += 1

    plt.title("Grafico teorico di wS al variare di alpha")
    plt.ylabel("wS")
    plt.xlabel("alpha")
    plt.legend()
    plt.savefig('log/Grafico teorico di wS al variare di alpha.png')
    plt.show()
    plt.close()

def graficowSm(alpha, ws, mu):

    for i in range(len(mu)):
        x=mu[i]
        y=ws[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(alpha,alpha[i]))
    
    asseX=[]
    for i in range(1000, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(alpha))
    assiY=[[]]
    i=0
    for alf in tmp:
        assiY.append([])
        for mo in asseX:
            ro=1-math.exp(-(alf/mo))
            assiY[i].append((alf)/((mo**2)*ro))
        plt.plot(asseX, assiY[i], label='alpha='+str(alf)+'pkt/s', color=colori(alpha,alf))

        i += 1

    plt.title("Grafico teorico di wS al variare di mu")
    plt.ylabel("wS")
    plt.xlabel("mu")
    plt.legend()
    plt.savefig('log/Grafico teorico di wS al variare di mu.png')
    plt.show()
    plt.close()

def graficolQa(alpha, lq, mu):

    for i in range(len(alpha)):
        x=alpha[i]
        y=lq[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(mu,mu[i]))
    
    asseX=[]
    for i in range(1, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(mu))
    assiY=[[]]
    i=0
    for mo in tmp:
        assiY.append([])
        for alf in asseX:
            ro=1-math.exp(-(alf/mo))
            assiY[i].append((alf-ro*mo)/mo)
        plt.plot(asseX, assiY[i], label='mu='+str(mo)+'pkt/s', color=colori(mu,mo))

        i += 1

    plt.title("Grafico teorico di lQ al variare di alpha")
    plt.ylabel("lQ")
    plt.xlabel("alpha")
    plt.legend()
    plt.savefig('log/Grafico teorico di lQ al variare di alpha.png')
    plt.show()
    plt.close()

def graficolSa(alpha, ls, mu):

    for i in range(len(alpha)):
        x=alpha[i]
        y=ls[i]
        plt.plot(x,y, marker='o', markersize=5, linestyle='', color=colori(mu,mu[i]))
    
    asseX=[]
    for i in range(1, 30000):
        asseX.append(float(i)/1000)

    tmp = list(set(mu))
    assiY=[[]]
    i=0
    for mo in tmp:
        assiY.append([])
        for alf in asseX:
            assiY[i].append(alf/mo)
        plt.plot(asseX, assiY[i], label='mu='+str(mo)+'pkt/s', color=colori(mu,mo))

        i += 1

    plt.title("Grafico teorico di lS rispetto ad alpha")
    plt.ylabel("lS")
    plt.xlabel("alpha")
    plt.legend()
    plt.savefig('log/Grafico teorico di lS rispetto ad alpha.png')
    plt.show()
    plt.close()

def disegnaGrafici():
    wq=[]
    ws=[]
    alf=[]
    mu=[]
    lq=[]
    ls=[]
    try:
        i = open("data.tmp", "r")
        while True:
            Alfa = i.readline()
            TassoMorti = i.readline()
            WQ = i.readline()
            WS = i.readline()
            LQ = i.readline()
            LS = i.readline()
            if not Alfa or not TassoMorti or not WQ or not WS or not LQ or not LS:#or not LQ
                break
            alf.append(int(Alfa))
            mu.append(int(TassoMorti))
            wq.append(float(WQ))
            ws.append(float(WS))
            lq.append(float(LQ))
            ls.append(float(LS))

        i.close()
        #delete = input("Vuoi eliminare il file con i dati?(N/y)")
        delete = "y"
        if delete=="y":
            try:
                os.remove('data.tmp')
            except Exception as error:
                print("Errore eliminazione file: ", error, "\n")
        
        graficowQ(alf, wq, mu)
        graficowQa(alf, wq, mu)
        graficowQm(alf, wq, mu)
        graficowS(alf, ws, mu)
        graficowSa(alf, ws, mu)        
        graficowSm(alf, ws, mu)
        graficolQa(alf, lq, mu)
        graficolSa(alf, ls, mu)
        
    except Exception as error:
        print("Error: ", error, "\n")

if __name__ == '__main__':
    disegnaGrafici()

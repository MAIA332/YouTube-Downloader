from pytube import YouTube
import os

def to_mp4(url,path):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(path)

def to_audio(url, format_,path):
    youtube = YouTube(url).streams.filter(only_audio=True).first()
    out_file = youtube.download(path)
    base,ex = os.path.splitext(out_file) 
    new_file = base + format_
    os.rename(out_file, new_file) 
    print(f'\n --------------------- \n O arquivo: {base}{ex} convertido para {new_file} foi baixado em {path}')


if __name__ == '__main__':

    while True:

        os.system('cls')

        while True:
            try:
                url = input('URL: ')
                op = int(input('\n 1-- MP3 \n 2-- MP4 \n 3-- WAV \n formato: '))

                print('--------------------')

                path_c = input('Deseja personalizar o caminho? o padrão será a pasta deste arquivo (s/n): ')
                break
            
            except:
                print('\n Não foi possivel continuar, verifique a opção e tente novamente \n')

        try:
            while True:

                if path_c == 's':
                    print('\n Para criar uma pasta no diretorio atual apenas digite o nome da pasta e pressione enter')
                    print('\n Para especificar uma pasta, insira seu caminho absoluto \n')
                    path = input('Digite o caminho:  ')
                    break

                elif path_c == 'n':
                    path = os.path.dirname(os.path.realpath(__file__))
                    break

                else:
                     print(f'\n Desculpe, não entendi {path}, tente corrigir a escrita, a barra deve ser normal: /')
        
        except Exception as e:

            os.system('cls')
            print(f' \n -- Não foi possivel prosseguir devido ao seguinte erro : \n \n {e}')

        try:
            while True:

                if op == 1:
                    to_audio(url,format_='.mp3',path=path)
                    break

                elif op == 2:
                    to_mp4(url,path=path)
                    break

                elif op ==3:
                    to_audio(url,format_='.wav',path=path)
                    break

                else:
                    print(f'\n Desculpe, não entendi {op}')
        
        except Exception as e:

            os.system('cls')
            print(f' \n -- Não foi possivel prosseuir devido ao seguinte erro : \n \n {e}')
        
        print('-------------------- \n')

        op = input('Deseja continuar? (s/n): ')

        if op == 's':
            pass
        elif op =='n':
            exit()



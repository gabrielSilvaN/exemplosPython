from pygame import mixer

mixer.init()

mixer.music.load("D:\\Gabriel\\Músicas\\Black Sabbath\\Black Sabbath Vol. 4\\03 Changes.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print('Pressione "p" para pausar e "r" para iniciar novamente')
    print('Pressione "e" para fechar o programa')

    query = input(">>>")
    if query == 'p':
        mixer.music.pause()

    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
        



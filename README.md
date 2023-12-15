# SEL0337

RFID


Na prática foi configurado um circuito com a Raspberry Pi, incorporando o módulo RFID-RC522. A comunicação SPI foi ativada, e a biblioteca Python do módulo RFID foi instalada para gravação dos NUSP na TAG RFID para posterior leitura em um circuito com LED.
Ao aproximar uma Tag do leitor RFID, aciona LEDs verde indicando acesso liberado ou vermelho indicando acesso negado com base no ID cadastrado. O funcionamento do sistema é demonstrado no GIF a seguir, em que é aproximado uma TAG com chave diferente da cadastrada.

https://github.com/VictorMRMP/SEL0337/assets/83428029/bc12f847-c35b-424c-b9f7-a19e05c2cdf1

Câmera


A câmera foi integrada à Raspberry Pi e testada por meio do libcamera-hello, Haar Cascade e as bibliotecas Python OpenCV e PiCamera2 foram utilizadas para detecção facial.

![WhatsApp Image 2023-12-15 at 14 49 48](https://github.com/VictorMRMP/SEL0337/assets/83428029/2b2d97d0-6e9b-4bd6-beaf-c21fc2338e5f)

Em seguida foi adicionado a função de mostrar o NUSP da dupla na janela de detecção dos rostos.

![WhatsApp Image 2023-12-15 at 14 49 48 (1)](https://github.com/VictorMRMP/SEL0337/assets/83428029/5379b3aa-8bc4-4161-bed8-959dbb85da99)

# Desafios Target Ribeirão

<a><img src='https://github.com/Nurux/Target_test_ribeirao/blob/main/media_demo/img_ilustrativa.png'></a>

<a href="https://github.com/Nurux/Target_test_ribeirao/blob/main/media_demo/Target_ribeirao.mp4">Video demonstrativo</a>

## Tem duas versões do codigo disponivel!
    - 1° No modo terminal 
    - 2° Com interface grafica

A versão relatada no video e imagem demonstrativa trata-se da versão de interface grafica que por sua vez usa a lib PySimpleGUI.
Pra executar esta versão deve-se instalar a lib, caso use o pip o comando é: 

    pip install PySimpleGUI

ou caso use Linux/Mac:

    pip3 install PySimpleGUI


---

### Respostas dos desafios

### 1 
Observe o trecho de código abaixo:

````
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça {

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
````

Ao final do processamento, qual será o valor da variável SOMA?

<font color="red">*RESP:* </font> 94

---

### 2 
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

<font color="red">*RESP:*</font> Olhar arquivo main.py em qualquer versão e executa-lo

---

### 3 
Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____

#

<font color="red">*RESP:*</font>
 - a = 9
 - b = 128
 - c = 49
 - d = 100
 - e = 13
 - f = 200

---

### 4 
Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

#

<font color="red">*RESP:*</font>
quando o carro e o caminhao se cruzarem eles estarão na metade do caminho entre as duas cidades, que é de 50 km de cada uma.

O carro levará 50 km / 110 km/h = 0,45 horas = 27 minutos para chegar ao ponto de cruzamento.

O caminhão levará 50 km / 80 km/h + 2 x 5 minutos = 0,75 horas = 45 minutos para chegar ao ponto de cruzamento.

Portanto, o carro estará mais próximo de Ribeirão Preto quando os veículos se cruzarem, pois levará menos tempo para chegar ao ponto de cruzamento.

---

### 5
Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

<font color="red">*RESP:*</font> Olhar arquivo main.py e executa-lo

# TAG - Engenharia Reversa

Para zerar o jogo e resgatar as flags, a ideia era fazer engenharia reversa do programa.

## Ajustes iniciais

Observando a estrutura do programa pelo Ghidra, observamos que ele executa as funções em certa ordem.

![Untitled](images/Untitled.png)

Para poder analisar melhor, criei esses três arquivos de flag localmente para o programa parar de reclamar e sobreescrevi os hexadecimais da função **alarm(10)**, dentro da **setup()**, e do **ptrace**.

## Level 1

Assim que você executa o game, ele te pergunta seu nome e o serial. Nesse momento apenas coloquei **epic_dijkstra**, que é o nick do meu time, e o serial **2910000-3076-5273-1**.

Esse serial foi descoberto analisando a função **level1()**.

As informações eram:

- O serial tem 20 caracteres
- Os ‘tokens’ do serial são separados por traços (-)
- São 4 tokens
- O primeiro é múltiplo de 291
- O segundo é 3076
- O terceiro é 5273
- O quarto é 1

Ou seja, bastou completar o primeiro token com zeros até o tamanho total ficar 19 (levando em conta que o 20º caracter seria um \n).

Ao resolver no servidor resgatamos a flag:

```
gris{welcome_aboard_pirate}
```

## Level 2

Aqui estamos em um labirinto. Se você encontra uma parede, você morre e o programa finaliza. Além disso existem coordenas de caminho normal, munição (mais 1 bala), inimigo (menos 1 bala e menos 10 de HP) e boss (level 3). Para andar basta enviar **wasd**.

Nessa etapa eu fiz um script em python para resolver de forma semi-automática. Ele tentava os caminhos para mim e eu ia desenhando o mapa no photoshop. Só fiz isso porque sabia que era um mapa pequeno 25x25, ou seja, 625 blocos no total. Achei bonitinho desenhar o mapa todo.

![Untitled](images/Untitled%201.png)

Legenda:

- **Azul**: Início
- **Cinza**: Caminho
- **Preto**: Parede
- **Amarelo**: Munição
- **Vermelho**: Inimigo
- **Verde**: Boss

Ao chegar no boss no servidor, resgatamos a flag:

```
gris{nice_maze_solver_you_have}
```

## Level 3

Chegando no boss os comandos aqui são simples, ‘a’ para atacar e ‘b’ para bloquear (que no caso não adianta de nada). 

O primeiro ponto aqui é que o boss tem 5HP, então você precisa ter no mínimo 5 balas. O segundo, é que ele tem 5% de chance de errar o ataque, então se você der sorte o suficiente dele errar 4 ataques, você consegue matar ele mandando sempre um ‘a’.

O último ponto e crucial, é que essa RNG é definida a partir de uma seed no srand(). Portanto para uma seed igual, o comportamento do boss sempre será o mesmo.

Com isso em mente, fiz um programa em C (**seedfinder.c**) com a mesma lógica observada pelo Ghidra para gerar a seed. Essa seed é gerada a partír do nome que você escolhe no começo do jogo.

Basicamente eu uso o nome da equipe e faço um bruteforce de um append até gerar uma seed em que de 5 ataques, o boss erre 4.

Importante ressaltar que tive que maximizar a eficiência do programa, tirando funções como **puts()**, **printf()** e **rand()** desnecessárias, e fazendo ele escrever num arquivo quando encontrasse a seed perfeita.

O nick que gera a seed ideal encontrado foi: **epic_dijkstra.4441990**

Ao utilizar o resolver.py, ou o comando:

```
printf 'epic_dijkstra.4441990\n2910000-3076-5273-1\nw\nw\na\na\nw\nw\nw\nw\nw\nw\nw\nw\nw\nd\nw\nw\nw\nw\ns\ns\ns\ns\na\ns\ns\ns\ns\ns\ns\na\na\na\ns\na\na\na\na\na\na\ns\na\na\na\nd\nd\nd\nw\nw\nw\na\nw\nw\na\na\na\na\na\nw\na\nd\nw\nw\nw\nw\nw\nw\na\nw\na\nw\nw\nw\nw\nw\na\na\nw\nw\na\na\na\na\na\n' | nc 35.184.230.50 3000
```

Encontramos a última flag:

```
gris{congratz_here_are_the_credits}
```

![Untitled](images/Untitled%202.png)
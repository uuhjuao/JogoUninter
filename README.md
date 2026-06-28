# Attack on Shinobi

Attack on Shinobi é um jogo 2D desenvolvido em Python utilizando a biblioteca Pygame como trabalho da disciplina de Programação Orientada a Objetos.

O objetivo do jogo é sobreviver durante 60 segundos enfrentando inimigos que surgem continuamente dos dois lados da tela. Ao final da partida, o jogador pode visualizar suas estatísticas e seu desempenho é salvo em um ranking local.

## Funcionalidades

- Menu principal
- Tela de inserção do nome do jogador
- Tela de controles
- Movimentação do personagem
- Sistema de ataque
- Inimigos com IA simples
- Sistema de vidas
- Contador de tempo
- Contador de inimigos derrotados (Kills)
- Tela de vitória e derrota
- Sistema de Score utilizando JSON
- Música de menu e música durante a partida

## Tecnologias utilizadas

- Python 3.11
- Pygame 2.6
- JSON (armazenamento do ranking)
- Programação Orientada a Objetos (POO)

## Bibliotecas utilizadas

```python
pygame
json
random
pathlib
```

## Estrutura do projeto

```
├── asset/             # Imagens e músicas
├── code/              # Classes do jogo
├── score.json         # Ranking dos jogadores
├── main.py            # Arquivo principal
```

## Como executar

1. Clone este repositório.
2. Instale as dependências:

```bash
pip install pygame
```

3. Execute o projeto:

```bash
python main.py
```

Ou utilize o executável (`.exe`) disponível na pasta de distribuição.

## Autor

**João Marçião**

RU: **5174119**

Projeto desenvolvido para fins acadêmicos.

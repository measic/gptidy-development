### Respostas:
### Menor Mulher Morreu: 2 anos
### Menor Mulher Sobreviveu: 7 meses

### Menor Homem Morreu: 1 ano
### Menor Homem Sobreviveu: 4 meses


### Maior Mulher Morreu: 57 anos
### Maior Mulher Sobreviveu: 63 anos

### Maior Homem Morreu: 74 anos
### Maior Homem Sobreviveu: 80 anos
print_full(train.groupby(['Sobreviventes','Idade','Sexo']).size())
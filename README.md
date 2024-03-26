# Kaggle Titanic

Repositório com propósito didático contendo o passo a passo para tratamento dos dados e geração de submissões ao Kaggle. São testadas algumas metodologias de limpeza dos dados, assim como são utilizados os algoritmos de Árvore de Decisão e Rede Neural, obtendo 0.775 e 0.804 de acurácia, respectivamente.

## Utilizando o projeto

Os dados originais estão dentro de `data/original`, enquanto a pasta `data/processed` contém os resultados de processamento feitos nos notebooks. Já a pasta `data/submissions` contém os envios realizados ao Kaggle.

A pasta `src`, por sua vez, contem em ordem os notebooks com os tratamentos dos dados e criação dos algoritmos. As bibliotecas utilizadas podem ser encontradas em `requirements.txt`. 

> Para executar corretamente este projeto, utilizar as versões 3.10 ou 3.11 do Python. Utilizar versões anteriores poderá trazer erros nos tratamentos dos dados e versões posteriores, como a 3.12, possivelmente terão problemas na execução do modelo de Rede Neural.
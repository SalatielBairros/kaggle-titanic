import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

SEED = 5
np.random.seed(SEED)

treino = pd.read_csv('https://raw.githubusercontent.com/SalatielBairros/kaggle-titanic/main/data/processed_v2/train_dummies_2.csv')
teste = pd.read_csv('https://raw.githubusercontent.com/SalatielBairros/kaggle-titanic/main/data/processed_v2/test_dummies_2.csv')
Xvalidation = teste.drop(columns=['PassengerId'])
treino.head(2)

X = treino.drop(columns=['Survived'])
y = treino['Survived']

treino_x, teste_x, treino_y, teste_y = train_test_split(X, y, test_size = 0.2, stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

best_params = {
    'criterion': 'gini',
    'max_depth': 35,
    'min_samples_split': 4,
    'min_samples_leaf': 4,
    'n_estimators': 25,
    'random_state': SEED
}

modelo = RandomForestClassifier(**best_params)
modelo.fit(X, y)
predicoes = modelo.predict(Xvalidation)
resultado = pd.DataFrame()
resultado['PassengerId'] = teste['PassengerId']
resultado['Survived'] = predicoes
resultado.to_csv('./data/submissions/current_best_model.csv', index=False)

print(modelo)
from sklearn import tree
"""
    label:
        carro-esporte = 0
        minivan = 1
"""

features = [[300, 2], [450, 2], [200, 8], [150, 9]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

predicao = clf.predict([[450, 2]])

resultado = ['Carro esporte', 'Minivan'][int(predicao)]
print(f'{resultado}')

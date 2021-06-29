#decode the additives in your food
#E numbers are given to chemicals which have complex names.The numbering system was put into place in the 1960s,which each additive number based on its properties.these are prefixed with an E for Europe.
#Example : Aliminium : E173

Enumber = int(input('Enter the E number behind the snack package to decode additive : '))

if Enumber in range(100,200):
    print('Food colours')
elif Enumber in range(200,300):
    print('Preservatives')
elif Enumber in range(300,400):
    print('Antioxidants')
elif Enumber in range(400,500):
    print('Thickeners,emulsifiers and stabilisers')
elif Enumber in range(500,600):
    print('Acidity,regulators and anti-caking agents')
elif Enumber in range(600,700):
    print('Flavour enhancers')
elif Enumber in range(700,900):
    print('Sweeteners,foaming agents and gases')
#!/Users/morgan/opt/miniconda3/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataframe = pd.read_csv("iris.csv")

def regression(df):
    """
    Module to regress petal length against sepal length for Iris dataset.

    Parameters
    ----------
    df: dataframe
        The data frame containing your data of interest. Must have columns "petal_length_cm" and "seapl_length_cm" within the dataframe.

    Returns
    -------

    regression
        The regression object containing the slope and intercept of your regression, and other regression parameters.

    Examples
    --------
    >>> regression(versicolor)
    regression
    """

#    x = df.petal_length_cm
#    y = df.sepal_length_cm    
#    regression = stats.linregress(x, y)
#    return regression 



#if __name__ == '__main__':
#    regression = regression(df)
    



#versicolor
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
versx = versicolor.petal_length_cm
versy = versicolor.sepal_length_cm
vers_reg = stats.linregress(versx, versy)
plt.scatter(versx, versy, label = 'Data')
plt.plot(versx, vers_reg.slope * versx + vers_reg.intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("versicolor_petal_v_sepal_length_regress.png")



#setosa
setosa = dataframe[dataframe.species == "Iris_setosa"]
setx = setosa.petal_length_cm
sety = setosa.sepal_length_cm
plt.scatter(setx, sety, label = 'Data')
set_reg = stats.linregress(setx, sety)
plt.plot(setx, set_reg.slope * setx + set_reg.intercept, color = "purple", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("setosa_petal_v_sepal_length_regress.png")




#virginica
virginica = dataframe[dataframe.species == "Iris_virginica"]
virgx = virginica.petal_length_cm
virgy = virginica.sepal_length_cm
virg_reg = stats.linregress(virgx, virgy)
plt.scatter(virgx, virgy, label = 'Data')
plt.plot(virgx, virg_reg.slope * virgx + virg_reg.intercept, color = "red", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("virginica_petal_v_sepal_length_regress.png")



#remember modular code, functions, docstrings, descriptive variable names, make importable



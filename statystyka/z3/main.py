import numpy as np
import pandas as pd
from scipy.stats import shapiro, ttest_ind, ttest_1samp, bartlett, ttest_rel

def perform_ttest_1samp(data, expected_value, alpha=0.05):
    t_statistic, p_value = ttest_1samp(data, expected_value)
    print(f"\nWyniki jednopoprzecznych testów t:")
    print(f"Statystyka t: {t_statistic}")
    print(f"Wartość P: {p_value}")
    if p_value < alpha:
        print("Odrzuć hipotezę zerową. Istnieją istotne różnice.")
    else:
        print("Brak powodu do odrzucenia hipotezy zerowej. Brak istotnych różnic.")

def perform_shapiro_test(data, column_name, alpha=0.05):
    stat, p_value = shapiro(data)
    print(f"\nWyniki testu Shapiro-Wilka dla '{column_name}':")
    print(f"Statystyka: {stat}")
    print(f"Wartość P: {p_value}")
    if p_value < alpha:
        print(f"Odrzuć hipotezę zerową dla '{column_name}'. Zmienna nie pochodzi z rozkładu normalnego.")
    else:
        print(f"Brak powodu do odrzucenia hipotezy zerowej dla '{column_name}'. Zmienna pochodzi z rozkładu normalnego.")

def perform_ttest_ind(data1, data2, var_names, alpha=0.05):
    t_statistic, p_value = ttest_ind(data1, data2, equal_var=False)
    print(f"\nWyniki testu t niezależnego dla {var_names}:")
    print(f"Statystyka t: {t_statistic}")
    print(f"Wartość P: {p_value}")
    if p_value < alpha:
        print("Odrzuć hipotezę zerową. Istnieją istotne różnice w średnich.")
    else:
        print("Brak powodu do odrzucenia hipotezy zerowej. Brak istotnych różnic w średnich.")

def perform_bartlett_test(data1, data2, var_names, alpha=0.05):
    stat, p_value = bartlett(data1, data2)
    print(f"\nWyniki testu Bartletta dla {var_names}:")
    print(f"Statystyka: {stat}")
    print(f"Wartość P: {p_value}")
    if p_value < alpha:
        print("Odrzuć hipotezę zerową. Istnieją istotne różnice w wariancjach.")
    else:
        print("Brak powodu do odrzucenia hipotezy zerowej. Brak istotnych różnic w wariancjach.")

def perform_ttest_rel(data1, data2, var_name, alpha=0.05):
    t_statistic, p_value = ttest_rel(data1, data2)
    print(f"\nWyniki sparowanego testu t dla {var_name}:")
    print(f"Statystyka t: {t_statistic}")
    print(f"Wartość P: {p_value}")
    if p_value < alpha:
        print(f"Odrzuć hipotezę zerową dla {var_name}. Istnieją istotne różnice w średnich.")
    else:
        print(f"Brak powodu do odrzucenia hipotezy zerowej dla {var_name}. Brak istotnych różnic w średnich.")

# Zadanie 1
print("\nZadanie 1")
mean, std_dev, num_elements = 2, 30, 200
sample = np.random.normal(mean, std_dev, num_elements)
perform_ttest_1samp(sample, 2.5)

# Zadanie 2
print("\nZadanie 2")
df = pd.read_csv('napoje.csv', delimiter=';')
df.columns = df.columns.str.strip()
perform_ttest_1samp(df['lech'], 60500)
perform_ttest_1samp(df['cola'], 222000)
perform_ttest_1samp(df['regionalne'], 43500)

# Zadanie 3
print("\nZadanie 3")
for column in df.columns[2:]:
    perform_shapiro_test(df[column], column)

# Zadanie 4
print("\nZadanie 4")
pairs = [('okocim', 'lech'), ('fanta', 'regionalne'), ('cola', 'pepsi')]
for var1, var2 in pairs:
    perform_ttest_ind(df[var1], df[var2], f"{var1} i {var2}")

# Zadanie 5
print("\nZadanie 5")
pairs = [('okocim', 'lech'), ('żywiec', 'fanta'), ('regionalne', 'cola')]
for var1, var2 in pairs:
    perform_bartlett_test(df[var1], df[var2], f"{var1} i {var2}")

# Zadanie 6
print("\nZadanie 6")
group_2001 = df[df['rok'] == 2001]['regionalne']
group_2015 = df[df['rok'] == 2015]['regionalne']
perform_ttest_ind(group_2001, group_2015, "regionalne między 2001 a 2015")

# Zadanie 7
print("\nZadanie 7")
df_reklama = pd.read_csv('napoje_po_reklamie.csv', delimiter=';')
df_reklama.columns = df_reklama.columns.str.strip()

cola_2016 = df[df['rok'] == 2016]['cola']
fanta_2016 = df[df['rok'] == 2016]['fanta']
pepsi_2016 = df[df['rok'] == 2016]['pepsi']

cola_po_reklamie = df_reklama['cola']
fanta_po_reklamie = df_reklama['fanta']
pepsi_po_reklamie = df_reklama['pepsi']

perform_ttest_rel(cola_2016, cola_po_reklamie, "cola")
perform_ttest_rel(fanta_2016, fanta_po_reklamie, "fanta")
perform_ttest_rel(pepsi_2016, pepsi_po_reklamie, "pepsi")

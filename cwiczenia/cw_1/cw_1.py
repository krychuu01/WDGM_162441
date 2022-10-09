import numpy as np

# ZADANIA

# 1. Utworzyć tablicę zawierającą 50 piątek

arr = np.ones(50)
arr.fill(5)

print(f'ZAD 1. : \n {arr}')

# 2. Utworzyc tablice o rozmiarze 5x5 z wartosciami od 1 do 25

arr = np.arange(1, 26)
arr = arr.reshape(5, 5)
TABLICA_Z_ZADANIA_2 = arr

print(f'ZAD 2. : \n {arr}')

# 3. Utworzyc tablicę liczb parzystych od 10 do 50

arr = np.arange(10, 50, 2)
print(f'ZAD 3. : \n {arr}')

# 4. Utworzyc macierz, w ktorej na przekątnej znajdą się
# wartości równe 8, a pozostale będą wynosiły 0

arr = np.diag([8, 8, 8])
print(f'ZAD 4. : \n {arr}')

# 5. Utworzyc tablice o rozmiarze 10x10 z wartosciami zwiekszajacymi sie o 0.01

arr = np.arange(0, 1, 0.01, dtype='f').reshape(10, 10)
print(f'ZAD 5. : \n {arr}')

# 6. Utworzyc przestrzen liniowa 50 wartosci z zakresu 0-1

lin = np.linspace(0, 1, 50)
print(f'ZAD 6. : \n {lin}')

# 7. Wybrać podtablice 12-elementową, z tablicy utworzonej w zadaniu 2, z wartosciami w zakresie 12-25

print(f'ZAD 7. : \n {TABLICA_Z_ZADANIA_2[2:5, 1:5]}')

# 8. Wybrać 3 pierwsze elementy z ostatniej kolumny tablicy utworzonej w zadaniu 2, a nastepnie ułożyć z nich kolumne

print(f'ZAD 8. : \n {TABLICA_Z_ZADANIA_2[0:3, 4].reshape(3, 1)}')

# 9. Wyznaczyć sumę wartości elementów znajdujących się w dwóch ostatnich wierszach macierzy utworzonej w zadaniu 2

print(f'ZAD 9. : \n {(TABLICA_Z_ZADANIA_2[3, :] + TABLICA_Z_ZADANIA_2[4, :]).sum()}')

# 10. Przygotować skrypt, który stworzy tensor zawierający losowe wartości całkowite, losowym wymiarze
# i losowym rozmiarze każdego z wymiarów

# jak to zrobić?

rand1 = np.random.randint(1, 5)
rand2 = np.random.randint(1, 5)
rand3 = np.random.randint(1, 5)

arr = np.random.randint(1, 50, (rand1, rand2, rand3))
print(f'TEST 10: \n {arr}')


segundo= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, ..., 57, 58, 59, 60)
hora= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
día= (1,2,3,4)
minuto = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, ..., 57, 58, 59, 60)
horas_a_minutos = hora[4] * 60
días_a_horas = día * 24
minutos_a_horas = minuto * 60
horas_a_días = hora / 24
minutos_a_segundos = minuto  60
segundos_a_minutos= segundo / 60



print(día[1], 'días tienen', (día[1]*hora[23]), 'horas')

print( (hora[4]),'horas tienen', (minutos_a_segundos))
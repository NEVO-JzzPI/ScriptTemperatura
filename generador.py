import numpy as np

# rango de temperatura y humedad

temperatura_rango = np.arange(-1,31)
humedad_rango = np.arange(0,101)

#Probabilidades
probabilidades_temperatura = []
probabilidades_humedad = []

#70% de 18 a 24 grados y 30% el resto en temperatura
conteo_t_favorables = len(np.arange(18, 25))
conteo_t_restantes = len(temperatura_rango) - conteo_t_favorables

# 70% de probabilidad para el rango favorable de humedad (70 a 90) y 30% para el resto
conteo_h_favorables = len(np.arange(70, 91))
conteo_h_restantes = len(humedad_rango) - conteo_h_favorables

# Cada grado entre 18-24 tiene ~10% de probabilidad y cada uno de los otros grados tiene ~1.2% de probabilidad
prob_tem_alta = 0.70 / conteo_t_favorables  
prob_tem_baja = 0.30 / conteo_t_restantes   

# Cada porcentaje de humedad entre 70-90 tiene ~3.5% de probabilidad y cada uno de los otros porcentajes tiene ~0.3% de probabilidad
prob_hum_alta = 0.70 / conteo_h_favorables
prob_hum_baja = 0.30 / conteo_h_restantes

#asigna las probabilidades correctas a cada temperatura
for temp in temperatura_rango:
    if 18 <= temp <= 24:
        probabilidades_temperatura.append(prob_tem_alta)
    else:
        probabilidades_temperatura.append(prob_tem_baja)

for humedad in humedad_rango:
    if 70 <= humedad <= 90:
        probabilidades_humedad.append(prob_hum_alta)
    else:
        probabilidades_humedad.append(prob_hum_baja)

# Selección de temperatura y humedad según las probabilidades definidas
def generar_datos():
    temperatura_elegida = int(np.random.choice(temperatura_rango, size=1, p=probabilidades_temperatura)[0])
    humedad_elegida = int(np.random.choice(humedad_rango, size=1, p=probabilidades_humedad)[0])
    return {"temperatura": temperatura_elegida, "humedad": humedad_elegida}


#datos de la bebida
temperatura_bebida=float(input("ingrese la temperatura de la bebida(°C):"))
hora_dia=int(input("ingrese la hora del dia(en 24 horas):"))
tipo_bebida=input("ingrese el tipo de bebida(cafe, te o chai caliente):")

#temperatura de la bebida 
if temperatura_bebida<50:
    m_temperatura="debe esperar a que se caliente"
elif 50<=temperatura_bebida<=70:
  m_temperatura="se puede servir de inmediato"
else:
  m_temperatura="bebida muy caliente, deberia de esperar un poco mas"

#hora del dia
if 6<=hora_dia<11:
  m_hora="las bebidas se sirven mas rapido"
else:
  m_hora="espera el turno"

#dar resultados
print("temperatura de la bebida:",m_temperatura)
print("hora dia:",m_hora)
  

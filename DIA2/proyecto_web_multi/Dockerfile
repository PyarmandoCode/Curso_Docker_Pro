#Etapa1: etapa de la construccion
FROM python:3.9 as builder

WORKDIR /app

#Copiar los requisitos al contenedor
COPY requirements.txt .
#Actualizar PIP a la ultima version
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools wheel

#Instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Copiar el codigo fuente
COPY . .
RUN rm requirements.txt

#Etap2 Etapa de Produccion
FROM builder
WORKDIR /app

#Copiar las dependencias instaladas de la etapa anterior
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

#Copiar el codigo fuente de la etapa anterior
COPY --from=builder /app/* .

#Exponemos en Puerto
EXPOSE 5000
CMD [ "python" ,"app.py" ]



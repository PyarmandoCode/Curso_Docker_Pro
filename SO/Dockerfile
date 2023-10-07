#Usa la Imagen base de Ubuntu 20.4
FROM ubuntu

#Etiqueta para indicar quien es el mantenedor de esa imagen
LABEL maintainer="Armando Ruiz"


#Configura un usuario de Root
ARG username=myuser
ARG userhome=/home/${username}

#Establecer el usuario por defecto

USER ${username}
WORKDIR ${userhome}

# #Exponer en un puerto
EXPOSE 8080

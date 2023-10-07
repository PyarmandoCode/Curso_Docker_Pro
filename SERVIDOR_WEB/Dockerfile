# instalando mi servidor web y mi SO
FROM nginx:1.19.0-alpine
#Copia los archivos HTML ,images ,estilos al direcorio de trabajo de NGINX
COPY . /usr/share/nginx/html
#Exponer a otro Puerto

EXPOSE 80

#Comando por defecto al ejecutar el contenedor 

CMD ["nginx","-g","daemon off;"]


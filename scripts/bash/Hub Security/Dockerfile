# Usa una imagen base ligera con posibles vulnerabilidades
FROM alpine:3.9

# Desactiva la verificación de certificados (Mala práctica)
RUN apk --no-cache --no-progress add wget \
    && wget --no-check-certificate https://example.com/somefile

# Instala paquetes desactualizados (con vulnerabilidades conocidas)
RUN apk --no-cache add \
    openssl=1.1.1b-r1 \
    python2=2.7.15-r1

# Agrega una cuenta de usuario con permisos inseguros
RUN adduser -D insecure-user && echo 'insecure-user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Copia un archivo con permisos inseguros
COPY vulnerable-script.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/vulnerable-script.sh

# Exponer un puerto innecesario
EXPOSE 12345

# Comando final
CMD ["sh", "-c", "echo Vulnerable container running; sleep infinity"]

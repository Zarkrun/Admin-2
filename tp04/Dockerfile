# Utilise l'image de base ubuntu/bind9
FROM ubuntu/bind9  

# Copie le fichier de configuration named.conf dans le répertoire /etc/bind
COPY named.conf /etc/bind/named.conf

# Copie le fichier de zone mazone.zone dans le répertoire /etc/bind
COPY mazone.zone /etc/bind/mazone.zone

# Met à jour les paquets et installe l'éditeur de texte nano
RUN apt-get update && apt-get -y install nano

# Change le propriétaire et les permissions du répertoire /etc/bind
RUN chown -R bind:bind /etc/bind && chmod -R 777 /etc/bind

# Démarre le service named avec les options spécifiées
CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]
#!/bin/sh

echo "⏳ Attente que les services soient disponibles..."

# Attendre que le nom 'api' et 'front' soient résolvables en DNS
until getent hosts api && getent hosts front; do
    echo "🔄 En attente de résolution DNS pour 'api' et 'front'..."
    sleep 2
done

echo "✅ Services résolus, démarrage de NGINX..."
exec nginx -g 'daemon off;'
#!/bin/bash
echo '======================='
echo 'Fast Instalation, run as sudo'
echo '======================='
echo 'Install php'
echo '======================='
apt install php libapache2-mod-php php-common php-gmp php-curl php-intl php-mbstring php-xmlrpc php-mysql php-gd php-imap php-ldap php-cas php-bcmath php-xml php-cli php-zip php-sqlite3
echo 'Install composer'
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === '756890a4488ce9024fc62c56153228907f1545c228516cbf63f885e036d37e9a59d27d63f46af1d4d07ee0f76181c7d3') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
mv composer.phar /usr/local/bin/composer
echo '======================='
echo 'Instaling mariaDb'
echo '======================='
apt install mariadb-server mariadb-client
echo '======================='
echo 'Configure Database'
echo 'Choose a root pasword and choose YES on all'
echo '======================='
mysql_secure_installation
while :
 do
 echo '======================='
 echo 'Type again the root password you choosed'	
 echo '======================='
 read -p 'Password:' password
 echo Password was $password ?
 echo 'Yes=1 or No=2'
 read conf
 if [ $conf -eq 1 ] 
 then 
  break 
 fi
done
echo '======================='
echo 'Starting Database Server'
echo '======================='
systemctl start mariadb.service
systemctl enable mariadb.service
echo '======================='
echo 'Configuring Database'
echo '======================='
mysql -u root --password=$password -Bse "DROP DATABASE IF EXISTS cakephp;CREATE DATABASE cakephp;DROP USER IF EXISTS 'cakephpuser'@'localhost';CREATE USER 'cakephpuser'@'localhost' IDENTIFIED BY 'c@k3_Us3r_p@ssw0rd';GRANT ALL ON cakephp.* TO 'cakephpuser'@'localhost' WITH GRANT OPTION;FLUSH PRIVILEGES;EXIT;"
mysql -u root --password=$password < ./database_without_foreignkeys.sql
#mysql -u root --password=$password < ./setup_database.sql
systemctl start mariadb
echo '======================='
echo 'Installing adminer for easier manipulation of database'
echo '======================='
apt install adminer
a2enconf adminer.conf
echo '======================='
echo 'Adminer in: https://127.0.0.1/adminer/'
echo '======================='
echo '======================='
echo 'Installing Python Dependencies'
echo '======================='
./FastPython.sh
echo '======================='
echo 'Creating project'
echo '======================='
mkdir /var/www/cakephp
#Compress
#O FICHEIRO PYTHON TEM DE ESTAR NA DIRETORIA DO WWW ROOT DO CAKE - cria diretoria scans na webroot
#cp scaner.py scansDefinitions.py sqlConnector.py /var/www/cakephp/app/webroot
#tar -czvf Samuel_ProjectoFinalAnciber.tar.gz ./cakephp
tar -xzvf Samuel_ProjectoFinalAnciber.tar.gz -C /var/www/
#mete o script acessivel de qualquer lado
chmod +x /var/www/cakephp/app/webroot/scanner.py
ln /var/www/cakephp/app/webroot/scanner.py /usr/local/bin/scanner.py
#cd /var/www/cakephp
#composer create-project --prefer-dist cakephp/app
#cd /var/www/cakephp/app/
#composer install && composer update && composer dump-autoload --optimize
#nano /var/www/cakephp/app/config/app_local.php
#Copiar o meu trabalho para aqui
echo '======================='
echo 'Checking some last permissions'
echo '======================='
chown -R www-data:www-data /var/www/cakephp
chmod -R 755 /var/www/cakephp
echo '======================='
echo 'Deploying server'
echo '======================='
python3 /var/www/cakephp/app/webroot/scanner.py &
cd /var/www/cakephp/app/bin/
./cake server
echo 'Visit http://localhost:8765/'


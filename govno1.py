import os
foldername = raw_input("Enter foldername: ")
if len(foldername) >= 0:

os.system('sudo mkdir -p /srv/www/%s/home/%s && sudo mkdir -p /srv/www/%s/sites/%s.muctr.ru') % foldername
os.system('sudo adduser —home /srv/www/%s/home/%s —no-create-home —shell /bin/false —firstuid 901 —lastuid 999 —ingroup www-data %s') % foldername
os.system('sudo chown %s:www-data /srv/www/%s/sites/%s.muctr.ru && sudo chmod 755 /srv/www/%s/sites/%s.muctr.ru') % foldername
else:
	print ("Monkey eats banana")
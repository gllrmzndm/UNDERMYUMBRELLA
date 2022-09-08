#!/usr/bin/python3
import sys, getopt
import argparse
import sense_hat
import time
import MySQLdb as mariadb


sensor_name = 'Temperatuur';
# database connection configuration
dbconfig = {
    'user': 'sensem',
    'password': 'h@',
    'host': 'localhost',
    'database': 'weerstation'
}

# parse arguments
verbose = True
interval = 10   # second

opts, args = getopt .getopt(sys.argv[1:], "vt:")

for opt, arg in opts:
    if opt == '-v':
        verbose = False
    elif opt == '-t':
        interval = int(arg)

# instantiate a sense-hat object
sh = sense_hat.SenseHat()

# Vervolgens moet er een databaseconnectie gemaakt worden.
mariadb_connection = mariadb.connect(**dbconfig)
if verbose:
    print("Database connected")

# create the database cursor for executing SQL queries
cursor = mariadb_connection.cursor()

# turn on autocommit
cursor.autocommit = True


# determine the sensor_id for temperature sensor
cursor.execute("SELECT id FROM sensor WHERE naam=%s", [sensor_name])

sensor_id = cursor.fetchone()
if sensor_id == None:
    print("Error: no sensor found with naam = %s" % sensor_name)
    sys.exit(2)
if verbose:
    print("Reading data from sensor %s with id %s" % (sensor_name, sensor_id[0]))


# infinite loop
try:
    while True:
        # measure temperature
        temp = round(sh.get_temperature(),1) - 10
        # verbose
        if verbose:
            print("Temperature: %s C" % temp)

except:
    print('nothing')

finally:
    print('whatever')



# store measurement in database
cursor.execute('INSERT INTO meting (waarde, sensor_id) VALUES (%s, %s);', (temp, sensor_id[0]))

# commit measurements
mariadb_connection.commit();
if verbose:
    print("Temperature committed");

# wait a while
time.sleep(interval)

# close db connection
mariadb_connection.close()
# done

# Extra opdrachten

# 1. Hoe kan je het script automatisch laten starten?
# De quick-and-dirty way:
# Voeg het measure.py-script toe aan het eind van het /etc/rc.local-script. Zie als voorbeeld in rc.local het welcome-windespi.py-script. Test door een reboot te doen (sudo reboot).

# Voor de gevorderde Linux kenner: hoe kan je dit nog meer doen?

Anacron, cron, crontab, systemd blah blah

# 2. Hoe kan je het script verbeteren?
# Zoals het er nu staat, is het script eenvoudig, doet het wat het moet doen, maar is het niet bepaald robuust. Welke verbeteringen kan je nog aanbrengen?

# Dit was het voor vandaag. De checklist van de dag:
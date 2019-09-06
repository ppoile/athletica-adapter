athletica-adapter
=================

Mehrkampf-Adapter to Athletica

Athletica-adapter is a Django project.

It is named 'athletica-adapter' since it uses and extends athletica.

Doc
---

Model dependencies can be generated as follows:
$ python manage.py graph_models stadion meeting main | dot -T pdf > athletica-models.pdf

SQL-Monitoring
--------------

Enable SQL monitoring as follows:
$ mysql --user root --password
mysql> SET GLOBAL general_log = "ON";
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like "general_log%";
+------------------+----------------------------------+
| Variable_name    | Value                            |
+------------------+----------------------------------+
| general_log      | ON                               |
| general_log_file | /var/lib/mysql/andi-xubuntu2.log |
+------------------+----------------------------------+
2 rows in set (0.00 sec)

mysql>

$ sudo tail -f /var/lib/mysql/andi-xubuntu.log

TODO
----

The following tasks are to be done:
- Unittest Rangliste
- Implement Serieneinteilung ordered by Rangliste

Zeitmessung with Linux
----------------------

When running the server on linux, zeitmessung needs to be set up as follows:
$ sudo mkdir -p /mnt/optic2-work
$ sudo mount -t cifs //192.168.1.112/work /mnt/optic2-work -o username=athletica,password=athletica,uid=www-data,gid=www-data

Under Meeting/Zeitmessung one can now enter path '/mnt/optic2-work'.

Docker
------

Build and tag a new image:
$ docker-compose build
$ docker-compose push

Now the image can be used with ppoile/docker-athletica (docker-compose)...

Bash into running container:
$ docker-compose exec django bash

django-webodt
-------------

In order to not get deprecation warnings upon server start upgrade django-webodt as follows:
$ pip install --upgrade git+https://github.com/dimasciput/django-webodt

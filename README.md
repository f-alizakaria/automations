# Handddle Automations
## _Automatic installation_

#

## Installation

Execute the following command:

```sh
cd <path>/automations/

sh ./setup.sh <profile_name> <url>  

# sh ./setup.sh handddle handddle.com
```

#


#### After installation

Verify that these directories are not empty or contain these files:

```sh
/usr/local/handddle/{applications/logos, handddle_jetson_python/bash_scripts/}

/home/<user>/.config/autostart/handddle_app.desktop

/etc/systemd/system/handddle_jetson_python.service

~/Desktop/{handddle.desktop, maintenance.desktop}
```

What remain to be done is to check that the application is working properly and start the python service:

```sh
systemctl start <service>

systemctl status <service>
```

## Remove installation files

Now we can remove all installation files:

```sh
rm <path>/automations
```

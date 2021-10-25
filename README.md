# FlaskApi
This repository contains few python scripts with easy FlaskApi calls (Both Oracle and SQL databases)

I chose to run these Flask apps through rc.local service as follows:
sudo nohup python3 /scripts/Flask/OracleApp.py > /scripts/Flask/OracleLog.txt 2>&1 &

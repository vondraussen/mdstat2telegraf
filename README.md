# mdstat Telegraf
Simple python script to convert mdstat info to influx line protocol for telegraf.

I've copied the idea from: https://community.influxdata.com/t/how-to-collect-mdadm-data-with-telegraf/9313/3


## Install
Copy `mdstatus.py` to `/usr/local/bin/mdstatus`.
```bash
sudo cp mdstatus.py /usr/local/bin/mdstatus
sudo chmod +x /usr/local/bin/mdstatus
```
Add the following to your `telegraf.conf`:
```bash
[[inputs.exec]]
  commands = ["/usr/local/bin/mdstatus"]
  timeout = "2s"
  data_format = "influx"
```
Restart `telegraf.service`:
```
sudo systemctl restart telegraf.service
```
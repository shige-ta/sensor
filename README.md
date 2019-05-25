Humidity thermometer adopts bme 280

![bme280](https://github.com/test-okome/sensor/blob/master/bme280.JPG "bme280")

# gcp-project

### モジュールインストール

```
pip install -r gcp-project/requirements.txt -t li
```

### デプロイ

```
gcloud app deploy
```

# raspberrypi

### モジュールインストール

```
mkdir lib
pip install -r raspberrypi/requirements.txt
```

### cron 設定

```
crontab -e
```

### 設定追記して保存

```
*/5 * * * * python /home/pi/bme280.py >> /home/pi/log.txt
```

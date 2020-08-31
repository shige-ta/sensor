# sensor
ラズパイで温湿度(bme280)で計った数値をgoogle app engineにAPI経由で送信し、DataStoreに保存しておいて表示。

# DEMO
![bme280](https://github.com/test-okome/sensor/blob/master/bme280.JPG "bme280")

# Features
# Requirement
# Installation
```bash
mkdir lib
pip install -r raspberrypi/requirements.txt -t lib
```

# Usage
```bash
cd gcp-project/
gcloud app deploy
```

# cron 設定
```bash
crontab -e
```

# 設定追記して保存
```bash
*/5 * * * * python /home/pi/bme280.py >> /home/pi/log.txt
```

# Note
# Author
* 作成者 @test-okome

# License
ライセンスを明示する
"@test-okome" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

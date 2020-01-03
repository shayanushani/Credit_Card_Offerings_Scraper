NOT MEANT FOR COMMERCIAL USE 

READ THE TERMS OF AGREEMENT OF EACH SITE BEFORE RUNNING ANY SCRIPT 

PURELY MEANT FOR ACADEMIC REASONS

# directions

document I used... 
https://wired-world.com/?p=351

---


get google chrome drivers and headless chomium

```
$ cd /path/to/your_serverless_dir

$ mkdir -p bin/
```
---

### download chromedriver
```
$ curl -SL https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip > chromedriver.zip

$ unzip chromedriver.zip

$ mv chromedriver ./bin/chromedriver-linux
```


### download headless-chromium
```
$ curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
$ unzip headless-chromium.zip
$ mv headless-chromium ./bin/headless-chromium
```

### clean
```
$ rm headless-chromium.zip chromedriver.zip
```

## Prereqs

1. log into lab:
2. log into notebook:
3. select python notebook:

![Alt text](docs/deploy_notebook.png?raw=true "python_notebook")

## Install/Configure python environment

--proxy http://web-proxy.corp.hpecorp.net:8080

0. sanity test
```
!pip3 --version
!python3 --version
```
1. install packaging, note: if you are not behind corporate proxy; yoy may remove --proxy flag
```
!pip3 install pydicom --proxy http://web-proxy.corp.hpecorp.net:8080
!pip3 install numpy --proxy http://web-proxy.corp.hpecorp.net:8080
!pip3 install pillow --proxy http://web-proxy.corp.hpecorp.net:8080
!pip3 install cython --proxy http://web-proxy.corp.hpecorp.net:8080
!pip3 install pylibjpeg pylibjpeg-libjpeg pylibjpeg-openjpeg --proxy http://web-proxy.corp.hpecorp.net:8080
!pip3 install git+https://github.com/Who8MyLunch/CharPyLS --proxy http://web-proxy.corp.hpecorp.net:8080
```
or
```
!pip3 install -r requirements.txt --proxy http://web-proxy.corp.hpecorp.net:8080
```

2. test read dicom format
```
python3 1.py
```


3. (optionally) download sample data
```
!pip3 install git+https://github.com/pydicom/pydicom-data --proxy http://web-proxy.corp.hpecorp.net:8080
!python3 -c "import pydicom; pydicom.data.fetch_data_files()"
```
copy downloaded sample files from to local repo (bellow shows where data is downloaded just for reference)
```
C:\Users\harrisod\AppData\Local\Programs\Python\Python37\Lib\site-packages\dicom
```


##

docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc /etc/orthanc --verbose
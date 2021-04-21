0. sanity test
```
pip3 --version
python3 --version
```
1. install packaging
```
pip install pydicom
pip install numpy
pip install pillow
pip install cython
pip install git+https://github.com/Who8MyLunch/CharPyLS
pip install pylibjpeg pylibjpeg-libjpeg pylibjpeg-openjpeg
```
or
```
pip --user install -r requirements.txt
```

2. test read dicom format
```
python3 1.py
```


3. (optionally) download sample data
```
pip install git+https://github.com/pydicom/pydicom-data
python -c "import pydicom; pydicom.data.fetch_data_files()"
```
copy downloaded sample files from to local repo (bellow shows where data is downloaded just for reference)
```
C:\Users\harrisod\AppData\Local\Programs\Python\Python37\Lib\site-packages\dicom
```

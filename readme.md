sanity test
```
pip3 --version
python3 --version
```
install packaging
```
python3 -m pip install --upgrade pip
pip3 --no-cache-dir install -r requirements.txt
pip3 install git+https://github.com/Who8MyLunch/CharPyLS
```
read and plot data with 1.py
```
python3 1.py
```

optional: to download some more sample data, ( bellow shows where data is downloaded just for reference)
```
pip install git+https://github.com/pydicom/pydicom-data
python -c "import pydicom; pydicom.data.fetch_data_files()"
C:\Users\harrisod\AppData\Local\Programs\Python\Python37\Lib\site-packages\dicom
```

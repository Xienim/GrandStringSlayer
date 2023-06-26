
# GrandStringSlayer

GrandStringSlayer is a decryption tool written in python for string decryption of GrandString Trojan Banker.


## Usage

First you must extract the key used in the sample to decrypt the strings and then set the key in the key variable. For the encrypted strings you will have to put all the strings in a file located in the same directory as the script.
```python
file = "StringsEnc.txt"
key = "KEY-HERE_KEY-HERE_KEY-HERE"
}
```
After that you can run the script and check the output with the decrypted strings.
```
python3 GrandStringSlayer.py
```
&nbsp;
![App Screenshot](https://github.com/Xienim/GrandStringSlayer/blob/main/decryptor.png)

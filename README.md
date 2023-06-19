#  WEBSCRAPER TOOL


#### 1)click here:  https://github.com/itsbilyatt/webscraper/tree/main
#### 2)download as a zip
#### 3)extract it
#### 4)Run this command : # pip install 'local file path'  
        

```python
# import library
from webscraper import Webscraper
```

## 1) To get soup content(it includes data with html tag) from website


```python
Webscraper('url').soup_content()
```

## 2)To get soup text (data without html tag) from website


```python
Webscraper('url').soup_text()
```

## 3)soup text  data in form of string to do string operation with that


```python
text_data=Webscraper('url').soup_text_string()
```


```python
text_data
```


```python
type(text_data)
```

## 4)soup content  data in form of string to do string operation with that 


```python
content_data = Webscraper('url').soup_content_string()
```


```python
content_data
```


```python
type(content_data)
```


```python

```

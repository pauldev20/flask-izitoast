# Flask-iziToast

* [Introduction](#introduction)
* [Usage](#usage)
* [Settings](#settings)

## Introduction
This is a flask module to use the iziToast notifications with the flask flash function.

## Usage

**HTML:**
```html
<!DOCTYPE html>
<html lang="en">

<head>  
    <title>Home</title>
    {% assets "izi_css" %}
        <link rel="stylesheet" href="{{ ASSET_URL }}" />
    {% endassets %}
    {{ izi.message() }}
</head>  

<body>  
    {% assets "izi_js" %}
        <script type="text/javascript" src="{{ ASSET_URL }}"></script>
    {% endassets %}
    <h3>Welcome to the website</h3>  
</body>  

</html>  
```

**Python:**
```python
from flask import Flask, render_template, flash
from flask_izi import Izi

app = Flask(__name__)
app.secret_key = '12345' #your very secret key
izi = Izi(app)

@app.route('/')
def home():
    flash('Hello from iziToast!')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```

## Settings
You can set some parameters of the Toasts.

| Parameter | Default | Values | Description
|   :---:   |  :---:  | :---:  |    :---:
| IZI_POSITION  | 'bottomRight' | 'bottomRight', 'bottomLeft', 'topRight', 'topLeft', 'topCenter', 'bottomCenter', 'center' | this parameter defines the postition of the Toast
| IZI_TIMEOUT   | 15000 | can be basically any `int` value | this defines how long the Toast will be displayed

The parameters are set like this:
```python
app.config[{parameter}] = {value}
```
for example:
```python
app.config['IZI_POSITION'] = 'bottomRight'
```
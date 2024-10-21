# Invoking Python Script in UiPath

## Prerequisities
- Python installation **strictly** `Python 3.7` or `Python 3.8`.

## How to setup  in UiPath Studio
- Install `UiPath.Python.Activities` package.
- Navigate to the Activities Panel and type in python.
- Select the `Python Scope`, `Load Python Script`, `Invoke Python Method` Activities.

#### **Python Scope Acivity Properties setup**
- In the path property - Provide the python path variable for example `C:\path\to\AppData\Local\Programs\Python\Python38\`.
- In the target property - Select the target `x32` or `x64`.
- In the version property - Select the python version `3.7` or `3.8` or `Auto`.



![image](https://github.com/Klaus-in-Tech/uipath-python/assets/31986394/fa4638b3-a5d5-4db7-877b-dc7c8043ab82)

#### **Load Python Script Acivity Properties setup**
- In the File property - Fill in the path to your python script.
- In the Result property - Create the Python Object variable.

  
![image](https://github.com/Klaus-in-Tech/uipath-python/assets/31986394/167b756c-6d2a-46c4-8cef-7c8eb13d041b)

#### **Invoke Python Method Properties setup**
- In the InputParameters - Provide input parameters if any.
- In the instance property - Provide the Python Object from the Load Python Activity.
- In the Name property - Provide your python method name.


![image](https://github.com/Klaus-in-Tech/uipath-python/assets/31986394/aa4f31f7-b46c-412e-a297-65528e636065)

## User Manual for this demo
For this demo, I used a python script that clears your downloads folder free feel to give it a test run.

## Author
- [Github](https://github.com/Klaus-in-Tech)
- [LinkedIn](https://www.linkedin.com/in/kakoozaallanklaus/)
- [Twitter](https://twitter.com/Klaus_in_Tech)
- [Instagram](https://instagram.com/klaus_allan_?igshid=ZDdkNTZiNTM=)

### Feel free to connect with me on my socials as listed above. 😊

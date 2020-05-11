# copyright_detection
This code repository is aimed to perform copyright detection in videos by ViSiL model achitecture (https://github.com/MKLab-ITI/visil) which is based on Spatio-Temporal video similarity. The main idea is using the spatio or spatio-temporal deep learning models like ResNet or I3D respectively to perform video-to-video comparison by frames. The project itself is a web application based on Django framework with all necessary functionality written in a form of html pages and forms. Moreover, this project consists of docker-compose.yml file and instructions how to run this project by docker image from docker hub. 

## Dataset
You may upload the videos directly to application by web interface by chossing two options - to which category files are belongigng to and there these files located in your file system. So, queries videos are videos which will be inspected to similarity to database videos. Second ones are protected by copyright laws by legend and usually we have few query videos and many of database videos. 

## How to install and use
Actually you have two oprions of how to install and then run this application.

### 1) Download docker-compose.yml and run docker image
First of all you need to install docker and docker-compose on your system to be able to run next commands. 

Next, you have to run the next command to install the image of the project form docker hub to your computer:  
``` docker pull delamio/visil_recognizer_project:2.0 ```  
After it, you run next command in directory there the downloaded docker-compose file is located:
``` docker-compose up
Finally, this project will be up-and-running and you will be able to start using it by going to localhost:8000 page and by this open the home page of teh project where you can start working. The home page consists of all needed instructions.

### 2) Clone this repo, install requirements and weights

First of all, clone thsi repository to directory. Then please install all dependencies from requirements.txt. Pay specil attention that the tensorflow-1.15 is used in this project, not the second version.  
After it, please load to the weights achive and unzip it in visil_model directory of the project by next commands:
```bash
wget http://ndd.iti.gr/visil/ckpt.zip
unzip ckpt.zip
```
Finally, you may run next command to run your server and then go to the localhost:8000 to access the home page of the application with all instructions on the main page.  
```python.exe C:/Users/delamio/PycharmProjects/myapp/manage.py runserver 8000```




You have 2 options how to run this 

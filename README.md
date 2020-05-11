# copyright_detection
This code repository is aimed to perform copyright detection in videos by ViSiL model achitecture (https://github.com/MKLab-ITI/visil) which is based on Spatio-Temporal video similarity. The main idea is using the spatio or spatio-temporal deep learning models like ResNet or I3D respectively to perform video-to-video comparison by frames. The project itself is a web application based on Django framework with all necessary functionality written in a form of html pages and forms. Moreover, this project consists of docker-compose.yml file and instructions how to run this project by docker image from docker hub. 

## Dataset
You may upload the videos directly to application by web interface by chossing two options - to which category files are belongigng to and there these files located in your file system. So, queries videos are videos which will be inspected to similarity to database videos. Second ones are protected by copyright laws by legend and usually we have few query videos and many of database videos. 

## How to install
Actually you have two oprions of how to install and then run this application.

### 1) Download docker-compose.yml and run docker image
First of all you need to install docker and docker-compose on your system to be able to run next commands. 

Next, you have to run the next command to install the image of the project form docker hub to your computer:  
``` docker pull delamio/visil_recognizer_project:2.0 ```  
After it, you run next command in directory there the downloaded docker-compose file is located:
``` docker-compose up```  
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

## How to use

This repository has three main options or actions which you can perform from the home page by pressing the certain buttons. By these options you will be able to manipulate with videos data and run the model to achieve the results in form of json file.

### Option 1: View all the videos and delete them
Next page displays all teh videos which are already uploaded to the system and provide abilities to: see which videos are belonging to queries and database datasets respectively, link to this videos with ability to download them and mark the videos which you want to delete. Also, there are two buttons: one on the top to return to home page and at the very bottom to delete marked videos. After deleting the videos the content of the page will be updated.
### Option 2: Upload new videos
This page consists of two main parts: one of them is radio button which marks for which category the uploading videos are belonging to - there two options: queries and database, second part is uploading button which calls your file manager and asks you to choose one or multiple videos to upload. After finishing the all the choosings press the bottom button to run the uploading program. Then, after pressing this button you will be redirected to home page. Important: all the videos are indexed by their names and this is why all teh video names must be unique.
### Option 3: Perform computations and download the result
This option runs the main deep learning model of the system, which takes all the uploaded videos and perform comparison of the queries videos to database ones. After it, the results of comparison will be written in JSON file. This file has the next structure: first dictionary is the name of the each query video to its comparison dictionary. Then, in teh second dictionaty we have correspondence between the name of the database file and its similarity to the given query video. Lastly, the system will redirect the user to the download page where the user will be given ability to download the resulting JSON.

## Understanding the results
The file is in JSON format and
contains a dictionary with every query id as keys, and another dictionary that contains the similarities of the dataset
videos to the corresponding queries as values. See the example below:
```bash
    {
      "wrC_Uqk3juY": {
        "KQh6RCW_nAo": 0.716,
        "0q82oQa3upE": 0.300,
          ...},
      "k_NT43aJ_Jw": {
        "-KuR8y1gjJQ": 1.0,
        "Xb19O5Iur44": 0.417,
          ...},
      ....
    }
    ```
```

# FR_Template

This Software allow you to get financials informations about cryptocurrencies by using Python3 and the UI that will let you interact to the software with a modern graphic user interface.

[![Image](https://alternative.me/crypto/fear-and-greed-index.png)](https://alternative.me/crypto/fear-and-greed-index.png)  

## Getting Started  
  
To get a copy of the project, you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However, if you're using a prompt console on an Unix machine use this line :

```
git clone https://github.com/Franck1333/FR_Template.git
```
  
### Prerequisites  
  
To use the project, you will need some Hardware :
  
```  
A Raspberry Pi (Last Version is better) or any Linux computer compatible,
An Internet Connection,
A Micro S.D card (8 Gb Minimum),
A Display (like the Pimoroni 4inch HyperPixel Display --> https://bit.ly/2FVOy5j).
```  
  And you will also need some libraries and softwares :

```
- Python version 3
- An OS up to date
```

Be sure to be Up to date with your OS and Python3 environement with this command line:
```
- sudo apt-get update && sudo apt-get upgrade && sudo pip3 install --upgrade pip
```

You can install the *Pimoroni HyperPixel 4* like this :
```
- The Github page : https://github.com/pimoroni/hyperpixel4
- The command line Setup (need to be install) : https://get.pimoroni.com/hyperpixel4 | bash 
```
  
### Downloading/Installing
To get and downloaded the files, use this line : 
```
git clone https://github.com/Franck1333/FR_Template.git
```
When the project is Downloaded, check your `pi` folder, and you will see the folder `FR_Template` .

When you did it, you will have to launch the file called `setup.py` to install the dependencies neccessary for the project with this command line : 

```
    sudo python3 setup.py install
```

There is another way to install all the dependencies needed:

        sudo pip3 install -r requirements.txt

If some problem during the installation occured, please execute this command :
```
    sudo pip3 install cbpro cmc pandas numpy matplotlib pydub kivy
```

## Run
#### The Way to run the project :
To run the project; if you want to see the console activities, you can launch the file called `Main.py`  into the Command Line Prompt with `python3 Main.py` in the main folder.

## Running the tests  
  
That's how to test features:

    python3 <file>.py

## The Folders and Files

In this project we've got some folders

#### Folders
```
Example : 	Any help or example that I used for the project
Services:	Main features 
```
#### Files in "/CryptoWatch-Tkinter/Services/"

Main features of the program
```
- Info_Hardware.py: This feature allow to the Main program to get informations about the status of processors(Usage,Temp),RAM(Usage). 

- nettoyage_du_cache.py: Ancient program that allow all the program which using to delete all the Python2 Cache Files.
```

Folders inside
 ```
 - Sounds: Sound Pack use by the Main Program 
 - Téléchargements: This folder is use by the Main Program to download in this folder all the ressources which come from Internet 
 ```

## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You !  :heart:

[![Image](https://i.goopics.net/51JA2.jpg)](https://goopics.net/i/51JA2)

#Hopfield Artificial Neural Network
##Dependencies
* numpy
* PyQt5
* cython
* pillow (PIL)
* tqdm

##Datas to learn
Datas are either images or numbers, and are located in data folder. 

##How to use it
The hopfield network code (located in network folder) is cythonized, therefore compiling is required:
    
    $ cd network
    $ python setup.py build_ext --inplace

And then: 

    $ cd .. 
    $ python main.py

##GUI screenshot
![learning pictures](http://i.imgur.com/iSYbLDg.png =200x150)




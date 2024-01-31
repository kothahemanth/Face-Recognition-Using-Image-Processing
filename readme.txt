Firstly, Install the Python Software to work this Project.

The Python version required for this Project is 3.8.10. Because some of  this importing are unable to installed from the Present version.

The Version can be Dowloaded from the Below Linkk:

https://www.python.org/downloads/release/python-3810/

Installations of the project:

With out installation of these packages the code will not be able run completely.

Commands:

1. OpenCV

	---> pip install opencv-python

2.  To install Dlib 

	---> pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f

If the above one does not work then install:

Download the Dlib source(.tar.gz) from the Python Package Index : https://pypi.org/project/dlib/#files extract it and enter into the folder.

And then enter in the cmd 

	---> python setup.py install

3. cmake

	---> pip install cmake

The cmake can also installed through the website. The link is Below:

https://cmake.org/

Then dowload according to the Operating System i.e., 32-bit or 64-bit. And also add the path in the Environment Variables like:

set PATH="%PATH%;C:\Program Files\CMake\bin" 

If the packages dlib and cmake have not installed properly then the Face recognition module will not installed. The both cmake and dlib are mainly used to install 

the Face recognition Module.

4. Face Recognition Module 
	
	---> pip install face_recognition

5. tkinter

	---> pip install tkinter

6. numpy 

	---> pip install numpy

The Execution can be Done in the Visual Studio, Jupiter Notebook (or) spyder. The best thing to use is Jupiter Notebook where you can see all the commands 

how there are working.

The project file is named as the "source code" where it consistes of some "test" folder and the "train" folder where it consists of some the images that are trained 

and tested.

The main file in the "source code" folder is the "GUI.ipynb" for the GUI based Output.




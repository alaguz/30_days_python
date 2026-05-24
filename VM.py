Setting up Virtual Environments
To start with project, it would be better to have a virtual environment. 
Virtual environment can help us to create an isolated or separate environment. 
This will help us to avoid conflicts in dependencies across projects.
If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, 
we will access only packages which are specific for that project. Open your terminal and install virtualenv



exit()
pip install virtualenv




After installing the virtualenv package go to your project folder and create a virtual env by writing:

python -m venv venv

Let us check if the the venv was created by using ls (or dir for windows command prompt) command.

ls



Activation of the virtual environment in Windows may very on Windows Power shell and git bash.

venv\Scripts\activate



After you write the activation command, your project directory will start with venv. 
# (venv) PS C:\Users\alanj> 


Now, lets check the available packages in this project by writing pip freeze. You will not see any packages.

We are going to do a small flask project so let us install flask package to this project.


pip install Flask





Now, let us write pip freeze to see a list of installed packages in the project:

pip freeze



When you finish you should dactivate active project using deactivate.
deactivate


The necessary modules to work with flask are installed. Now, your project directory is ready for a flask project. 
You should include the venv to your .gitignore file not to push it to github.




# Use virtual environments so:

projects stay isolated
dependencies don’t clash
setups are reproducible
your machine stays clean

They are considered standard practice in Python development.


EX: Create a project directory with a virtual environment based on the example given above.
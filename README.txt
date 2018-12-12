Movie Recommendation System on MovieLens Dataset

Author: Tianyou Xiao (txiao3@u.rochester.edu)
  	Ziyu Song (zsong10@u.rochester.edu)

Date: 12/12/2018

Installation Requirement:
numpy v1.15.0
pandas v0.23.4
PyTorch v0.4.1
Seaborn v0.9.0
matplotlib v3.0.1
scikit-learn v0.20.1


Files included:
->MRS.ipynb: A python notebook file containing our collaborative filtering recommendation system implementation, together with data preprocessing, data visualization and some essential results as outputs.
->NN.ipynb: A python notebook file containing our neural network autoencoder implementation and essential results.
->MRS.pdf: PDF verison of MRS.ipynb for fast check
->NN.pdf: PDF version of NN.ipynb for fast check
->MRS.py: python source code file for running collaborative filtering system
->NN.py: python source code file for running neural network system
->README.txt: Readme file of our programs.
->ml-latest-small: The small version of Movielens datasets provided by GroupLens (https://grouplens.org/datasets/movielens/latest/). This folder contains several csv files recording our data. For this project, we mainly used ratings.csv to do predictions.
->Report.pdf: The final report of our project in PDF version.
Presentation.ppt: Slides of project presentation as a reference of extra credits.


How to run our programs and check results:
The simplest way to see our codes and results is to just check our PDF versions of python notebook files, which contains both codes and some essential results.
If you want to run our program by yourself, you can either:
1. Use jupyter notebook and run through the program again, or
2. Run our python files (MRS.py and NN.py), which may only print some final test results of our program.
   In this case, go to our files' directory, type: python3 MRS.py	python3 NN.py. 
   The results will be printed in the terminal.

==================================
Extra Credits:
1. Presentation on Thursday, Dec. 13th.
2. We applied the 2nd, 3rd and 4th criteria: performing a comparative study using different existing algorithms (comparison between memory-based collaborative filtering recommendation system and model-based neural network autoencoder recommendation system), applying a modified version of an algorithm covered in class (top-k collaborative filtering with item-item based and user-user based), applying a new algorithm (deep learning techniques, neural network autoencoder).
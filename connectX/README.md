# Kaggle

This is the Kaggle code for the project 'connectX', concerned with coming up with a 'bot' that can play connect 4 (very well).
My approach uses a large CNN to build policy functions and value functions for the state of the board (using the REINFORCE algorithm).
Then given these 2 functions, we use MonteCarloTreeSearch to actually find the 'best move' at any state of the game.

The model for the policy and value functions are built in the file CNNtf.ipynb.
The code for implementing the gradient updates in REINFORCE are in the file REINFORCE.ipynb
The model for the MonteCarloTreeSearch is in the file easyMCTS.ipynb

The files helper.ipynb and board_obj.ipynb define the class and helper functions for the object that contains the relevant information about the state of the game.

This is a work in progress, and it is planned to update the easyMCTS into a more powerful version of it (learning action values, not state values).


Most of the code is from first principles, as it is more fun this way, and more instructive (to both me and a reader).
The code that is not from first principles is that which uses tensorflow, as the models are very large, and adding layers like residual layers and batch-norm gives complicated and large gradient expressions.


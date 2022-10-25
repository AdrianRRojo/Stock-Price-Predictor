# Stock-Price-Predictor

## Overview
---
The goal of this project is to make use of machine learning to, as accurately as possible, generete a future price prediction on the different companies on the New York Stock Exchange (NYSE). Is this possible? The Stock market is often seen as highly volitale and unpredictable, but Investment firms, hedge funds and even individuals have been using financial models to better understand market behavior and make profitable investments and trades. Investors make predictions based on news, reports, and any other information that will help them make educated guess, we can, and will, design a similar algorithm that will help us make educated guesses.


## Goal this project is trying to achieve
--- 
The purpose of this project is to accurately predict the future closing value of a given stock across a given period of time.

## How we plan to do this / Technology used
---
- We will be implementing a Long Short Term Memory (LSTM) Neural Network algorithm and Deep Learning models to generate predictions
  - What is LSTM? LSTM is an extension of Recurring Neueral Networks (RNN). " It is capable of processing the entire sequence of data, apart from single data points such as images. This finds application in speech recognition, machine translation, etc. LSTM is a special kind of RNN, which shows outstanding performance on a large variety of problems." - intellipaat.com @ https://intellipaat.com/blog/what-is-lstm/
  ![RNN-v-s-LSTM-a-RNNs-use-their-internal-state-memory-to-process-sequences-of-inputs](https://user-images.githubusercontent.com/108231637/197599859-07610330-74d7-4899-8282-24f73bd1fadd.jpg)

  
 - We will be using Tensor Flow (https://www.tensorflow.org/), an open-source library for numerical computation and large-scale machine learning.
 
  
 ## MVPS
 ---
 - [ ] Retrieve stock price data from Yahoo Finance
 - [ ] Generate a price prediction
 - [ ] Generate a line graph showing the current price trajectory
 - [ ] Show the history of the stocks price based on a given time frame i.e 3 months, 6 months, or a year
 - [ ] Create a plan to expand on this project after completion
 
 ## Stretch Goals
 ---
 - [ ] Allow for multipe types of graphs i.e a bar graph.
 - [ ] Deploy it live so that others may use this resource as well.
 - [ ] Allow for stocks outside of the NYSE and generate a prediction from those as well 
 
 ## User Stories
 ---
 - As a user, I would like to recieve a price prediction for a stock of my choosing
 - As a user, I want to see a line graph visual representation of the trajectory
 - As a user, I want to like to look at the price history as well as the furture prediction.
 
 ## Potential Roadblocks
 ---
 - Achieving a high level of accuracy
 - Problems in generating the graphs
 - Due date time limit.
 
 ### Wireframe
 ---
 - Example graph I expect to output.


 ![predicted-stock-price-In-the-Fig-2-the-graph-has-been-plot-for-whole-data-set-along-with](https://user-images.githubusercontent.com/108231637/197602743-93f16269-c6fe-4fb0-bd2d-12e33dc28d75.png)

## Install instructions
---
- Fork and clone this repo
- pip install package && pip freeze > requirements.txt 

### My schedule (Subject to change)
---

- Tuesday: 
  - Research and familiarize myself with TensorFlow and machine learning
  - Research current industry standard price prediction algorithims
  
- Wednesday:
  - Begin (If I haven't already) coding and creating the project.
  - Retrieve price data from Yahoo Finance
  
- Thursday:
  - Continue to build on the work of Wednesday
  - Re-evalaute the position of the project and stretch goals. 
    - Mid way through the project I will re-evaluate my current goals to ensure I am working on what is absolutely necessary to meeting MVP
  - I should be recieving a price prediction by this point.
  
- Friday:
  - I expect this day will largely be dedicated to debugging and refining the algorithm for a higher level of accuracy and efficiency 
  
- Saturday:
  - Continue debugging and begin working on exporting graphs
  - Ensure The project is metting MVP
  
- Sunday:
  - Ensure I have a project that meets MVP requirements. 
  - If the project is largely bug free and has met MVP, begin working on stretch goals that are achieveable in the time frame.
  
 - Monday: 
~ Presentation Day ~
  
 

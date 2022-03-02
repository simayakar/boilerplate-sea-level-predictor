import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']      
    fig, ax = plt.subplots()
    plt.scatter(x, y)


    # Create first line of best fit
    result = linregress(x, y)
    x_predict = pd.Series([i for i in range(1880,2051)])
    y_predict = result.intercept + result.slope*(x_predict)
    plt.plot(x_predict, y_predict, 'r')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    new_x = df2['Year']
    new_y = df2['CSIRO Adjusted Sea Level']
    result2 = linregress(new_x, new_y)
    nx_predict = pd.Series([i for i in range(2000,2051)])
    ny_predict = result2.intercept + result2.slope*(nx_predict)
    plt.plot(nx_predict, ny_predict, 'y')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
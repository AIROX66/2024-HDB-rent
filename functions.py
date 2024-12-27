import os
import json
import requests
import pandas as pd
import numpy as np
import seaborn as sns
from dotenv import load_dotenv
import matplotlib.pyplot as plt


def load_api_key():
    load_dotenv()
    api_key = os.getenv('API_KEY_26122024')
    if api_key:
        return api_key
    else:
        logger.info("KEY not found.")

def plotting(title, type_of_plot, data, x_columns, y_columns, 
             category = None, desired_order = None, x_min = None, x_max = None, y_max = None):
    #plt.figure(figsize=(20, 8))
    plt.title(title, fontsize=16)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(rotation=90)
    
    
    if type_of_plot == 'boxplot':
        sns.boxplot(y = data[y_columns], 
                    x = data[x_columns], 
                    palette = 'bright',
                    hue = data[category] if category is not None else None, 
                    order = desired_order if desired_order is not None else None,)
        
    elif type_of_plot == 'barplot':
        sns.barplot(y = data[y_columns], 
                    x = data[x_columns], 
                    palette = 'bright',
                    hue = data[category] if category is not None else None, 
                    order = desired_order if desired_order is not None else None)
        
    elif type_of_plot == 'histplot':
        sns.histplot(x = data[y_columns], 
                    hue = data[category] if category is not None else None)
        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)
        plt.xlabel('Category', fontsize=12)
    
    else:
        plt.close()
    
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    plt.savefig(f'{title}.png', dpi = 369, bbox_inches='tight')
    plt.show()

def point_plotting(title, type_of_plot, data, x_columns, y_columns, 
             category = None):
    plt.figure(figsize=(20, 8))
    plt.title(title, fontsize=16)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    
    if type_of_plot == 'lineplot':
        sns.lineplot(y = data[y_columns], 
                    x = data[x_columns], 
                    marker = "x",
                    color = 'black',
                    markerfacecolor="none", 
                    markeredgecolor=None, 
                    hue = data[category] if category is not None else None)
        
    elif type_of_plot == 'scatterplot':
        sns.barplot(y = data[y_columns], 
                    x = data[x_columns], 
                    hue = data[category] if category is not None else None)
        
    plt.savefig(f'{title}.png', dpi = 369)
    plt.show()

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    return R * c



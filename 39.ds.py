import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
data = pd.read_csv("C:/Users/SOORIYA RAJAN.B/Downloads/transaction_data1.csv")
features = ['total_amount_spent', 'number_of_items']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[features])
num_clusters = 4  # Adjust this based on your analysis
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(scaled_features)
sns.scatterplot(data=data, x='total_amount_spent',
                y='number_of_items', hue='cluster', palette='Set1')
plt.title('Customer Segmentation based on Spending and Purchase Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.show()

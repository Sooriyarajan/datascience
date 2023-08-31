import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SOORIYA RAJAN.B/Downloads/transaction_data.csv")
selected_features = ['total_amount_spent', 'frequency_of_visits']
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data[selected_features])
num_clusters = 4  
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(normalized_data)
plt.scatter(data['total_amount_spent'],
            data['frequency_of_visits'], c=data['cluster'], cmap='rainbow')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation')
plt.show()

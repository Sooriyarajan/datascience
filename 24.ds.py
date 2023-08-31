import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
data = np.array([[1, 2, 0],
                 [3, 4, 1],
                 [5, 6, 0],
                 [7, 8, 1]])
X = data[:, :-1] 
y = data[:, -1]  
new_patient_features = [
    float(input(f"Enter feature {i+1}: ")) for i in range(X.shape[1])]
k = int(input("Enter the number of neighbors (k): "))
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
new_patient_scaled = scaler.transform([new_patient_features])
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_scaled, y)
prediction = knn_classifier.predict(new_patient_scaled)
if prediction[0] == 0:
    print("Prediction: No condition")
else:
    print("Prediction: Condition")

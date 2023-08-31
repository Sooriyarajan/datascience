from sklearn.linear_model import LinearRegression
dataset = [
    [1400, 3, 'SuburbA', 250000],
    [1200, 2, 'SuburbB', 220000],
    [1600, 4, 'SuburbC', 280000],
    [1000, 2, 'SuburbB', 190000],
    [1800, 3, 'SuburbA', 300000]
]
X = [[house[0], house[1]] for house in dataset]
y = [house[3] for house in dataset]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter area (sq. ft.): "))
bedrooms = int(input("Enter number of bedrooms: "))
new_house = [[area, bedrooms]]
predicted_price = model.predict(new_house)
print(f"The predicted price of the new house is: ${predicted_price[0]:,.2f}")

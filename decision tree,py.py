from sklearn import tree

# Create the decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier on the given dataset

# Define the features and labels
# Features: [Age, Income, Student]
# Labels: [Buy (1), Don't Buy (0)]
X = [[20, 50000, 1], [25, 70000, 0], [30, 90000, 1], [35, 120000, 0], [40, 150000, 1], [45, 180000, 0], [50, 200000, 1], [55, 220000, 0], [60, 250000, 1], [65, 280000, 0]]
y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Train the classifier
clf = clf.fit(X, y)

# Get user input for features
age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
student = int(input("Are you a student? (1 for yes, 0 for no): "))

# Predict using the trained classifier
prediction = clf.predict([[age, income, student]])

# Print the prediction
if prediction[0] == 1:
    print("Based on the information you provided, you should buy a computer.")
else:
    print("Based on the information you provided, you should not buy a computer.")

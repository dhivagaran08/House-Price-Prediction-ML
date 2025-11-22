#House Price Prediction – Machine Learning Project
📘 Dataset (house_prices.csv)
A sample dataset with two columns:

Area (sq ft)	Price
1200	200000
1500	250000
1800	310000
2000	340000
2200	380000

You can replace this with a larger dataset for better accuracy.

🚀 How to Run the Project
1️⃣ Install Dependencies
Open Terminal / CMD and run:

bash
Copy code
pip install pandas scikit-learn
2️⃣ Run the Model
Navigate to project folder and run:

bash
Copy code
python model.py
🧠 Code Explanation
Train-Test Split
80% → training

20% → testing
Used to check how well the model performs on unseen data.

Linear Regression
The model learns:

ini
Copy code
Price = m × Area + C
Custom Prediction
The program predicts the price for a house area of 1500 sq ft.

📈 Sample Output
less
Copy code
Predictions on test data: [240000. 300000.]
Predicted price for 1500 sq ft: [250000.]
🗂 Files Included
1️⃣ model.py
Contains all ML code:

Load data

Train model

Predict

Display results

2️⃣ house_prices.csv
Sample dataset for training and testing the model.

✨ Future Improvements
You can upgrade this project later with:

🔹 Multiple features (bedrooms, location, bathrooms…)
🔹 Data visualization
🔹 Model accuracy evaluation
🔹 Saving model as .pkl
🔹 Web UI using Flask or Streamlit

📬 Author
Dhivagaran
Beginner ML Engineer | Aspiring to work in USA 🇺🇸


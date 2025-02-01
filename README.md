# 🚀 Job Market Analysis & Salary Prediction  

## 📌 Overview  

This project aims to analyze job market trends and predict salaries based on various job-related factors.  
It includes:  

✅ **Machine Learning Model** – Predicts salaries based on job characteristics.  
✅ **Tableau Dashboard** – Provides interactive visual insights on job trends, salaries, and required skills.  
✅ **Web Application** – A Flask-based UI where users can enter job details and get salary predictions.  
✅ **Data Scraping & Processing** – Extracted and cleaned job postings from multiple platforms.    

---

## 🚀 Features  

🔹 **Data Collection** – Scraped job postings from multiple platforms using Selenium & BeautifulSoup.  
🔹 **Data Preprocessing** – Handled missing values, encoded categorical variables, and engineered features.  
🔹 **Salary Prediction Model** – Built using machine learning techniques trained on disclosed salary data.  
🔹 **Web Application** 🌐 – Users can enter job details such as:  
   - **Department & Role Category**  
   - **Experience Level**  
   - **Educational Qualification (UG/PG)**  
   - **Skills Required**  
   - Get an **instant salary prediction!** 💰  
🔹 **Tableau Dashboard** 📊 – Interactive visual insights on:  
   - **Salary distributions across industries**  
   - **Skills in demand**  
   - **Experience vs. Salary trends**  
   - **Most common job locations**  
🔹 **Imputation of Missing Salaries** – Used the trained model to predict and fill in salaries for job posts marked as "Not Disclosed."  
  
---

## 🛠 Technologies Used  

🔹 **Python** 🐍 – For data preprocessing, model training, and salary prediction.  
🔹 **Pandas, NumPy** 📊 – Data manipulation and numerical computations.  
🔹 **Scikit-Learn** 🤖 – Machine learning model training and evaluation.  
🔹 **Flask** 🌐 – Web framework for building the interactive salary prediction web app.  
🔹 **Tableau** 📊 – For interactive data visualization and insights.  
🔹 **Selenium** 🕵️‍♂️ – Web scraping job listings from various platforms.  
🔹 **Matplotlib & Seaborn** 📉 – Data visualization for exploratory data analysis.  
🔹 **Git & GitHub** 🌍 – Version control and project hosting.  

---

## 📊 Tableau Dashboard  
Explore key job market trends and salary insights with our **interactive Tableau dashboard**.  
🔗 **Live Dashboard:** (https://public.tableau.com/views/your-dashboard-link)  

📌 **Dashboard Features:**  
- **Job Market Trends**: Analyze demand across industries, departments, and roles.  
- **Salary Distributions**: Compare salary trends across experience levels and locations. 
- **Geographical Insights**: Visualize job availability and salary variations by location.  

---

## ⚙️ Running the Web App  
1️⃣ **Install dependencies:**  
```bash
pip install -r requirements.txt
```
2️⃣ **Run the Flask app:**
```bash
python main.py
```
3️⃣ **Open the web app in your browser:**
http://localhost:8000

---

## 📊 Model Training  
📌 The salary prediction model is trained on job postings with disclosed salaries.
📌 After training, the model imputes missing salaries where salary is 'Not Disclosed'.
📌 Feature Engineering includes:
✔️ Encoding Department & Role Category
✔️ Categorizing Experience Levels
✔️ Encoding Education Requirements
✔️ Handling missing values & outliers in salary data 

---

## 💡 Future Improvements
🚀 Fine-tune the model using deep learning techniques
📈 Expand data sources to improve prediction accuracy
📊 Implement real-time job market insights 
📊 Enhance the Tableau dashboard with real-time data updates

---

## 📞 Contact  
If you have any questions or suggestions, feel free to reach out:  
📧 **Email:** keskartejas01@gmail.com  
📌 **LinkedIn:** https://www.linkedin.com/in/tejas-keskar-329634288
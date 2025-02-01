import pickle

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

departments_data = {
    "BFSI, Investments & Trading": ["Lending", "Banking Operations", "Life Insurance", "Others", "General Insurance"],
    "Consulting": ["IT Consulting", "Management Consulting", "Others"],
    "Administration & Facilities": ["Administration", "Others"],
    "Data Science & Analytics": ["Data Science & Machine Learning", "Business Intelligence & Analytics", "Others"],
    "Finance & Accounting": ["Accounting & Taxation", "Finance", "Others"],
    "Healthcare & Life Sciences": ["Doctor", "Nursing", "Others"],
    "Human Resources": ["HR Operations", "Recruitment & Talent Acquisition", "Others"],
    "Marketing & Communication": ["Marketing", "Digital Marketing", "Others"],
    "Production, Manufacturing & Engineering": ["Engineering", "Operations", "Others"],
    "Sales & Business Development": ["Sales Support & Operations", "Enterprise & B2B Sales", "Others"],
    "Customer Success, Service & Operations": ["Customer Success", "Operations", "Others"],
    "Engineering - Software & QA": ["Software Development", "DevOps", "Testing", "Others"],
    "Project & Program Management": ["IT Project Management", "Finance", "Others"],
    "Research & Development": ["Engineering & Manufacturing", "Others"],
    "Food, Beverage & Hospitality": ["Food Services", "Hospitality", "Others"]
}

    
    # Define experience ranges with their corresponding labels
experience_dict = {
    "Entry-level": (0, 1),
    "Junior": (1, 3),
    "Mid-level": (3, 5),
    "Experienced": (5, 10),
    "Senior": (10, 15),
    "Expert": (15, float('inf'))  # Using infinity for experience above 15
}

# ['Entry-level', 'Experienced', 'Expert', 'Junior', 'Mid-level',
#        'Senior']

with open("Department_encoder.pkl", "rb") as file:
    department_encoder = pickle.load(file)

with open("experience_Category_encoder.pkl", "rb") as file:
    experience_Category_encoder = pickle.load(file)


@app.route('/', methods=["GET"])
def root():
    # Pass departments data keys to the template
    departments = list(departments_data.keys())
    return render_template('index.html', departments=departments)

@app.route('/get_roles', methods=["POST"])
def get_roles():
    department = request.json.get("department")
    # Return the role categories for the selected department
    role_categories = departments_data.get(department, [])
    return jsonify({"roles": role_categories})

@app.route('/predict', methods=["POST"])
def predict_churn_value():
    # print(request.form)
    # department = request.form.get("department_encoder")
    department = department_encoder.transform([request.form.get('department')])

    role_category = request.form.get("role_category")

    # experience = request.form.get("experience")
    experience = int(request.form.get("experience"))


    # Find the corresponding experience level
    experience_level = None
    for level, (min_exp, max_exp) in experience_dict.items():
        if min_exp <= experience <= max_exp:
            experience_level = level
            break

    # If no match is found (just a safety check)
    if experience_level is None:
        experience_level = "Unknown"


    experience = experience_Category_encoder.transform([experience_level])


    # Print the experience level to console for debugging
    print("Experience Level:", experience_level)
    print("exp level value",experience[0])
    education_ug = int(request.form.get("education_ug"))
    education_pg = int(request.form.get("education_pg"))
    print(department[0])
    print(role_category)
    print(experience)
    print(education_ug)
    print(education_pg)
    return "model"


# @app.route('/predict', methods=["POST"])
# def predict_churn_value():
#     # Print form values to the console
#     print("Department:", request.form.get("department"))
#     print("Role Category:", request.form.get("role_category"))
#     print("Experience:", request.form.get("experience"))
#     print("UG:", request.form.get("education_ug"))
#     print("PG:", request.form.get("education_pg"))
    
#     return "Form values printed to console."

app.run(host="0.0.0.0", port=8000, debug=True)


#
# ['Administration & Facilities', 'BFSI, Investments & Trading',
#        'Consulting', 'Content, Editorial & Journalism',
#        'Customer Success, Service & Operations',
#        'Data Science & Analytics', 'Engineering - Software & QA',
#        'Environment Health & Safety', 'Finance & Accounting',
#        'Food, Beverage & Hospitality', 'Healthcare & Life Sciences',
#        'Human Resources', 'Legal & Regulatory',
#        'Marketing & Communication', 'Merchandising, Retail & eCommerce',
#        'Others', 'Product Management',
#        'Production, Manufacturing & Engineering',
#        'Project & Program Management', 'Research & Development',
#        'Risk Management & Compliance', 'Sales & Business Development',
#        'Sports, Fitness & Personal Care', 'Strategic & Top Management']
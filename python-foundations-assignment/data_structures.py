
#  Exercise 1 – Favourite Tools List

print("*" * 30)
print("     FAVOURITE TOOLS LIST")
print("*" * 30)

tools = ["Python", "SQL", "Pandas", "Airflow"]
print(f"  Initial list  : {tools}")

tools.append("dbt")
print(f"  After append  : {tools}")

tools.insert(1, "Jupyter Notebook")
print(f"  After insert  : {tools}")

tools.remove("Airflow")
print(f"  After remove  : {tools}")

print(f"  Final list    : {tools}\n")


#  Exercise 2 – Student Scores


print("*" * 30)
print("     STUDENT SCORES")
print("*" * 30)

scores = [78, 92, 66, 88, 74, 91, 60, 43]
print(f"  Scores  : {scores}")
print(f"  Highest : {max(scores)}")
print(f"  Lowest  : {min(scores)}")
print(f"  Average : {sum(scores) / len(scores):.2f}\n")


#  Exercise 3 – Shopping List Manager

print("*" * 30)
print("     SHOPPING LIST MANAGER")
print("*" * 30)

shopping_list = ["tomatoes", "rice", "palm oil", "fresh red pepper"]
print(f"  Shopping list   : {shopping_list}")

shopping_list.append("chicken")
shopping_list.append("iced titus fish")
print(f"  After additions : {shopping_list}")

shopping_list.remove("rice")
print(f"After removal   : {shopping_list}")

print(f"Items in list   : {len(shopping_list)}")
print(f"Sorted list     : {sorted(shopping_list)}\n")


# Exercise 4 – Country Capitals (Tuples)


print("*" * 30)
print("           COUNTRY CAPITALS")
print("*" * 30)

country_capitals = (
    ("Nigeria",      "Abuja"),
    ("Ghana",        "Accra"),
    ("Kenya",        "Nairobi"),
    ("South Africa", "Pretoria"),
    ("Cameroon",       "Yaoundé"),
)

print("  Country         =>  Capital")
print("-" * 35)
for country, capital in country_capitals:
    print(f"  {country:<10} => {capital}")
print()


#  Exercise 5 – Unique Visitors (Sets)

print("*" * 30)
print("            UNIQUE VISITORS")
print("*" * 30)

raw_visitors = [
    "amaka", "bimbo", "stella", "alex",
    "eneotse", "bimbo", "okon", "amaka", "farida",
]
print(f"  Raw visitor log  : {raw_visitors}")
print(f"  Total vistors    : {len(raw_visitors)}")

unique_visitors = set(raw_visitors)
print(f"  Unique visitors  : {unique_visitors}")
print(f"  Unique count     : {len(unique_visitors)}\n")


#  Exercise 6 – Common Skills (Set Operations)


print("*" * 30)
print("     COMMON SKILLS")
print("*" * 30)

ada_skills    = {"Python", "SQL", "Tableau", "Excel", "dbt"}
blessing_skills = {"Python", "Power BI", "SQL", "Spark", "Kafka"}

common   = ada_skills & blessing_skills
only_ada = ada_skills - blessing_skills
either   = ada_skills | blessing_skills

print(f"  Ada's skills        : {ada_skills}")
print(f"  Blessing's skills   : {blessing_skills}")
print(f"  Common skills       : {common}")
print(f"  Ada only            : {only_ada}")
print(f"  All unique skills   : {either}\n")


#  Exercise 7 – Student Record (Dictionary)

print("*" * 30)
print("            STUDENT RECORD")
print("*" * 30)

student = {
    "name"      : "Ngumimi Bethel Tuse",
    "matric_no" : "BU/22/CS/1042",
    "university": "Bingham University, Abuja",
    "programme" : "Computer Science",
    "level"     : 300,
    "cgpa"      : 4.62,
    "skills"    : ["Python", "SQL", "ETL Pipelines", "Figma"],
}

print("  ****** Student Information *******************")
for field, value in student.items():
    label = field.replace("_", " ").title()
    print(f"  {label:<15}: {value}")

student["level"] = 400
print(f"\n  [Updated] Level is now: {student['level']}\n")


#  Exercise 8 – Mini Contact Book (Dictionary of Dicts)

print("*" * 30)
print("     MINI CONTACT BOOK")
print("*" * 30)

contacts = {
    "Zara": {
        "phone"  : "+234-801-111-2222",
        "email"  : "zara@hotmail.com",
        "city"   : "Lagos",
    },
    "Akunna": {
        "phone"  : "+234-803-333-4444",
        "email"  : "akunna@hotmail.com",
        "city"   : "Enugu",
    },
    "Fatima": {
        "phone"  : "+234-806-555-6666",
        "email"  : "fatima@hotmail.com",
        "city"   : "Kano",
    },
}

print("  All Contacts:")
print(" " + "*" * 30)
for name, info in contacts.items():
    print(f"  {name}")
    for key, value in info.items():
        print(f"    {key.title():<8}: {value}")
    print()

search = input("  Search contact by name : ").strip().title()

if search in contacts:
    info = contacts[search]
    print(f"\n  Found '{search}':")
    for key, value in info.items():
        print(f"     {key.title():<8}: {value}")
else:
    print(f"\n  '{search}' not found in contact book.")
print()
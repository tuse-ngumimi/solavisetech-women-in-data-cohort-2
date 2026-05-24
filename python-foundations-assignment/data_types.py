# Exercise 1 - Data Types and Personal Bio

name : str = "Ngumimi Bethel Tuse"
age : int = 20
height : float = 165.1
fav_tech_field : str = "Data Engineering"
is_student : bool = True

print("*" * 30)
print("     PERSONAL BIO GENERATOR")
print("*" * 30)
print(
    f"Hi! My name is {name}. I am {age} years old, "
    f"{height}cm tall, and I am currently a student: {is_student}.\n"
    f"My favourite field in tech is {fav_tech_field}, and I am passionate about it "
    f"because I believe data has the power to transform healthcare\n"
    f"and communities across Nigeria."
)
print()
 
# Exercise 2 – Type Checker

 
greeting = "Hello, Python!"
salary = 300000
pi = 3.14
is_african = True
student_scores = [45, 82, 98]
fruits = {"mango", "banana", "orange"}


print("*" * 30)
print("     TYPE CHECKER")
print("*" * 30)
 
variables = {
    "string" : greeting,
    "integer"    : salary,
    "float"      : pi,
    "boolean"   : is_african,
    "list"      : student_scores,
    "set"      : fruits,
}
 
for var_name, value in variables.items():
    print(f"  {var_name} → {type(value)}")
print()
 
 
# Exercise 3 – Data Conversion

 
print("*" * 30)
print("     DATA CONVERSION")
print("*" * 30)
 
# integer to string 
int_value   = 1456
converted_str = str(int)
print(f"  Integer  {int_value}  => String  {converted_str}   & type: {type(converted_str)}")
 
# float to integer
float_value = 9.87
converted_int  = int(float_value)
print(f"  Float    {float_value}  =>  Integer {converted_int}     & type: {type(converted_int)}")
 
# string number to float
number_value  = "365"
converted_num  = int(number_value)
print(f"  String   {number_value}  => Integer {converted_num}     & type: {type(converted_num)} \n")

 
# Exercise 4 – User Information

 
print("*" * 30)
print("     USER INFORMATION")
print("*" * 30)
 
user_name    = input(" What is your name?    => ")
user_age     = input(" How old are you?      => ")
user_country = input(" What country are you from? => ").strip().title()
print()

if user_country == "Nigeria":
    country_fact = (
        f"  The town of Igbo-Ora in southwestern Nigeria is known as the 'Twin Capital of the World.' \n"
        f"  It boasts an unusually high rate of twin births, with approximately 50 sets of twins per 1,000 births — nearly four times the global average."
    )
elif user_country == "Ghana":
    country_fact = (
        f"  In 1957, Ghana became the first nation in sub-Saharan Africa to achieve independence from European colonial rule." 
        f"  This paved the way for the rest of the continent."
    )
elif user_country == "Cameroon":
    country_fact = (
       f"  It is famously referred to as 'Africa in Miniature'." 
       f"  This is  because it encompasses almost every major climate and geographic feature found across the entire continent, including rainforests, deserts, mountains, and savannas."
    )
elif user_country == "Germany":
    country_fact = (
       f"  It is technically illegal to run out of gas on the Autobahn." 
       f"  Because stopping on the famous highway system for non-emergencies is strictly prohibited, running out of fuel is considered a preventable human error and can result in a fine."
    )
elif user_country == "Kenya":
    country_fact = (
        f"  Nairobi is the only capital city in the world that houses a national park within its city limits." 
        f"  Visitors can go on a safari in Nairobi National Park and see lions, giraffes, and rhinos with a backdrop of city skyscrapers."
    )
elif user_country in ["Usa", "United States", "Us", "USA"]:
    country_fact = (
        f"  The current 50-star American flag was designed in 1958 by a 17-year-old high school student named Robert G. Heft for a history class project."
        f"  His teacher originally gave him a B- for the design, but promised to raise the grade if Congress accepted it — which they did."
    )
else:
    country_fact = (
        f"  That's interesting! {user_country} has its own unique culture and history. "
        f"  Every country has something special to offer, and it's great to learn about different places around the world."
    )

print(
    f"\n  Hello, {user_name}! You are {user_age} years old "
    f"and you're joining us all the way from {user_country}."
    f"\n\n  Fun Fact: {country_fact}"
    f"\n\n  Welcome to the Women in Data Cohort 2. "
    f"Get ready to learn and connect!"
)
print()
 
 
# Exercise 5 – Temperature Converter 

 
print("*" * 30)
print("     CELSIUS TO FAHRENHEIT TEMPERATURE CONVERTER")
print("*" * 30)
 
celsius    = float(input("  Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
 
print(f"\n  {celsius}°C  =  {fahrenheit:.2f}°F")
print()
 
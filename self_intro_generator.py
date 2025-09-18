import datetime

name = input("What is your name: ").strip();
age = input("What is your age: ").strip();
city = input("Which city do you live in?: ");
profession = input("Enter your profession: ");
hobby = input("Enter your hobby: ");

msg = (f'''Hello my name is {name}, I am {age} years old and live in {city}
I work at {profession} and I absolutely enjoy {hobby} in my free time
Nice to meet you!\n'''
       );

curr_time = datetime.date.today().isoformat()
msg += f"\nLogged in on {curr_time}";

pattern = "*"*70

print(f"{pattern}\n{msg}\n{pattern}");



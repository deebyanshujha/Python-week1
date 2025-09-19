people = int(input("enter the total number: "));
names = [];
for i in range(0,people):
    name = input("Enter the name : ").strip();
    names.append(name);

bill = float(input("Enter the total bill: "));

split = round(bill/people,2);

pattern = "*"*70;
print(f"{pattern}\n");
for i in names:
    print(f"bill split of {i} is {split}\n")
print(pattern);
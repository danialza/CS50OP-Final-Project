import time

data = []

def get_data():
    date_input = input("When this Expense Happened!(YYYY-MM-DD or Use Today): ")
    amount_input = float(input("How much you paid? (Number PLZ): "))
    category_input = input("Which category you mean?! (e.g., groceries, salary, investment): ")
    type_input = input("Which Type? (income/expense): ")
    note_input = input("Note! if you want: ")

    if date_input.lower() == "today":
        date_input = time.strftime("%Y-%m-%d")

    dic_data = {
        "date" : date_input,
        "amount" : amount_input,
        "category" : category_input,
        "type" : type_input,
        "note" : note_input
     }
    
    data.append(dic_data)
    
    print("Data Added successfully!!")
    for a_data in data:
        print(a_data)

    return dic_data        

def main():
    get_data()

if __name__ == "__main__":
    main()

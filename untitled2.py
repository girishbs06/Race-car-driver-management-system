import os

index_file = "driver_index.txt"
data_file = "driver_data.txt"

def add_driver():
    driver_id = input("Enter driver ID: ")
    name = input("Enter driver name: ")
    team = input("Enter driver's team: ")
    car_number = input("Enter driver's car number: ")
    
    with open(index_file, "a") as index_f, open(data_file, "a") as data_f:
        index_f.write(f"{driver_id},{data_f.tell()}\n")
        data_f.write(f"{driver_id},{name},{team},{car_number}\n")
    
    print("Driver added successfully!")

def display_driver():
    print("----- Driver List -----")
    
    with open(data_file, "r") as data_f:
        for line in data_f:
            driver_id, name, team, car_number = line.strip().split(",")
            print(f"Driver ID: {driver_id}")
            print(f"Name: {name}")
            print(f"Team: {team}")
            print(f"Car Number: {car_number}")
            print("-----------------------")

def update_driver():
    driver_id = input("Enter driver ID to update: ")
    
    with open(index_file, "r") as index_f:
        for line in index_f:
            index_driver_id, data_offset = line.strip().split(",")
            if index_driver_id == driver_id:
                with open(data_file, "r+") as data_f:
                    data_f.seek(int(data_offset))
                    line = data_f.readline()
                    current_position = data_f.tell()
                    driver_id, name, team, car_number = line.strip().split(",")
                    
                    new_name = input(f"Enter new name for driver {driver_id}: ")
                    new_team = input(f"Enter new team for driver {driver_id}: ")
                    new_car_number = input(f"Enter new car number for driver {driver_id}: ")
                    
                    updated_data = f"{driver_id},{new_name},{new_team},{new_car_number}"
                    data_f.seek(int(data_offset))
                    data_f.write(updated_data)
                    data_f.truncate()
                    
                    print("Driver updated successfully!")
                    return
    
    print("Driver ID not found!")

def search_driver():
    driver_id = input("Enter driver ID to search: ")
    
    with open(index_file, "r") as index_f:
        for line in index_f:
            index_driver_id, data_offset = line.strip().split(",")
            if index_driver_id == driver_id:
                with open(data_file, "r") as data_f:
                    data_f.seek(int(data_offset))
                    driver_data = data_f.readline().strip().split(",")
                    print("----- Driver Details -----")
                    print(f"Driver ID: {driver_data[0]}")
                    print(f"Name: {driver_data[1]}")
                    print(f"Team: {driver_data[2]}")
                    print(f"Car Number: {driver_data[3]}")
                    print("--------------------------")
                    return
    
    print("Driver ID not found!")

def main():
    while True:
        print("----- Race Car Driver Management System -----")
        print("1. Add Driver")
        print("2. Display Drivers")
        print("3. Update Driver")
        print("4. Search Driver")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_driver()
        elif choice == "2":
            display_driver()
        elif choice == "3":
            update_driver()
        elif choice == "4":
            search_driver()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
        print()

if __name__ == "__main__":
    if not os.path.exists(index_file):
        open(index_file, "w").close()
    if not os.path.exists(data_file):
        open(data_file, "w").close()
    
    main()
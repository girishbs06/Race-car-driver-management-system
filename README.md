# Race-car-driver-management-system
This code is a simple Race Car Driver Management System implemented in Python. It allows users to perform various operations related to race car drivers, such as

 adding, displaying, updating, and searching for driver information. Here's how it works:

1. Two text files are used to store driver data:

 - `driver_index.txt`: This file stores the index information for each driver. It contains lines with the format: `driver_id, data_offset`. The `driver_id` is a unique identifier

 for each driver, and `data_offset` indicates the position in the `driver_data.txt` file where the corresponding driver's data can be found.

 - `driver_data.txt`: This file stores the actual driver data, including the driver ID, name, team, and car number. Each line in this file has the format: `driver_id, name, team,

 car_number`.

2. The main functionality of the program is implemented in the following functions:

 - `add_driver()`: Allows the user to input driver information (ID, name, team, car number) and appends this information to both the index and data files.

 - `display_driver()`: Reads the data from the `driver_data.txt` file and displays a list of all drivers, including their details.

 - `update_driver()`: Allows the user to input a driver ID, then searches for that ID in the index file to locate the driver's data in the data file. The user can then update the

 driver's name, team, and car number.

 - `search_driver()`: Allows the user to input a driver ID and searches for that ID in the index file. If found, it retrieves and displays the details of the corresponding driver.

3. The `main()` function provides a simple command-line menu to interact with these functions. The user is repeatedly prompted to choose an option (add, display,

update, search, or exit).

4. When the program starts (`if _name_ == "_main_":`), it checks if the index and data files exist. If they don't, it creates empty files for them.

Overall, this code provides a basic command-line interface for managing race car driver information, allowing you to add, display, update, and search for driver details.

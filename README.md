# Hash-Function

## Hash Function Price List

### Hash Function Pseudocode

#### Data Storage Functions

FUNCTION hash_function(item_name)
    IF item_name length is 1 THEN
        RETURN (ASCII value of character) modulo 991 + 10
    ELSE
        first_ascii = ASCII value of first character
        second_ascii = ASCII value of second character (or 0 if none)
        last_ascii = ASCII value of last character
        second_last_ascii = ASCII value of second-last character (or 0 if none)
        sum = first_ascii + second_ascii + last_ascii + second_last_ascii
        RETURN (sum modulo 991 + 10)

FUNCTION save_price_list(price_list, filename)
    OPEN filename in write mode
    WRITE price_list as JSON to file
    CLOSE file

FUNCTION load_price_list(filename)
    IF file exists THEN
        OPEN filename in read mode
        READ JSON data into price_list
        RETURN price_list
    ELSE
        RETURN empty dictionary

#### Item Management Functions

FUNCTION add_to_price_list(price_list, item_name)
    price = hash_function(item_name)
    ADD item_name:price to price_list
    save_price_list(price_list)

FUNCTION remove_from_price_list(price_list, item_name)
    IF item_name exists in price_list THEN
        REMOVE item from price_list
        save_price_list(price_list)
        DISPLAY "Item removed" message
    ELSE
        DISPLAY "Item not found" message

FUNCTION display_price_list(price_list)
    SORT price_list by item names
    FOR each item in sorted price_list:
        DISPLAY item name and price

FUNCTION initialize_price_list()
    CREATE list of predefined grocery items
    load existing price_list from file
    FOR each predefined item:
        IF item not in price_list THEN
            add_to_price_list(item)
    RETURN price_list

#### Main Program Flow

FUNCTION main()
    price_list = initialize_price_list()
    LOOP forever:
        DISPLAY menu options
        GET user action
        IF action is "exit" THEN
            EXIT program
        IF action is "add" THEN
            GET item name from user
            IF item not in price_list THEN
                add_to_price_list(item)
                DISPLAY success message
            ELSE
                DISPLAY "already exists" message
        IF action is "get" THEN
            GET item name from user
            IF item in price_list THEN
                DISPLAY item price
            ELSE
                DISPLAY "not found" message
        IF action is "remove" THEN
            GET item name from user
            remove_from_price_list(item)
        IF action is "list" THEN
            display_price_list(price_list)

#### Program Entry Point

IF program is run directly THEN
    CALL main()

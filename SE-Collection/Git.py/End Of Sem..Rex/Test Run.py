while True:
    begin_mr = input("\nEnter beginning meter reading:")
    if len(begin_mr) > 0 and begin_mr.isdigit() and 0 < int(begin_mr) < 999999999:
        begin_meter_reading = int(begin_mr)
        print(begin_meter_reading)
        break
    else:
        print("Error, either enter something or enter valid input!")

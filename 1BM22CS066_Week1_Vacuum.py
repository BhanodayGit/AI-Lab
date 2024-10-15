def vacuum_cleaner():
    target_state = {'X': '0', 'Y': '0'}
    total_cost = 0
    vacuum_position = input("Enter Location of Vacuum: ") 
    room_status = input("Enter status of " + vacuum_position + ": ") 
    other_room_status = input("Enter status of the other room: ")
    print("Initial Room Conditions: " + str(target_state))
    
    if vacuum_position == 'X':
        print("Vacuum is placed in Location X")
        if room_status == '1':
            print("Location X is Dirty.")
            target_state['X'] = '0'
            total_cost += 1 
            print("Cost for CLEANING X: " + str(total_cost))
            print("Location X has been Cleaned.")
        if other_room_status == '1':
            print("Location Y is Dirty.")
            print("Moving right to Location Y.")
            total_cost += 1 
            print("COST for moving RIGHT: " + str(total_cost))
            target_state['Y'] = '0'
            total_cost += 1 
            print("COST for SUCK: " + str(total_cost))
            print("Location Y has been Cleaned.")
        else:
            print("No action. Cost: " + str(total_cost))
            print("Location Y is already clean.")
    else:
        print("Vacuum is placed in Location Y")
        if room_status == '1':
            print("Location Y is Dirty.")
            target_state['Y'] = '0'
            total_cost += 1 
            print("COST for CLEANING Y: " + str(total_cost))
            print("Location Y has been Cleaned.")
        if other_room_status == '1':
            print("Location X is Dirty.")
            print("Moving LEFT to Location X.")
            total_cost += 1 
            print("COST for moving LEFT: " + str(total_cost))
            target_state['X'] = '0'
            total_cost += 1 
            print("COST for SUCK: " + str(total_cost))
            print("Location X has been Cleaned.")
        else:
            print("No action. Cost: " + str(total_cost))
            print("Location X is already clean.")

    print("TARGET STATE: ")
    print(target_state)
    print("Performance Measurement: " + str(total_cost))

vacuum_cleaner()

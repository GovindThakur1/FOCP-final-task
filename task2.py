# Creating required variables
runner_details_list = []
number_of_runners = 0
total_time = 0
fastest_time = 0
slowest_time = 0

# Printing on the screen
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")

# Prompting the user to enter the value in specific format
print('Enter the runner datas in the format (Runner_Number::Time_Seconds) ')

# Taking the user input and checking if valid. If entered value is valid then
# it is appended to runner_details_list otherwise exception part is executed.
while True:
    try:
        user_input = input('> ')

        # Parsing the user input based on :: delimiter. It will be a list
        parsed_input = user_input.strip().split('::')

        # Loop breaks if user enters END
        if user_input == 'END':
            runner_details_list.append(user_input)
            break

        # Raising exception if user input does not contain :: delimiter
        elif '::' not in user_input:
            raise ValueError

        # Separating runner number and time taken after parsing the input
        data_runner_number = int(parsed_input[0])
        data_runner_time = int(parsed_input[1])

    # Exception handling and prompting whenever there is exception and using
    # continue to skip the current iteration
    except ValueError:
        print('Error in data stream. Ignoring. Carry on.')
        continue

    # Appending the runner number and time taken in a list runner_details_list
    runner_details_list.append([data_runner_number, data_runner_time])

# If the user enters nothing but End then the below statement is executed
if runner_details_list[0] == 'END':
    print('No data found. Nothing to do. What a pity!')
    quit()

# Creating empty list variables to store runner number and time taken
runner_numbers = []
times_taken = []

# Creating list of runner numbers and time taken from runner_details_list except
# the last value 'End'.
for individual_runner_detail in runner_details_list:
    if individual_runner_detail == 'END':
        break

    runner_numbers.append(individual_runner_detail[0])
    times_taken.append(individual_runner_detail[1])

    # Calculate total number of runners and total time
    number_of_runners += 1
    total_time += individual_runner_detail[1]

# Calculating average time, fastest_time and slowest time and correcting grammar
# based on number of minutes and seconds
average_time_taken = total_time / number_of_runners
average_minutes = int(average_time_taken // 60)
average_seconds = int(average_time_taken % 60)

avg_min = 'minute' if average_minutes == 1 else 'minutes'
avg_sec = 'second' if average_seconds == 1 else 'seconds'

fastest_time = min(times_taken)
fastest_time_minutes = fastest_time // 60
fastest_time_seconds = fastest_time % 60

f_min = 'minute' if fastest_time_minutes == 1 else 'minutes'
f_sec = 'second' if fastest_time_seconds == 1 else 'seconds'

slowest_time = max(times_taken)
slowest_time_minutes = slowest_time // 60
slowest_time_seconds = slowest_time % 60

s_min = 'minute' if slowest_time_minutes == 1 else 'minutes'
s_sec = 'second' if slowest_time_seconds == 1 else 'seconds'

# Finding fastest runner number
fastest_runner_number = runner_numbers[times_taken.index(fastest_time)]

# Printing the results
print('\nTotal Runners:', number_of_runners)
print('Average Time:  {} {}, {} {}'.format(average_minutes, avg_min,
                                           average_seconds, avg_sec))
print('Fastest Time:  {} {}, {} {}'.format(fastest_time_minutes, f_min,
                                           fastest_time_seconds, f_sec))
print('Slowest Time:  {} {}, {} {}'.format(slowest_time_minutes, s_min,
                                           slowest_time_seconds, s_sec))
print('\nBest Time Here: Runner #{}'.format(fastest_runner_number))

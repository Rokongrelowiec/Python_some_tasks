class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'


def meeting():
    starting_hour = input("Enter start of meeting: ")
    meeting_time = int(input("Enter meeting time [in minutes]: "))

    starting_hour = starting_hour.strip()

    hour_start = int(starting_hour[0] + starting_hour[1])
    min_start = int(starting_hour[3] + starting_hour[4])

    i = 0
    while True:
        if (meeting_time - (i * 60)) >= 0:
            i += 1
        else:
            break

    if i > 0:
        i -= 1

    hour_meeting = i
    min_meeting = meeting_time - hour_meeting * 60
    final_hour = hour_start + hour_meeting

    e = 0

    while True:
        if ((min_meeting + min_start) - 60 * e) > 59:
            e += 1
        else:
            break

    final_hour += e
    final_min = (min_meeting + min_start) - e * 60

    while final_hour >= 24:
        final_hour -= 24

    print(f"{bcolors.OK}Meeting ends at: {final_hour} : {final_min}{bcolors.RESET}")

meeting()

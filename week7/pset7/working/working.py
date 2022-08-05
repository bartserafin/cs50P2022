import re


def main():
    """
    Convert 12h hours clock time format to 24h hours clock time format
    input:9 AM to 5 PM
    output: 9 to 17
    """
    print(convert(input("Hours: ")).strip())


def convert(s):
    # find all times in input
    matches = re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b", s, re.IGNORECASE)
    result = []

    # print(matches)

    if not matches:
        raise ValueError
    else:

        # Check if only start time and end time provided
        if len(matches) != 2:
            raise ValueError
        else:

            # check bounds hours: 1-12, minutes: 0-60
            for time in matches:
                if ':' in time:
                    try:
                        hours = int(time.split(' ')[0].split(':')[0])
                        minutes = int(time.split(' ')[0].split(':')[1])
                    except:
                        raise ValueError
                else:
                    try:
                        hours = int(time.split(' ')[0])
                        minutes = 0
                    except:
                        raise ValueError

                if not (1 <= hours <= 12 and 0 <= minutes < 60):
                    raise ValueError

                # print(f'Hours: {hours}, minutes: {minutes}')


                # convert 12 hours to 24 hours format
                # convert AM
                if 'AM' in time.upper():
                    if hours == 12:
                        hours = '00'
                    elif hours < 10:
                        hours = '0' + str(hours)
                    if minutes:
                        if minutes < 10:
                            minutes = '0' + str(minutes)
                        result.append(f'{str(hours)}:{str(minutes)}')
                    else:
                        result.append(f'{str(hours)}:00')


                # convert PM
                if 'PM' in time.upper():
                    if hours == 12:
                        hours = 0
                    if minutes:
                        if minutes < 10:
                            minutes = '0' + str(minutes)
                        result.append(f'{str(hours+12)}:{str(minutes)}')
                    else:
                        result.append(f'{str(hours+12)}:00')



    answer = f'{result[0]} to {result[1]}'

    return answer





if __name__ == "__main__":
    main()
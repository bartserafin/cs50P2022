import sys
import csv

def main():
    validate()
    csv_cleaner()

def validate():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1]:
        sys.exit(f"Could not read {sys.argv[1]}")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        return True

def csv_cleaner():
    input_list = []
    with open(sys.argv[1]) as input:
        input_reader = csv.DictReader(input)
        for row in input_reader:
            input_list.append(row)

        print(input_list)

        with open(sys.argv[2], "w") as output:
            fieldnames = ['first', 'last', 'house']
            output_writer = csv.DictWriter(output, fieldnames=fieldnames)
            # write headers first
            output_writer.writerow(
                {
                    fieldnames[0]: fieldnames[0],
                    fieldnames[1]: fieldnames[1],
                    fieldnames[2]: fieldnames[2]
                }
            )

            # write students
            for student in input_list:
                output_writer.writerow(
                    {
                        fieldnames[0]: student['name'].split(',')[1].strip(), # grab name
                        fieldnames[1]: student['name'].split(',')[0].strip(), # grab last name
                        fieldnames[2]: student['house'] # grab house
                    }
            )



if __name__ == '__main__':
    main()
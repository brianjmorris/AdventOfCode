class DayOne:

    def __init__(self, input_path):
        self.input_path = input_path

    def print_most_calories(self):
        current = 0
        most = 0
        f = open(self.input_path, "r")

        for line in f:
            if line.strip():
                current += int(line)

                if most < current:
                    most = current

            else:
                current = 0

        print("Most calories: " + str(most))


    def print_top_3_most_calories(self):
        current = 0
        most = 0
        second_most = 0
        third_most = 0
        f = open(self.input_path, "r")

        for line in f:
            if line.strip():
                current += int(line)

                if most < current:
                    third_most = second_most
                    second_most = most
                    most = current
                elif second_most < current:
                    third_most = second_most
                    second_most = current
                elif second_most < current:
                    third_most = current

            else:
                current = 0

        print("Most calories: " + str(most))
        print("Second most calories: " + str(second_most))
        print("Third most calories: " + str(third_most))

        print("\nTotal of top 3: " + str(most + second_most + third_most))


day_one = DayOne("Input/DayOneInput.txt")

# day_one.print_most_calories()
day_one.print_top_3_most_calories()
class DaySix:

    def __init__(self, input_path):
        self.input_path = input_path
    

    def find_start_of_packet_marker(self, data):
        for i in range(len(data) - 3):
            if data[i] != data[i+1] and data[i] != data[i+2] and data[i] != data[i+3] and data[i+1] != data[i+2] and data[i+1] != data[i+3] and data[i+2] != data[i+3]:
                return i + 4
    

    def find_marker(self, data, window_size):
        i = window_size
        window = ""

        while i < len(data):
            # get the current window
            window = data[(i - window_size):i]
            
            # start at the end of the window
            j = window_size - 1
            window_increment = 1
            unique_window = True

            while 0 <= j:
                # check if current character is present more than once
                if 1 < window.count(window[j]):

                    # determine how far to increment the window
                    window_increment += window.find(window[j])

                    unique_window = False
                    break

                j -= 1

            if unique_window:
                return i

            i += window_increment

        return None


    def main(self, part):

        f = open(self.input_path, "r")
        data = f.read().strip()

        if part == 1:
            #return self.find_start_of_packet_marker(data)
            return self.find_marker(data, 4)
        else:
            return self.find_marker(data, 14)



day_six = DaySix("Input/DaySixInput.txt")

print("Part One: " + str(day_six.main(1)))

print("Part Two: " + str(day_six.main(2)))
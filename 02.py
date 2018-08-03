# Read data
file_obj = open("input_data_02.dat", "r")
#file_obj = open("input_data_02_2.dat", "r")
data = file_obj.readlines()

#==================================================
# CLASS DOOR
#==================================================

class Door:
    # Current state
    row = 1
    col = 1
    code = []
    # Move around pad
    def move(self, direction):
        if direction == 'R':
            self.col = min(2, self.col+1)
        elif direction == 'L':
            self.col = max(0, self.col-1)
        elif direction == 'D':
            self.row = min(2, self.row+1)
        elif direction == 'U':
            self.row = max(0, self.row-1)
    # Obtain number
    def current_number(self):
        if (self.row == 0 and self.col == 0):
            self.code.append(1)
        elif (self.row == 0 and self.col == 1):
            self.code.append(2)
        elif (self.row == 0 and self.col == 2):
            self.code.append(3)
        elif (self.row == 1 and self.col == 0):
            self.code.append(4)
        elif (self.row == 1 and self.col == 1):
            self.code.append(5)
        elif (self.row == 1 and self.col == 2):
            self.code.append(6)
        elif (self.row == 2 and self.col == 0):
            self.code.append(7)
        elif (self.row == 2 and self.col == 1):
            self.code.append(8)
        elif (self.row == 2 and self.col == 2):
            self.code.append(9)
    # Obtain code
    def navigate(self, data):
        for line in data:
            for i in range(len(line)):
                self.move(line[i])
            self.current_number()
d = Door()
d.navigate(data)
print(d.code)


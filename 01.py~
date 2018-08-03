# Read data
file_obj = open("input_data_01.dat", "r")
data = file_obj.readlines()

instructions = data[0].split(', ')
#print(data)

print(instructions)
# Class position
class Position:
    pos_sequence = [[0, 0]]
    pos_vertical = 0
    pos_horizontal = 0
    direction = 'N'
    def __initi__(self):
        print('initialized')

    # Change direction
    def change_dir(self, ins):
        if self.direction == 'N':
            if ins[0] == 'R':
                self.direction = 'E'
            else:
                self.direction = 'W'
        elif self.direction == 'E':
            if ins[0] == 'R':
                self.direction = 'S'
            else:
                self.direction = 'N'
        elif self.direction == 'S':
            if ins[0] == 'R':
                self.direction = 'W'
            else:
                self.direction = 'E'
        elif self.direction == 'W':
            if ins[0] == 'R':
                self.direction = 'N'
            else:
                self.direction = 'S'
                
    # Move
    def move(self, ins):
        val = int(ins[1:])
        for i in range(val):
            # Direction North
            if self.direction == 'N':
                self.pos_vertical = self.pos_vertical + 1    
            # Direction South                
            elif self.direction == 'S':
                self.pos_vertical = self.pos_vertical - 1
            # Direction Esat
            elif self.direction == 'E':
                self.pos_horizontal = self.pos_horizontal + 1
            # Direction Wext
            elif self.direction == 'W': 
                self.pos_horizontal = self.pos_horizontal - 1
            # Check if visited location
            if [self.pos_vertical, self.pos_horizontal] in self.pos_sequence:
                print('Position repeated: [', self.pos_vertical, ',', self.pos_horizontal,']')
            self.pos_sequence.append([self.pos_vertical, self.pos_horizontal])

    # Steps
    def step(self, ins):
        self.change_dir(ins)
        self.move(ins)
    # Follow instructions
    def take_steps(self, instructions):
        for ins in instructions:
            self.step(ins)
    # Print status
    def print_status(self):
        print(['Position Vertical: ', self.pos_vertical])
        print(['Position Horizontal: ', self.pos_horizontal])

pos = Position()
pos.take_steps(instructions)
pos.print_status()
print(pos.pos_sequence)


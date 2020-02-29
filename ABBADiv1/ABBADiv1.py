class ABBADiv1:    
    def reverse_str(self, s):
        s = list(s)
        s.reverse()
        return ''.join(s)

    def canObtain(self, initial, target):
        if target == initial:
            return 'Possible'
        elif len(target) < len(initial):
            return 'Impossible'
        elif target[0] == 'A' and target[-1:] == 'A':
            return self.canObtain(initial, target[:-1])
        elif target[0] == 'B' and target[-1:] == 'B':
            return self.canObtain(initial, self.reverse_str(target)[:-1])
        elif target[0] == 'A' and target[-1:] == 'B':
            return 'Impossible'
        elif target[0] == 'B' and target[-1:] == 'A':
            tmp = self.reverse_str(target)
            if self.canObtain(initial, target[:-1]) == 'Possible' \
            or \
            self.canObtain(initial, tmp[:-1]) == 'Possible':
                return 'Possible'
            else:
                return 'Impossible'
        else:
            return 'Impossible'
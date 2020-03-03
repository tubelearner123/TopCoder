class ANewHope:
    def index_pos_diff(self, week_1, week_2, shirt_num):
        pos_in_week_1 = week_1.index(shirt_num)
        pos_in_week_2 = week_2.index(shirt_num)
        # -1 for len(week) because it starts counting at 1 
        pos_len_until_weekend_1 = ( len(week_1) - 1 ) - pos_in_week_1
        pos_len_from_start_of_week_2 = pos_in_week_2
        # +1 because there is a day between the two weeks
        return pos_len_until_weekend_1 + pos_len_from_start_of_week_2 + 1

    def is_possible_within_washing_days(self, week_1, week_2, D):
        for elem in week_1:
            if self.index_pos_diff(week_1, week_2, elem) < D:
                return False
        return True

    def list_shift_right(self, list_input, n):
        return list_input[-n:] + list_input[:-n]

    def count(self, firstWeek, lastWeek, D):
        result = 2
        firstWeek = list(firstWeek)
        lastWeek = list(lastWeek)
        curr_week = firstWeek
        while True:
            if self.is_possible_within_washing_days(curr_week, lastWeek, D):
                break
            else:
                next_possible_week = self.list_shift_right(curr_week, 1)
                while self.is_possible_within_washing_days(curr_week, next_possible_week, D) == False:
                    next_possible_week = self.list_shift_right(next_possible_week, 1)
                curr_week = next_possible_week
                result += 1
        if result == 2 and firstWeek == lastWeek:
            return 1
        return result
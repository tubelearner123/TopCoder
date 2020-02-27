class A0Paper:
    def calculate_combined_carry_over(self, list_A, curr_pos):
        result = 0

        #generate reversed list
        reversed_list_i = list(range(curr_pos))
        reversed_list_i.reverse()

        for i in range(curr_pos):
            result += list_A[i] * (2 ** (reversed_list_i[i]+1))

        return result

    def canBuild(self, A):
        list_A = list(A)
        curr_pos = 0
        
        while curr_pos < len(list_A):

            curr_A = list_A[curr_pos]
            curr_acc = self.calculate_combined_carry_over(list_A, curr_pos)

            if curr_A > 0 and (curr_A + curr_acc) >= 2 ** curr_pos:
                return 'Possible'

            curr_pos += 1
            
        return 'Impossible'
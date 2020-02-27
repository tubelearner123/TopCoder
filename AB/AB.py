class AB:

    a_letter = 'A'
    b_letter = 'B'
    a_code = 0
    b_code = 1

    def convert_from_bits_to_str(self, list_bits):
        result = ''
        for curr_bit in list_bits:
            if curr_bit == self.a_code:
                result += self.a_letter
            elif curr_bit == self.b_code:
                result += self.b_letter
        return result

    def createString(self, N, K):
        all_possible_cases = self.gen_permutation(N)
        for curr_list_bits in all_possible_cases:
            if self.satisfy_K(K, curr_list_bits):
                return self.convert_from_bits_to_str(curr_list_bits)
        return ''

    def gen_permutation(self, n):
        if n == 1:
            return [[0], [1]]
        else:
            result = []
            for elem in self.gen_permutation(n-1):
                result.append([0] + elem)
                result.append([1] + elem)
            return result

    def satisfy_K(self, K, list_bits):

        K_pair_counter = 0

        # Two cursors -> main_cursor and check_for_A_cursor
        main_cursor = 0

        while main_cursor < len(list_bits):

            if list_bits[main_cursor] == self.b_code:

                # Once we have found B, we start looking for all A before B
                check_for_A_cursor = 0
                while check_for_A_cursor < main_cursor:
                    if list_bits[check_for_A_cursor] == self.a_code:
                        K_pair_counter += 1
                    check_for_A_cursor += 1

            main_cursor += 1

        if K == K_pair_counter:
            return True
        else:
            return False
class AccessChanger:
    def convert(self, program):
        program = list(program)
        result = []
        for line in program:
            split_comments = line.split('//')
            uncommented_code = split_comments[0]
            converted_code = '.'.join(uncommented_code.split('->'))
            result.append('//'.join([converted_code] + split_comments[1:]))
        return tuple(result)
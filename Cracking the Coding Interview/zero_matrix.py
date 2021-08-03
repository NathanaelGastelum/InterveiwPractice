# Question 1.8 

# Input: M x N matrix
# Output: none (done in place)

# Follow-up: O(1) space

class ZeroMatrix:
    def zero(self, matrix):
        row_has_zero = False
        col_has_zero = False

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if row == 0:
                        row_has_zero = True
                    if col == 0:
                        col_has_zero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[row])):
                    matrix[row][col] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        # handle at the end to avoid overwriting log
        if row_has_zero == True and col_has_zero == True:
            for col in range(len(matrix[0])):
                    matrix[0][col] = 0
            for row in range(len(matrix)):
                    matrix[row][0] = 0
        elif row_has_zero == True:
            for i in range(len(matrix)):
                matrix[0][i] = 0
        elif col_has_zero == True:
            for i in range(len(matrix[0])):
                matrix[i][i] = 0


test_matrix = [[[1, 2, 3, 4],
                [1, 0, 3, 4],
                [1, 2, 3, 4]],

                [[1, 2, 3, 4],
                [1, 2, 3, 4],
                [1, 2, 3, 0]],

                [[0, 2, 3, 4],
                [1, 2, 0, 4],
                [1, 2, 3, 4]],

                [[0, 2],
                [1, 2]],

                [[1, 0],
                [1, 2]],

                [[0]]]
expected = [[[1, 0, 3, 4],
            [0, 0, 0, 0],
            [1, 0, 3, 4]],

            [[1, 2, 3, 0],
            [1, 2, 3, 0],
            [0, 0, 0, 0]],

            [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 0, 4]],

            [[0, 0],
            [0, 2]],

            [[0, 0],
            [1, 0]],
            
            [[0]]]
for i in range(len(test_matrix)):
    ZeroMatrix().zero(test_matrix[i])
    assert test_matrix[i] == expected[i], f"Test {i}: expected: {expected[i]}, recieved: {test_matrix[i]}"

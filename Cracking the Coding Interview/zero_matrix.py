# Question 1.8 

# Input: M x N matrix
# Output: none (done in place)

class ZeroMatrix:
    def zero(self, matrix):
        zero_log = {"rows":set(), "cols":set()}

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zero_log["rows"].add(row)
                    zero_log["cols"].add(col)
        
        for row in zero_log["rows"]:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0
        for col in zero_log["cols"]:
            for row in range(len(matrix)):
                matrix[row][col] = 0


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
            
            [[0]]]
for i in range(len(test_matrix)):
    ZeroMatrix().zero(test_matrix[i])
    assert test_matrix[i] == expected[i], f"Test {i}: expected: {expected[i]}, recieved: {test_matrix[i]}"

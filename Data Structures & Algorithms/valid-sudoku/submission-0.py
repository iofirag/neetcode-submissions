class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # cube check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cube_ctr = 0
                cube_set = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        cube_num = board[k][l]
                        if cube_num.isdigit():
                            cube_set.add(cube_num)
                            cube_ctr += 1
                if cube_ctr != len(cube_set):
                    # unique digits in set : equal to all founded digits in cube
                    return False
                print('--------------')

        for i in range(9):
            # row check
            row_ctr = 0
            row_set = set()
            for row_num in board[i]:
                if row_num.isdigit():
                    row_set.add(row_num)
                    row_ctr += 1
            if row_ctr != len(row_set):
                # unique digits in set : equal to all founded digits in row
                return False
            
            # column check
            column_ctr = 0
            column_set = set()
            for j in range(9):
                comumn_num = board[j][i]
                if comumn_num.isdigit():
                    column_set.add(comumn_num)
                    column_ctr += 1
            if column_ctr != len(column_set):
                # unique digits in set : equal to all founded digits in column
                return False

        return True
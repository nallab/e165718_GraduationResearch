"""
精度を算出する．
"""
import csv

score = 0
Correct_Answer = 0
accuracy = 0
count = 0
with open('./review/star5_comp.csv')as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        count += 1
        score = row[1].strip()
        score = int(score)
        print('レビュー' + str(count) + ': ' + str(score))
        # # -レビュー (star1, star2)
        # if score < 0:
        #     Correct_Answer += 1
        # else:
        #     continue

        # # +-0レビュー (star3)
        # if score == 0:
        #     Correct_Answer += 1
        # else:
        #     continue

        # +レビュー (star4, star5)
        if score > 0:
            Correct_Answer += 1
        else:
            continue

accuracy = Correct_Answer/count
print('\n')
print('正解数: ' + str(Correct_Answer))
print('精度: ' + str(accuracy))

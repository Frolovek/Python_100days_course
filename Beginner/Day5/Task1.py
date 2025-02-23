student_scores = [180, 124, 165, 173, 189, 169, 146]

print(max(student_scores))

maximum_score = student_scores[0]

for score in student_scores:
    if score > maximum_score:
        maximum_score = score

print(maximum_score)
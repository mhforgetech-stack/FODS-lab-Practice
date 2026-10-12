import numpy as np
student scores = np.array([
  [80,75,90,85]
  [70,80,85,75]
  [90,85,95,80]
  [85,90,88,92]
])

subjects = ["Math","Science","English","History"]

average_scores = np.mean(Student_Scores,axis=0)

print("Average score for each subject:")

for i in range(4):
  print(subjects[i],":",average_scores[i])
highest_subject = subjects[np.argmax(average_scores)]
print("Subject with the highest average score:",highest_subject)

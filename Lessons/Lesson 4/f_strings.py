
users = ["user1", "user1232", "new_user3"]
scores = [12.3, 2.4, 18.4]

# print(users[0], users[1], users[2])
# print(scores[0], scores[1], scores[2])

#  user1  user1232  new_user3
#   12.3       2.4       18.4

user_1_l = len(users[0])
user_2_l = len(users[1])
user_3_l = len(users[2])

print(f" {users[0]}  {users[1]}  {users[2]}")
print(f" {scores[0]:>{user_1_l}}  {scores[1]:>{user_2_l}}  {scores[2]:>{user_3_l}}")

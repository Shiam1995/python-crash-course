cars = ["Byd Seal", "Tesla", "Camaro"]
statements = ["I like the shape", "I like the movie"]

print(cars)
print(statements)

message = "I like  " + cars[0] + " because" + statements[0]
message_1 = "I like  " + cars[1] + " because" + statements[0]
message_2 = "I like  " + cars[2] + " because" + statements[1]

message_list = [message, message_1, message_2]
print(message_list)

for message in message_list:
    print(message)
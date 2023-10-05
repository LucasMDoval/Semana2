initial_position : int(input("initial position in meters: "))
initial_velocity : int(input("initial velocity in m/s: "))
acceleration : int(input("enter acceleration m/s2: "))
time : int(input("enter time in seconds: "))


final_position = (initial_position + initial_velocity * time+ (0.5 * acceleration  * time**2))

final_velocity = initial_velocity + (acceleration * time) 

print (final_position, "m")
print(final_velocity, "m/s")
print(acceleration, "m/s^2")
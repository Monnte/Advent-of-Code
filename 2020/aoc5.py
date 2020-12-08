with open("input5") as f:
    seats = f.readlines()
seats = [x.strip() for x in seats]

max_id = 0
min_id_seat = 8
max_id_seat = 127*8 + 7

seats_ids = list(range(min_id_seat, max_id_seat))

for data in seats:

    row_out = data[0:7].replace("B", "1")
    row_out = row_out.replace("F", "0")
    column_out = data[7:].replace("R", "1")
    column_out = column_out.replace("L", "0")

    seat_id = int(row_out, 2) * 8 + int(column_out, 2)

    if(seat_id > max_id):
        max_id = seat_id

    seats_ids[seat_id - 8] = ""

print("1 answer : " + str(max_id))
print("2 answer : " + str(seats_ids))

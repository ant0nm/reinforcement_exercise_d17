rooms_and_events = { 'data': { 'rooms':
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

room201_capacity = rooms_and_events['data']['rooms'][0]['capacity']
print("Capacity of room 201: {}".format(room201_capacity))
room201 = rooms_and_events['data']['rooms'][0]

print()
print("Room 201 capacity check:")
events = rooms_and_events['data']['events']
for event in events:
    result = ""
    if event["room_id"] == room201["id"]:
        result += "{} attendees".format(event['attendees'])
        if event['attendees'] <= room201_capacity:
            result += " vs {} capacity - OK".format(room201_capacity)
        else:
            result += " - not OK"
    if result == "":
        pass
    else:
        print(result)

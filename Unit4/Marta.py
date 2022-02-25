


#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:
def get_key(val):
    for key, value in new_dict.items():
        #print(f'looking for {val}\n')
        #print(f'found {value}')
        
        if val == value:
            return key
     
    return "key doesn't exist"

num_taps = 0
marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')
new_dict = {}

for line in marta_file:
    split_line = line.split(',')
    station_id = split_line[3]
    if station_id in new_dict:
        new_dict[station_id] += 1
    else:
        new_dict[station_id] = 1
    num_taps += 1
print(num_taps/len(new_dict))



average = num_taps/len(new_dict)
taps_list = list(new_dict.values())
closest = 9999999999999999
difference = 9999999999999999
for tap in taps_list:
    check_mech = abs(average - tap)
    print(f"checking value {check_mech}")
    print(f"before check {closest}")
    if check_mech <= difference:
        closest = tap
        difference = check_mech
        print(f"after check {closest}")
    

print(get_key(closest))

sorted_list = sorted(taps_list)
print(get_key(sorted_list[0]))


#You may add whatever code you want from here on to answer those three
#questions.
#
#HINT: although there are six items on each line of the file, you only
#need one of them: station ID. If you use split(",") to split up each
#line, station ID will be at index 3 on the list.
#
#HINT 2: You'll probably want to use a dictionary, with station IDs as
#the keys and 








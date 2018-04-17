import random as r
import csv

################################################
#
#   Do Not run.
#
################################################

def main():
    area_code = ["714", "310", "323", "562", "909"]
    user_id = r.randint(100000, 999999)
    sex = ["M", "F"]
    age = 0
    full_name = ''
    user = ["Boomy", "koto", "Dr", "inRed", "Xx", "xX", "XXX", "killer", "Dank", "Clone", "Dino",
            "Frost", "dreamer", "aroma", "", "tier", "queen", "royal", "gunner", "gunter",
            "snobby", "lonely", "solo", "latean", "lone", "loner", "galaxy_", "birdy",
            "sinner", "loc", "xX69", "xX420", "", "", "flower", "star", "Dropper", "_"]
    total = 0
    kills = 0
    deaths = 0
    wins = 0
    games_played = 0
    last_names =[]
    with open("last_names.txt", 'r') as f:
        for line in f:
            last_names.append(line)

        print("** Executing last names **")
    
    with open("males.txt", 'r') as f:
        male_names = []
        for line in f:
            new_line = line.replace(' ', ',')
            temp = new_line.split(',')
            male_names.append(temp[0])

        
        print("** Executing male names **")
		
    with open("females.txt", 'r') as f:
        female_names = []
        for line in f:
            new_line = line.replace(' ', ',')
            temp = new_line.split(',')
            female_names.append(temp[0])
	    
        print("** Executing female names **")
        
    lst_of_ids = []

    with open("competitors.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Phone", "Sex", "Age", "Username", "Kills", "Deaths", "Wins", "Games"])

        print("** Executing headers**")
        
        numbers = 0
        phone = ""
        for i in range(100):
            numbers = r.randint(1000000, 9999999)
            phone = r.choice(area_code) + str(numbers)
            user_id = r.randint(100000, 999999)
            while user_id not in lst_of_ids:
                lst_of_ids.append(user_id)
                user_id = r.randint(100000, 999999)

            s = r.choice(sex)
            if s == 'M':
                full_name = r.choice(male_names)
            else:
                full_name = r.choice(female_names)

            print("Player: {} created".format(i))
            username = r.choice(user) + full_name + str(r.randint(50, 999))
            full_name = full_name + " " + r.choice(last_names)
            
            # ID,Name,Phone,Sex,Age,User,Kills,Deaths,Wins,Games
            writer.writerow([user_id, full_name.title().strip('\n'), phone, s, r.randint(18, 34), username.title(), r.randint(0, 500), r.randint(0, 500), r.randint(0, 100), r.randint(0, 160)])

        
        print("** Executing players **")
        
if __name__ == "__main__":
    main()

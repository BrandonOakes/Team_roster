#import csv file
import csv

#utilize __name__ == __'main__': block- so script not executed when imported
if __name__ == '__main__':

	with open('/Users/boltfever/Downloads/soccer_players.csv') as file_object:
		#read csv file
		roster = csv.reader(file_object)
		list_of_players =[]
		for player in roster:
			# delete the height index
			del player[1]
			
			#place players in list to create list with list of players
			list_of_players.append(player)

		#delete the first element [Name, Soccer Experience, Guardian Name (s)]
		del list_of_players[0]
			


	    #Make 3 teams -Sharks/Raptors/Dragons
		Sharks = []
		Raptors = []
		Dragons = []
	    
	   

		for player_profile in list_of_players:
		#Put 3 players with experience in each team
			if player_profile[1] == 'YES' and len(Sharks) < 4:
				Sharks.append(player_profile)
			#put 3 players without experience on Sharks roster	
			else:
				if player_profile[1] == 'NO':
					Sharks.append(player_profile)
					#make sure Sharks rosters does not exceed 6 players
					if len(Sharks) == 6:
						break
		
        #make copy of roster 
		Sharks_roster = Sharks[:]

		

		for player_profile in list_of_players:
		#Put 3 players with experience in each team
			if player_profile[1] == 'YES' and player_profile not in Sharks:
				Raptors.append(player_profile)
				if len(Raptors) ==3:
					break
		#put 3 players without experience on Raptors roster		
		for player_profile in list_of_players:
			if player_profile[1] == 'NO' and player_profile not in Sharks:
				Raptors.append(player_profile)
				if len(Raptors) == 6:
					break
		
        #make copy of roster
		Raptors_roster = Raptors[:]


		
	    
	    #Add first two teams together so third team knows what players have been chosen
		Sharks += Raptors
		players_taken = Sharks

		for player_profile in list_of_players:
		#Put 3 players with experience on team, make sure players have not already been selected
			if player_profile[1] == 'YES' and player_profile not in players_taken:
				Dragons.append(player_profile)
				if len(Dragons) == 3:
					break
		#put 3 players without experience on Dragons
		for player_profile in list_of_players:
			if player_profile[1] == 'NO' and player_profile not in players_taken:
				Dragons.append(player_profile)
				if len(Dragons) == 6:
					break
		

		Dragons_roster = Dragons[:]
	#create function to send all team rosters back to text.file
	def writing_team_in(team):
		with open('teams.txt', 'a') as file:
			if team == Dragons_roster:
				file.write('Dragons')
			elif team == Raptors_roster:
				file.write('Raptors')
			elif team == Sharks_roster:
				file.write('Sharks')
			file.write('\n' + '\n')
			for plyer in team:
				#make individual list of player profile into string so it can put written in text
				player_info = ', '.join(plyer)
				file.write(player_info + '\n')
			file.write('\n')

	writing_team_in(Sharks_roster)
	writing_team_in(Raptors_roster)
	writing_team_in(Dragons_roster)







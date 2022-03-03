# Created by: Joshua Cutting
# Created on: 3/1/2022
# Purpose: To keep score of the CNY Hackathon Simulation
# Current Service Checks:
#  - www
#  - www content
#  - router icmp
#  - sshlogin



import time
import requests
import os

class Team:
	teamName = ""
	teamExternalIP = ""
	teamShellIP = ""
	teamHttpURL = ""
	teamPoints = 0
	teamData = open("teamdata/name.data", "a")

	def __init__(self, teamName, teamExternalIP, teamShellIP):
		self.teamName = teamName
		#self.teamExternalIP = teamExternalIP
		#self.teamShellIP = teamShellIP

		self.teamExternalIP="192.168.1.174"
		self.teamShellIP="192.168.1.181"
		self.teamHttpURL = "http://"+self.teamExternalIP
		self.writeCurrentData()
		namedata = open("teamdata/name.data", "a")
		namedata.write(self.teamName+".data\n")
		namedata.close()
		print("Team Created!")

	def __init__(self, teamName, teamExternalIP, teamShellIP, *args):
		self.teamName = str.rstrip(teamName)
		self.teamExternalIP = str.rstrip(teamExternalIP)
		self.teamShellIP = str.rstrip(teamShellIP)
		self.teamHttpURL = "http://"+self.teamExternalIP
		if(len(args) > 0):
			self.teamPoints = args[0]
			print(self.teamName+" Re-initialized!")
		else:
			self.teamPoints = 0
			self.writeCurrentData()
			namedata = open("teamdata/name.data", "a")
			namedata.write(self.teamName+".data\n")
			namedata.close()
			print("Team Created!")

	def writeCurrentData(self):
		self.teamData = open("teamdata/"+self.teamName+".data", "w")
		self.teamData.write("")
		self.teamData.close()
		self.teamData = open("teamdata/"+self.teamName+".data", "a")
		self.teamData.write(self.teamName+"\n")
		self.teamData.write(str(self.teamPoints)+"\n")
		self.teamData.write(self.teamExternalIP+"\n")
		self.teamData.write(self.teamShellIP+"\n")
		self.teamData.close()








def main():
	running = True
	originalTime = time.time()
	currentTime = time.time()
	timePerCycle = 5
	teams = []
	newgame = input("Do you want to start a new game? (Y/N) : ")
	if(newgame=="Y"):
		os.system("rm teamdata/*")
		numOfTeams = int(input("How many teams are part-taking? : "))

		for i in range(0,numOfTeams):
			newname = input("Team name? : ")
			newIP = input("What is " + newname +"\'s public IP? : ")
			newShellIP = input("What is "+newname+"\'s public Shell IP? : ")
			newteam = Team(newname, newIP, newShellIP)
			teams.append(newteam)
	else:
		print("Loading teams...")
		namedata = open("teamdata/name.data", "r")
		lines = namedata.readlines()
		print(lines)
		for i in range (0,len(lines)):
			teamdata = open(str.rstrip("teamdata/"+lines[i]), "r")
			teamLines = teamdata.readlines()
			newname = teamLines[0]
			newscore = int(teamLines[1])
			newExternalIP = teamLines[2]
			newShellIP = teamLines[3]
			newteam = Team(newname, newExternalIP, newShellIP, newscore)
			teams.append(newteam)
			teamdata.close()

		namedata.close()


	while running:
		currentTime = time.time()
		if currentTime - originalTime >= timePerCycle:
			for team in teams:
				icmpOn = False
				print("Checking... "+team.teamName+"'s services.")

				#router icmp checks
				try:
					os.system('ping -c 1 -w 2 '+team.teamExternalIP+' | grep \"packet loss\" | cut -d \" \" -f 6 > output/routericmp_output')
					f = open("output/routericmp_output", "r")
					temp = repr(f.read())
					if(temp[1]=='0'):
						icmpOn = True
						team.teamPoints+=1
						print(team.teamName+" scored for router ICMP!")
					else:
						print(team.teamName+" did not score for router ICMP.")
						print(team.teamName+" did not score for www response.")
						print(team.teamName+" did not score for www content.")



				#www and www content checks
					if icmpOn:
						try:
							response = requests.get(team.teamHttpURL)
							team.teamPoints+=1
							print(team.teamName+" scored for www response!")
							if(response.status_code==200):
								team.teamPoints+=1
								print(team.teamName+" scored for www content!")
							else:
								print(team.teamName+" did not score for www content.")
						except:
							print(team.teamName+" did not score for www response.")
							print(team.teamName+" did not score for www content.")


				except Exception as e:
					print(e)
				#shell login check

				try:
					os.system('echo 255 > output/sshlogin_output')
					os.system('ssh -q tom@'+team.teamShellIP+ ' exit && echo $? > output/sshlogin_output')
					f = open("output/sshlogin_output", "r")
					if(repr(f.read())==repr('0\n')):
						team.teamPoints+=1
						print(team.teamName+" scored for ssh login!")
					else:
						print(team.teamName+" did not score for ssh login.")
				except Exception as e:
					print(e)

				team.writeCurrentData()

			originalTime = time.time()



if __name__ == '__main__':
	main()




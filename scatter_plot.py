Gryffindor = dataNum.loc[data["Hogwarts House"] == "Gryffindor"]["History of Magic"]
Gryffindor2 = dataNum.loc[data["Hogwarts House"] == "Gryffindor"]["Transfiguration"]

Slytherin = dataNum.loc[data["Hogwarts House"] == "Slytherin"]["History of Magic"]
Slytherin2 = dataNum.loc[data["Hogwarts House"] == "Slytherin"]["Transfiguration"]

Ravenclaw = dataNum.loc[data["Hogwarts House"] == "Ravenclaw"]["History of Magic"]
Ravenclaw2 = dataNum.loc[data["Hogwarts House"] == "Ravenclaw"]["Transfiguration"]

Hufflepuff = dataNum.loc[data["Hogwarts House"] == "Hufflepuff"]["History of Magic"]
Hufflepuff2 = dataNum.loc[data["Hogwarts House"] == "Hufflepuff"]["Transfiguration"]


# plt.figure()
# plt.scatter(Gryffindor, Gryffindor2, label = 'students', color='r')
# plt.scatter(Slytherin, Slytherin2, label = 'students', color='y')
# plt.scatter(Ravenclaw, Ravenclaw2, label = 'students', color='g')
# plt.scatter(Hufflepuff, Hufflepuff2, label = 'students', color='b')
# plt.legend()
# plt.title("correlated features")
# plt.xlabel("Astronomy")
# plt.ylabel("Defense Against the Dark Arts")
# plt.show()

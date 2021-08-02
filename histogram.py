# for col in dataNum.columns:
#     Gryffindor = dataNum.loc[data["Hogwarts House"] == "Gryffindor"][col]
#     Slytherin = dataNum.loc[data["Hogwarts House"] == "Slytherin"][col]
#     Ravenclaw = dataNum.loc[data["Hogwarts House"] == "Ravenclaw"][col]
#     Hufflepuff = dataNum.loc[data["Hogwarts House"] == "Hufflepuff"][col]
#     plt.figure()
#     plt.hist(Gryffindor, bins=25, alpha=0.5, label = 'Gry', color = 'r')
#     plt.hist(Ravenclaw, bins=25, alpha=0.5, label = 'Rav', color = 'b')
#     plt.hist(Slytherin, bins=25, alpha=0.5, label = 'Sly', color = 'g')
#     plt.hist(Hufflepuff, bins=25, alpha=0.5, label = 'Huf', color = 'y')
#     plt.legend(loc = 'upper right')
#     plt.title(col)
#     plt.savefig(col + ".png")
#     # plt.show()
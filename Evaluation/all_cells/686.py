colors = {"s002": "#E32636", "s003": "#B0BF1A", "s004": "#7CB9E8", "s005": "#84DE02", "s007": "#EFDECD", "s008": "#00308F", "s010": "#0048BA", "s011": "#AF002A", "s012": "#C9FFE5", "s013": "#72A0C1", "s015": "#C46210", "s016": "#B284BE", "s017": "#E52B50", "s018": "#9F2B68", "s019": "#F19CBB", "s020": "#AB274F", "s021": "#D3212D", "s022": "#3B7A57", "s024": "#FFBF00", "s025": "#FF7E00", "s026": "#3B3B6D", "s027": "#391802", "s028": "#804040", "s029": "#D3AF37", "s030": "#34B334", "s031": "#FF8B00", "s032": "#FF9899", "s033": "#431C53", "s034": "#B32134", "s035": "#FF033E", "s036": "#CFCFCF", "s037": "#551B8C", "s038": "#F2B400", "s039": "#9966CC", "s040": "#A4C639", "s041": "#F2F3F4", "s042": "#CD9575", "s043": "#665D1E", "s044": "#915C83", "s046": "#841B2D", "s047": "#FAEBD7", "s048": "#008000", "s049": "#66B447", "s050": "#8DB600", "s051": "#FBCEB1", "s052": "#00FFFF", "s053": "#7FFFD4", "s054": "#D0FF14", "s055": "#C0C0C0", "s056": "#4B5320", "s057": "#3B444B"}
reduced_keystrokes_ = reduced_keystrokes[:,:2]

vis_users = ["s005", "s010", "s011", "s016"]
plt.figure(figsize=(10,10))
for i, point in enumerate(reduced_keystrokes_):
    #Para facilitar a visualização, faremos o plot de apenas quatro usuários
    if recordings[i][0] in vis_users:
        plt.scatter(point[0], point[1], c=colors[recordings[i][0]])
plt.title("Dados de digitação dos usuários {} (SVD)".format(", ".join(vis_users)))
plt.show()
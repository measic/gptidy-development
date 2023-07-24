def plot_stacked_scores(athlete):
    plt.figure(figsize=(30,10))
    
    x = np.arange(len(athlete))
    
    athlete['additional_index'] = x
    scores = [
        athlete.climbing_scores,
        athlete.yoga_scores,

        athlete.tech_scores,
        athlete.power_scores,

        athlete.gym_scores,
        athlete.arc_scores,

        athlete.hang_scores,
    ]
    
    labels = ['Climbing', 'Yoga', 'Technique', 'Power', 'Gymnastics', 'ARC', 'Hangboarding',  ]
    colors = [ 'cornflowerblue', 'darkturquoise', 'mediumorchid', 'red', 'gold', 'gray', 'lightgreen', ]

    y = np.vstack(scores)
    plt.stackplot(x, y, labels=labels, colors=colors)
    plt.plot(x, athlete.scores, marker='o', color='lightgray')

    for index, row in athlete.iterrows():
        if row.notes:
            plt.annotate(row.notes, xy=(row.additional_index, row.scores), fontsize=14, fontweight='bold')
            
    plt.legend(loc=2)
    plt.show()
    
def plot_scores(athlete):
    """
    Plot the following scores:
    
    - Hangboard
    - Climbing
    - Gymnastics 
    - Technical Scores
    
    """
    fig, axes = plt.subplots()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    
    ax1.set_title('Hangboarding')
    ax2.set_title('Gymnastics')
    ax3.set_title('Climbing')
    ax4.set_title('Technique')
    
    athlete_hang_scores = athlete[athlete.hang > 0]
    athelete_gym_scores = athlete[athlete.gym_scores > 0]
    athlete_climbing_scores = athlete[athlete.climbing_scores > 0]
    athlete_tech_scores = athlete[athlete.tech_scores > 0]
    
    # plt.figure(figsize=(20,10))
    # plt.plot(athlete_hang_scores.hang_scores, marker='o', color='green')
    
    athlete_hang_scores.hang_scores.plot(ax=ax1, figsize=(20, 10), marker='o', color='green')
    athelete_gym_scores.gym_scores.plot(ax=ax2, figsize=(20, 10), marker='o', color='gold')
    athlete_climbing_scores.climbing_scores.plot(ax=ax3, figsize=(20, 10), marker='o', color='cornflowerblue')
    athlete_tech_scores.tech_scores.plot(ax=ax4, figsize=(20, 10), marker='o', color='mediumorchid')
    
    plt.show()
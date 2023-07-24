### Read the csv file to get labels
# Visualizations will be shown in the notebook.
%matplotlib inline

with open('signnames.csv', 'r') as signfile:
    signs = csv.reader(signfile)
    sign_dict = {}
    for row in signs:
        try:
            int(row[0])
            sign_dict[row[0]] = row[1]
        except:
            continue

# print(sign_dict)

def get_frequencies(num_labels, sign_dict):
    text_labels = [sign_dict[str(num_label)] for num_label in num_labels]
    # Get frequencies for text_labels
    freq_dict = {}
    for text_label in text_labels:
        if text_label not in freq_dict:
            freq_dict[text_label] = 1
        else:
            freq_dict[text_label] += 1
    return freq_dict

sign_frequencies = get_frequencies(y_train, sign_dict)

fig, ax = plt.subplots(figsize=(15, 10))
classes = list(sign_dict.values())
ind = np.arange(len(classes))
width = 0.8

rects = ax.bar(ind, sign_frequencies.values(), width, align="edge", alpha=0.5)
ax.set_ylabel('Frequency')
ax.set_title('Traffic Sign Classes')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(sign_frequencies.keys(), rotation=90)
plt.show()
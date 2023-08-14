# Getting the tsv file from the gien link provided using request library
url="https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv"
response = requests.get(url)

with open('image_predictions.tsv', 'wb') as file:
    file.write(response.content)
    
#reading the file
img_predictions = pd.read_csv('image_predictions.tsv',sep='\t')
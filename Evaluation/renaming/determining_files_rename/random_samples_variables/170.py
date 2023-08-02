output_directory = 'test_images_output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
variable_def = mpimg.imread('test_images/solidYellowLeft.jpg')
print('This image is:', type(variable_def), 'with dimensions:', variable_def.shape)
plt.imshow(variable_def)
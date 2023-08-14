white_output = 'white.mp4'
clip1 = VideoFileClip("solidWhiteRight.mp4")
clearUnjitter()
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
%time white_clip.write_videofile(white_output, audio=False)
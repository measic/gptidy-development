out_dir = "tmp"   # Name of an arbitray directory for temporary storage of Gepard input and output. Change as you like.
gepard_root = "/path/to/gepard"   # Change to the directory in which you installed Gepard.
gepard_jar = f"{gepard_root}/dist/Gepard-1.40.jar"
gepard_mat = f"{gepard_root}/resources/matrices/edna.mat"
gepard_command = f"java -cp {gepard_jar} org.gepard.client.cmdline.CommandLine -matrix {gepard_mat}"
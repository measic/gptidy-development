#TRAINING
logs_chatbot = Chatbot.fit(x= [X_[:dataset_cut,:], padded_T[:dataset_cut,:-1]], y = T_[:dataset_cut,1:], 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size,
                                    callbacks = [callback]).history
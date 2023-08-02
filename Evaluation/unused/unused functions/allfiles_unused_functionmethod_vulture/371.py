def get_neighbour_messages(sender, receiver):
    messages = []
    for n in sender.neighbours:
        if n is not receiver:
            messages.append(sender.in_msgs[n])
    return messages
    
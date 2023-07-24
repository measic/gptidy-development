# ANSWER 1.5
def receive_msg(self, other, msg):
    
    
    if other not in self.in_msgs or not np.allclose(self.in_msgs[other], msg):
        self.in_msgs[other] = msg
        
        pending = []
        for n in self.neighbours:
            if can_send_message(self, n):
                pending.append(n)
        
        self.pending.update(pending)
    
    else:
        self.in_msgs[other] = msg
    
    
    
Node.receive_msg = receive_msg

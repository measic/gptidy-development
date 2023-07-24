Formatted code:
```python
def can_send_message(sender, receiver):
    for n in sender.neighbours:
        if n is not receiver and n not in sender.in_msgs:
            return False
    
    return True

# Do the results make sense?
print(can_send_message(X, X_prior))
print(can_send_message(X_prior, X))
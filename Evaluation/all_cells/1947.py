for pid in TensorBoard.list()['pid']:
    TensorBoard().stop(pid)
    print 'Stopped TensorBoard with pid {}'.format(pid)
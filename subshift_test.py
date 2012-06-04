def subshift(L, start, end, insert_at):
    #'Nick Craig-Wood'
    temp = L[start:end]
    L = L[:start] + L[end:]
    return L[:insert_at] + temp + L[insert_at:]

def inplace_shift(L, start, length, pos):
    if pos > start + length:
        (a, b, c) = (start, start + length, pos)
    elif pos <= start:
        (a, b, c) = (pos, start, start + length)
    else:
        raise ValueError("Cannot shift a subsequence to inside itself")

    span1, span2 = (b - a, c - b)
    if span1 < span2:
        tmp = L[a:b]
        L[a:a + span2] = L[b:c]
        L[c - span1:c] = tmp
    else:
        tmp = L[b:c]
        L[a + span2:c] = L[a:b]
        L[a:a + span2] = tmp

# Think this works correctly now
def unbeli(x, start, end, at): 

    # Cannot shift to a position in the range of the 
    # subsequence to be shifted
    if at > start and at <= end:
        raise ValueError('Goal position cannot be in origin range')

    x[at:at] = x[start:end]

    # If the subsequence is shifted in front of it's
    # position, compensate for the offset
    if at < start:
        offset = end - start
        x[start+offset:end+offset] = []
    else:
        x[start:end] = []

def subshift2(L, start, length, pos):
    #'PaulP.R.O.'
    temp = pos - length
    S = L[start:length+start]
    for i in range(start, temp):
        L[i] = L[i + length]
    for i in range(0,length):
        L[i + temp] = S[i]
    return L

def shift(L,start,n,i):
    #'vivek'
    return L[:start]+L[start+n:i]+L[start:start+n]+L[i:]
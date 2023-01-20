def solution(startPosition, speed):
    maxMeetings = -1;
    for i in range(len(startPosition)):
        for j in range(i+1,len(startPosition)):
            if speed[j] != speed[i]:
                meetingPoint=(startPosition[i] - startPosition[j]) / (speed[j] - speed[i])
                if (meetingPoint >= 0):
                    currentMeeting = 2
                    for k in range(j+1,len(startPosition)):
                        if startPosition[i] + speed[i] * meetingPoint == startPosition[k] + speed[k] * meetingPoint:
                            currentMeeting+=1;
                    if currentMeeting > maxMeetings:
                        maxMeetings = currentMeeting
    return maxMeetings;


def solution(p, s):
    if len(set(s))==1:
        return -1
    t=[]
    a=[]
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            try: t.append((p[j]-p[i])/(s[i]-s[j]))
            except ZeroDivisionError: break
    asdkjf=(max(t, key=t.count))
    for i in range(len(p)):
        a.append(p[i]+s[i]*asdkjf)
    return a.count(max(a, key=a.count))
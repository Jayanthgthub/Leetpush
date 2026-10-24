class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        Days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        no_of_days = [0]
        for i in range(len(Days_per_month)):
            no_of_days.append(no_of_days[-1]+Days_per_month[i])
        given_dates = [arriveAlice,leaveAlice,arriveBob,leaveBob]
        for i in range(len(given_dates)):
            k = map(int,given_dates[i].split("-"))
            given_dates[i]= no_of_days[k[0]-1] + k[1]
        started_days = max(given_dates[0],given_dates[2])
        leave_days =min(given_dates[1],given_dates[3])
        if started_days>leave_days:
            return 0
        return  leave_days-started_days+1

        
        
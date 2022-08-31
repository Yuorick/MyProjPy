#import math
import time


class Actions:
    mn_max_records = pow(2,31)
    m_listID =[]
    m_listT = []

    def __init__(self, listID, listT):
        self.m_listID = listID
        self.m_listT = listT


    def add(self,user_id, time):
        if len(self.m_listID)< self.mn_max_records:
            self.m_listID.append(user_id)
            self.m_listT.append(time)
        else:
            self.m_listID.pop(self.mn_max_records - 1)
            self.m_listT.pop(self.mn_max_records - 1)
            self.m_listID.append(user_id)
            self.m_listT.append(time)

   
    def   count(self, k, time_):
        # создание списка id, n
        listID = self.m_listID
        listT = self.m_listT
        list_IDrez = []
        list_Numrez = []
        tcur = time.time()

        for i in range (0, len(self.m_listT)):
            if self.m_listT[len(self.m_listT) - i] < tcur - time_:
                listID.pop(len(self.m_listT) - i)
                #listT.pop(len(self.m_listT) - i)

        for i in range (0, len(listID)):
            if list_IDrez.count(listID[i]) > 0:
                continue
            list_IDrez.append(listID[i])
            ncur = listID[i].count(listID[i], i)
            list_Numrez.append(ncur)

        return list_Numrez.count(k)



print('qy-qu')
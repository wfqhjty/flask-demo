class TransmitInfo:
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        dict={0:0}
        self.caculate(relation,0,n-1,k,dict)
        return dict[0]

    
    def caculate(self,relation,left,right,k,dict):
        if k==1:
            if self.is_exist(relation,left,right):
                dict[0]+=1
        if k==2:
            count=self.count(relation,left,right)
            if count>0:
                dict[0]+=count
        if k>2:
            pre=self.get_pre(relation,right)
            next=self.get_next(relation,left)
            if len(pre)>0 and len(next)>0:
                for i in next:
                    for j in pre:
                        self.caculate(relation,i,j,k-2,dict)


    def is_exist(self, relation, left, right):
        for i in relation:
            if i[0] == left and i[1] == right:
                return True
        return False

    
    def count(self, relation, left, right):
        count = 0
        for i in relation:
            if i[0] == left and self.is_exist(relation, i[1], right):
                count += 1
        return count


    def get_next(self,relation,left):
        next=[]
        for i in relation:
            if i[0]==left:
                next.append(i[1])
        return next


    def get_pre(self,relation,right):
        next=[]
        for i in relation:
            if i[1]==right:
                next.append(i[0])
        return next


if __name__ == "__main__":
    transmitInfo=TransmitInfo()
    relation=[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    print(transmitInfo.numWays(5,relation,3))
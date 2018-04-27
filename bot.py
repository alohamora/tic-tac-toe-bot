from __future__ import print_function
import copy
import random
import datetime

INFINITY = 1e20
INF = 1e10
class Team70:

    def __init__(self):
        self.termVal = INFINITY
        self.limit = 5
        self.count = 0
        self.blockweight = [6,4,4,6,4,3,3,4,4,3,3,4,6,4,4,6]
        self.weight = [2,3,3,2,3,4,4,3,3,4,4,3,2,3,3,2]
        self.dict = {'x':1,'o':-1,'-':0,'d':0}
        self.trans = {}
        self.timeLimit = datetime.timedelta(seconds = 15)
        self.begin = INFINITY
        self.limitReach = 0

    def evaluate(self,board,blx,bly):
        val=0
        blscorewin=INF/100
        pat=[0,1,24]

        # Horizontol win
        for i in xrange(4):
            mark=board.board_status[4*blx+i][4*bly]
            if (mark!='-'):
            	if (mark==board.board_status[4*blx+i][4*bly+1]):
            		if (mark==board.board_status[4*blx+i][4*bly+2]):
	            		if (mark==board.board_status[4*blx+i][4*bly+3]):
	            			return (blscorewin*self.dict[mark])

        # Vertical win
        for i in xrange(4):
            mark=board.board_status[4*blx][4*bly+i]
            if (mark!='-'):
            	if (mark==board.board_status[4*blx+1][4*bly+i]):
            		if (mark==board.board_status[4*blx+2][4*bly+i]):
	            		if (mark==board.board_status[4*blx+3][4*bly+i]):
	            			return (blscorewin*self.dict[mark])

	    # Diamond win
	    for i in xrange(2):
	    	for j in xrange(2):
	            mark=board.board_status[4*blx+i][4*bly+j+1]
	            if (mark!='-'):
	            	if (board.board_status[4*blx+i][4*bly+j+1]==board.board_status[4*blx+i+1][4*bly+j+2]):
	            		if (board.board_status[4*blx+i+1][4*bly+j+2]==board.board_status[4*blx+i+2][4*bly+j+1]):
		            		if (board.board_status[4*blx+i+2][4*bly+j+1]==board.board_status[4*blx+i+1][4*bly+j]):
		            			return (blscorewin*self.dict[mark])

        # Horizontol score x
        for i in xrange(4):
            count=1
            blwin=1
            for j in xrange(4):
                mark = board.board_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=pat[2]*self.weight[4*i+j]
                elif (mark=='-'):
                    count*=pat[1]*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=pat[0]
                    blwin=0
            val+=count
            #if (blwin==1):
                #return blscorewin*self.weight[4*blx+bly]

        # Horizontol score -o
        for i in xrange(4):
            count=1
            blwin=1
            for j in xrange(4):
                mark = board.board_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=pat[0]
                    blwin=0
                elif (mark=='-'):
                    count*=pat[1]*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=pat[2]*self.weight[4*i+j]
            val-=count
            # if (blwin==1):
                # return -1*blscorewin*self.weight[4*blx+bly]

        # Vertical score x
        for j in xrange(4):
            count=1
            blwin=1
            for i in xrange(4):
                mark = board.board_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=pat[2]*self.weight[4*i+j]
                elif (mark=='-'):
                    count*=pat[1]*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=pat[0]
                    blwin=0
            val+=count
            # if (blwin==1):
                #return blscorewin*self.weight[4*blx+bly]

        # Vertical score -o
        for j in xrange(4):
            count=1
            blwin=1
            for i in xrange(4):
                mark = board.board_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=pat[0]
                    blwin=0
                elif (mark=='-'):
                    count*=pat[1]*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=pat[2]*self.weight[4*i+j]
            val-=count
            # if (blwin==1):
                # return -1*blscorewin*self.weight[4*blx+bly]

        # Diamond score x
        for j in xrange(2):
            for k in xrange(2):
                count=1
                blwin=1
                if (board.board_status[4*blx+j][4*bly+1+k]=='x'):
                    count*=pat[2]
                if (board.board_status[4*blx+j][4*bly+1+k]=='o'):
                    count*=pat[0]
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k]=='x'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+1][4*bly+k]=='o'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='x'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='o'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k+2]=='x'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+1][4*bly+k+2]=='o'):
                    count*=0
                    blwin=0

                if (board.board_status[4*blx+j][4*bly+1+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+2+k]=='-'):
                    count*=pat[1]
                    blwin=0
                val+=(4*4*3*3*count)
                # if (blwin==1):
                    #return blscorewin*self.weight[4*blx+bly]

        # Diamond score -o
        for j in xrange(2):
            for k in xrange(2):
                count=1
                blwin=1
                if (board.board_status[4*blx+j][4*bly+1+k]=='x'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j][4*bly+1+k]=='o'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+1][4*bly+k]=='x'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k]=='o'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='x'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='o'):
                    count*=pat[2]
                if (board.board_status[4*blx+j+1][4*bly+k+2]=='x'):
                    count*=0
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k+2]=='o'):
                    count*=pat[2]

                if (board.board_status[4*blx+j][4*bly+1+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+2][4*bly+1+k]=='-'):
                    count*=pat[1]
                    blwin=0
                if (board.board_status[4*blx+j+1][4*bly+2+k]=='-'):
                    count*=pat[1]
                    blwin=0
                val-=(4*4*3*3*count)
                # if (blwin==1):
                    # return -1*blscorewin*self.weight[4*blx+bly]
        # print ('val is ',val)
        return val

    def blockEval(self,board):
        val=0
        blx=0
        bly=0
        fac=[0,1,24]

        blscorewin=INFINITY

        # Horizontol win
        for i in xrange(4):
            mark=board.block_status[4*blx+i][4*bly]
            if (mark!='-' and mark!='d'):
            	if (mark==board.block_status[4*blx+i][4*bly+1]):
            		if (mark==board.block_status[4*blx+i][4*bly+2]):
	            		if (mark==board.block_status[4*blx+i][4*bly+3]):
	            			return (blscorewin*self.dict[mark])

        # Vertical win
        for i in xrange(4):
            mark=board.block_status[4*blx][4*bly+i]
            if (mark!='-' and mark!='d'):
            	if (mark==board.block_status[4*blx+1][4*bly+i]):
            		if (mark==board.block_status[4*blx+2][4*bly+i]):
	            		if (mark==board.block_status[4*blx+3][4*bly+i]):
	            			return (blscorewin*self.dict[mark])

	    # Diamond win
	    for i in xrange(2):
	    	for j in xrange(2):
	            mark=board.block_status[4*blx+i][4*bly+j+1]
	            if (mark!='-' and mark!='d'):
	            	if (board.block_status[4*blx+i][4*bly+j+1]==board.block_status[4*blx+i+1][4*bly+j+2]):
	            		if (board.block_status[4*blx+i+1][4*bly+j+2]==board.block_status[4*blx+i+2][4*bly+j+1]):
		            		if (board.block_status[4*blx+i+2][4*bly+j+1]==board.block_status[4*blx+i+1][4*bly+j]):
		            			return (blscorewin*self.dict[mark])


        # Horizontol score x
        for i in xrange(4):
            count=1
            blwin=1
            for j in xrange(4):
                mark = board.block_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=fac[2]*self.weight[4*i+j]
                elif (mark=='-'):
                    count*=fac[1]*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o' or mark=='d'):
                    count*=0
                    blwin=0
            val+=count
            if (blwin==1):
                return blscorewin

        # Horizontol score -o
        blwin=1
        for i in xrange(4):
            count=1
            blwin=1
            for j in xrange(4):
                mark = board.block_status[4*blx+i][4*bly+j]
                if (mark=='x' or mark=='d'):
                    count*=0
                    blwin=0
                elif (mark=='-'):
                    count*=1*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=fac[2]*self.weight[4*i+j]
            val-=count
            if (blwin==1):
                return -1*blscorewin

        # Vertical score x
        blwin=1
        for j in xrange(4):
            count=1
            blwin=1
            for i in xrange(4):
                mark = board.block_status[4*blx+i][4*bly+j]
                if (mark=='x'):
                    count*=fac[2]*self.weight[4*i+j]
                elif (mark=='-'):
                    count*=1*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o' or mark=='d'):
                    count*=0
                    blwin=0
            val+=count
            if (blwin==1):
                return blscorewin

        # Vertical score -o
        blwin=1
        for j in xrange(4):
            count=1
            blwin=1
            for i in xrange(4):
                mark = board.block_status[4*blx+i][4*bly+j]
                if (mark=='x' or mark=='d'):
                    count*=0
                    blwin=0
                elif (mark=='-'):
                    count*=1*self.weight[4*i+j]
                    blwin=0
                elif (mark=='o'):
                    count*=fac[2]*self.weight[4*i+j]
            val-=count
            if (blwin==1):
                return -1*blscorewin

        # Diamond score x
        blwin=1
        for j in xrange(2):
            for k in xrange(2):
                count=1
                blwin=1
                if (board.block_status[4*blx+j][4*bly+1+k]=='x'):
                    count*=fac[2]
                if (board.block_status[4*blx+j][4*bly+1+k]=='o'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='x'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+1][4*bly+k]=='o'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='x'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='o'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k+2]=='x'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+1][4*bly+k+2]=='o'):
                    count*=0
                    blwin=0

                if (board.block_status[4*blx+j][4*bly+1+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+2+k]=='-'):
                    blwin=0

                if (board.block_status[4*blx+j][4*bly+1+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+2+k]=='d'):
                    count*=0
                    blwin=0
                val+=(4*4*3*3*count)
                if (blwin==1):
                    return blscorewin

        # Diamond score -o
        blwin=1
        for j in xrange(2):
            for k in xrange(2):
                count=1
                blwin=1
                if (board.block_status[4*blx+j][4*bly+1+k]=='x'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j][4*bly+1+k]=='o'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+1][4*bly+k]=='x'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='o'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='x'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='o'):
                    count*=fac[2]
                if (board.block_status[4*blx+j+1][4*bly+k+2]=='x'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k+2]=='o'):
                    count*=fac[2]

                if (board.block_status[4*blx+j][4*bly+1+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='-'):
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+2+k]=='-'):
                    blwin=0

                if (board.block_status[4*blx+j][4*bly+1+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+2][4*bly+1+k]=='d'):
                    count*=0
                    blwin=0
                if (board.block_status[4*blx+j+1][4*bly+2+k]=='d'):
                    count*=0
                    blwin=0
                val-=(4*4*3*3*count)
                if (blwin==1):
                    return -1*blscorewin

        return val

    def heuristic(self, board):
        tmpBlock = copy.deepcopy(board.block_status)
        final = 0
        for i in xrange(4):
            for j in xrange(4):
                blvalue = self.evaluate(board,i,j)
                # print(aaja,i,j)
                final += blvalue

        final += self.blockEval(board)*1000000
        del(tmpBlock)
        return final

    def alphaBeta(self, board, old_move, flag, depth, alpha, beta, cntwin):
        # Taking 'x' as the maximising player
        # nodeval[0]=heurestic value of the node/board state , nodeval[1]=chosen position of the marker


        cells = board.find_valid_move_cells(old_move)
        random.shuffle(cells)

        if (flag == 'x'):
            nodeVal = -INFINITY, cells[0]
            new = 'o'
            tmp = copy.deepcopy(board.block_status)
            a = alpha

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                    # print("breaking at depth ",depth)
                    self.limitReach = 1
                    break
                board.update(old_move, chosen, flag)
                # print("chosen ",chosen)
                if (board.find_terminal_state()[0] == 'x'):
                	# X WINS THE BOARD
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    nodeVal = self.termVal-depth,chosen
                    break
                elif (board.find_terminal_state()[0] == 'o'):
                	# O WINS THE BOARD
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE'):
                	# DRAW OF THE FINAL BOARD
                    x = 0
                    d = 0
                    o = 0
                    tmp1 = 0
                    for i2 in xrange(4):
                        for j2 in xrange(4):
                            if(board.block_status[i2][j2] == 'x'):
                                x += 1*(self.blockweight[4*i2+j2])
                            if(board.block_status[i2][j2] == 'o'):
                                o += 1*(self.blockweight[4*i2+j2])
                            if(board.block_status[i2][j2] == 'd'):
                                d += 1
                    if(x==o):
                        tmp1 = 0
                    elif(x>o):
                        tmp1 = INFINITY/2 + 100*(x-o)
                    else:
                        tmp1 = -INFINITY/2 - 100*(o-x)
                    # print(tmp1)
                elif( depth >= self.limit):
                    tmp1 = self.heuristic(board)
                    if (tmp1==INFINITY):
                        tmp1= INFINITY-depth
                    elif (tmp1== (-1*INFINITY)):
                        tmp1= tmp1+depth
                    # print("Heuristic value for ",chosen," is ",tmp1)
                else:
                    checkwin=self.evaluate(board,chosen[0]/4,chosen[1]/4)
                    if (checkwin==INF/100 and cntwin==0):
                        # print ('depth is ',depth,' and pos is ',chosen[0],' ',chosen[1],' for ',flag)
                        tmp1 = self.alphaBeta(board, chosen, 'x', depth+1, a, beta,1)[0]
                        # cntwin=0
                        # new='o'
                    else:
                    	# block win on bonus move
	                    tmp1 = self.alphaBeta(board, chosen, new, depth+1, a, beta,0)[0]

                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                if(nodeVal[0] < tmp1):
                    nodeVal = tmp1,chosen
                # print("The nodeval is ",nodeVal)
                a = max(a, tmp1)
                if beta <= nodeVal[0] :
                    break
            del(tmp)

        if (flag == 'o'):
            nodeVal = INFINITY, cells[0]
            new = 'x'
            tmp = copy.deepcopy(board.block_status)
            b = beta

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                    # print("breaking")
                    self.limitReach = 1
                    break
                board.update(old_move, chosen, flag)

                if(board.find_terminal_state()[0] == 'o'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    nodeVal = (-1*self.termVal)+depth,chosen
                    break
                elif(board.find_terminal_state()[0] == 'x'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE'):
                    x = 0
                    d = 0
                    o = 0
                    tmp1 = 0

                    for i2 in range(4):
                        for j2 in range(4):
                            if board.block_status[i2][j2] == 'x':
                                x += 1
                            if board.block_status[i2][j2] == 'o':
                                o += 1
                            if board.block_status[i2][j2] == 'd':
                                d += 1
                    if(x==o):
                        tmp1 = 0
                    elif(x>o):
                        tmp1 = INFINITY/2 + 100*(x-o)
                    else:
                        tmp1 = -INFINITY/2 - 100*(o-x)

                elif(depth >= self.limit):
                    tmp1 = self.heuristic(board)
                    if (tmp1== -1*INFINITY):
                        tmp1= (-1*INFINITY)+depth
                    elif (tmp1== INFINITY):
                        tmp1= tmp1-depth
                else:
                    checkwin=self.evaluate(board,chosen[0]/4,chosen[1]/4)
                    if (checkwin==-INF/100 and cntwin==0):
                        # print ('depth is ',depth,' and pos is ',chosen[0],' ',chosen[1],' for ',flag)
                        tmp1 = self.alphaBeta(board, chosen, 'o', depth+1, alpha, b,1)[0]
                        # cntwin=0
                        # new='x'
                    else:
                    	# block win on bonus move
	                    tmp1 = self.alphaBeta(board, chosen, new, depth+1, alpha, b,0)[0]

                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                if(nodeVal[0] > tmp1):
                    nodeVal = tmp1,chosen
                b = min(b, tmp1)
                if alpha >= nodeVal[0] :
                    break
            del(tmp)

        return nodeVal

    def move(self, board, old_move, flag):
        self.begin = datetime.datetime.utcnow()
        self.count += 1
        self.limitReach = 0
        self.trans.clear()
        # print(self.trans.items())
        # print (INFINITY)
        # if (self.count==1 and flag=='x'):
        #     # mymove[0]=5
        #     # mymove[1]=5
        #     # board.update(old_move,(5,5),flag)
        #     print ('Heurestic value of blocks was ',1000000*self.blockEval(board))
        #     print ('Heurestic value of board was ',self.heuristic(board))
        #     print ('I play ',flag)
        #     # board.board_status[5][5]='-'
        #     return 5,5
        # else:
        mymove = board.find_valid_move_cells(old_move)[0]
        for i in xrange(3,120):
            self.trans.clear()
            self.limit = i
            # print("in depth ",i)
            bval = self.alphaBeta(board, old_move, flag, 1, -INFINITY, INFINITY,0)
            getval = bval[1]
            # print("returned from depth ",i)
            if(self.limitReach == 0):
                mymove = getval
            else:
                break
        # board.update(old_move,mymove,flag)
        # print ('Heurestic value of blocks was ',1000000*self.blockEval(board))
        # print ('Heurestic value of board was ',self.heuristic(board))
        # print ('I play 24 24 24 24 24',flag)
        # board.board_status[mymove[0]][mymove[1]]='-'
        if (flag=='x' and self.count==1):
            mymove=[5,5]
        return mymove[0], mymove[1]

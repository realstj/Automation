import logging
from collections import deque
import math

class Trans:
    datetime=None
    amount=None
    price=None
 
    def __init__(self, datetime, amount, price):
        self.datetime=datetime
        self.amount=amount
        self.price=price
     
    def getInfo(self):
        return(str(self.datetime)+"; "+
                str(self.amount)+"; "+
                str(self.price))+"; "
 
def balanceFifo(all_trans):
 
    qTransactions = deque() 
    trans_result = list()
 
    for t in all_trans:
        #Add first element to the queue
        if len(qTransactions)==0:
            #logging.debug('Added the first element: %s',t.getInfo())
            qTransactions.append(t)
            continue
 
        while (t.amount!=0 and len(qTransactions)>0):
            #investigate the first element from the queue
            tq=qTransactions.popleft()
            #the same type of transaction: both sell or both buy
            if tq.amount*t.amount>0:
                #return the first element back to the same place
                qTransactions.appendleft(tq)
                #add the new element to the list
                qTransactions.append(t)
                #logging.debug('Added: %s',t.getInfo())
                break
             
            #contrary transactions: (sell and buy) or (buy and sell) 
            if tq.amount*t.amount<0:
                #logging.debug('Transaction : %s',t.getInfo())
                #logging.debug('... try to balance with: %s',tq.getInfo())
 
                #The element in the queue have more units and takes in the current transaction
                if abs(tq.amount)>abs(t.amount):
                    result = insertTransaction(tq.datetime,t.datetime,\
                            math.copysign(t.amount,tq.amount), tq.price,t.price)
                    trans_result.append(result)
                    
                    #update the amount of the element in the queue
                    tq.amount=tq.amount+t.amount
                    #return the element back to the same place
                    qTransactions.appendleft(tq)
                    #logging.debug('Removed transaction: %s',t.getInfo())
                    #the transaction has been balanced, take a new transaction
                    break
                 
                #The element from the queue and transaction have the same amount of units
                if abs(tq.amount)==abs(t.amount):
                    result = insertTransaction(tq.datetime,t.datetime,\
                                math.copysign(t.amount,tq.amount), tq.price,t.price)
                    trans_result.append(result)
                    
                    #update the amount in the transaction 
                    t.amount=0
                    #logging.debug('Balanced, removed transaction: %s',t.getInfo())
                    #logging.debug('Balanced, removed from the queue: %s',tq.getInfo())
                    #the transaction has been balanced, take a new transaction
                    continue
                    
                #The transaction has more units
                if abs(tq.amount)<abs(t.amount):
                    #update the units in transaction, (remove element from the queue)
                    t.amount=t.amount+tq.amount
                    result = insertTransaction(tq.datetime,t.datetime,tq.amount,tq.price,t.price)
                    trans_result.append(result)
                    #logging.debug('Removed from queue: %s',tq.getInfo())
                     
                    #the transaction has not been balanced, 
                    #take a new element from the queue (t.amount>0)
                    continue
                 
        #We have unbalanced transaction but the queue is empty            
        if (t.amount!=0 and len(qTransactions)==0):
            #Add unbalanced transaction to the queue
            #The queue changes polarisation
            qTransactions.append(t)
            #logging.debug('Left element: %s',t.getInfo())
     
     
    #If something remained in the queue, treat it as open or part-open transactions
    while (len(qTransactions)>0):
        tq=qTransactions.popleft()
        #logging.debug('Remained on list transaction: %s',tq.getInfo())
        
    return trans_result
 
def insertTransaction(dateStart,dateEnd,amount,priceStart,priceEnd):
    #print("Bought={}, sold={},  amount={}, buy price={}, sell_price={}, gain={}".\
    #        format(dateStart,dateEnd,amount,priceStart,priceEnd, amount*(priceEnd-priceStart)))
    result = [dateStart,dateEnd,amount,priceStart,priceEnd, amount*(priceEnd-priceStart)]
    return result
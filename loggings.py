
#login module
# import logging
# logging.basicConfig(level=logging.DEBUG)
# # logging.disable()
# n=10
# sum=0
# for i in range(10):
#     sum=+i
#     # logging.info(i) #different level of logging levels
#     # logging.error(i)
#     logging.debug(i)
#     logging.critical(i)
#     logging.warning(i)
# print(sum)






# progarm
import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s")
logging.debug("start of the program")
def fact(n):
    logging.debug("start of factorial (%d)"%(n))
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug("i is "+str(i)+" total is"+str(total))
    logging.debug("end of torial(%d)"%(n))
    return total
print(fact(5))
logging.debug("end of the program")

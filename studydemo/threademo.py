import time
import thread

def timer01(no,interval):
	cnt  = 0
	while cnt<5:
		print('Thread:(%d) Time:%s\n' %(cnt,time.ctime()))
		time.sleep(interval)
		cnt += 1
	thread.exit_thread()

def test():
	thread.start_new_thread(timer01,(1,2))
	#thread.start_new_thread(timer01,(10,2))
	time.sleep(10)
    



if __name__ == '__main__':
	test()



from time import sleep 
import schedule
import sys
sys.path.insert(0, '/home/annlee/solar-scare/server/wingbeats_pi')

def impML():
    import wingbeatpi_v2
    print('hello')

schedule.every().day.at("11:32").do(impML)

while True:
    schedule.run_pending()
    sleep(1)

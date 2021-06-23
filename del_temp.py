#importing modules
import os

user_config = os.path.expanduser("~")
TARGET1 = f"{user_config}\AppData\Local\Temp"
TARGET2 = "C:\Windows\Temp"

print(f"Deleting files in: \n{TARGET1}\n{TARGET2}")

def del_temp():
    count1 = 0
    count2 = 0
    #counting the number of files(brute way until better solution)
    for root,_,files in os.walk(TARGET1):
        for file in files:
            count2 += 1
    for root,_,files in os.walk(TARGET2):
        for file in files:
            count2 += 1

    for root,_,files in os.walk(TARGET1):
        for file in files:
            #print(f'{file}')
            try:
                os.remove(os.path.join(root, file))
                count1 += 1
            except Exception as e:
                #print(e)
                continue


    for root,_,files in os.walk(TARGET2):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                count1 += 1
            except Exception as e:
                #print(e)
                continue
    print('[INFO]: Task completed!')
    print(f'[INFO]: Deleted {count1} file(s) from {count2} file(s) in the folders.')

del_temp()
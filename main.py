from os import stat, truncate
import pandas

data = pandas.read_csv("data.csv")

def check_crop_status(crop_name,time,weather):
    index = 0

    while True:
        try:
            if crop_name == data.iloc[index]['crop_name']:
                crop_data = {
                    "time" : int(data.iloc[index]['time']),
                    "weather" : str(data.iloc[index]['unhealthy_wheater']),
                }

                if time >= crop_data['time'] or weather == crop_data['weather']:
                    return "unsafe"
                else:
                    return "safe"
            
            index = index + 1
        except:
            break
    return "err"

if __name__ == "__main__":
    crop_name = input("Enter crop name: ")
    time = int(input("How much time passed till you planted crops: "))
    weather = input("Enter current weather: ")

    status = check_crop_status(crop_name,time,weather)

    if status == "unsafe":
        print("Your crops are unhealthy :(")
    elif status == "safe":
        print("Your crops are healthy :)")
    elif status == "err":
        print("Error... data not found")
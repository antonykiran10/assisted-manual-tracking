import cv2
import pandas as pd

def play_video(video_path, output_csv):
    cap = cv2.VideoCapture(video_path)
    flag = 0  # Initial flag value

    # Create an empty DataFrame to store the data
    data = {'Frame Number': [], 'Timestamp (seconds)': [], 'Key Pressed': []}

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Get the current frame's timestamp
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        # Display the timestamp on the upper left corner
        cv2.putText(frame, f'Time: {current_time:.2f} seconds', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


        cv2.imshow('Frame', frame)

        key = cv2.waitKey(0) & 0xFF

        # Append data to the DataFrame
        data['Frame Number'].append(cap.get(cv2.CAP_PROP_POS_FRAMES))
        data['Timestamp (seconds)'].append(current_time)
        data['Key Pressed'].append(chr(key))

        if key == ord('1'):
            flag += 1
        elif key == ord('0'):
            pass  # Do nothing, don't increment flag
        elif key == 27:  # 27 corresponds to the 'Esc' key
            break  # Exit the loop if 'Esc' is pressed
    cap.release()
    cv2.destroyAllWindows()
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    return flag



# main program starts here:
my_path = '/home/antony/Desktop/nikita/' # Replace with the path to your video file
video_name = '20230404_174850.mp4'  # Replace with the name of your video file
video_path = my_path + video_name
output_csv = my_path + video_name + '.csv'
frames = play_video(video_path, output_csv)
fps = 30 # Put the frame rate of the video
time = frames/fps
print('Total time spend behaving: ', f"{time:.2f}", ' seconds') # you change the number of decimals places here



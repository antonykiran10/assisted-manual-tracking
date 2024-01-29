# assisted-manual-tracking
Used for onscreen manual tracking and recording of animal behaviour from video files and output a CSV file.

Overview:
---------

The code is a script designed to play a video, allowing the user to label specific frames with key presses. The labeled data is then stored in a CSV file, including the frame number, timestamp, and the key pressed during labeling. The script terminates when the 'Esc' key is pressed.

1\. `play_video` Function:
--------------------------

### Purpose:

This function plays a video and captures user inputs to label specific frames. It also records the frame number, timestamp, and key pressed for each labeled frame. The labeled data is stored in a DataFrame and saved to a CSV file.

### Parameters:

*   `video_path`: String, the path to the input video file.
*   `output_csv`: String, the path to the output CSV file where labeled data will be stored.

### Returns:

An integer representing the total number of frames labeled during the video playback.

Important Notes:
----------------

*   The script uses OpenCV for video playback and capturing user input.
*   The labeled data includes the frame number, timestamp, and the key pressed during labeling.
*   The script terminates when the 'Esc' key is pressed.
*   The labeled data is saved in a CSV file specified by the `output_csv` parameter.

2\. Main Program:
-----------------

The main program initializes the video path, video name, and output CSV file path. It then calls the `play_video` function, calculates the total time spent labeling (assuming a frame rate of 30 frames per second), and prints the result.

### Main Program Variables:

*   `my_path`: String, the path to the directory containing the video file.
*   `video_name`: String, the name of the video file.
*   `video_path`: String, the full path to the video file.
*   `output_csv`: String, the full path to the output CSV file.
*   `frames`: Integer, the total number of frames labeled during video playback.
*   `fps`: Integer, the assumed frame rate of the video (30 frames per second).
*   `time`: Float, the total time spent labeling in seconds.

### Output:

The script prints the total time spent labeling in seconds.

Comments:
---------

*   Some commented-out code segments are present, which can be uncommented if additional functionality is needed (e.g., decrementing the flag, deleting the last entry).
*   The script assumes a frame rate of 30 frames per second (`fps`). Adjustments may be needed based on the actual frame rate of the video.
*   The script saves the labeled data in a CSV file with columns: 'Frame Number', 'Timestamp (seconds)', and 'Key Pressed'.
Message ChatGPT…


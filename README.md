# Meteor Challenge

## Tasks:

1. **Count the number of Stars**
2. **Count the number of Meteors**
3. **If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water**
4. **(Optional) Find the phrase that is hidden in the dots in the sky.**
   - a. HINT 1: 175 Characters
   - b. HINT 2: Most of the last tasks’ code can be reused for this one

Please, send us the result and code you used to solve the tasks above. Explain how you achieved the results in each question. Good work!!

## Subject: [CHALLENGE] [METEOR] _Pedro Nogueira Barboza_

## Answers:

| Requested                    | Number | how I did found the answer                                                                                   |
| ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| Number of Stars              | 315    | I counted the number of pixels that are white.                                                               |
| Number of Meteors            | 328    | I counted the number of pixels that are red.                                                                 |
| Meteors falling on the Water | 105    | I counted the number of red pixels that are in the same columns as the blue pixels, whose positions I noted. |

### Pixel Reference:

- (pure white) Stars
- (pure red) Meteors
- (pure blue) Water
- (pure black) Ground

## Prerequisites

Before running this project, you will need to have the Pillow library installed. To install Pillow, run the following command in your terminal:

```bash
pip install Pillow
```

## Running the Project

To run this project, follow these steps:

1. Clone the repository to your local computer.
2. Navigate to the project directory.
3. Ensure the image `meteor_challenge_01.png` is in the same directory as the script.
4. Run the script with the command:

   ```bash
   python main.py
   ```

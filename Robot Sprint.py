def center():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    is_centered = False
    while is_centered == False:
        x = None
        detection_info = vision_ctrl.get_marker_detection_info()
        print(detection_info)
        if len(detection_info) > 3:
            x = float(detection_info[2])
            print(x)

        if x != None:
            if x < 0.56 and abs(x - 0.53) > 0.01:
                chassis_ctrl.move_with_distance(-90, 0.03)
            elif x > 0.52 and abs(x - 0.52) > 0.01:
                chassis_ctrl.move_with_distance(90, 0.03)
            else:
                is_centered = True
                print("Robot is centered by x axis")


# Function to tell robot to return to start from room 1

def room_1_ret():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 4.7)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.35)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(6)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)


# Function to tell robot to return to start from room 3

def room_3_ret():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 1.2)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 4.82)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 1.64)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.23)
    # BACK TO START FROM HALLWAY
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 3.76)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 44)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 49)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.77)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(6)
    gimbal_ctrl.recenter()
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)


# Function to tell robot to return to start from room 4

def room_4_ret():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.08)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 44)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 49)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.77)
    media_ctrl.play_sound(rm_define.media_custom_audio_2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 1080)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)


# Scanning for marker

marker_found = False


def scan_for_marker():
    # Turn on detection and scan left and right until you hit a marker.rm_define.media_custom_audio_0
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    global marker_found
    marker_found = False
    gimbal_ctrl.yaw_ctrl(-90)
    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)


# Telling robot what to do once marker found

def vision_recognized_marker_letter_F(msg):
    # center()
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    media_ctrl.play_sound(rm_define.media_sound_recognize_success)
    time.sleep(3)
    gun_ctrl.fire_once()
    marker_found = True


# Scanning for person

def scan_for_person_and_play_sound():
    global person_found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_found = False
    while person_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)


# Telling robot what to do once person is found

def vision_recognized_people(msg):
    global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_custom_audio_0)
    person_found = True


# Start of main program

def start():
    # Defining room types
    room_one_type = 3
    room_two_type = 2
    room_three_type = 1
    room_four_type = 1

    # Setting Robot Settings

    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(60)
    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_trans_speed(1)
    gimbal_ctrl.recenter()
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)

    # To first room

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.35)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # First Room Logic

    if room_one_type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 4.76)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_marker()
        # Return to hall
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
    elif room_one_type == 2:
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_marquee)
        media_ctrl.play_sound(rm_define.media_custom_audio_1)
        time.sleep(2)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
    elif room_one_type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 4.76)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_person_and_play_sound()
        room_1_ret()
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.35)
        chassis_ctrl.move_with_distance(0, 5)

    # To turn

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.48)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 49)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 44)
    gimbal_ctrl.recenter()
    time.sleep(5)

    # to Second room from turn

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.4)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Room Two logic since room 2 will always be do not enter does not need other if statments
    if room_two_type == 2:
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_marquee)
        media_ctrl.play_sound(rm_define.media_custom_audio_1)
        time.sleep(1)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

    # To third room

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.65)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Room three logic

    if room_three_type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 2.23)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.64)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.82)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.2)
        # scans for marker and takes action
        scan_for_marker()
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.82)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.64)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.23)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)

    elif room_three_type == 2:
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_marquee)
        rm_define.media_custom_audio_1
        time.sleep(2)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

    elif room_three_type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 2.23)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.64)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.82)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.2)
        # scans for marker and takes action
        scan_for_person_and_play_sound()
        room_3_ret()
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.35)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.48)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 49)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 44)
        time.sleep(7)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 0.4)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.65)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)

    # to last room

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.31)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Room Four Logic

    if room_four_type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_marker()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
        # Return to home after last room
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.08)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 44)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 49)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.77)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 720)
        media_ctrl.play_sound(rm_define.media_custom_audio_2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, )
    elif room_four_type == 2:
        gimbal_ctrl.recenter()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_marquee)
        rm_define.media_custom_audio_1
        time.sleep(2)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.08)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 44)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 49)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.77)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 720)
        media_ctrl.play_sound(rm_define.media_custom_audio_2)

    elif room_four_type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_flash)
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_marquee)
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_person_and_play_sound()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.19)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        time.sleep(5)
        room_4_ret()

    # gimbal_ctrl.pitch_ctrl(20)
    # gimbal_ctrl.yaw_ctrl(100)
    # gimbal_ctrl.recenter()

import serial
from serial.tools import list_ports

import unittest
import STServo_Python.Gimbal
from STServo_Python.Gimbal import Gimbal
import time


class TestGimbal(unittest.TestCase):

    def test_list_connected_devices_via_com_ports(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"""
            -------- {port.name}  -------- 
            device: {port.device}
            pid: {port.pid}
            vid: {port.vid}
            description: {port.description}
            interface: {port.interface}
            location: {port.location}
            hwid: {port.hwid}
            manufacture: {port.manufacturer}
            serial_number: {port.serial_number}
            """)

        self.assertTrue(len(ports) != 0, "No COM devices")
        self.assertTrue(len(ports) == 1, "Multiple COM devices connected. Could not resolve appropriate driver board")

    def test_set_middle_position_per_x_y_coordinates(self):
        gimbal = Gimbal(serial.tools.list_ports.comports()[0].name)
        gimbal.start()
        gimbal.calibrate(30, 10)
        time.sleep(5)
        gimbal.shutdown()

    def test_move_right_by_45_degree_when_servo_has_a_stable_speed_of_0_088_degrees_per_second(self):
        gimbal = Gimbal(serial.tools.list_ports.comports()[0].name)
        gimbal.start()
        gimbal.calibrate(30, 10)
        time.sleep(5)
        gimbal.move_x(45, 0.088, 0)
        gimbal.shutdown()

    def test_rotate_right_by_45_degree_when_servo_has_a_stable_speed_of_0_088_degrees_per_second(self):
        gimbal = Gimbal(serial.tools.list_ports.comports()[0].name)
        gimbal.start()
        gimbal.calibrate(30, 10)
        time.sleep(5)
        gimbal.turn_on_wheel_mode()
        gimbal.rotate_x(0.088, 0)
        gimbal.shutdown()